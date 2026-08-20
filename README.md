# LeetCode Solutions — Problem Folders

37 classic LeetCode problems, each in its own numbered folder.

Every folder contains:

| File | Contents |
|---|---|
| `solution.py` / `solution.c` / `solution.cpp` | The code snippet for the problem |
| `README.md` | Brief details: problem summary, how the approach works, complexity, and notes |

## Index

| # | Folder | Problem (LeetCode) | Lang | Difficulty | Approach in one line |
|---|---|---|---|---|---|
| 01 | `01-two-sum` | Two Sum (#1) | Python | Easy | Complement lookup with in-list search |
| 02 | `02-add-two-numbers` | Add Two Numbers (#2) | Python | Medium | Digit-wise list addition with carry |
| 03 | `03-longest-substring-without-repeating-characters` | Longest Substring Without Repeating Characters (#3) | Python | Medium | Sliding window + last-seen index map |
| 04 | `04-median-of-two-sorted-arrays` | Median of Two Sorted Arrays (#4) | Python | Hard | Merge, sort, take the middle |
| 05 | `05-longest-palindromic-substring` | Longest Palindromic Substring (#5) | Python | Medium | Expand around every center |
| 06 | `06-zigzag-conversion` | Zigzag Conversion (#6) | Python | Medium | Simulate rows with a direction step |
| 07 | `07-reverse-integer` | Reverse Integer (#7) | Python | Easy | Digit extraction & rebuild with overflow guard |
| 08 | `08-string-to-integer-atoi` | String to Integer (atoi) (#8) | Python | Medium | Strip, read sign, scan digits, clamp |
| 09 | `09-palindrome-number` | Palindrome Number (#9) | Python | Easy | Reverse only the second half numerically |
| 10 | `10-regular-expression-matching` | Regular Expression Matching (#10) | Python | Hard | Memoized DFS with the `*` case split |
| 11 | `11-container-with-most-water` | Container With Most Water (#11) | Python | Medium | Two pointers, always move the shorter |
| 12 | `12-integer-to-roman` | Integer to Roman (#12) | Python | Medium | Greedy table incl. subtractive pairs |
| 13 | `13-roman-to-integer` | Roman to Integer (#13) | Python | Easy | Add/subtract based on the next value |
| 14 | `14-longest-common-prefix` | Longest Common Prefix (#14) | Python | Easy | Compare first & last after sorting |
| 15 | `15-3sum` | 3Sum (#15) | Python | Medium | Sort + fix one index + two pointers, dedupe |
| 16 | `16-3sum-closest` | 3Sum Closest (#16) | Python | Medium | Sort + two pointers minimizing the diff |
| 17 | `17-letter-combinations-of-a-phone-number` | Letter Combinations of a Phone Number (#17) | Python | Medium | Iterative prefix expansion |
| 18 | `18-4sum` | 4Sum (#18) | Python | Medium | Sort + two nested loops + two pointers |
| 19 | `19-valid-parentheses` | Valid Parentheses (#20) | Python | Easy | Stack of openers |
| 20 | `20-merge-two-sorted-lists` | Merge Two Sorted Lists (#21) | Python | Easy | Dummy-node merge of two lists |
| 21 | `21-generate-parentheses` | Generate Parentheses (#22) | Python | Medium | BFS with open/close counts |
| 22 | `22-remove-duplicates-from-sorted-array` | Remove Duplicates from Sorted Array (#26) | Python | Easy | Slow/fast two pointers |
| 23 | `23-remove-element` | Remove Element (#27) | Python | Easy | Write-pointer in-place compaction |
| 24 | `24-implement-strstr` | Implement strStr() (#28) | Python | Easy | Brute-force sliding window |
| 25 | `25-search-insert-position` | Search Insert Position (#35) | Python | Easy | Binary search; `low` is the insert index |
| 26 | `26-add-binary` | Add Binary (#67) | C | Easy | Add from the ends with a carry |
| 27 | `27-climbing-stairs` | Climbing Stairs (#70) | Python | Easy | Iterative Fibonacci DP |
| 28 | `28-merge-sorted-array` | Merge Sorted Array (#88) | C | Easy | Merge backwards from the end |
| 29 | `29-majority-element` | Majority Element (#169) | Python | Easy | Boyer-Moore majority vote |
| 30 | `30-third-maximum-number` | Third Maximum Number (#414) | Python | Easy | Track top-3 distinct values |
| 31 | `31-maximum-xor-of-two-numbers-in-an-array` | Maximum XOR of Two Numbers in an Array (#421) | Python | Medium | Bit-by-bit greedy with prefix sets |
| 32 | `32-number-complement` | Number Complement (#476) | C++ | Easy | Build a full-width mask, then XOR |
| 33 | `33-total-hamming-distance` | Total Hamming Distance (#477) | C | Medium | Per-bit `ones × zeros` counting |
| 34 | `34-alternating-bits` | Alternating Bits (#693) | C | Easy | Power-of-two test on `n ^ (n >> 1)` |
| 35 | `35-one-bit-character` | One Bit Character (#717) | Python | Easy | Decode with step 1 or 2 from the front |
| 36 | `36-bitwise-or-of-array-ranges` | Bitwise OR of Array Ranges (#848) | C | Hard | Distinct ORs per right endpoint |
| 37 | `37-minimum-bit-flips-to-convert-number` | Minimum Bit Flips to Convert Number (#1318) | Python | Easy | Popcount of `start ^ goal` |

## Notes on the snippets

- **Python** files that referenced `List` / `Optional` without imports had the needed `typing` import added so they run standalone.
- **Linked-list** problems (02, 20) include a local `ListNode` class so the snippet runs outside LeetCode (the judge provides it there).
- **C** files that used `malloc` / `strlen` / `qsort` / `memmove` had the matching `<stdlib.h>` / `<string.h>` includes added for standalone compilation.
- Code was kept as provided; the README `Notes` section in each folder flags any behavioural caveats (e.g. O(n²) brute-force variants, in-place input mutation).
