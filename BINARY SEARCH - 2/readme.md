# Q101. LeetCode 852: Peak Index in a Mountain Array

**Topic:** Binary Search

**Difficulty:** Medium

**LeetCode:** 852. Peak Index in a Mountain Array

---

# 🧩 Problem Statement

You are given a **mountain array**.

A mountain array is an array where:

- Elements first **strictly increase**
- Then **strictly decrease**

Return the **index of the peak element** (maximum element).

---

## Example 1

```text
Input: arr = [0,1,0]

Output: 1
```

Explanation:

```text
0 → 1 → 0

Peak = 1
Index = 1
```

---

## Example 2

```text
Input: arr = [0,2,4,6,3,1]

Output: 3
```

Explanation

```text
          Peak
            ↓
0   2   4   6   3   1
            ↑
         Index = 3
```

---

# 🔒 Constraints

- 3 <= arr.length <= 10⁵
- arr is guaranteed to be a mountain array.

---

# 🤔 First Thought (Brute Force)

A beginner might think:

> "Let's simply find the maximum element."

Python:

```python
def peakIndexInMountainArray(arr):
    maximum = max(arr)
    return arr.index(maximum)
```

### Time Complexity

Finding maximum → **O(n)**

Finding index → **O(n)**

Overall:

**O(n)**

Works, but we can do much better.

---

# 💡 Observation

Look carefully at a mountain array.

```text
1 3 5 8 12 10 6 2
```

Notice something interesting.

### Left Side

```text
1 < 3
3 < 5
5 < 8
8 < 12
```

Numbers are increasing.

---

### Right Side

```text
12 > 10
10 > 6
6 > 2
```

Numbers are decreasing.

The peak separates these two regions.

---

# 🧠 Intuition

Suppose we are standing at **mid**.

Question:

**Can we know where the peak lies by looking at only one neighbour?**

Yes!

---

## Case 1

Suppose

```text
1 3 5 7 9 12 15 14 11
        ↑
      mid
```

Compare

```text
arr[mid] = 7

arr[mid+1] = 9
```

Since

```text
7 < 9
```

We are still climbing the mountain.

The peak **must be on the right**.

So

```python
start = mid + 1
```

---

## Case 2

Suppose

```text
1 3 5 8 12 10 6
          ↑
         mid
```

Compare

```text
12 > 10
```

Now we are going downhill.

That means

The peak is

- either mid itself
- or somewhere on the left.

So

```python
end = mid
```

Notice

We **don't write**

```python
end = mid - 1
```

Why?

Because **mid itself may be the peak**.

If we remove it,

we might lose the answer.

---

# 🎯 Pattern Recognition

Whenever the problem says

- Mountain Array
- Bitonic Array
- Increasing then Decreasing
- Find Maximum

Immediately think

> **Binary Search**

---

# 🚀 Optimal Approach (Binary Search)

Instead of checking every element,

keep cutting the search space into half.

At every step

compare

```text
arr[mid]

vs

arr[mid+1]
```

---

## Algorithm

1. Initialize

```python
start = 0
end = len(arr)-1
```

---

2. While

```python
start < end
```

---

3. Find mid

```python
mid = (start+end)//2
```

---

4. Compare

If

```python
arr[mid] < arr[mid+1]
```

Peak lies on right.

```python
start = mid+1
```

Else

Peak lies on left (or mid).

```python
end = mid
```

---

5. When

```python
start == end
```

Both point to the peak.

Return

```python
start
```

---

# ✅ Python Solution

```python
class Solution:
    def peakIndexInMountainArray(self, arr):

        start = 0
        end = len(arr) - 1

        while start < end:

            mid = (start + end) // 2

            if arr[mid] < arr[mid + 1]:
                start = mid + 1

            else:
                end = mid

        return start
```

---

# 📝 Dry Run

Input

```text
arr = [0,2,5,7,4,1]
```

Initially

```text
start = 0

end = 5
```

---

### Iteration 1

```text
mid = 2

arr[mid] = 5

arr[mid+1] = 7
```

Since

```text
5 < 7
```

Move right

```text
start = 3
```

---

Current Search Space

```text
0 2 5 | 7 4 1
        ↑
      start
```

---

### Iteration 2

```text
start = 3

end = 5

mid = 4
```

Compare

```text
arr[4] = 4

arr[5] = 1
```

Since

```text
4 > 1
```

Move left

```text
end = 4
```

---

### Iteration 3

```text
start = 3

end = 4

mid = 3
```

Compare

```text
7 > 4
```

Move left

```text
end = 3
```

Now

```text
start == end == 3
```

Answer

```text
Peak Index = 3
```

---

# 📊 Time Complexity

Each iteration removes half of the search space.

```text
n

↓

n/2

↓

n/4

↓

n/8
```

Time Complexity

```text
O(log n)
```

---

# 💾 Space Complexity

Only a few variables are used.

```text
O(1)
```

---

# ❌ Common Mistakes

## Mistake 1

Using

```python
while start <= end
```

Instead of

```python
while start < end
```

This may access

```python
arr[mid+1]
```

when

```python
mid == len(arr)-1
```

leading to an IndexError.

---

## Mistake 2

Writing

```python
end = mid - 1
```

Wrong!

Because **mid itself can be the peak**.

Always write

```python
end = mid
```

---

## Mistake 3

Returning

```python
mid
```

after the loop.

Wrong.

Return

```python
start
```

or

```python
end
```

Both point to the peak.

---

# 🧠 Interview Tips

If the interviewer asks:

> Why compare only with `arr[mid+1]`?

Answer:

Because in a mountain array:

- If `arr[mid] < arr[mid+1]`, we are on the increasing slope, so the peak is to the right.
- If `arr[mid] > arr[mid+1]`, we are on the decreasing slope, so the peak is at `mid` or to its left.

One neighbour is enough to determine the direction.

---

# 🔄 Brute Force vs Optimal

| Approach | Time | Space |
|----------|------|-------|
| Find Maximum | O(n) | O(1) |
| Binary Search | **O(log n)** | O(1) |

---

# 🎯 Pattern Learned

This is the **Binary Search on Mountain/Bitonic Array** pattern.

Whenever you see:

- Mountain Array
- Bitonic Array
- Find Peak
- Increasing then Decreasing

Think:

```text
Compare arr[mid] with arr[mid+1]

↓

Increasing?

Go Right

↓

Decreasing?

Go Left
```

---

# 📚 Similar Problems

- LeetCode 852 — Peak Index in a Mountain Array
- LeetCode 162 — Find Peak Element
- Find Maximum in Bitonic Array
- Search in Bitonic Array

---

# 📝 Key Takeaways

- A mountain array has one unique peak.
- Compare `arr[mid]` with `arr[mid + 1]` to determine which side the peak lies on.
- If climbing (`arr[mid] < arr[mid+1]`), move right.
- If descending (`arr[mid] > arr[mid+1]`), keep `mid` and move left.
- Use `while start < end`.
- Return `start` (or `end`) after the loop.

> **Golden Rule:** In mountain-array binary search, don't discard `mid` when moving left, because `mid` itself might be the peak.
# Q102. LeetCode 33: Search in Rotated Sorted Array

**Topic:** Binary Search

**Difficulty:** Medium

**LeetCode:** 33. Search in Rotated Sorted Array

---

# 🧩 Problem Statement

Suppose an array sorted in ascending order is **rotated** at some pivot.

You are given the rotated array and a target value.

Return the **index** of the target.

If the target does not exist, return **-1**.

You **must solve it in O(log n)** time.

---

## Example 1

```text
Input

nums = [4,5,6,7,0,1,2]

target = 0

Output

4
```

---

## Example 2

```text
Input

nums = [4,5,6,7,0,1,2]

target = 3

Output

-1
```

---

## Example 3

```text
Input

nums = [1]

target = 1

Output

0
```

---

# 🔒 Constraints

- 1 <= nums.length <= 5000
- All elements are unique.
- nums is sorted and then rotated.
- O(log n) solution required.

---

# 🤔 What is a Rotated Sorted Array?

Normally, a sorted array looks like this:

```text
1 2 3 4 5 6 7
```

Now suppose we rotate it.

Rotate by 3 positions:

```text
5 6 7 1 2 3 4
```

Rotate by 4 positions:

```text
4 5 6 7 1 2 3
```

Notice something...

The array is **not completely unsorted**.

It is actually made of **two sorted parts**.

Example

```text
4 5 6 7 | 0 1 2
```

Left part

```text
4 5 6 7
```

Sorted.

Right part

```text
0 1 2
```

Also sorted.

This observation is the key to solving the problem.

---

# 🧠 Beginner Intuition

Most beginners think:

> "I'll check every element."

```python
for i in range(len(nums)):
    if nums[i] == target:
        return i

return -1
```

### Time Complexity

```text
O(n)
```

Works.

But the problem specifically asks for

```text
O(log n)
```

So we need Binary Search.

---

# 💡 The Biggest Question

Binary Search only works on **sorted arrays**.

But this array isn't fully sorted.

So how can Binary Search work?

Answer:

At every moment,

**at least one half is guaranteed to be sorted.**

---

# 🔍 Observation

Suppose

```text
4 5 6 7 0 1 2
```

Take

```text
mid = 3
```

```text
4 5 6 7 0 1 2
      ↑
```

Now compare

```text
nums[start]

and

nums[mid]
```

```text
4 <= 7
```

That means

the **left half** is sorted.

---

Another example

```text
6 7 8 1 2 3 4
```

Suppose

```text
mid = 4
```

```text
6 7 8 1 2 3 4
        ↑
```

Now

```text
nums[start] = 6

nums[mid] = 2
```

```text
6 <= 2 ?

No.
```

That means

the **right half** is sorted.

---

# 🎯 Main Idea

Every iteration

Ask only one question:

> Which half is sorted?

Once you know the sorted half,

check whether the target lies inside it.

If yes

Search there.

Else

Search the other half.

---

# 🚀 Algorithm

### Step 1

Initialize

```python
start = 0
end = len(nums)-1
```

---

### Step 2

While

```python
start <= end
```

---

### Step 3

Find

```python
mid
```

---

### Step 4

If

```python
nums[mid] == target
```

Return

```python
mid
```

---

### Step 5

Check whether

Left Half

is sorted.

```python
nums[start] <= nums[mid]
```

If yes

check whether target lies inside

```text
nums[start]

↓

target

↓

nums[mid]
```

If yes

Search Left

Else

Search Right

---

### Step 6

Otherwise

Right Half

must be sorted.

Check

```text
nums[mid]

↓

target

↓

nums[end]
```

If yes

Search Right

Else

Search Left

---

# 📊 Visual Intuition

Example

```text
4 5 6 7 0 1 2
```

Suppose

```text
mid = 3

value = 7
```

```text
4 <= 7

YES
```

Left side

```text
4 5 6 7
```

is sorted.

Now ask

Is

```text
target = 6
```

inside

```text
4...7
```

YES

Ignore the right half.

---

Another example

```text
6 7 1 2 3 4 5
```

Suppose

```text
mid = 3

value = 2
```

```text
6 <= 2

NO
```

Therefore

Right side

```text
2 3 4 5
```

is sorted.

Now ask

Does target belong there?

---

# ✅ Python Solution

```python
class Solution:
    def search(self, nums, target):

        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[start] <= nums[mid]:

                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            # Right half is sorted
            else:

                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1
```

---

# 📝 Complete Dry Run

Input

```text
nums = [4,5,6,7,0,1,2]

target = 0
```

Initially

```text
start = 0

end = 6
```

---

### Iteration 1

```text
mid = 3

nums[mid] = 7
```

Target?

No.

Check

```text
nums[start] <= nums[mid]

4 <= 7

YES
```

Left side sorted.

Is

```text
0

between

4 and 7 ?
```

No.

Search right.

```text
start = 4
```

---

### Iteration 2

Now

```text
start = 4

end = 6
```

Mid

```text
5
```

Value

```text
1
```

Right side sorted.

Target

0

Not in right.

Search left.

```text
end = 4
```

---

### Iteration 3

```text
start = 4

end = 4

mid = 4
```

Found

```text
0
```

Return

```text
4
```

---

# ❌ Common Mistakes

## Mistake 1

Checking

```python
nums[mid] <= nums[end]
```

first.

It still works,

but most interviewers expect

checking the left side first because it's easier to understand.

---

## Mistake 2

Forgetting

```python
<=
```

Example

```python
nums[start] <= nums[mid]
```

Using

```python
<
```

may fail when

```text
start == mid
```

---

## Mistake 3

Wrong range check

Correct

```python
nums[start] <= target < nums[mid]
```

Not

```python
nums[start] < target <= nums[mid]
```

Pay close attention to the equality signs.

---

# 🧠 Why Does This Work?

Every iteration,

one half is perfectly sorted.

A sorted half allows us to decide

whether the target belongs there.

If it doesn't,

we discard that entire half.

Just like Binary Search,

we remove half the search space every iteration.

---

# ⏱ Complexity

### Time

Each iteration removes half of the array.

```text
O(log n)
```

---

### Space

Only variables are used.

```text
O(1)
```

---

# 🎯 Pattern Recognition

Whenever you hear

- Rotated Sorted Array
- Rotated Binary Search
- Search after Rotation

Immediately think

```text
Find which half is sorted

↓

Check whether target belongs there

↓

Discard the other half
```

---

# 📚 Similar Problems

- LeetCode 33 — Search in Rotated Sorted Array
- LeetCode 81 — Search in Rotated Sorted Array II
- LeetCode 153 — Find Minimum in Rotated Sorted Array
- LeetCode 154 — Find Minimum in Rotated Sorted Array II

---

# 📝 Key Takeaways

- A rotated array always contains **one sorted half**.
- Use Binary Search to identify the sorted half.
- Check if the target belongs to that half.
- Discard the other half.
- Continue until the target is found or the search space becomes empty.
- Time Complexity is **O(log n)**.

---

# 🧠 Memory Trick

```text
Rotated Array

↓

Find Mid

↓

Which Half is Sorted?

↓

Does Target Belong There?

↓

YES → Search There

NO → Search Other Half
```

> **Golden Rule:** In every iteration of a rotated binary search, first identify the sorted half, then decide whether the target lies inside it.
# Q103. Book Allocation Problem

**Topic:** Binary Search on Answer\
**Difficulty:** Hard\
**Pattern:** Binary Search on Answer

------------------------------------------------------------------------

# 🧩 Problem Statement

You are given: - An array `books[]` where each element represents the
number of pages in a book. - An integer `students`.

Allocate books such that:

-   Every student gets **at least one** book.
-   Books assigned to a student are **contiguous**.
-   Every book is allocated.
-   Minimize the **maximum pages** assigned to any student.

Return the minimum possible maximum pages.

------------------------------------------------------------------------

## Example

``` text
books = [12, 34, 67, 90]
students = 2

Output = 113
```

Possible allocations:

``` text
12 | 34 67 90  -> max = 191
12 34 | 67 90  -> max = 157
12 34 67 | 90  -> max = 113 ✅
```

------------------------------------------------------------------------

# 🤔 Beginner Intuition

A beginner usually thinks:

> "Let's try every possible way of dividing the books."

For 4 books and 2 students there are only a few partitions.

But imagine:

-   100 books
-   20 students

Trying every partition becomes impossible.

So brute force is not practical.

------------------------------------------------------------------------

# 💡 The Biggest Observation

Notice something important.

The answer is **not an index**.

The answer is a **number of pages**.

Question:

Can the answer ever be **50 pages**?

No.

Because one book itself may have **90 pages**.

So the minimum answer can never be smaller than

``` python
max(books)
```

Similarly,

the largest possible answer is when one student gets every book.

``` python
sum(books)
```

Therefore the answer always lies between

``` text
max(books)  ----------->  sum(books)
```

Whenever the answer lies inside a range,

think:

# 🚀 Binary Search on Answer

------------------------------------------------------------------------

# 🧠 New Way of Thinking

Instead of asking

> "Where is the answer?"

Ask

> "Can this answer work?"

Suppose we guess

``` text
limit = 113
```

Can we allocate books so that no student reads more than **113 pages**?

If YES

Try a smaller answer.

If NO

Increase the answer.

------------------------------------------------------------------------

# 🎯 Search Space

``` python
low = max(books)
high = sum(books)
```

For

``` text
books = [12,34,67,90]
```

``` text
low = 90
high = 203
```

Binary Search will happen only in this range.

------------------------------------------------------------------------

# 🧠 Greedy Validation (isPossible)

Suppose

``` text
limit = 113
```

Student 1

``` text
12
12+34 = 46
46+67 = 113
```

Next book

``` text
90
```

Cannot fit.

Start Student 2.

Student 2

``` text
90
```

Only 2 students used.

So 113 works.

------------------------------------------------------------------------

Suppose

``` text
limit = 100
```

Student 1

``` text
12+34 = 46
```

Cannot add 67.

Student 2

``` text
67
```

Cannot add 90.

Need Student 3.

But only 2 students exist.

So 100 does NOT work.

------------------------------------------------------------------------

# 🔍 Algorithm

1.  If students \> books, return -1.
2.  Set `low = max(books)`.
3.  Set `high = sum(books)`.
4.  Binary Search on this range.
5.  For every `mid`, check using greedy allocation.
6.  If possible:
    -   Save answer.
    -   Search left.
7.  Otherwise:
    -   Search right.

------------------------------------------------------------------------

# ✅ Python Solution

``` python
class Solution:

    def isPossible(self, books, students, limit):

        student_count = 1
        pages = 0

        for book in books:

            if pages + book <= limit:
                pages += book
            else:
                student_count += 1
                pages = book

                if student_count > students:
                    return False

        return True

    def allocateBooks(self, books, students):

        if students > len(books):
            return -1

        low = max(books)
        high = sum(books)

        answer = high

        while low <= high:

            mid = (low + high) // 2

            if self.isPossible(books, students, mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
```

------------------------------------------------------------------------

# 📝 Line-by-Line Explanation

### `isPossible()`

This function answers one question:

> Can all books be allocated if one student can read at most `limit`
> pages?

We greedily keep adding books to the current student.

If the next book exceeds the limit,

we assign it to a new student.

If students required become greater than the available students,

return `False`.

Otherwise return `True`.

------------------------------------------------------------------------

### Binary Search

``` python
low = max(books)
high = sum(books)
```

The answer cannot be outside this range.

For every guessed answer (`mid`):

-   Possible → save it and try smaller.
-   Not possible → increase the answer.

------------------------------------------------------------------------

# 📖 Complete Dry Run

``` text
books = [12,34,67,90]
students = 2
```

Search Space

``` text
90 ------------------ 203
```

Guess

``` text
146
```

Possible ✅

Search Left

------------------------------------------------------------------------

Guess

``` text
117
```

Possible ✅

Search Left

------------------------------------------------------------------------

Guess

``` text
103
```

Not Possible ❌

Search Right

------------------------------------------------------------------------

Guess

``` text
110
```

Not Possible ❌

Search Right

------------------------------------------------------------------------

Guess

``` text
113
```

Possible ✅

Search Left

Loop Ends.

Answer

``` text
113
```

------------------------------------------------------------------------

# ❓Why Does Greedy Work?

Many beginners ask:

> Why do we keep filling one student before moving to the next?

Because stopping early can never reduce the number of students.

Giving a student fewer books only pushes more books to later students.

So greedily filling each student minimizes the number of students used.

------------------------------------------------------------------------

# ⚠️ Common Mistakes

### ❌ Starting from 0

Wrong

``` python
low = 0
```

Correct

``` python
low = max(books)
```

------------------------------------------------------------------------

### ❌ Ending at max(books)

Wrong

``` python
high = max(books)
```

Correct

``` python
high = sum(books)
```

------------------------------------------------------------------------

### ❌ Forgetting

``` python
students > len(books)
```

Someone would receive zero books.

Return

``` text
-1
```

------------------------------------------------------------------------

# 🧠 Pattern Recognition

Whenever the problem says

-   Allocate
-   Capacity
-   Minimum Maximum
-   Maximum Minimum
-   Smallest Possible Value

Think

``` text
Binary Search on Answer
```

------------------------------------------------------------------------

# ⏱ Complexity

Validation:

``` text
O(n)
```

Binary Search:

``` text
O(log(sum(books)))
```

Overall

``` text
O(n log(sum))
```

Space

``` text
O(1)
```

------------------------------------------------------------------------

# 📚 Similar Problems

-   Painter's Partition Problem
-   Split Array Largest Sum
-   Capacity to Ship Packages Within D Days
-   Koko Eating Bananas

------------------------------------------------------------------------

# 🎯 Key Takeaways

-   Search the **answer**, not the array.
-   Lower bound = largest single book.
-   Upper bound = total pages.
-   Use greedy to validate a guessed answer.
-   If a guess works, search left.
-   If it doesn't, search right.

------------------------------------------------------------------------

# 🧠 Memory Trick

``` text
Minimum Maximum

↓

Find Search Space

↓

Binary Search

↓

Greedy Check

↓

Possible?

YES → Smaller

NO → Bigger
```
# Q104. Capacity to Ship Packages Within D Days

**Topic:** Binary Search on Answer\
**Difficulty:** Medium\
**LeetCode:** 1011. Capacity To Ship Packages Within D Days

------------------------------------------------------------------------

# 🧩 Problem Statement

You are given:

-   An array `weights[]` representing package weights.
-   An integer `days`.

A ship can carry packages **in order** and cannot split a package.

Find the **minimum ship capacity** required to ship all packages within
the given number of days.

------------------------------------------------------------------------

## Example

``` text
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

Output = 15
```

------------------------------------------------------------------------

# 🤔 Beginner Intuition

A brute-force approach is to try every ship capacity until one works.

This is slow because the answer could be very large.

Instead, notice that the answer is a **capacity**, not an index.

So we'll Binary Search over the possible capacities.

------------------------------------------------------------------------

# 💡 Search Space

Minimum possible capacity:

``` python
low = max(weights)
```

A ship must at least carry the heaviest package.

Maximum possible capacity:

``` python
high = sum(weights)
```

One day ships everything.

So the answer lies between

``` text
max(weights) ---------> sum(weights)
```

------------------------------------------------------------------------

# 🧠 Binary Search on Answer

Suppose we guess

``` text
capacity = 15
```

Question:

> Can all packages be shipped within 5 days?

If yes

→ Try a smaller capacity.

If no

→ Increase the capacity.

------------------------------------------------------------------------

# 🚀 Greedy Validation

Keep loading packages until the next package exceeds the capacity.

Then start a new day.

If the number of days used exceeds the allowed days,

the capacity is too small.

------------------------------------------------------------------------

# 🔍 Algorithm

1.  `low = max(weights)`
2.  `high = sum(weights)`
3.  Binary Search on capacity.
4.  Use a helper function to check if a capacity works.
5.  If possible, save answer and search left.
6.  Otherwise search right.

------------------------------------------------------------------------

# ✅ Python Solution

``` python
class Solution:

    def canShip(self, weights, days, capacity):

        current = 0
        used_days = 1

        for weight in weights:

            if current + weight <= capacity:
                current += weight

            else:
                used_days += 1
                current = weight

                if used_days > days:
                    return False

        return True

    def shipWithinDays(self, weights, days):

        low = max(weights)
        high = sum(weights)

        answer = high

        while low <= high:

            mid = (low + high) // 2

            if self.canShip(weights, days, mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
```

------------------------------------------------------------------------

# 📖 Dry Run

Input

``` text
weights = [1,2,3,4,5,6,7,8,9,10]

days = 5
```

Search Space

``` text
low = 10
high = 55
```

Suppose

``` text
capacity = 15
```

Day 1

``` text
1+2+3+4+5 = 15
```

Day 2

``` text
6+7 = 13
```

Day 3

``` text
8
```

Day 4

``` text
9
```

Day 5

``` text
10
```

Exactly 5 days.

Capacity works.

Try smaller.

Eventually Binary Search finds

``` text
15
```

as the minimum capacity.

------------------------------------------------------------------------

# ❓Why Does Greedy Work?

To minimize the required capacity,

we should fill today's ship as much as possible.

Leaving unused space today can only push packages to later days,

never reducing the number of days.

------------------------------------------------------------------------

# ⚠️ Common Mistakes

### ❌ Starting Binary Search from 0

Correct:

``` python
low = max(weights)
```

------------------------------------------------------------------------

### ❌ Forgetting package order

Packages **must remain in order**.

Sorting the array changes the problem.

------------------------------------------------------------------------

### ❌ Splitting a package

One package cannot be divided across multiple days.

------------------------------------------------------------------------

# 🎯 Pattern Recognition

Keywords:

-   Minimum Capacity
-   Within D Days
-   Minimize Maximum
-   Feasible Capacity

Think:

``` text
Binary Search on Answer
```

------------------------------------------------------------------------

# ⏱ Complexity

Validation

``` text
O(n)
```

Binary Search

``` text
O(log(sum(weights)))
```

Overall

``` text
O(n log(sum))
```

Space

``` text
O(1)
```

------------------------------------------------------------------------

# 📚 Similar Problems

-   Book Allocation Problem
-   Painter's Partition Problem
-   Split Array Largest Sum
-   Koko Eating Bananas

------------------------------------------------------------------------

# 📝 Key Takeaways

-   Search the **capacity**, not the array.
-   Lower bound = heaviest package.
-   Upper bound = total weight.
-   Use a greedy simulation to validate a guessed capacity.
-   If a capacity works, try a smaller one.
-   If it fails, increase it.

------------------------------------------------------------------------

# 🧠 Memory Trick

``` text
Capacity Problem

↓

Search Capacity

↓

Greedy Simulation

↓

Possible?

YES → Smaller

NO → Bigger
```
# Q105. LeetCode 875: Koko Eating Bananas

**Topic:** Binary Search on Answer\
**Difficulty:** Medium\
**Pattern:** Binary Search on Answer

------------------------------------------------------------------------

# 🧩 Problem Statement

Koko loves bananas.

You are given:

-   `piles[]` where each element represents bananas in one pile.
-   `h` hours.

Koko chooses an eating speed `k` (bananas/hour).

Every hour she chooses one pile and eats up to `k` bananas from that
pile. If the pile has fewer than `k` bananas, she finishes that pile and
waits until the next hour.

Find the **minimum eating speed** so that Koko finishes all bananas
within `h` hours.

------------------------------------------------------------------------

## Example

``` text
piles = [3,6,7,11]
h = 8

Output = 4
```

------------------------------------------------------------------------

# 🤔 Beginner Intuition

A beginner might try every possible speed:

``` text
1 banana/hour
2 bananas/hour
3 bananas/hour
...
```

until one works.

This is too slow when pile sizes are very large.

------------------------------------------------------------------------

# 💡 Observation

The answer is **not an index**.

The answer is an **eating speed**.

Minimum possible speed?

``` python
1
```

Maximum possible speed?

``` python
max(piles)
```

If Koko eats as fast as the largest pile, every pile finishes in one
hour.

So our search space becomes

``` text
1 ------------------> max(piles)
```

Whenever the answer lies inside a range,

think

# 🚀 Binary Search on Answer

------------------------------------------------------------------------

# 🧠 Main Idea

Guess an eating speed.

Question:

> Can Koko finish all bananas within `h` hours?

If YES

Try a smaller speed.

If NO

Increase the speed.

------------------------------------------------------------------------

# 📝 How to Check a Speed?

Suppose

``` text
speed = 4

piles = [3,6,7,11]
```

Hours required

``` text
3 -> 1 hour

6 -> 2 hours

7 -> 2 hours

11 -> 3 hours
```

Total

``` text
1+2+2+3 = 8
```

Exactly 8 hours.

So speed 4 works.

------------------------------------------------------------------------

# 🔍 Why Use Ceiling?

Suppose

``` text
Pile = 7

Speed = 3
```

She eats

``` text
3

3

1
```

Hours

``` text
3
```

Not

``` text
7//3 = 2
```

We need

``` python
ceil(7/3)
```

or

``` python
(pile + speed - 1) // speed
```

------------------------------------------------------------------------

# 🔍 Algorithm

1.  low = 1
2.  high = max(piles)
3.  Binary Search.
4.  Compute total hours for every guessed speed.
5.  If hours \<= h:
    -   save answer
    -   search left
6.  Else
    -   search right.

------------------------------------------------------------------------

# ✅ Python Solution

``` python
class Solution:

    def canFinish(self, piles, h, speed):

        hours = 0

        for pile in piles:
            hours += (pile + speed - 1) // speed

        return hours <= h

    def minEatingSpeed(self, piles, h):

        low = 1
        high = max(piles)

        answer = high

        while low <= high:

            mid = (low + high) // 2

            if self.canFinish(piles, h, mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
```

------------------------------------------------------------------------

# 📖 Complete Dry Run

``` text
piles = [3,6,7,11]
h = 8
```

Search Space

``` text
1 -------- 11
```

Guess

``` text
speed = 6
```

Hours

``` text
1+1+2+2 = 6
```

Works ✅

Try smaller.

------------------------------------------------------------------------

Guess

``` text
speed = 3
```

Hours

``` text
1+2+3+4 = 10
```

Too slow ❌

Increase speed.

------------------------------------------------------------------------

Guess

``` text
speed = 4
```

Hours

``` text
1+2+2+3 = 8
```

Works ✅

Try smaller.

Binary Search finishes.

Answer

``` text
4
```
# Pythonic Way
```python
class Solution:
    def minEatingSpeed(self, piles, h):

        def canFinish(speed):
            return sum((pile + speed - 1) // speed for pile in piles) <= h

        low, high = 1, max(piles)

        while low <= high:

            mid = (low + high) // 2

            if canFinish(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low
```
------------------------------------------------------------------------

# ❓Why Greedy Works?

Once the speed is fixed,

there is only one way to calculate the total hours.

Each pile contributes independently.

If total hours fit within `h`, the speed is feasible.

------------------------------------------------------------------------

# ⚠️ Common Mistakes

### ❌ Using floor division

Wrong

``` python
hours += pile // speed
```

Correct

``` python
hours += (pile + speed - 1) // speed
```

because partial piles still consume one full hour.

------------------------------------------------------------------------

### ❌ Starting from speed 0

Division by zero.

Always

``` python
low = 1
```

------------------------------------------------------------------------

### ❌ Searching beyond `max(piles)`

No need.

A speed larger than the biggest pile offers no benefit.

------------------------------------------------------------------------

# 🎯 Pattern Recognition

Keywords:

-   Minimum Speed
-   Minimum Capacity
-   Minimum Maximum
-   Finish within Time

Think

``` text
Binary Search on Answer
```

------------------------------------------------------------------------

# ⏱ Complexity

Validation

``` text
O(n)
```

Binary Search

``` text
O(log(max(piles)))
```

Overall

``` text
O(n log(max(piles)))
```

Space

``` text
O(1)
```

------------------------------------------------------------------------

# 📚 Similar Problems

-   Book Allocation Problem
-   Capacity to Ship Packages Within D Days
-   Split Array Largest Sum
-   Painter's Partition Problem

------------------------------------------------------------------------

# 📝 Key Takeaways

-   Search over possible eating speeds.
-   Lower bound = 1.
-   Upper bound = largest pile.
-   Use ceiling division to compute hours.
-   If a speed works, search for a smaller one.
-   If it doesn't, increase the speed.

------------------------------------------------------------------------

# 🧠 Memory Trick

``` text
Minimum Speed

↓

Search Speed

↓

Calculate Hours

↓

Possible?

YES → Smaller Speed

NO → Bigger Speed
```