# 📓 Learning Journal

The evolution of this repo, topic by topic — written from what the commit history and code actually show, not retrofitted. This is the file worth re-reading most, since it's the part a templated repo can't fake.

---

### Foundations (Jun 11 – Jun 14)

**What happened:** Five days, six+ commits, moving fast through operators → conditionals → loops → nested loops → pattern printing. Commit messages shift from declarative ("Fundamentals of Language") to corrective ("Added Some patterns, alternatives, and corrections") by day 4 — a sign of iterating on pattern-printing logic until it actually worked rather than getting it right the first time.

**Insight:** Pattern printing (`NESTED LOOPING`, `NESTED LOOPING 2`) is where nested-loop intuition actually gets tested — it's easy to "understand" loops abstractly and still get the row/column relationship wrong on a triangle pattern.

---

### Arrays Phase Begins (Jun 19 – Jun 22)

**Gap noted:** Five days between the foundations phase and array work starting (Jun 14 → Jun 19) — first visible break in the otherwise daily cadence.

**What happened:** Array basics, then "Solved some basic array problems," then "Completed array basics" the next day — three separate passes at the same folder before moving on, suggesting array fundamentals took more than one sitting to feel solid.

**Same day:** Linear Search and Binary Search both landed Jun 22 — binary search introduced immediately after linear search, with the contrast (O(n) vs O(log n)) likely the point of pairing them.

---

### Sorting Fundamentals (Jun 23)

**What happened:** Bubble Sort, Selection Sort, and Insertion Sort all committed on the same day, with bubble sort split into its own commit before the combined "Completed Bubble, Selection and Insertion Sort" commit — looks like bubble sort was understood first and the other two came faster once the swap-based mental model was in place.

**Pattern recognition forming:** This is the day before merge/quick/cyclic sort show up (Jun 30 – Jul 1), so the O(n²) sorts were deliberately done first as a baseline before the faster divide-and-conquer approaches.

---

### Matrix / Multidimensional Arrays (Jun 23 – Jun 24)

**What happened:** "Started Multidimension array" → "Basic Operations on multidimensional array" → two separate "Completed Leetcode Questions" commits same day (Jun 24). The repeated commit message suggests multiple matrix problems (rotate, spiral, transpose, diagonal sum) were solved in one extended session.

**Mistake worth noting from the code itself:** `rotate_image.py` has a commented-out alternative implementation (row-by-row reversal) left in the file alongside the transpose-then-reverse approach that was kept — a record of trying one approach, then switching to a cleaner one without deleting the evidence. That's worth preserving rather than cleaning up; it shows the comparison was made deliberately.

---

### Strings & Sets (Jun 25 – Jun 26)

**What happened:** Strings (reversal, ASCII case toggling) on Jun 25, then Sets and hashing the next day, with two near-duplicate "Learnt About Bitwise Operators and memory" commits on Jun 26 — likely a small follow-up fix or amendment rather than two separate learning sessions.

**Aha moment (from the code):** `two_sum.py` checks the complement against the map *before* inserting the current number. This ordering is the actual insight of the hashing pattern over brute force — get it backwards and an element can pair with itself.

---

### Recursion (Jun 27 – Jun 28)

**What happened:** Recursion fundamentals Jun 27, then a dense Jun 28 — Fibonacci, "Practicing Recursion Questions," and "Solved pow, sqrt, prime numbers" all same day.

**Mistake → correction, visible in the code:** `RECURSION - 3/gcd.py` keeps all three GCD approaches in one file — brute-force decrementing search, subtraction-based, and Euclidean — rather than just keeping the final answer. That's a direct record of recognizing the brute-force version works but is slow, and deliberately working up to the Euclidean algorithm instead of jumping straight to it.

---

### Array Problems & Merge Sort (Jun 29 – Jun 30)

**What happened:** "Solved 3 leetcode array questions" → "Solved Leetcode questions and different algo" → "Solved Array Questions" → "Solved 3Sum and learn Merge Sort Algo," each as a separate commit across two days. The granularity increased here — more, smaller commits instead of one big "completed X" commit, suggesting each problem (Kadane's, Boyer-Moore, container with most water, trapping rain water, 3Sum) was committed close to when it was solved rather than batched.

**Recognition trick learned:** 3Sum is two-pointer applied to a sorted array — same family as container-with-most-water, just with an extra fixed index and duplicate-skipping logic layered on top.

---

### Quick Sort & Cyclic Sort (Jul 1)

**What happened:** Both committed the same day — "Quick Sort Completed" then "CYclic Sort and Its Problem" (note the typo, left as-is, a small honest artifact of moving fast).

**Recognition trick (from the cyclic sort notes themselves):** the repo's own `readme.md` for this folder states it plainly — *"Whenever you hear 'numbers are from 1 to n,' think Cyclic Sort."* That's the kind of trigger phrase this whole journal exists to capture.

**Swap logic, and the bug it avoids:** Both `cyclic_sort.py` and the quick-sort folder's `missing_number.py` use the same idea — swap a number to its correct index unless it's already correct, then move on. The common bug (confirmed by checking the code) is incrementing the pointer unconditionally instead of only in the "already correct" branch, which causes elements to get skipped before they're properly placed.

---

### Binary Search, Round 2 (Jul 1)

**What happened:** Same day as quick/cyclic sort — "Solved Some binary Search questions," going beyond the basic linear/binary search from `ADVANCED ARRAYS/` into insertion-point and first/last-occurrence variants.

**Pattern recognition:** Binary search isn't one algorithm — it's a boundary-narrowing technique that changes its narrowing condition based on what you're looking for (existence vs. insertion point vs. first/last occurrence). The two-pass approach in `first_last_pos.py` (search for start, then search for end, reusing the same helper) is the cleanest way to see that.

---

## Open Questions / Doubts Worth Revisiting

- When does cyclic sort's O(1)-space approach actually beat a hash-set approach in practice, beyond the range constraint being satisfied? Worth a deliberate comparison.
- Quick sort's worst-case O(n²) on sorted input — randomized pivot selection hasn't been implemented yet. Good next addition to the `QUICK SORT/` folder.
- No sliding window problems yet, despite several two-pointer problems bordering on it (Container With Most Water is adjacent). Worth doing a deliberate sliding-window session next to see where the line actually is.

---

*This file should grow with every learning session, not just every "completed" milestone — half-finished attempts and corrected mistakes are exactly what make this useful to read later.*
