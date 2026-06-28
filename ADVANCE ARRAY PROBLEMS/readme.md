# 📘 Day 63 - Two Pointer Problems (Python)

## Topics Covered

* Merge Sorted Array
* Remove Duplicates from Sorted Array
* Duplicate Zeros
* Move Zeroes

---

# ✅ Q83. Merge Sorted Array

## Problem

Merge two sorted arrays into `nums1` **in-place**.

`nums1` has enough extra space at the end to hold all elements of `nums2`.

### Example

```text
Input:
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

Output:
[1,2,2,3,5,6]
```

---

## DSA Approach

```python
class Solution:
    def merge(self, nums1, m, nums2, n):

        i = m - 1
        j = n - 1
        k = len(nums1) - 1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```

---

## Algorithm

1. Keep three pointers:

   * `i` → Last valid element of `nums1`
   * `j` → Last element of `nums2`
   * `k` → Last position of `nums1`
2. Compare `nums1[i]` and `nums2[j]`.
3. Put the larger element at `nums1[k]`.
4. Move the corresponding pointer.
5. Copy remaining elements of `nums2`.

---

## Dry Run

```
nums1 = [2,5,8,0,0,0]
nums2 = [1,4,7]

Compare 8 and 7
↓

[2,5,8,0,0,8]

Compare 5 and 7
↓

[2,5,8,0,7,8]

Compare 5 and 4
↓

[2,5,8,5,7,8]

Compare 2 and 4
↓

[2,5,4,5,7,8]

Compare 2 and 1
↓

[2,2,4,5,7,8]

Copy remaining 1

↓

[1,2,4,5,7,8]
```

---

## Complexity

* **Time:** `O(m+n)`
* **Space:** `O(1)`

---

## ⭐ Pythonic Way

```python
class Solution:
    def merge(self, nums1, m, nums2, n):

        nums1[m:] = nums2
        nums1.sort()
```

### Pythonic Explanation

### Slice Assignment

```python
nums1[m:] = nums2
```

Replaces everything from index `m` onward.

Example

```python
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]

nums1[3:] = nums2
```

Result

```python
[1,2,3,2,5,6]
```

Then

```python
nums1.sort()
```

sorts the array.

---

# ✅ Q84. Remove Duplicates from Sorted Array

## Problem

Remove duplicates **in-place** from a sorted array.

Return the number of unique elements.

Example

```text
Input:
[1,1,2]

Output:
2

Array becomes

[1,2,_]
```

---

## DSA Approach

```python
class Solution:
    def removeDuplicates(self, nums):

        j = 1

        for i in range(len(nums)-1):

            if nums[i] != nums[i+1]:
                nums[j] = nums[i+1]
                j += 1

        return j
```

---

## Algorithm

1. Traverse using pointer `i`.
2. Use pointer `j` to store unique elements.
3. Whenever adjacent elements differ,
   copy the new value.
4. Return `j`.

---

## Dry Run

```
[1,1,2,2,3]

↓

1==1

Skip

↓

1!=2

Store 2

↓

2==2

Skip

↓

2!=3

Store 3

↓

[1,2,3]

Return 3
```

---

## Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

---

## ⭐ Pythonic Way

```python
class Solution:
    def removeDuplicates(self, nums):

        nums[:] = sorted(set(nums))

        return len(nums)
```

### Pythonic Explanation

### `set()`

Removes duplicate values.

```python
set([1,1,2,2,3])

↓

{1,2,3}
```

### `sorted()`

Returns a sorted list.

```python
sorted({3,2,1})

↓

[1,2,3]
```

### Slice Assignment

```python
nums[:] = ...
```

Modifies the original list instead of creating a new one.

---

# ✅ Q85. Duplicate Zeros

## Problem

Duplicate every zero while shifting remaining elements.

Example

```text
Input

[1,0,2,3,0,4]

Output

[1,0,0,2,3,0]
```

---

## DSA Approach

```python
class Solution:
    def duplicateZeros(self, arr):

        zeros = 0

        for num in arr:
            if num == 0:
                zeros += 1

        i = len(arr) - 1
        j = len(arr) - 1 + zeros

        while i < j:

            if j < len(arr):
                arr[j] = arr[i]

            j -= 1

            if arr[i] == 0:

                if j < len(arr):
                    arr[j] = 0

                j -= 1

            i -= 1
```

---

## Algorithm

1. Count total zeros.
2. Imagine the expanded array.
3. Traverse backwards.
4. Copy every element.
5. Duplicate zeros while moving.

---

## Dry Run

```
[1,0,2,3]

↓

Zero Count = 1

↓

Shift from back

↓

Duplicate 0

↓

[1,0,0,2]
```

---

## Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

---

## ⭐ Pythonic Way

```python
class Solution:
    def duplicateZeros(self, arr):

        i = 0

        while i < len(arr):

            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1

            i += 1
```

### Pythonic Explanation

### `insert(index, value)`

Adds an element at a given index.

```python
arr=[1,2,3]

arr.insert(1,100)

↓

[1,100,2,3]
```

### `pop()`

Removes the last element.

```python
arr.pop()
```

---

# ✅ Q86. Move Zeroes

## Problem

Move all zeros to the end while preserving the order of non-zero elements.

Example

```text
Input

[0,1,0,3,12]

Output

[1,3,12,0,0]
```

---

## DSA Approach

```python
class Solution:
    def moveZeroes(self, nums):

        j = 0

        for i in range(len(nums)):

            if nums[i] != 0:

                nums[i], nums[j] = nums[j], nums[i]

                j += 1
```

---

## Algorithm

1. Traverse the array.
2. When a non-zero is found,
   swap it with index `j`.
3. Increment `j`.

---

## Dry Run

```
[0,1,0,3,12]

↓

Swap 1

↓

[1,0,0,3,12]

↓

Swap 3

↓

[1,3,0,0,12]

↓

Swap 12

↓

[1,3,12,0,0]
```

---

## Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

---

## ⭐ Pythonic Way

```python
class Solution:
    def moveZeroes(self, nums):

        nums.sort(key=lambda x: x == 0)
```

### Pythonic Explanation

### `key=`

The `key` parameter tells `sort()` how to compare elements.

Here,

```python
lambda x: x == 0
```

returns:

* `False` for non-zero numbers
* `True` for zeros

Since Python sorts `False` before `True`, all non-zero values come first and all zeros move to the end.

Example

```python
[0,1,0,3,12]

↓

False True False False False

↓

[1,3,12,0,0]
```

---

# 📊 Complexity Comparison

| Problem            | Technique            | Time   | Space |
| ------------------ | -------------------- | ------ | ----- |
| Merge Sorted Array | Three Pointers       | O(m+n) | O(1)  |
| Remove Duplicates  | Two Pointers         | O(n)   | O(1)  |
| Duplicate Zeros    | Reverse Two Pointers | O(n)   | O(1)  |
| Move Zeroes        | Two Pointers         | O(n)   | O(1)  |

---

# 📚 Key Learnings

* Three pointers are useful when merging arrays in-place.
* Two pointers efficiently solve duplicate and zero-shifting problems.
* Traversing from the end prevents overwriting elements.
* Python provides concise alternatives such as `sort()`, `set()`, `insert()`, `pop()`, and slice assignment, but interviews generally expect the DSA solutions first.
