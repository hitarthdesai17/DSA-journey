# 📘 Day74_Q90_Sort_Colors.md

# ✅ Q90. Sort Colors (LeetCode 75)

## Problem

Given an array `nums` containing only `0`, `1`, and `2`, sort the array **in-place** without using the built-in sort function.

The numbers represent:

* `0` → Red
* `1` → White
* `2` → Blue

The final order should be:

```text
0 0 ... 1 1 ... 2 2 ...
```

---

# Example 1

```text
Input:
nums = [2,0,2,1,1,0]

Output:
[0,0,1,1,2,2]
```

---

# Example 2

```text
Input:
nums = [2,0,1]

Output:
[0,1,2]
```

---

# Method 1 : Dutch National Flag Algorithm (Optimal)

## DSA Solution (Python)

```python
class Solution:
    def sortColors(self, nums):

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:

                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1
                mid += 1

            elif nums[mid] == 2:

                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1

            else:

                mid += 1
```

---

# Algorithm

We divide the array into **four regions**.

```
0s | 1s | Unknown | 2s

^     ^        ^      ^
0    low      mid    high
```

Initially

```
Unknown = Entire Array
```

---

## Pointer Meaning

### `low`

Next position where a `0` should go.

---

### `mid`

Current element being checked.

---

### `high`

Next position where a `2` should go.

---

# Rules

### Case 1

If

```python
nums[mid] == 0
```

Swap with `low`.

Then

```python
low += 1
mid += 1
```

Why?

Because both positions are now correctly placed.

---

### Case 2

If

```python
nums[mid] == 1
```

Nothing to do.

Just

```python
mid += 1
```

because `1` belongs in the middle.

---

### Case 3

If

```python
nums[mid] == 2
```

Swap with `high`.

```python
high -= 1
```

Do **NOT** increment `mid`.

---

# Why Don't We Increment `mid`?

Suppose

```
2 1 0

^

mid
```

Swap

```
0 1 2

^

mid
```

The new value at `mid` is `0`.

We haven't processed it yet.

If we move `mid`, we skip it.

So after swapping with `high`, only move `high`.

---

# Dry Run

Input

```
[2,0,2,1,1,0]
```

Initially

```
low = 0

mid = 0

high = 5
```

---

### Step 1

```
2 0 2 1 1 0
^

mid
```

Swap with high.

```
0 0 2 1 1 2
^

mid

high = 4
```

---

### Step 2

```
0 0 2 1 1 2
^

mid
```

Swap with low.

```
0 0 2 1 1 2

low=1

mid=1
```

---

### Step 3

```
0 0 2 1 1 2
  ^

mid
```

Again swap with low.

```
0 0 2 1 1 2

low=2

mid=2
```

---

### Step 4

```
0 0 2 1 1 2
    ^

mid
```

Swap with high.

```
0 0 1 1 2 2

high=3

mid stays
```

---

### Step 5

```
0 0 1 1 2 2
    ^

mid
```

Current value is `1`.

Move

```
mid=3
```

---

### Step 6

Again

```
nums[mid] = 1
```

Move

```
mid=4
```

Now

```
mid > high
```

Stop.

Answer

```
[0,0,1,1,2,2]
```

---

# Visualization

Before

```
| Unknown |

2 0 2 1 1 0
```

After processing

```
| 0s | 1s | 2s |

0 0 1 1 2 2
```

---

# Complexity

```
Time  : O(n)

Space : O(1)
```

Only one traversal is required.

---

# Method 2 : Brute Force

```python
class Solution:
    def sortColors(self, nums):

        nums.sort()
```

---

# Complexity

```
Time  : O(n log n)

Space : Depends on implementation
```

This works on LeetCode but **does not satisfy** the interview requirement.

---

# ⭐ Pythonic Way

```python
class Solution:
    def sortColors(self, nums):

        nums.sort()
```

---

# Pythonic Explanation

## New Function : `sort()`

Sorts the list **in-place**.

Example

```python
arr = [2,0,1]

arr.sort()

print(arr)
```

Output

```
[0,1,2]
```

---

## Difference Between `sort()` and `sorted()`

### `sort()`

Changes the original list.

```python
arr = [3,1,2]

arr.sort()

print(arr)
```

Output

```
[1,2,3]
```

---

### `sorted()`

Returns a **new list**.

```python
arr = [3,1,2]

newArr = sorted(arr)

print(arr)
print(newArr)
```

Output

```
[3,1,2]

[1,2,3]
```

Original list remains unchanged.

---

# Why Dutch National Flag is Better?

Suppose

```
2 0 2 1 1 0
```

Sorting compares many elements.

Dutch National Flag only checks each element once.

Every element is moved directly to its correct region.

---

# Comparison

| Method              | Time       | Space   |
| ------------------- | ---------- | ------- |
| Built-in Sort       | O(n log n) | Depends |
| Dutch National Flag | O(n)       | O(1)    |

---

# Key Learnings

* Use **three pointers**:

  * `low`
  * `mid`
  * `high`
* `0` goes to the front.
* `2` goes to the back.
* `1` stays in the middle.
* After swapping with `high`, **do not increment `mid`** because the swapped element still needs to be checked.

---

# Interview Tips

Whenever you hear:

* Array contains only **3 distinct values**
* Sort in **O(n)**
* Sort **in-place**
* No extra space

Think of the **Dutch National Flag Algorithm**.

It is the expected interview solution.

```
Time  : O(n)

Space : O(1)
```
# 📘 Day74_Q91_Trapping_Rain_Water.md

# ✅ Q91. Trapping Rain Water (LeetCode 42)

## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

---

# Example 1

```text
Input:
height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output:
6
```

Visualization

```text
            █
      █~~~~~█
  █~~~██~█~~██
█~██~█████████
--------------
```

The `~` represents trapped water.

---

# Example 2

```text
Input:
height = [4,2,0,3,2,5]

Output:
9
```

---

# Method 1 : Prefix Maximum Arrays (Optimal)

## DSA Solution (Python)

```python
class Solution:
    def trap(self, height):

        n = len(height)

        left = [0] * n
        right = [0] * n

        left[0] = height[0]

        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        right[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        water = 0

        for i in range(n):
            water += min(left[i], right[i]) - height[i]

        return water
```

---

# Algorithm

## Step 1

Create two arrays.

```python
left = [0] * n
right = [0] * n
```

* `left[i]` = tallest building from the **left** till index `i`
* `right[i]` = tallest building from the **right** till index `i`

---

## Step 2

Build the `left` array.

```python
left[i] = max(left[i-1], height[i])
```

---

## Step 3

Build the `right` array.

```python
right[i] = max(right[i+1], height[i])
```

---

## Step 4

Water trapped at every index

```python
min(left[i], right[i]) - height[i]
```

Why minimum?

Water can only rise as high as the **shorter wall**.

---

## Step 5

Add water from every index.

---

# Dry Run

Input

```text
height = [4,2,0,3,2,5]
```

---

## Build Left Array

Initially

```text
left

[4,0,0,0,0,0]
```

After loop

```text
[4,4,4,4,4,5]
```

---

## Build Right Array

Initially

```text
right

[0,0,0,0,0,5]
```

After loop

```text
[5,5,5,5,5,5]
```

---

## Calculate Water

| Index | Height | Left | Right | Water |
| ----: | -----: | ---: | ----: | ----: |
|     0 |      4 |    4 |     5 |     0 |
|     1 |      2 |    4 |     5 |     2 |
|     2 |      0 |    4 |     5 |     4 |
|     3 |      3 |    4 |     5 |     1 |
|     4 |      2 |    4 |     5 |     2 |
|     5 |      5 |    5 |     5 |     0 |

Total

```text
2+4+1+2 = 9
```

Answer

```text
9
```

---

# Why Use `min(left,right)`?

Suppose

```text
4      6
█      █
█      █
█  ?   █
█      █
```

Water can only rise till

```text
4
```

because the left wall is shorter.

If we used

```python
max(left,right)
```

we would incorrectly trap water higher than the shorter wall.

---

# Visualization

Height

```text
4 2 0 3 2 5
```

Left Maximum

```text
4 4 4 4 4 5
```

Right Maximum

```text
5 5 5 5 5 5
```

Water

```text
0 2 4 1 2 0
```

---

# Complexity

```text
Time  : O(n)

Space : O(n)
```

---

# ⭐ Pythonic Way

```python
class Solution:
    def trap(self, height):

        n = len(height)

        left = [0] * n
        right = [0] * n

        left[0] = height[0]

        for i in range(1, n):
            left[i] = max(left[i-1], height[i])

        right[-1] = height[-1]

        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        return sum(
            min(left[i], right[i]) - height[i]
            for i in range(n)
        )
```

---

# Pythonic Explanation

## New Function : `sum()`

Adds every value from an iterable.

Example

```python
nums = [1,2,3]

print(sum(nums))
```

Output

```text
6
```

---

## Generator Expression

```python
sum(
    min(left[i], right[i]) - height[i]
    for i in range(n)
)
```

Instead of writing

```python
water = 0

for i in range(n):
    water += ...
```

we directly generate every trapped water value and sum them.

Example

```python
sum(x*x for x in range(5))
```

becomes

```text
0+1+4+9+16

↓

30
```

---

## Negative Index

```python
right[-1]
```

means

```text
Last element
```

Example

```python
arr = [10,20,30]

arr[-1]

↓

30
```

---

# ⭐ Interview Optimized Solution (Two Pointers)

This is the **best interview solution** because it uses **O(1) space**.

```python
class Solution:
    def trap(self, height):

        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0

        water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]

                left += 1

            else:

                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]

                right -= 1

        return water
```

---

# Why Does the Two-Pointer Method Work?

At every step:

* The **smaller side** determines the maximum possible water.
* Move only the smaller pointer.
* Update the corresponding maximum height.
* Add trapped water if the current bar is lower than the maximum.

No extra arrays are needed.

---

# Complexity Comparison

| Method                     | Time | Space |
| -------------------------- | ---- | ----- |
| Prefix Left & Right Arrays | O(n) | O(n)  |
| Two Pointers               | O(n) | O(1)  |

---

# Key Learnings

* Water above a bar depends on the **shorter** of the tallest bars on its left and right.
* Formula:

```text
Water = min(leftMax, rightMax) - currentHeight
```

* Prefix arrays make the solution easy to understand.
* The two-pointer approach is the optimal interview solution.

---

# Interview Tips

Whenever you hear:

* Rain Water
* Elevation Map
* Trapped Water
* Histogram

Think:

```text
Left Maximum

+

Right Maximum

↓

Water = min(left,right)-height
```

Then remember the optimization:

```text
Prefix Arrays

↓

Two Pointers
```

Final Complexities:

```text
Prefix Arrays

Time  : O(n)
Space : O(n)

Two Pointers

Time  : O(n)
Space : O(1)
```
# 📘 Day74_Q92_Container_With_Most_Water.md

# ✅ Q92. Container With Most Water (LeetCode 11)

## Problem

You are given an integer array `height`.

Each element represents the height of a vertical line.

Choose **two lines** such that together with the x-axis they form a container that holds the **maximum amount of water**.

Return the maximum amount of water.

---

# Example 1

```text
Input:
height = [1,8,6,2,5,4,8,3,7]

Output:
49
```

Visualization

```text
Height

8 |      █           █
7 |      █           █
6 |      █ █         █
5 |      █ █   █     █
4 |      █ █   █ █   █
3 |      █ █   █ █   █ █
2 |      █ █ █ █ █   █ █
1 |█     █ █ █ █ █ █ █ █
 -------------------------
  0 1 2 3 4 5 6 7 8
```

Best container

```text
Height = min(8,7) = 7

Width = 8-1 = 7

Area = 7 × 7 = 49
```

---

# Formula

```text
Area = Width × Height

Width = Right - Left

Height = min(height[left], height[right])
```

---

# Method 1 : Brute Force

## DSA Solution (Python)

```python
class Solution:
    def maxArea(self, height):

        maximum = 0

        for i in range(len(height)):

            for j in range(i + 1, len(height)):

                width = j - i

                currentHeight = min(height[i], height[j])

                area = width * currentHeight

                maximum = max(maximum, area)

        return maximum
```

---

# Algorithm

For every pair

```text
(i,j)
```

Calculate

* Width
* Minimum height
* Area

Update the maximum area.

---

# Dry Run

Input

```text
[1,8,6]
```

Pair

```text
(1,8)

Width = 1

Height = 1

Area = 1
```

Pair

```text
(1,6)

Width = 2

Height = 1

Area = 2
```

Pair

```text
(8,6)

Width = 1

Height = 6

Area = 6
```

Answer

```text
6
```

---

# Complexity

```text
Time  : O(n²)

Space : O(1)
```

---

# Method 2 : Two Pointer (Optimal)

## DSA Solution (Python)

```python
class Solution:
    def maxArea(self, height):

        left = 0
        right = len(height) - 1

        maximum = 0

        while left < right:

            width = right - left

            currentHeight = min(
                height[left],
                height[right]
            )

            area = width * currentHeight

            maximum = max(maximum, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum
```

---

# Algorithm

Start with

```text
Left = Beginning

Right = End
```

At every step

Calculate

```text
Width

×

Minimum Height
```

Update answer.

Move the pointer having the **smaller height**.

---

# Why Move the Smaller Height?

Suppose

```text
8           3

█           █
█           █
█           █
```

Area

```text
Width × 3
```

The height is limited by

```text
3
```

Moving the taller wall cannot increase the height.

Only moving the smaller wall gives a chance of finding a taller wall.

---

# Why Don't We Move the Taller Pointer?

Example

```text
1             8

█             █
              █
              █
```

Current area

```text
Width × 1
```

If we move the taller wall

```text
1         6

█         █
          █
```

The height is still

```text
1
```

Width decreases.

Area definitely decreases.

So moving the taller wall never helps.

---

# Dry Run

Input

```text
height =
[1,8,6,2,5,4,8,3,7]
```

Initially

```text
left = 0

right = 8
```

---

Step 1

```text
Height

1 and 7

Width

8

Area

8
```

Move

```text
Left
```

because

```text
1 < 7
```

---

Step 2

```text
8 and 7

Width = 7

Height = 7

Area = 49
```

Maximum

```text
49
```

Move

```text
Right
```

because

```text
7 < 8
```

---

Continue until

```text
left == right
```

Answer

```text
49
```

---

# Visualization

Initial

```text
L               R

1 8 6 2 5 4 8 3 7
```

After moving pointers

```text
  L           R

1 8 6 2 5 4 8 3 7
```

Best area found

```text
49
```

---

# Complexity

```text
Time  : O(n)

Space : O(1)
```

---

# ⭐ Pythonic Way

```python
class Solution:
    def maxArea(self, height):

        left = 0
        right = len(height) - 1

        maximum = 0

        while left < right:

            maximum = max(
                maximum,
                (right - left)
                * min(height[left], height[right])
            )

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum
```

---

# Pythonic Explanation

## New Function : `min()`

Returns the smaller value.

Example

```python
min(8,7)
```

Output

```text
7
```

The water level is always limited by the shorter wall.

---

## New Function : `max()`

Returns the larger value.

Example

```python
max(20,35)
```

Output

```text
35
```

Used to keep track of the best area.

---

## Why Write It in One Line?

Instead of

```python
width = right-left

height = min(...)

area = width*height

maximum = max(maximum,area)
```

we directly compute

```python
maximum = max(
    maximum,
    (right-left) *
    min(height[left], height[right])
)
```

This is more compact while doing exactly the same work.

---

# Comparison

| Method      | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(n²) | O(1)  |
| Two Pointer | O(n)  | O(1)  |

---

# Difference Between Q91 and Q92

| Trapping Rain Water                           | Container With Most Water                           |
| --------------------------------------------- | --------------------------------------------------- |
| Water trapped **between all bars**            | Water held by **only two bars**                     |
| Formula: `min(leftMax, rightMax) - height[i]` | Formula: `width × min(height[left], height[right])` |
| Uses Prefix Arrays / Two Pointers             | Uses Two Pointers                                   |
| Every index contributes                       | Only one pair contributes                           |

---

# Key Learnings

* Area depends on:

  * Width
  * Smaller height
* Always move the pointer having the smaller height.
* Moving the taller wall only decreases width without increasing the limiting height.
* The two-pointer solution reduces the time complexity from **O(n²)** to **O(n)**.

---

# Interview Tips

Whenever you hear:

* Two vertical lines
* Maximum water
* Container

Immediately think:

```text
Area

=

Width

×

Minimum Height
```

Then remember:

```text
Move the Smaller Pointer
```

This gives the optimal solution.

```text
Time  : O(n)

Space : O(1)
```
