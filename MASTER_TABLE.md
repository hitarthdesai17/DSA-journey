# 🗂️ Master Problem Table

Every problem solved in this repo, in one place. Source: root `README.md`'s problem log plus the `PATTERNS.md` deep-dive entries, cross-checked against actual files in the repo.

> **Confidence** here reflects how solid the implementation looks (clean, no leftover bugs, handles edge cases) — not a self-rating, but an assessment from reading the code.

| # | Problem | Difficulty | Pattern | Topic | Time | Space | Status | Repo File | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| LC 1 | Two Sum | Easy | Hashing | Sets/Maps | O(n) | O(n) | ✅ | `SETS/two_sum.py` | High |
| LC 1572 | Matrix Diagonal Sum | Easy | Matrix Traversal | Matrix | O(n) | O(1) | ✅ | `MULTIDIMENSIONAL ARRAYS/sum_diagonal.py` | High |
| LC 867 | Transpose Matrix | Easy | Matrix Traversal | Matrix | O(n²) | O(1) in-place (square) | ✅ | `PROBLEMS ON MATRIX/transpose.py` | High |
| LC 48 | Rotate Image | Medium | Matrix Traversal | Matrix | O(n²) | O(1) | ✅ | `PROBLEMS ON MATRIX/rotate_image.py` | High |
| LC 54 | Spiral Matrix | Medium | Matrix Traversal | Matrix | O(rows×cols) | O(1) extra | ✅ | `PROBLEMS ON MATRIX/spiral_matrix.py` | Medium |
| LC 9 | Palindrome Number | Easy | Math / Strings | Strings | O(log n) | O(1) | ✅ | `STRINGS/` (exact line not isolated) | Medium |
| LC 1832 | Check if the Sentence Is a Pangram | Easy | Hashing | Strings/Sets | O(n) | O(1) (26 letters) | ✅ | Logged in README; file not isolated in this pass | Medium |
| LC 771 | Jewels and Stones | Easy | Hashing | Sets | O(n) | O(n) | ✅ | `SETS/count_jewels_in_stones.py` | High |
| LC 202 | Happy Number | Easy | Hashing (cycle detection) | Sets | O(log n) per pass | O(log n) | ✅ | `SETS/happy_number.py` | High |
| LC 2351 | First Letter to Appear Twice | Easy | Hashing | Maps | O(n) | O(n) | ✅ | `QUESTIONS ON MAP/first_letter_twice.py` | High |
| LC 231 | Power of Two | Easy | Bitwise | Bitwise | O(1) | O(1) | ✅ | `Bitwise and Memory Concepts/power_of_2.py` | High |
| LC 326 | Power of Three | Easy | Bitwise / Math | Bitwise | O(log₃ n) | O(1) | ✅ | Logged in README; not isolated as separate function in this pass | Low — verify |
| LC 342 | Power of Four | Easy | Bitwise | Bitwise | O(1) | O(1) | ✅ | `Bitwise and Memory Concepts/power_of_2.py` (`isPowerofFour`) | High |
| LC 509 | Fibonacci Number | Easy | Recursion | Recursion | O(2ⁿ) naive | O(n) stack | ✅ | `RECURSION-2/fib.py` | Medium — not yet memoized |
| LC 1979 | Find Greatest Common Divisor of Array | Easy | Recursion | Recursion | O(log(min(a,b))) | O(log(min(a,b))) stack | ✅ | `RECURSION - 3/gcd.py` | High |
| LC 204 | Count Primes | Medium | Recursion / Math | Recursion | O(n√n) naive | O(n) worst | ✅ | `RECURSION - 4/count_prime.py` | Medium — Sieve would be faster |
| LC 69 | Sqrt(x) | Easy | Recursion / Binary Search | Recursion | O(log n) | O(log n) stack | ✅ | `RECURSION - 4/sqrt(n).py` | High |
| LC 50 | Pow(x, n) | Medium | Recursion | Recursion | O(log n) | O(log n) stack | ✅ | Logged in README; not isolated as separate file in this pass | Low — verify |
| LC 15 | 3Sum | Medium | Two Pointers | Arrays | O(n²) | O(n) or O(1) | ✅ | `PROBLEM AND MERGE SORT/3_sum.py` | High |
| — | Merge Sort | — | Divide & Conquer | Sorting | O(n log n) | O(n) | ✅ | `PROBLEM AND MERGE SORT/merge_sort.py` | High |
| — | Merge Sorted Array (two-array merge) | Easy | Two Pointers | Arrays | O(n+m) | O(n+m) | ✅ | `ADVANCE ARRAY PROBLEMS/merge_sort_array.py` | High |
| — | Quick Sort | — | Divide & Conquer | Sorting | O(n log n) avg | O(log n) | ✅ | `QUICK SORT/quick_sort.py` | High |
| LC 268 | Missing Number | Easy | Cyclic Sort / Swap | Sorting | O(n) | O(1) | ✅ | `QUICK SORT/missing_number.py` | High |
| — | Cyclic Sort | — | Cyclic Sort | Sorting | O(n) | O(1) | ✅ | `CYCLIC SORT/cyclic_sort.py` | High |
| LC 448 | Find All Numbers Disappeared in an Array | Easy | Cyclic Sort | Sorting | O(n) | O(1) extra | ✅ | `CYCLIC SORT/disappearing_numbers.py` | High |
| LC 35 | Search Insert Position | Easy | Binary Search | Searching | O(log n) | O(1) | ✅ | `BINARY SEARCH/search_insert_pos.py` | High |
| LC 34 | Find First and Last Position of Element in Sorted Array | Medium | Binary Search | Searching | O(log n) | O(1) | ✅ | `BINARY SEARCH/first_last_pos.py` | High |
| LC 53 | Maximum Subarray | Medium | Kadane's Algorithm | Arrays | O(n) | O(1) | ✅ | `ADVANCE ARRAY PROBLEMS - 2/max_subarray.py` | High |
| LC 169 | Majority Element | Easy | Boyer-Moore Voting | Arrays | O(n) | O(1) | ✅ | `ADVANCE ARRAY PROBLEMS - 2/majority_element.py` | High |
| LC 75 | Sort Colors | Medium | Two Pointers (Dutch Flag) | Arrays | O(n) | O(1) | ✅ | `ADVANCE ARRAY PROBLEMS - 3/sort_colours.py` | High |
| LC 11 | Container With Most Water | Medium | Two Pointers | Arrays | O(n) | O(1) | ✅ | `ADVANCE ARRAY PROBLEMS - 3/most_water.py` | High |
| LC 42 | Trapping Rain Water | Hard | Precompute + scan | Arrays | O(n) | O(n) | ✅ | `ADVANCE ARRAY PROBLEMS - 3/trap_rain_water.py` | High |
| LC 2418 | Sort the People | Easy | Hashing + Sort | Maps | O(n log n) | O(n) | ✅ | `QUESTIONS ON MAP/sort_people.py` | Medium — assumes unique heights |

---

## Notes

- Rows marked **"not isolated in this pass"** are logged in the original root README's problem log but weren't matched to a specific standalone file during this audit — likely solved inline in a multi-problem file (e.g. `STRINGS/problems.py` contains several string problems in one script). Worth splitting into individual files for traceability next time you're in that folder.
- This table only includes problems with a clear LeetCode number or a clearly-named non-LeetCode algorithm (e.g. raw Merge Sort/Quick Sort implementations). Foundational practice files (loops, patterns, calculator, etc.) are intentionally excluded — see `ROADMAP.md` Phase 1 for those.

---

*Update this table by appending rows, not rewriting it — keeps git diffs readable and preserves the order problems were actually solved in.*
