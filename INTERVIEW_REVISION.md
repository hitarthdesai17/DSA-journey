# 🌙 Interview Revision — One Night Before

Skim top to bottom once. This isn't for learning — it's for triggering recognition on patterns already covered in this repo (`PATTERNS.md` has the full version with code).

---

## 1. Pattern Recognition — What's Actually Covered Here

| Signal in the problem | Pattern | Where in repo |
|---|---|---|
| "Numbers are from 1 to n" / "find missing/duplicate in range" | **Cyclic Sort** | `CYCLIC SORT/` |
| Sorted array, need an index or insertion point | **Binary Search** | `BINARY SEARCH/`, `ADVANCED ARRAYS/` |
| Need to sort, no extra space, divide problem in half | **Quick Sort / Merge Sort** | `QUICK SORT/`, `PROBLEM AND MERGE SORT/` |
| Pair/triplet sum in array, opposite-end scanning | **Two Pointers** | `ADVANCE ARRAY PROBLEMS/`, `PROBLEM AND MERGE SORT/` (3Sum) |
| Counting, frequency, "have I seen this before" | **Hashing (Set/Map)** | `SETS/`, `QUESTIONS ON MAP/` |
| Need O(1) extra info about presence/count | **Set / Dict lookup** | `SETS/` |
| Self-similar subproblem (factorial, GCD, sqrt) | **Recursion** | `RECURSION/` through `RECURSION - 4/` |
| Power-of-two checks, fast halving/doubling | **Bitwise tricks** | `Bitwise and Memory Concepts/` |
| 2D grid manipulation (rotate, transpose, spiral) | **Matrix traversal** | `PROBLEMS ON MATRIX/`, `MULTIDIMENSIONAL ARRAYS/` |

**Not yet covered — don't pretend to know these cold:** Sliding Window, Backtracking, Linked Lists, Trees, Graphs, Dynamic Programming. If asked, be honest about where you are rather than bluffing a template.

---

## 2. Recognition Tricks (from your own notes)

- **Cyclic Sort** — the moment you hear *"numbers are from 1 to n"* or *"every number appears once except..."*, think Cyclic Sort before anything else. The trick: a number `v` belongs at index `v - 1`.
- **Quick Sort intuition** — pick a pivot, smaller elements left, larger elements right, recurse on each half. Think "class monitor" sorting students by height.
- **Binary Search variants** — not just "find the target." Also: find insertion point, find first/last occurrence. The boundary condition (`<` vs `<=`, `mid` vs `mid+1`) is where bugs live — re-derive it on paper, don't recite it.
- **Two Pointers** — sorted array + need a pair/triplet that sums to something → start pointers at both ends and move inward based on comparison to target.

---

## 3. Complexity Cheat Sheet

| Operation | Time | Space |
|---|---|---|
| Array access | O(1) | — |
| Array insert/delete (middle) | O(n) | — |
| Set/Dict get, set, "in" check | O(1) avg | O(n) |
| Bubble / Selection / Insertion Sort | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) avg, O(n²) worst | O(log n) |
| Cyclic Sort | O(n) | O(1) |
| Binary Search | O(log n) | O(1) |
| Recursion (linear, e.g. factorial) | O(n) | O(n) call stack |

---

## 4. Common Pitfalls (worth re-checking before you code)

- Binary search off-by-one: decide up front whether `right = len(nums)` or `len(nums) - 1`, and stay consistent.
- Cyclic Sort infinite-loop bug: forgetting the swap condition check (`nums[i] != nums[correct_index]`) before swapping.
- Quick Sort worst case: already-sorted input with a naive pivot choice degrades to O(n²) — mention this if asked about pivot selection.
- Two Sum / 3Sum: using a hash set is O(n) but breaks the "sorted + two pointers" approach if the array needs to stay in original order for the output indices.
- Recursion: always state the base case out loud before writing the recursive call — it's the easiest thing to forget under interview pressure.

---

## 5. Python Syntax Reminders

- Tuple swap: `a, b = b, a`
- `set()` for O(1) "have I seen this" checks
- `dict.get(key, default)` to avoid `KeyError` checks
- Bit check for power of two: `n > 0 and (n & (n - 1)) == 0`
- List slicing for reversal: `arr[::-1]`
- `sorted(arr, key=lambda x: ...)` for custom sort order

---

## 6. Last-Minute Reminders

- Say your approach out loud before coding — even a rough one.
- State time/space complexity at the end without being asked.
- Ask about edge cases early: empty array, single element, duplicates, already sorted.
- If you don't know a pattern (sliding window, trees, DP — see section 1), say so and reason from first principles rather than guessing a template. Interviewers respect that more than a wrong confident answer.

---

*Update this file as new patterns get added to the repo — see `PATTERNS.md` for the full reference each entry here is pulled from.*
