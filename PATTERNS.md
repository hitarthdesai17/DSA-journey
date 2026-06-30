# 🧩 Patterns

Every pattern actually implemented in this repo, with the real template pulled from the corresponding file — not generic boilerplate. Problems list links back to the repo file. See `INTERVIEW_REVISION.md` for the condensed night-before version of this file.

---

## Cyclic Sort

**Recognition:** Numbers confined to a range `1..n` (or `0..n-1`), each expected to appear once. Triggered by phrases like "missing number," "duplicate number," "set mismatch."

**Template** (`CYCLIC SORT/cyclic_sort.py`):
```python
def cyclicSort(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    return nums
```

**Variant — find all missing numbers** (`CYCLIC SORT/disappearing_numbers.py`): run the same placement pass, then scan for `nums[i] != i + 1`.

| Complexity | Value |
|---|---|
| Time | O(n) |
| Space | O(1) |

**Problems solved:** Cyclic Sort (basic), Find All Numbers Disappeared in an Array

**Common mistakes:**
- Forgetting to check `nums[i] != nums[correct]` before swapping — causes an infinite loop when a duplicate is already in place.
- Mixing up `i += 1` (only happens in the `else` branch) — incrementing unconditionally skips the just-swapped element.

**Interview tip:** State out loud why this beats sorting — O(n) instead of O(n log n) — *because* the range constraint lets you compute the correct index directly.

**Related patterns:** Hashing (alternative O(n) approach using a set, but O(n) extra space instead of O(1))

---

## Binary Search

**Recognition:** Sorted array. Need an index, an insertion point, or a boundary (first/last occurrence).

**Template — search insert position** (`BINARY SEARCH/search_insert_pos.py`):
```python
def searchInsert(nums, target):
    f, l = 0, len(nums) - 1
    while f <= l:
        mid = (f + l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            f = mid + 1
        else:
            l = mid - 1
    return f
```

**Variant — first/last occurrence** (`BINARY SEARCH/first_last_pos.py`): run binary search twice, narrowing `last = mid - 1` on a match when searching for the start, and `first = mid + 1` when searching for the end.

| Complexity | Value |
|---|---|
| Time | O(log n) |
| Space | O(1) |

**Problems solved:** Search Insert Position (LeetCode 35), Find First and Last Position of Element in Sorted Array (LeetCode 34)

**Common mistakes:**
- Inconsistent boundary convention — decide once whether `l = len(nums) - 1` (closed interval, `<=` loop) or `l = len(nums)` (half-open, `<` loop), and don't mix them mid-function.
- For the first/last variant: forgetting that a match doesn't mean "done" — you have to keep narrowing toward the boundary instead of returning immediately.

**Interview tip:** Binary search variants (search on answer, rotated array search) all reduce to "what does my comparison function return," not memorizing different code per variant.

**Related patterns:** Search on Answer, Rotated Array Search — not yet implemented in this repo.

---

## Quick Sort (Divide & Conquer)

**Recognition:** Need to sort in place without the O(n) extra space merge sort requires; comfortable with average-case O(n log n) and willing to accept worst-case O(n²) risk.

**Template** (`QUICK SORT/quick_sort.py`):
```python
def findPivotIndex(arr, first, last):
    pivot = arr[last]
    i = first - 1
    for j in range(first, last):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[last] = arr[last], arr[i]
    return i

def quickSort(arr, first, last):
    if first >= last:
        return
    pIdx = findPivotIndex(arr, first, last)
    quickSort(arr, first, pIdx - 1)
    quickSort(arr, pIdx + 1, last)
```

**Variant — missing number via cyclic-sort-style swap** (`QUICK SORT/missing_number.py`) — included in this folder because it uses the same in-place swap-to-correct-position idea as the pivot partitioning above.

| Complexity | Value |
|---|---|
| Time | O(n log n) avg, O(n²) worst |
| Space | O(log n) (recursion stack) |

**Problems solved:** Quick Sort (from scratch), Missing Number (LeetCode 268)

**Common mistakes:**
- Choosing the last element as pivot on an already-sorted (or reverse-sorted) array degrades to O(n²) — know this trade-off and mention randomized pivot selection as a fix if asked.
- Off-by-one on the partition boundary (`i = first - 1` start) — easy to break when adapting from memory under pressure.

**Interview tip:** Be ready to explain *why* quicksort is usually preferred over merge sort in practice (in-place, better cache locality) despite the worse worst-case.

**Related patterns:** Merge Sort (stable, guaranteed O(n log n), but O(n) space)

---

## Merge Sort

**Recognition:** Need guaranteed O(n log n) regardless of input order, and stability matters, or you're merging two already-sorted sequences.

**Template — merging two sorted arrays** (`ADVANCE ARRAY PROBLEMS/merge_sort_array.py`):
```python
i = k = j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        ans[k] = arr1[i]; i += 1
    else:
        ans[k] = arr2[j]; j += 1
    k += 1
while i < len(arr1):
    ans[k] = arr1[i]; i += 1; k += 1
while j < len(arr2):
    ans[k] = arr2[j]; j += 1; k += 1
```

| Complexity | Value |
|---|---|
| Time | O(n log n) (O(n) for the merge step alone) |
| Space | O(n) |

**Problems solved:** Merge Sort, Merge Sorted Array

**Common mistakes:**
- Forgetting the two trailing `while` loops that flush whatever's left in the non-exhausted array.

**Related patterns:** Quick Sort

---

## Two Pointers

**Recognition:** Sorted (or sortable) array, looking for a pair/triplet matching a condition, or scanning from both ends toward the middle.

**Template — 3Sum** (`PROBLEM AND MERGE SORT/3_sum.py`):
```python
nums.sort()
for i in range(len(nums) - 2):
    if i != 0 and nums[i - 1] == nums[i]:
        continue
    j, k = i + 1, len(nums) - 1
    while j < k:
        total = nums[i] + nums[j] + nums[k]
        if total == 0:
            ans.append([nums[i], nums[j], nums[k]])
            j += 1; k -= 1
            while j < k and nums[j - 1] == nums[j]: j += 1
            while j < k and nums[k + 1] == nums[k]: k -= 1
        elif total < 0:
            j += 1
        else:
            k -= 1
```

**Variant — container with most water** (`ADVANCE ARRAY PROBLEMS - 3/most_water.py`): pointers start at both ends, always move the pointer at the shorter wall inward, since moving the taller one can never improve the area.

**Variant — Dutch National Flag / sort colors** (`ADVANCE ARRAY PROBLEMS - 3/sort_colours.py`): three pointers (`i`, `j`, `k`) partition into three regions in one pass.

| Complexity | Value |
|---|---|
| Time | O(n log n) for 3Sum (sort dominates), O(n) for most-water and sort-colors |
| Space | O(1) extra (excluding output) |

**Problems solved:** 3Sum (LeetCode 15), Container With Most Water, Sort Colors (LeetCode 75)

**Common mistakes:**
- 3Sum: forgetting the duplicate-skip `while` loops after a match — without them you get duplicate triplets.
- Container With Most Water: trying to move both pointers or the taller one — only the shorter wall can ever be the bottleneck, so only it should move.

**Interview tip:** When a brute force is O(n²) or O(n³) and the array can be sorted without losing needed information, two pointers is almost always the first thing to try.

**Related patterns:** Sliding Window (not yet implemented — the natural next pattern once a fixed-size or variable-size subarray condition appears)

---

## Hashing (Sets / Maps)

**Recognition:** Need O(1) "have I seen this" lookups, frequency counting, or complement checks.

**Template — Two Sum** (`SETS/two_sum.py`):
```python
numMap = {}
for i in range(len(nums)):
    complement = target - nums[i]
    if complement in numMap:
        return [numMap[complement], i]
    numMap[nums[i]] = i
return []
```

**Variant — cycle detection via seen-set** (`SETS/happy_number.py`): a `set()` tracks every sum seen so far; revisiting a sum means you're in a cycle that will never reach 1.

| Complexity | Value |
|---|---|
| Time | O(n) |
| Space | O(n) |

**Problems solved:** Two Sum (LeetCode 1), Happy Number (LeetCode 202), Jewels and Stones, First Letter to Appear Twice

**Common mistakes:**
- Computing the complement against the target *before* checking the map, but inserting the current number *after* — get this order backwards and you can match an element with itself.

**Interview tip:** Hashing trades O(n) space for O(1) lookups — always state that trade-off explicitly; it's the most common follow-up question ("can you do it without extra space?").

**Related patterns:** Cyclic Sort (O(1)-space alternative when the range constraint `1..n` holds)

---

## Bitwise Tricks

**Recognition:** Power-of-two checks, or any problem hinting at binary representation shortcuts.

**Template** (`Bitwise and Memory Concepts/power_of_2.py`):
```python
def isPowerOfTwo(num):
    return num > 0 and (num & (num - 1)) == 0
```

The trick: a power of two has exactly one bit set, so subtracting 1 flips every bit after it — ANDing the two together always yields 0.

| Complexity | Value |
|---|---|
| Time | O(1) |
| Space | O(1) |

**Problems solved:** Power of Two (LeetCode 231), Power of Three (LeetCode 326), Power of Four (LeetCode 342)

**Common mistakes:**
- Forgetting the `num > 0` guard — the bit trick alone returns `True` for `0` incorrectly.

**Status:** 🔄 In progress — only power-of-N checks covered so far; no XOR-based problems (e.g. Single Number) yet.

---

## Recursion (Foundations)

**Recognition:** Problem has a self-similar smaller subproblem and a clear base case — factorial, GCD, sqrt, prime checks.

**Template — GCD, three ways** (`RECURSION - 3/gcd.py`):
```python
# Euclidean algorithm — the one to default to in interviews
def euclidian_gcd(a, b):
    if b == 0:
        return a
    return euclidian_gcd(b, a % b)
```

The same file also implements GCD via brute-force decrementing search and via repeated subtraction — useful for explaining *why* the Euclidean version is preferred (O(log(min(a,b))) vs O(min(a,b))).

| Complexity | Value |
|---|---|
| Time | O(log(min(a,b))) for Euclidean GCD |
| Space | O(log(min(a,b))) call stack |

**Problems solved:** Factorial, Fibonacci, Sum of Digits, Reverse Digits, GCD, Count Primes, Square Root, Pow(x, n)

**Common mistakes:**
- Not stating the base case explicitly before writing the recursive call.
- Brute-force GCD by decrementing is correct but interviewers will immediately ask for the faster version — know the Euclidean algorithm cold.

**Interview tip:** Always mention the call-stack space cost of recursion — it's the most commonly missed part of complexity analysis for recursive solutions.

**Related patterns:** Backtracking (not yet implemented — natural extension once recursion needs to explore multiple branches and undo choices)

---

## Matrix Traversal

**Recognition:** 2D grid manipulation — rotation, transposition, diagonal sums, spiral order.

**Problems solved:** Rotate Image (LeetCode 48), Spiral Matrix (LeetCode 54), Transpose Matrix, Matrix Diagonal Sum (LeetCode 1572)

**Status:** Implemented in `PROBLEMS ON MATRIX/` and `MULTIDIMENSIONAL ARRAYS/` — not yet broken down into a dedicated pattern writeup here. Candidate for the next `PATTERNS.md` update once boundary-tracking notes are written up.

---

## Kadane's Algorithm (Max Subarray)

**Recognition:** "Maximum sum contiguous subarray" — running sum that resets when it drops below zero.

**Template** (`ADVANCE ARRAY PROBLEMS - 2/max_subarray.py`):
```python
f_sum, maxsum = 0, float("-inf")
for x in arr:
    f_sum += x
    if f_sum > maxsum:
        maxsum = f_sum
    if f_sum < 0:
        f_sum = 0
```

| Complexity | Value |
|---|---|
| Time | O(n) |
| Space | O(1) |

**Problems solved:** Maximum Subarray (LeetCode 53)

**Common mistakes:**
- Resetting `f_sum` to 0 *before* updating `maxsum` — must compare first, since the max could occur at the exact element that triggers the reset.

---

## Boyer-Moore Voting (Majority Element)

**Recognition:** "Find the element appearing more than n/2 times" — constant space required.

**Template** (`ADVANCE ARRAY PROBLEMS - 2/majority_element.py`):
```python
candidate, count = nums[0], 1
for x in nums[1:]:
    if count == 0:
        candidate, count = x, 1
    elif x == candidate:
        count += 1
    else:
        count -= 1
```

| Complexity | Value |
|---|---|
| Time | O(n) |
| Space | O(1) |

**Problems solved:** Majority Element (LeetCode 169)

**Common mistakes:**
- Assuming this works for "find element appearing more than n/3 times" without modification — that needs the extended Boyer-Moore with two candidates.

---

## Not Yet Covered

These patterns appear in `README.md`'s roadmap but have no implementation in the repo yet — listed here so this file stays honest rather than implying coverage that doesn't exist:

- Sliding Window
- Backtracking
- Linked List traversal patterns
- Tree DFS/BFS
- Graph traversal
- Dynamic Programming (1D and 2D)

---

*Cross-references: `INTERVIEW_REVISION.md` (condensed cheat sheet), `README.md` (pattern coverage table), `ROADMAP.md` (where each pattern sits in the learning sequence — not yet generated).*
