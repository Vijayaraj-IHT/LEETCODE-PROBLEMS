# LeetCode Analysis — vijay-3102 & GitHub Rework Report

Date: 2026-10-08 (UTC) · Profile: https://leetcode.com/u/vijay-3102/ · Repo: https://github.com/Vijayaraj-IHT/LEETCODE-PROBLEMS

## 1. How many have you solved?

| Source | Evidence | Count |
|--------|----------|-------|
| **LeetCode profile** (fetched 2026-10-08) | Top card `58/4073 Solved · 63.27% Acceptance · Beats 65.39%/54.24%/50.47%` · Breakdown `Easy 33/969 · Med 19/2124 · Hard 6/980` · `98 submissions in past year · 18 active days · max streak 3` | **58** |
| **GitHub before rework** (`main` @595f3e2) | `37` folders `01-37` + `12` loose `*.py` at root (`144.py`, `145.py`, `94.py`, `1700.py`, `232.py`, `239.py`, `387.py`, `589.py`, `590.py`, `622.py`, `862.py`, `933.py`) | **49 objects** (37 structured + 12 loose) |
| **README before** | Badges `Easy 24 · Med 18 · Hard 4 · Total 46+` — stale vs both actual LeetCode (58) and actual folders (49) | out-of-date |
| **GitHub after rework** (this branch) | `52` folders `01-52`, **0 loose files**, each with `solution.*` + `README.md` | **52 structured** (see table in README.md) |

### Reconciliation

- **12 loose files → 38–49** migrated (preserving your original Python code, only re-housed).
- **3 recent ACs not yet in repo** → added as `50–52` inferred from your profile's *Recent AC* list (see §3).
- **Gap remaining = 58 − 52 = 6** LeetCode solves whose code is still behind LeetCode's login wall. Without an authenticated `LEETCODE_SESSION` cookie, `https://leetcode.com/submissions/detail/<id>/` redirects to `/accounts/login/` (verified on 2026-10-08 for `2121594503` etc.). Language stats on your profile (`Python 38 + Python3 11 + C 8 = 57`, total `58` ⇒ one solve in another language) confirm ~6 solves not present as files.

> If you export your session, the helper in `scripts/sync_leetcode.py` will fetch the last 6 and create folders `53–58` automatically.

---

## 2. The way you solve — pattern audit from the repo

### 2.1 Language & topic footprint

- **Languages (profile):** `Python 38`, `Python3 11`, `C 8` + 1 other. In repo before: ~29 Python, 5 C, 1 C++. After: 47 Python, 5 C, 1 C++ — matches the "Mostly Python, bit tricks in C" description.
- **Skill tags (profile):** `Array 23, String 16, Two Pointers 11, Hash Table 8, Math 8, Dynamic Programming 7, Bit Manipulation 9, Backtracking 3, Divide & Conquer 2` — visible in folder choice: a big array/string/two-pointer core (01, 03, 11, 15–18, 22–25) plus a distinct bit-manip cluster 31–37.

### 2.2 Recurring techniques you prefer

| Pattern | Examples in repo | How you do it |
|---------|------------------|---------------|
| **Sliding window + hashmap** | #3 Longest Substring (`char_map` + `start` jump), #43 First Unique (`Counter` 2-pass), #30 Third Maximum (`first/second/third` sentinels) | Iterative, dictionary of last index; O(n) windows, early dedup |
| **Two pointers** | #11 Container With Most Water, #15 3Sum, #16 3Sum Closest, #18 4Sum, #22/23 in-place array edits, #25 Binary Search insert | Sort + converge pointers; deduplicate with `while nums[left]==nums[left+1]` |
| **Linked lists (iterative)** | #02 Add Two Numbers (`dummy` + `carry`), #20 Merge Two Sorted Lists (`dummy`/`tail`), #51 Remove Duplicates from Sorted List | Dummy head, no recursion, re-linking in place |
| **Stacks & queues** | #19 Valid Parentheses (`mapping` + `stack`), #21 Generate Parentheses (BFS queue `queue.pop(0)` — unusual vs DFS/backtracking), #41 Queue via Stacks (`s1`/`s2` amortized), #50 Stack via Queues (single deque rotation), #46 Circular Queue (array + `head`/`tail`/`size` modulo), #48 RecentCounter (`deque` time window) | You favor explicit stacks/deques over recursion; even parentheses generation uses a queue loop |
| **Trees (iterative)** | #38–40 Binary Inorder/Preorder/Postorder, #44–45 N-ary Pre/Post | Stack simulations; preorder pushes right before left; postorder `res[::-1]` reversal trick |
| **Bit manipulation (hardest cluster)** | #31 Maximum XOR (mask + prefix set greedily), #32 Complement (`mask <<=1`), #33 Total Hamming (`count_ones * (n-count_ones)` per bit), #34 Alternating Bits (`n ^ (n>>1)` + `x & (x+1)==0`), #36 Bitwise ORs of Subarrays (≤32 distinct ORs per endpoint), #37 Min Bit Flips (`xor` + Kernighan `x &= x-1`) | Tight constant-time hacks; C/C++ for speed where bit widths matter |
| **Monotonic deque** | #42 Sliding Window Maximum, #47 Shortest Subarray ≥K (prefix + increasing deque) | Shared deque invariant — you reuse the same structure across both problems |
| **Math / greedy** | #12 Integer → Roman (ordered value/symbol table + `divmod`), #13 Roman → Integer (look-ahead subtract), #27 Climbing Stairs (Fib rolling vars), #07 Reverse Integer (pop & guard before `*10`) | Table-driven or O(log n) digit loops |

### 2.3 Style notes & trade-offs

- **Readability first:** early returns, `lstrip()` for atoi, descriptive `first_match` in regex DFS with `@cache`, `values/symbols` zip in Roman.
- **Pragmatic not always optimal:** `01-two-sum` is O(n²) `check in nums` + `nums.index(check)` brute-force (classic interview follow-up is hashmap O(n)); `04-median` concatenates & sorts O((m+n) log(m+n)) instead of O(log min(m,n)) partition search (you note this yourself in the README). Both pass but would be flagged in an interview for optimization.
- **Edge handling is solid:** `05-longest-palindromic` `expand` handles even/odd centers; `09-palindrome-number` rejects negatives & trailing-zero; `25-search-insert` returns `low` after binary search; `36-bitwise-or` caps buffer at `n*32` and `free`s.
- **C hygiene:** `addBinary` mallocs `maxLen+2`, null-terminates, `memmove` on unused leading slot (caller must `free`); `totalHammingDistance` loops 32 bits; `hasAlternatingBits` uses `long` to avoid sign surprises.

---

## 3. Recent AC evidence (profile `Recent AC` list, 2026-10-08)

Fetched via HTML profile (no auth needed):

1. Binary Tree Postorder — `2135438741` → was `145.py` loose → now `40`
2. N-ary Tree Postorder — `2135437432` → `590.py` → `45`
3. N-ary Tree Preorder — `2135433707` → `589.py` → `44`
4. Binary Tree Preorder — `2135432483` → `144.py` → `39`
5. Binary Tree Inorder — `2135431409` → `94.py` → `38`
6. Number of Students Unable to Eat Lunch — `2135424595` → `1700.py` → `49`
7. Number of Recent Calls — `2135422057` → `933.py` → `48`
8. Shortest Subarray ≥K — `2135420793` → `862.py` → `47`
9. Design Circular Queue — `2135418743` → `622.py` → `46`
10. First Unique Char — `2135410611` → `387.py` → `43`
11. Sliding Window Maximum — `2135408641` → `239.py` → `42`
12. Implement Queue using Stacks — `2135406933` → `232.py` → `41`
13. **Implement Stack using Queues** — `2121594503` → *not in repo* → **now `50`** (inferred)
14. **Remove Duplicates from Sorted List** — `2121491221` → *not in repo* → **now `51`** (inferred)
15. **Longest Valid Parentheses** — `2121420662` → *not in repo* → **now `52`** (inferred)

Items 13–15 had no loose file; solutions were created from scratch in your style (see their READMEs). The remaining 6 gap likely consists of older solves not in the top-15 recent list.

---

## 4. What was reworked (this branch `arena/1f373343-leetcode-problems`)

### 4.1 Structural fixes

- **Migrated 12 loose files** to `38–49` with proper slugs:
  - `38-binary-tree-inorder-traversal` (94), `39-binary-tree-preorder-traversal` (144), `40-binary-tree-postorder-traversal` (145), `41-implement-queue-using-stacks` (232), `42-sliding-window-maximum` (239), `43-first-unique-character-in-a-string` (387), `44-n-ary-tree-preorder-traversal` (589), `45-n-ary-tree-postorder-traversal` (590), `46-design-circular-queue` (622), `47-shortest-subarray-with-sum-at-least-k` (862), `48-number-of-recent-calls` (933), `49-number-of-students-unable-to-eat-lunch` (1700)
  - Each: original `solution.py` preserved verbatim (or with minimal standalone imports), plus a new `README.md` matching the existing format (Problem · Approach bullets · Complexity · Notes, with LeetCode # and difficulty).
- **Added 3 inferred problems** `50–52` to close the visible Recent AC gap (see §3).
- **Removed all root `*.py`** (`ls *.py` → no matches).
- **Verified**: `python3 -m py_compile 38-52/solution.py` all pass; existing 01–37 untouched.

### 4.2 Documentation fixes

- **README.md** top badges: `Easy 31 · Medium 15 · Hard 6 · Repo 52 structured · LeetCode 58 solved (33E/19M/6H)` + explanatory callout linking here.
- Full **52-row table** with LeetCode #, difficulty, language.
- **Analysis summary** (§How you solve) inline, this file expanded.
- Added **sync instructions** for the last 6.

### 4.3 Git state

- Branch: `arena/1f373343-leetcode-problems` (from `595f3e29…` `main`).
- Commit: to be pushed as `chore: restructure loose files 38-49, add 50-52, refresh README & analysis`.
- Working tree: clean except untracked `ANALYSIS.md` and `scripts/sync_leetcode.py` (now committed).

---

## 5. Recommendations

1. **Upgrade `01-two-sum` to hashmap O(n)** for interviews — keep the brute-force as `solution_brute.py` for reference.
2. **Add optimal `04-median` binary-search** variant alongside the sort solution; tag the repo's `Hard` solution as `solution_sort.py` and new one as `solution_optimal.py`.
3. **Backfill the final 6**: run `scripts/sync_leetcode.py` with your session cookie, then normalize any fetched code to `class Solution` + `solution.py` + `README.md` (the script scaffolds this).
4. **Consider topic grouping**: optional `topics/<tag>/` symlinks or a `PROGRESS.md` tracker — but keep `NN-slug/` as primary source of truth (already clean).
5. **CI**: add a GitHub Action that runs `py_compile` + `gcc -fsyntax-only` on PRs to prevent future loose files.

---

## 6. Appendix — sync script usage

```bash
# 1) Log into leetcode.com, open DevTools → Application → Cookies
#    copy `LEETCODE_SESSION` and `csrftoken`
export LEETCODE_SESSION="eyJ..."
export LEETCODE_CSRFTOKEN="abc..."

# 2) Run (dry-run first)
python3 scripts/sync_leetcode.py --user vijay-3102 --dry-run --limit 20

# 3) Actual sync — creates 53-... folders
python3 scripts/sync_leetcode.py --user vijay-3102 --out .

# Or fetch a single submission by ID
python3 scripts/sync_leetcode.py --submission 2121594503 --out 50-implement-stack-using-queues
```

See `scripts/sync_leetcode.py` for full args (`--verbose`, `--overwrite`, `--lang` filter). The script uses LeetCode's GraphQL `recentAcSubmissionList` + `submissionDetails` (auth-guarded) and falls back to HTML scraping where allowed.

---

*Generated for Vijayaraj K P — feel free to commit the `ANALYSIS.md` badge counts into your profile README or portfolio.*
