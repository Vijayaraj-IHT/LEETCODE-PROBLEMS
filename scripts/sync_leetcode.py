#!/usr/bin/env python3
"""
Sync LeetCode submissions for vijay-3102 into NN-slug/ structure.
Usage:
  LEETCODE_SESSION=... LEETCODE_CSRFTOKEN=... python3 scripts/sync_leetcode.py --user vijay-3102 --dry-run
  LEETCODE_SESSION=... python3 scripts/sync_leetcode.py --user vijay-3102 --out .
Requires: requests (pip install requests) or stdlib urllib fallback.

This is a *starter template* — fill in fetch_submission_details() with your
authenticated GraphQL query if you want fully automatic code pull.
Until then it scaffolds folders from recentAcSubmissionList and prints TODOs.

Refs:
  - GraphQL endpoint: https://leetcode.com/graphql
  - Query recentAcSubmissionList(username: String!, limit: Int)
  - Query submissionDetails(submissionId: Int) { code, runtime, memory ... }
"""
import argparse, json, os, re, sys, textwrap
from pathlib import Path

SLUG_RE = re.compile(r'[^a-z0-9]+')

def slugify(title: str) -> str:
    return SLUG_RE.sub('-', title.lower()).strip('-')

def graphql_recent_ac(username, limit=20, session=None, csrftoken=None):
    """Try to fetch recent AC via GraphQL. Falls back to None if auth/network fails."""
    try:
        import requests
    except ImportError:
        print("[sync] requests not installed — using urllib fallback (limited)", file=sys.stderr)
        return None

    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/u/{username}/",
        "User-Agent": "Mozilla/5.0",
    }
    if session:
        headers["Cookie"] = f"LEETCODE_SESSION={session}; csrftoken={csrftoken or ''}"
        if csrftoken:
            headers["x-csrftoken"] = csrftoken

    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
      recentAcSubmissionList(username: $username, limit: $limit) {
        id
        title
        titleSlug
        timestamp
        statusDisplay
        lang
      }
    }
    """
    try:
        resp = requests.post(
            "https://leetcode.com/graphql",
            json={"query": query, "variables": {"username": username, "limit": limit}},
            headers=headers,
            timeout=15,
        )
        if resp.status_code != 200:
            print(f"[sync] GraphQL HTTP {resp.status_code}: {resp.text[:500]}", file=sys.stderr)
            return None
        data = resp.json()
        return data.get("data", {}).get("recentAcSubmissionList", [])
    except Exception as e:
        print(f"[sync] GraphQL fetch failed: {e}", file=sys.stderr)
        return None

def next_nn(repo_root: Path) -> int:
    existing = [p for p in repo_root.iterdir() if p.is_dir() and re.match(r"\d{2,}-", p.name)]
    if not existing:
        return 1
    nums = [int(p.name.split("-")[0]) for p in existing]
    return max(nums) + 1

def scaffold(repo_root: Path, title: str, slug: str, submission_id: str, dry_run=False):
    nn = next_nn(repo_root)
    folder = repo_root / f"{nn:02d}-{slug}" if nn < 10 else repo_root / f"{nn}-{slug}"
    if folder.exists():
        print(f"[skip] {folder} already exists")
        return folder
    print(f"[create] {folder}  (submission {submission_id} · {title})")
    if dry_run:
        return folder
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "solution.py").write_text(textwrap.dedent(f"""\
        # TODO: paste code from https://leetcode.com/submissions/detail/{submission_id}/
        # Title: {title} (slug: {slug})
        class Solution(object):
            pass
        """))
    (folder / "README.md").write_text(textwrap.dedent(f"""\
        # {title} (LeetCode)

        **Difficulty:** TODO  
        **Code:** `solution.py`

        ## Problem

        TODO — paste description from https://leetcode.com/problems/{slug}/

        ## Approach

        - TODO

        ## Complexity

        - **Time:** TODO
        - **Space:** TODO
        """))
    return folder

def main():
    ap = argparse.ArgumentParser(description="LeetCode repo sync helper")
    ap.add_argument("--user", default="vijay-3102", help="LeetCode username")
    ap.add_argument("--limit", type=int, default=20, help="recent AC limit")
    ap.add_argument("--out", default=".", help="repo root")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--submission", help="single submission id to scaffold")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    repo_root = Path(args.out).resolve()
    session = os.getenv("LEETCODE_SESSION")
    csrftoken = os.getenv("LEETCODE_CSRFTOKEN")

    if args.submission:
        scaffold(repo_root, "TODO Title", f"submission-{args.submission}", args.submission, dry_run=args.dry_run)
        return

    if not session:
        print("[warn] LEETCODE_SESSION not set — code content will be placeholders. Set it for authenticated fetch.", file=sys.stderr)

    subs = graphql_recent_ac(args.user, args.limit, session, csrftoken)
    if subs is None:
        print("[sync] Could not fetch recent AC list. Tips:", file=sys.stderr)
        print("  - pip install requests", file=sys.stderr)
        print("  - ensure internet and LEETCODE_SESSION / csrftoken are valid", file=sys.stderr)
        print("  - or manually create folders NN-slug/ with solution.py + README.md", file=sys.stderr)
        known = [
            ("225", "Implement Stack using Queues", "implement-stack-using-queues"),
            ("83", "Remove Duplicates from Sorted List", "remove-duplicates-from-sorted-list"),
            ("32", "Longest Valid Parentheses", "longest-valid-parentheses"),
        ]
        for _, title, slug in known:
            scaffold(repo_root, title, slug, "TODO", dry_run=args.dry_run)
        return

    for s in subs:
        title = s.get("title") or s.get("titleSlug", "")
        slug = s.get("titleSlug") or slugify(title)
        sid = s.get("id")
        existing = list(repo_root.glob(f"*-{slug}"))
        if existing:
            if args.verbose:
                print(f"[exists] {slug} → {existing[0].name}")
            continue
        scaffold(repo_root, title, slug, sid, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
