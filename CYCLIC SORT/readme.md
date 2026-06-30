# 📘 Day80_Q96_Cyclic_Sort.md

# ✅ Q96. Cyclic Sort

## Definition

Cyclic Sort is a sorting algorithm that works **only when the numbers are in a fixed range**, usually:

```text
1 to n
```

or

```text
0 to n-1
```

Instead of comparing adjacent elements like Bubble Sort, it places every number directly into its correct position.

---

# Example

```text
Input

[3,5,2,1,4]
```

Output

```text
[1,2,3,4,5]
```

---

# When Should We Use Cyclic Sort?

Cyclic Sort is useful when:

- Numbers are in the range **1 to n**
- Every number should appear exactly once
- We need to find:
  - Missing Number
  - Duplicate Number
  - First Missing Positive
  - Set Mismatch
  - Missing Numbers

Whenever you hear

> "Numbers are from 1 to n"

Think

```text
Cyclic Sort
```

---

# Why is it called "Cyclic" Sort?

Imagine every number knows where it belongs.

For example

```text
5 belongs at index 4

3 belongs at index 2

1 belongs at index 0
```

We keep swapping numbers until every number reaches its own home.

The numbers keep moving in a cycle until all are correctly placed.

---

# Important Idea

Suppose

```text
Array

[3,5,2,1,4]
```

Indexes

```text
0 1 2 3 4
```

Number

```text
3
```

belongs at

```text
Index 2
```

because

```text
3 - 1 = 2
```

---

# Why "number - 1"?

This is the most important concept.

Suppose numbers are

```text
1 2 3 4 5
```

Indexes are

```text
0 1 2 3 4
```

Notice

| Number | Correct Index |
|---------|--------------:|
|1|0|
|2|1|
|3|2|
|4|3|
|5|4|

Pattern

```text
Correct Index

=

Number - 1
```

Therefore

```python
correct = nums[i] - 1
```

---

# Python Solution

```python
class Solution:

    def cyclicSort(self, nums):

        i = 0

        while i < len(nums):

            correct = nums[i] - 1

            if nums[i] != nums[correct]:

                nums[i], nums[correct] = nums[correct], nums[i]

            else:

                i += 1

        return nums
```

---

# Line-by-Line Explanation

## Step 1

```python
i = 0
```

Start from the first element.

---

## Step 2

```python
correct = nums[i] - 1
```

Find where the current number actually belongs.

Example

```text
nums[i] = 5
```

Then

```text
correct = 4
```

because

```text
5 belongs at index 4
```

---

## Step 3

```python
if nums[i] != nums[correct]
```

Ask

> Is this number already in its correct position?

If not,

swap it.

---

## Step 4

```python
nums[i], nums[correct] = nums[correct], nums[i]
```

Move the number directly to its correct place.

---

## Step 5

Otherwise

```python
i += 1
```

Move to the next index.

---

# ❓ Why Don't We Increment `i` After Every Swap?

This is the biggest doubt beginners have.

Suppose

```text
[3,5,2,1,4]

^

i
```

Current number

```text
3
```

Swap

```text
[2,5,3,1,4]

^

i
```

Now

```text
2
```

has come to index 0.

Question:

Has **2** been checked?

No.

If we immediately do

```python
i += 1
```

we skip checking **2**.

It may still be in the wrong place.

Therefore

we stay at the same index

until the correct number reaches it.

Only then do we increment `i`.

---

# Complete Dry Run

Input

```text
[3,5,2,1,4]
```

---

## Step 1

```text
i = 0

3 belongs at index 2
```

Swap

```text
[2,5,3,1,4]
```

Stay at

```text
i = 0
```

---

## Step 2

Current

```text
2
```

belongs at

```text
1
```

Swap

```text
[5,2,3,1,4]
```

Stay

```text
i = 0
```

---

## Step 3

Current

```text
5
```

belongs

```text
4
```

Swap

```text
[4,2,3,1,5]
```

Stay

```text
i = 0
```

---

## Step 4

Current

```text
4
```

belongs

```text
3
```

Swap

```text
[1,2,3,4,5]
```

Stay

```text
i = 0
```

---

Now

```text
1
```

is finally correct.

Move

```text
i = 1
```

Continue...

Everything is already correct.

Answer

```text
[1,2,3,4,5]
```

---

# Visualization

Initially

```text
Index

0 1 2 3 4

Array

3 5 2 1 4
```

Final

```text
Index

0 1 2 3 4

Array

1 2 3 4 5
```

Every number reaches

```text
Number - 1
```

---

# Why Doesn't This Work for Every Array?

Suppose

```text
[10,20,30]
```

Where should

```text
20
```

go?

Using

```text
20-1

=

19
```

There is no

```text
Index 19
```

Therefore

Cyclic Sort only works when

numbers have a fixed range.

---

# Time Complexity

At first glance,

it looks like

```text
O(n²)
```

because swaps happen inside a loop.

Actually,

it is

```text
O(n)
```

Why?

Every swap places at least **one number into its correct position**.

Once a number reaches its correct position,

it never moves again.

Maximum swaps

```text
n
```

Maximum iterations

```text
n
```

Therefore

```text
O(n)
```

---

# Space Complexity

```text
O(1)
```

No extra arrays are used.

Sorting happens inside the original array.

---

# Stable or Not?

```text
❌ Not Stable
```

Equal elements may change order.

(Usually Cyclic Sort assumes unique elements.)

---

# Pythonic Way

The algorithm itself is already the cleanest Python implementation.

Python's

```python
nums.sort()
```

works for every array,

but Cyclic Sort is much faster for this special type of problem because it uses the properties of the input.

---

# Pythonic Explanation

## Tuple Swapping

Instead of

```python
temp = nums[i]
nums[i] = nums[correct]
nums[correct] = temp
```

Python allows

```python
nums[i], nums[correct] = nums[correct], nums[i]
```

Much shorter.

---

## Why Use `while` Instead of `for`?

Another beginner question.

Could we write

```python
for i in range(len(nums)):
```

No.

Why?

Because after swapping,

we sometimes want to stay on the **same index**.

A `for` loop automatically moves to the next index.

A `while` loop lets us decide.

If current number is wrong

```text
Stay

↓

Swap Again

↓

Stay

↓

Swap Again
```

Only move when the current index becomes correct.

---

# Common Mistakes

❌ Forgetting

```python
correct = nums[i]-1
```

---

❌ Incrementing `i` immediately after swapping.

---

❌ Using Cyclic Sort on arbitrary arrays.

---

❌ Forgetting the input must contain numbers from

```text
1 to n
```

or

```text
0 to n-1
```

---

# Comparison

| Algorithm | Time | Space | Works for Any Array |
|-----------|------|--------|---------------------|
| Bubble Sort | O(n²) | O(1) | ✅ |
| Selection Sort | O(n²) | O(1) | ✅ |
| Merge Sort | O(n log n) | O(n) | ✅ |
| Quick Sort | O(n log n) Avg | O(log n) | ✅ |
| Cyclic Sort | O(n) | O(1) | ❌ Only 1..n arrays |

---

# Where is Cyclic Sort Used?

Many famous interview problems use this idea:

- Missing Number
- Find All Missing Numbers
- Find Duplicate Number
- Find All Duplicates
- Set Mismatch
- First Missing Positive

Whenever you notice

```text
Numbers are from 1 to n
```

think

```text
Cyclic Sort
```

---

# Key Learnings

- Every number knows its correct position.
- Correct index = Number − 1.
- Swap until the current number reaches its home.
- Don't increment `i` after swapping.
- Increment `i` only when the current index is correct.
- Runs in O(n) because every swap fixes at least one element.

---

# Memory Trick

```text
Current Number

↓

Find Correct Index

↓

Already Correct?

↓

Yes → Move Forward

↓

No → Swap

↓

Stay on Same Index

↓

Repeat
```