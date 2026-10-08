<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:f7971e,50:ffb733,100:ffd200&height=190&section=header&text=LeetCode%20Problems&fontSize=50&fontColor=1a1a1a&animation=fadeIn&desc=Data%20Structures%20%26%20Algorithms%20Practice&descSize=18&descColor=1a1a1a&descAlignY=60"/>

<div align="center">

My hand-curated DSA practice — one folder per problem with a working solution and a short explanation.

<br/>

[![LeetCode](https://img.shields.io/badge/LeetCode-vijay--3102-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/vijay-3102/)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)

<br/>

![Easy](https://img.shields.io/badge/Easy-29-brightgreen?style=for-the-badge)
![Medium](https://img.shields.io/badge/Medium-15-orange?style=for-the-badge)
![Hard](https://img.shields.io/badge/Hard-5-red?style=for-the-badge)
![Total](https://img.shields.io/badge/Repo-49%20structured-2EA8E0?style=for-the-badge)
![LeetCode Solved](https://img.shields.io/badge/LeetCode-58%20solved%20(33E%2F19M%2F6H)-FFA116?style=for-the-badge)

</div>

> **Profile vs Repo:** [LeetCode @vijay-3102](https://leetcode.com/u/vijay-3102/) shows **58 solved** (33 Easy · 19 Medium · 6 Hard, 98 submissions, 63.27% acceptance). This repo now holds **49 fully structured** solutions — the previous **37 curated folders + 12 loose `*.py` files** have been migrated to `NN-slug/` (`38–49`). **9 LeetCode submissions** remain to be added manually — just create the next `NN-slug/` folder with `solution.py` + `README.md` (see template below). Full audit in [ANALYSIS.md](ANALYSIS.md).

---

## 📂 Structure

```
NN-problem-slug/
├── solution.py      # ✅ working solution (Python / C / C++)
└── README.md        # approach · complexity · notes
```

No loose `*.py` files at the root — every solution lives in its folder. Works with `python3 NN-*/solution.py` (or `gcc` for C).

Example:

```bash
python3 01-two-sum/solution.py
python3 38-binary-tree-inorder-traversal/solution.py
```

**To add the next problem manually (your preference):**

```bash
mkdir -p 50-implement-stack-using-queues
# paste your LeetCode code into solution.py
# copy any existing README.md as template, update title / LeetCode # / difficulty
```

## 📊 What's inside (49)

| # | LeetCode | Title | Difficulty | Lang |
|---|----------|-------|------------|------|
| 01 | 1 | Two Sum | Easy | Python |
| 02 | 2 | Add Two Numbers | Medium | Python |
| 03 | 3 | Longest Substring Without Repeating Characters | Medium | Python |
| 04 | 4 | Median of Two Sorted Arrays | Hard | Python |
| 05 | 5 | Longest Palindromic Substring | Medium | Python |
| 06 | 6 | Zigzag Conversion | Medium | Python |
| 07 | 7 | Reverse Integer | Easy | Python |
| 08 | 8 | String to Integer (atoi) | Medium | Python |
| 09 | 9 | Palindrome Number | Easy | Python |
| 10 | 10 | Regular Expression Matching | Hard | Python |
| 11 | 11 | Container With Most Water | Medium | Python |
| 12 | 12 | Integer to Roman | Medium | Python |
| 13 | 13 | Roman to Integer | Easy | Python |
| 14 | 14 | Longest Common Prefix | Easy | Python |
| 15 | 15 | 3Sum | Medium | Python |
| 16 | 16 | 3Sum Closest | Medium | Python |
| 17 | 17 | Letter Combinations of a Phone Number | Medium | Python |
| 18 | 18 | 4Sum | Medium | Python |
| 19 | 20 | Valid Parentheses | Easy | Python |
| 20 | 21 | Merge Two Sorted Lists | Easy | Python |
| 21 | 22 | Generate Parentheses | Medium | Python |
| 22 | 26 | Remove Duplicates from Sorted Array | Easy | Python |
| 23 | 27 | Remove Element | Easy | Python |
| 24 | 28 | Find the Index of First Occurrence (strStr) | Easy | Python |
| 25 | 35 | Search Insert Position | Easy | Python |
| 26 | 67 | Add Binary | Easy | C |
| 27 | 70 | Climbing Stairs | Easy | Python |
| 28 | 88 | Merge Sorted Array | Easy | C |
| 29 | 169 | Majority Element | Easy | Python |
| 30 | 414 | Third Maximum Number | Easy | Python |
| 31 | 421 | Maximum XOR of Two Numbers in an Array | Medium | Python |
| 32 | 476 | Number Complement | Easy | C++ |
| 33 | 477 | Total Hamming Distance | Medium | C |
| 34 | 693 | Alternating Bits | Easy | C |
| 35 | 717 | One Bit and Two Bit Characters | Easy | Python |
| 36 | 848 | Bitwise ORs of Subarrays | Hard | C |
| 37 | 1318 | Minimum Bit Flips to Convert Number | Easy | Python |
| **38** | 94 | Binary Tree Inorder Traversal | Easy | Python |
| **39** | 144 | Binary Tree Preorder Traversal | Easy | Python |
| **40** | 145 | Binary Tree Postorder Traversal | Easy | Python |
| **41** | 232 | Implement Queue using Stacks | Easy | Python |
| **42** | 239 | Sliding Window Maximum | Hard | Python |
| **43** | 387 | First Unique Character in a String | Easy | Python |
| **44** | 589 | N-ary Tree Preorder Traversal | Easy | Python |
| **45** | 590 | N-ary Tree Postorder Traversal | Easy | Python |
| **46** | 622 | Design Circular Queue | Medium | Python |
| **47** | 862 | Shortest Subarray with Sum at Least K | Hard | Python |
| **48** | 933 | Number of Recent Calls | Easy | Python |
| **49** | 1700 | Number of Students Unable to Eat Lunch | Easy | Python |

*Bold 38–49 migrated from former loose files (`144.py`, `145.py`, `94.py`, `232.py`, `239.py`, `387.py`, `589.py`, `590.py`, `622.py`, `862.py`, `933.py`, `1700.py`). Next slots `50+` are ready for your manual uploads.*

---

## 🧠 Topics Covered

<p align="center">
<img src="https://img.shields.io/badge/Arrays-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Strings-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Two%20Pointers-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Hash%20Tables-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Linked%20Lists-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Stacks%20%26%20Queues-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Recursion%20%26%20Backtracking-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Bit%20Manipulation-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Dynamic%20Programming-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Binary%20Search-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Trees-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Sliding%20Window-3776AB?style=flat-square"/>
<img src="https://img.shields.io/badge/Design-3776AB?style=flat-square"/>
</p>

## 🔍 How you solve (analysis summary)

> Full audit in **[ANALYSIS.md](ANALYSIS.md)**.

- **Idiomatic Python first** (`Python 38 + Python3 11` on profile), **C/C++ for bit tricks** (8× C, plus `solution.cpp`). Your bit manipulation suite is the strongest cluster (9× tagged on LeetCode).
- **Pattern reuse:** sliding window + hashmap (#3, #30, #43), two pointers (#11, #15–16, #18), Boyer-Moore voting (#29), monotonic deque (#42/#47), counter shortcut (#49), iterative tree stacks (#38–40, #44–45) — not recursion — to avoid depth limits.
- **Pragmatic over optimal at times:** e.g., `01-two-sum` is O(n²) `in` + `index` brute-force (not hashmap O(n)), `04-median` merges & sorts O((m+n) log(m+n)) instead of binary-search O(log min). Works, but flagged for upgrade.
- **Strengths:** bit hacks (`n ^ (n>>1)` + `x & (x+1)` for alternating bits), prefix-monotonic queue for #862, BFS queue for #21 Generate Parentheses, clean circular buffer (#46).

## 🚀 Run

```bash
python3 01-two-sum/solution.py
python3 38-binary-tree-inorder-traversal/solution.py
# C examples
gcc 26-add-binary/solution.c -o /tmp/addBinary && /tmp/addBinary
gcc 33-total-hamming-distance/solution.c -o /tmp/hamming && /tmp/hamming
```

<sub>Mostly **Python**, with a few solutions in **C/C++**. Former loose files now structured. Auto-synced archive note: [MY-LEETCODE](https://github.com/Vijayaraj-IHT/MY-LEETCODE) (404 — may be private).</sub>

---

<div align="center">

**Consistency over intensity · [Vijayaraj K P](https://github.com/Vijayaraj-IHT)**

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:ffd200,50:ffb733,100:f7971e&height=110&section=footer"/>
