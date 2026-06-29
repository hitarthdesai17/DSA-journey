# 📘 Day79_Q93_3Sum.md

# ✅ Q93. 3Sum (LeetCode 15)

## Problem Statement

Given an integer array `nums`, return **all unique triplets**

```text
[nums[i], nums[j], nums[k]]
```

such that

* `i != j`
* `i != k`
* `j != k`
* `nums[i] + nums[j] + nums[k] == 0`

The solution should not contain duplicate triplets.

---

# Example 1

```text
Input:
nums = [-1,0,1,2,-1,-4]

Output:
[[-1,-1,2],[-1,0,1]]
```

---

# Example 2

```text
Input:
nums = [0,1,1]

Output:
[]
```

---

# Example 3

```text
Input:
nums = [0,0,0]

Output:
[[0,0,0]]
```

---

# Method 1 : Brute Force

## Python Solution

```python
class Solution:
    def threeSum(self, nums):

        ans = set()

        n = len(nums)

        for i in range(n - 2):

            for j in range(i + 1, n - 1):

                for k in range(j + 1, n):

                    if nums[i] + nums[j] + nums[k] == 0:

                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))

                        ans.add(triplet)

        return [list(x) for x in ans]
```

---

# Algorithm

### Step 1

Pick the first element.

```python
for i in range(n-2):
```

---

### Step 2

Pick the second element.

```python
for j in range(i+1,n-1):
```

---

### Step 3

Pick the third element.

```python
for k in range(j+1,n):
```

---

### Step 4

Check

```python
nums[i] + nums[j] + nums[k]
```

If the sum is zero,

store it inside a set.

---

### Step 5

Convert the set back into a list.

---

# Why Use a Set?

Suppose

```text
[-1,0,1]
```

appears again.

Without a set,

both triplets would be stored.

A set keeps only unique values.

---

# Dry Run

Input

```text
[-1,0,1,2,-1,-4]
```

Possible triplets

```text
[-1,0,1]

↓

Sum = 0

Store
```

Another triplet

```text
[-1,-1,2]

↓

Sum = 0

Store
```

Answer

```text
[
[-1,-1,2],
[-1,0,1]
]
```

---

# Complexity

```text
Time  : O(n³)

Space : O(n)
```

---

# Method 2 : Two Pointer (Optimal)

## Python Solution

```python
class Solution:
    def threeSum(self, nums):

        nums.sort()

        ans = []

        n = len(nums)

        for i in range(n - 2):

            # Skip duplicate first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:

                    ans.append(
                        [nums[i], nums[left], nums[right]]
                    )

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:

                    left += 1

                else:

                    right -= 1

        return ans
```

---

# Algorithm

## Step 1

Sort the array.

```python
nums.sort()
```

Example

```text
Before

[-1,0,1,2,-1,-4]

↓

After

[-4,-1,-1,0,1,2]
```

---

## Step 2

Fix one element.

```python
nums[i]
```

---

## Step 3

Use two pointers.

```text
Left

↓

i L           R

-4 -1 -1 0 1 2
```

---

## Step 4

Find

```text
nums[left]+nums[right]
```

such that

```text
nums[i]

+

nums[left]

+

nums[right]

=

0
```

---

## Step 5

Move pointers.

If

```text
Total < 0
```

Move

```text
Left++
```

because we need a larger sum.

If

```text
Total > 0
```

Move

```text
Right--
```

because we need a smaller sum.

---

## Step 6

Whenever we find a valid triplet,

store it and skip duplicates.

---

# Complete Dry Run

Input

```text
[-1,0,1,2,-1,-4]
```

Sorted

```text
[-4,-1,-1,0,1,2]
```

---

## i = 0

```text
-4

Left = -1

Right = 2
```

Sum

```text
-3
```

Too small

Move Left.

Continue...

No answer.

---

## i = 1

```text
-1

Left = -1

Right = 2
```

Sum

```text
0
```

Store

```text
[-1,-1,2]
```

Move

```text
Left++

Right--
```

Now

```text
Left = 0

Right = 1
```

Again

```text
-1+0+1

=

0
```

Store

```text
[-1,0,1]
```

---

## i = 2

```text
nums[2]

=

-1
```

Same as previous.

Skip it.

---

Remaining iterations produce nothing.

Answer

```text
[
[-1,-1,2],
[-1,0,1]
]
```

---

# Why Skip Duplicates?

Suppose

```text
[-1,-1,-1,2,2]
```

Without

```python
continue
```

you would produce

```text
[-1,-1,2]
```

multiple times.

Duplicate skipping guarantees unique triplets.

---

# Pythonic Way

The optimized solution is already considered the standard Pythonic interview solution.

---

# Pythonic Explanation

## New Function : `sort()`

Sorts the list in-place.

Example

```python
nums = [3,1,2]

nums.sort()

print(nums)
```

Output

```text
[1,2,3]
```

Sorting allows us to use the two-pointer technique.

---

## New Keyword : `continue`

Skips the current iteration.

Example

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

Output

```text
0
1
3
4
```

---

## Why Check

```python
if i > 0 and nums[i] == nums[i-1]:
```

Suppose

```text
[-1,-1,-1,2]
```

The second `-1`

would produce exactly the same triplets as the first.

So we skip it.

---

## Why

```python
left < right
```

inside duplicate loops?

Example

```python
while left < right and nums[left] == nums[left-1]:
```

If we don't check

```python
left < right
```

the pointers may cross,

causing an IndexError or unnecessary comparisons.

---

# Comparison

| Method      | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(n³) | O(n)  |
| Two Pointer | O(n²) | O(1)* |

*Excluding the output list.

---

# Key Learnings

* Sort the array first.
* Fix one element.
* Use two pointers for the remaining two numbers.
* Skip duplicate values.
* Move:

  * Left pointer when the sum is too small.
  * Right pointer when the sum is too large.
* Two pointers reduce the complexity from **O(n³)** to **O(n²)**.

---

# Interview Tips

Whenever you hear:

* **3Sum**
* **Triplets**
* **Unique combinations**
* **Sorted array**

Think:

```text
Sort

↓

Fix One Element

↓

Two Pointers

↓

Skip Duplicates
```

Final Complexity:

```text
Time  : O(n²)

Space : O(1) (excluding output)
```
# 📘 Day79_Q94_Merge_Sort.md

# ✅ Q94. Merge Sort

## Problem Statement

Merge Sort is a **Divide and Conquer** sorting algorithm.

It works in three steps:

1. **Divide** the array into two halves.
2. **Conquer** by recursively sorting each half.
3. **Merge** the two sorted halves into one sorted array.

Unlike Bubble Sort or Selection Sort, Merge Sort is much faster for large datasets.

---

# Example

```text
Input:
[10,7,8,2,19,69,45,8]

Output:
[2,7,8,8,10,19,45,69]
```

---

# How Merge Sort Works

Imagine the array is repeatedly divided.

```text
             [10,7,8,2,19,69,45,8]
                     |
         -------------------------
         |                       |
     [10,7,8,2]            [19,69,45,8]
         |                       |
     ----------              ----------
     |        |              |        |
  [10,7]   [8,2]         [19,69]  [45,8]
     |        |              |        |
  ----      ----          ----      ----
 [10][7]  [8][2]       [19][69] [45][8]
```

Once every array contains only **one element**, we start merging them back.

---

# Python Solution

```python
class Solution:

    def mergeSort(self, arr):

        self.divide(arr, 0, len(arr) - 1)

        return arr


    def divide(self, arr, left, right):

        # Base Case
        if left >= right:
            return

        mid = (left + right) // 2

        # Sort left half
        self.divide(arr, left, mid)

        # Sort right half
        self.divide(arr, mid + 1, right)

        # Merge both halves
        self.merge(arr, left, mid, right)


    def merge(self, arr, left, mid, right):

        temp = []

        i = left
        j = mid + 1

        while i <= mid and j <= right:

            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):
            arr[left + k] = temp[k]
```

---

# Step 1 : Divide Function

```python
if left >= right:
    return
```

## Why?

If an array has

```text
1 element
```

it is already sorted.

Example

```text
[7]
```

Nothing needs to be done.

---

## Find Middle

```python
mid = (left + right) // 2
```

Example

```text
left = 0

right = 7

mid = 3
```

Array becomes

```text
0 1 2 3 | 4 5 6 7
```

---

## Recursive Calls

```python
self.divide(arr, left, mid)
```

Sorts

```text
Left Half
```

```python
self.divide(arr, mid+1, right)
```

Sorts

```text
Right Half
```

---

## Merge

```python
self.merge(arr, left, mid, right)
```

Combines two sorted halves.

---

# Step 2 : Merge Function

Initially

```python
temp = []

i = left

j = mid + 1
```

Example

```text
Left Half

7 10

Right Half

2 8
```

Pointers

```text
7 10

^

i

2 8

^

j
```

---

## Compare

```python
if arr[i] <= arr[j]
```

Smaller value goes into

```python
temp
```

---

## Copy Remaining Elements

Sometimes

```text
Left finishes first
```

Then copy everything from

```text
Right
```

Sometimes

```text
Right finishes first
```

Then copy everything from

```text
Left
```

---

## Copy Back

```python
for k in range(len(temp)):
    arr[left+k] = temp[k]
```

Now the original array contains the sorted section.

---

# Complete Dry Run

Input

```text
[10,7,8,2]
```

---

## Divide

```text
[10,7] [8,2]
```

Again

```text
[10] [7]

[8] [2]
```

---

## Merge

Merge

```text
10

7
```

↓

```text
7 10
```

Merge

```text
8

2
```

↓

```text
2 8
```

---

Merge

```text
7 10

2 8
```

Comparisons

```text
7 vs 2

↓

2
```

```text
7 vs 8

↓

7
```

```text
10 vs 8

↓

8
```

Remaining

```text
10
```

Final

```text
2 7 8 10
```

---

# Visualization

Before

```text
10 7 8 2
```

↓

Split

```text
10 7

8 2
```

↓

Split Again

```text
10

7

8

2
```

↓

Merge

```text
7 10

2 8
```

↓

Merge

```text
2 7 8 10
```

---

# Why Do We Need a Temporary Array?

Suppose

```text
Left

7 10

Right

2 8
```

If we directly overwrite

```text
arr
```

we may lose values that haven't been compared yet.

Using

```python
temp
```

keeps the merged result safe until we're ready to copy it back.

---

# Complexity

```text
Time  : O(n log n)

Space : O(n)
```

---

# Why is Time Complexity O(n log n)?

There are **two parts**:

### Dividing

Every time we split the array into two halves.

Example

```text
8

↓

4

↓

2

↓

1
```

Number of divisions

```text
log₂ n
```

---

### Merging

At every level,

every element is visited once.

```text
n operations
```

Therefore

```text
O(n)

×

O(log n)

=

O(n log n)
```

---

# ⭐ Pythonic Way

Python already provides a built-in sorting function.

```python
arr.sort()
```

or

```python
sorted(arr)
```

These are based on **Timsort**, which is even more optimized than Merge Sort for real-world data.

However, in interviews, you are usually expected to implement Merge Sort yourself.

---

# Pythonic Explanation

## New Operator : `//`

```python
mid = (left + right) // 2
```

`//` performs **floor division**.

Example

```python
7 // 2
```

Output

```text
3
```

---

## Why `mid + 1`?

Suppose

```text
left = 0

right = 7

mid = 3
```

Left half

```text
0 1 2 3
```

Right half

```text
4 5 6 7
```

So the second recursive call starts from

```python
mid + 1
```

---

## Why `temp.append()`?

Instead of assigning by index,

we simply add elements one by one.

Example

```python
temp = []

temp.append(5)

temp.append(8)
```

Result

```text
[5,8]
```

---

## Why

```python
arr[left + k] = temp[k]
```

Suppose

```text
left = 4
```

The merged part should begin from index 4.

So

```text
temp[0]

↓

arr[4]
```

```text
temp[1]

↓

arr[5]
```

and so on.

---

# Comparison

| Sorting Algorithm | Time       | Space | Stable |
| ----------------- | ---------- | ----- | ------ |
| Bubble Sort       | O(n²)      | O(1)  | ✅      |
| Selection Sort    | O(n²)      | O(1)  | ❌      |
| Insertion Sort    | O(n²)      | O(1)  | ✅      |
| Merge Sort        | O(n log n) | O(n)  | ✅      |

---

# Key Learnings

* Merge Sort follows the **Divide and Conquer** approach.
* First divide until every array has one element.
* Then merge while maintaining sorted order.
* A temporary array is required during merging.
* Merge Sort has guaranteed **O(n log n)** time complexity.
* It is a **stable sorting algorithm**, meaning equal elements keep their original relative order.

---

# Interview Tips

Whenever you hear:

* Divide and Conquer
* Stable Sort
* O(n log n)
* External Sorting
* Linked List Sorting

Think of **Merge Sort**.

Memory Trick:

```text
Divide

↓

Divide

↓

Divide

↓

Merge

↓

Merge

↓

Merge
```

Final Complexity

```text
Time  : O(n log n)

Space : O(n)
```