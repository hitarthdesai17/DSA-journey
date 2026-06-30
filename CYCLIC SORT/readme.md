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
# 📘 Day81_Cyclic_Sort_Problems.md

# 🌟 Cyclic Sort Pattern Problems

In this file we'll cover three famous LeetCode problems that use the **Cyclic Sort Pattern**.

1. ✅ LeetCode 268 – Missing Number
2. ✅ LeetCode 448 – Find All Numbers Disappeared in an Array
3. ✅ LeetCode 41 – First Missing Positive

---

# 🧠 Before Starting

The most important thing is **not the code**.

The most important thing is identifying **when Cyclic Sort can be used.**

Whenever you read a question ask yourself:

### Question 1

Are the numbers in a fixed range?

Examples

```text
0 to n

or

1 to n
```

If YES ✅

Go to Question 2.

---

### Question 2

Does every number have one fixed position?

Example

```text
Number 5

↓

Index 5
```

or

```text
Number 5

↓

Index 4

(5-1)
```

If YES ✅

Think

```text
CYCLIC SORT
```

---

# Pattern

Almost every Cyclic Sort problem looks like this.

```python
i = 0

while i < len(nums):

    correct = ...

    if current number is valid AND not at correct position:

        swap()

    else:

        i += 1
```

After sorting,

we simply check which positions are wrong.

Those wrong positions directly give the answer.

---

# ✅ Q94. LeetCode 268 - Missing Number

## Problem

Given an array containing

```text
0 → n
```

numbers,

exactly **one number is missing.**

Return that missing number.

---

## Example

```text
Input

[3,0,1]
```

Output

```text
2
```

---

# Intuition

Notice

```text
Numbers

0 1 2 3
```

Indexes

```text
0 1 2 3
```

Every number belongs to

```text
Same Index
```

Example

```text
3

↓

Index 3
```

Unlike previous Cyclic Sort,

there is **no -1 here.**

Correct index

```python
correct = nums[i]
```

---

# Why isn't there "-1"?

Because

Numbers start from

```text
0
```

not

```text
1
```

Example

|Number|Correct Index|
|------|-------------|
|0|0|
|1|1|
|2|2|
|3|3|

---

# Problem

Suppose

```text
nums=[3,0,1]

Length=3
```

Where should

```text
3
```

go?

Index

```text
3
```

doesn't exist.

Array only has

```text
0 1 2
```

Therefore

before swapping

we must check

```python
nums[i] < len(nums)
```

Otherwise

```python
nums[3]
```

will cause

```text
IndexError
```

---

# Algorithm

### Step 1

Put every valid number at its own index.

### Step 2

Traverse again.

If

```python
nums[i] != i
```

then

```text
i
```

is missing.

If every index is correct,

then answer is

```python
len(nums)
```

---

# Python Code

```python
class Solution:

    def missingNumber(self, nums):

        i = 0

        while i < len(nums):

            correct = nums[i]

            if nums[i] < len(nums) and nums[i] != nums[correct]:

                nums[i], nums[correct] = nums[correct], nums[i]

            else:

                i += 1

        for i in range(len(nums)):

            if nums[i] != i:

                return i

        return len(nums)
```

---

# Dry Run

Input

```text
[3,0,1]
```

Initially

```text
3 0 1
```

3 is ignored because

```text
3

=

len(nums)
```

Swap

```text
0

↓

Index 0
```

Array

```text
0 3 1
```

Swap

```text
1

↓

Index 1
```

Array

```text
0 1 3
```

Check

```text
Index 2

Expected

2

Found

3
```

Answer

```text
2
```

---

# Complexity

```text
Time

O(n)

Space

O(1)
```

==================================================================

# ✅ Q95. LeetCode 448 - Find All Numbers Disappeared in an Array

## Problem

Numbers are from

```text
1 to n
```

Some numbers appear twice.

Some are missing.

Return all missing numbers.

---

## Example

```text
Input

[4,3,2,7,8,2,3,1]
```

Output

```text
[5,6]
```

---

# Intuition

Numbers start from

```text
1
```

Therefore

Correct Index

```text
Number-1
```

Example

|Number|Correct Index|
|------|-------------|
|1|0|
|2|1|
|3|2|
|4|3|

---

# Why Does This Work?

Imagine lockers.

Locker

```text
0
```

should contain

```text
1
```

Locker

```text
1
```

should contain

```text
2
```

After everyone reaches their locker,

if locker

```text
4
```

contains

```text
3
```

instead of

```text
5
```

then

```text
5
```

never came.

Hence

```text
5
```

is missing.

---

# Algorithm

### Step 1

Place every number

at

```text
Number-1
```

### Step 2

Traverse again.

If

```python
nums[i] != i+1
```

then

```text
i+1
```

is missing.

---

# Python Code

```python
class Solution:

    def findDisappearedNumbers(self, nums):

        i = 0

        while i < len(nums):

            correct = nums[i]-1

            if nums[i] != nums[correct]:

                nums[i], nums[correct] = nums[correct], nums[i]

            else:

                i += 1

        ans = []

        for i in range(len(nums)):

            if nums[i] != i+1:

                ans.append(i+1)

        return ans
```

---

# Dry Run

After Cyclic Sort

```text
[1,2,3,4,3,2,7,8]
```

Check

```text
Index 4

Expected

5

Found

3
```

Missing

```text
5
```

Check

```text
Index 5

Expected

6

Found

2
```

Missing

```text
6
```

Answer

```text
[5,6]
```

---

# Complexity

```text
Time

O(n)

Space

O(1)
```

==================================================================

# ✅ Q96. LeetCode 41 - First Missing Positive

## Problem

Find the **smallest positive integer**

that is missing.

---

## Example

```text
Input

[3,4,-1,1]
```

Output

```text
2
```

---

# Why is this harder?

Array may contain

```text
Negative Numbers

Zero

Large Numbers
```

Example

```text
100

-7

0
```

These numbers have

no valid position.

We simply ignore them.

---

# Which numbers should we place?

Only

```text
1

to

n
```

Because only these numbers can affect the answer.

---

# Important Condition

```python
nums[i] > 0
```

Ignore

```text
Negative Numbers

Zero
```

---

```python
nums[i] <= len(nums)
```

Ignore

```text
100

200

500
```

because they have no valid index.

---

# Algorithm

### Step 1

Place only valid numbers

```text
1→n
```

at

```text
Number-1
```

### Step 2

Traverse.

First place where

```python
nums[i] != i+1
```

Return

```python
i+1
```

If everything is correct,

return

```python
len(nums)+1
```

---

# Python Code

```python
class Solution:

    def firstMissingPositive(self, nums):

        i = 0

        while i < len(nums):

            correct = nums[i]-1

            if (
                nums[i] > 0
                and nums[i] <= len(nums)
                and nums[i] != nums[correct]
            ):

                nums[i], nums[correct] = nums[correct], nums[i]

            else:

                i += 1

        for i in range(len(nums)):

            if nums[i] != i+1:

                return i+1

        return len(nums)+1
```

---

# Dry Run

Input

```text
[3,4,-1,1]
```

Ignore

```text
-1
```

because

```text
Negative
```

After Cyclic Sort

```text
[1,-1,3,4]
```

Check

```text
Index 0

Expected

1

Found

1
```

Good.

---

```text
Index 1

Expected

2

Found

-1
```

Therefore

```text
2
```

is the first missing positive.

---

# Complexity

```text
Time

O(n)

Space

O(1)
```

==================================================================

# ⭐ Python Concepts Used

## Tuple Swapping

Instead of

```python
temp=nums[i]
nums[i]=nums[j]
nums[j]=temp
```

Python allows

```python
nums[i],nums[j]=nums[j],nums[i]
```

---

## Why While Loop?

Many beginners ask

> Why not use a for loop?

Because after every swap,

we may need to check

the same index again.

A

```python
for
```

loop automatically moves forward.

A

```python
while
```

loop gives us control.

---

# 🎯 How to Identify Cyclic Sort Problems

Ask yourself

### Are numbers in a fixed range?

```text
0→n

or

1→n
```

↓

YES

---

### Does every number have one correct position?

↓

YES

---

Think

```text
CYCLIC SORT
```

---

# 📊 Comparison

| Problem | Range | Correct Index | Final Check |
|---------|------|---------------|-------------|
| Missing Number (268) | 0 → n | num | nums[i] != i |
| Find Disappeared Numbers (448) | 1 → n | num-1 | nums[i] != i+1 |
| First Missing Positive (41) | 1 → n (valid only) | num-1 | First nums[i] != i+1 |

---

# 🧠 Memory Trick

```text
Numbers from 0?

↓

Correct Index = Number

-----------------------

Numbers from 1?

↓

Correct Index = Number - 1

-----------------------

After Cyclic Sort

↓

Wrong Index

↓

Answer Found
```

# 🚀 Interview Pattern

Whenever you see:

- Missing Number
- Missing Positive
- Duplicate Number
- Numbers from 1 to n
- Numbers from 0 to n

Immediately ask yourself:

```text
Can every number be placed at one fixed index?

↓

YES

↓

Use Cyclic Sort
```