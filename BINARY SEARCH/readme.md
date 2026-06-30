# ✅ Q98. LeetCode 35 – Search Insert Position

## 📌 Problem Statement

You are given a **sorted array** of distinct integers and a target value.

Your task is to:

- Return the **index** if the target exists.
- If it does **not** exist, return the **index where it should be inserted** so that the array remains sorted.

---

## Example 1

```text
Input

nums = [1,3,5,6]
target = 5

Output

2
```

Explanation

```text
Index

0 1 2 3

Array

1 3 5 6
    ↑
Target = 5

Already exists at index 2.
```

---

## Example 2

```text
Input

nums = [1,3,5,6]
target = 2

Output

1
```

Explanation

```text
Current Array

1 3 5 6

Insert 2 here

1 2 3 5 6
```

So answer is

```text
1
```

---

## Example 3

```text
Input

nums = [1,3,5,6]
target = 7
```

Output

```text
4
```

Because

```text
1 3 5 6 7
        ↑
```

It should be inserted after the last element.

---

# 🧠 Beginner Intuition

A beginner's first thought might be:

> "I'll start from the first element and compare every number."

Example

```text
nums = [1,3,5,6]

target = 2
```

Compare

```text
1

↓

3

↓

Stop
```

Since

```text
2 < 3
```

Insert before 3.

This works.

But what if the array contains

```text
1,000,000 elements?
```

Worst case

```text
1,000,000 comparisons
```

Time Complexity

```text
O(n)
```

Can we do better?

Yes.

The array is already **sorted**, which is the biggest hint.

---

# 💡 Key Observation

Notice the array is sorted.

```text
1 3 5 6
```

When we check the middle element,

we immediately know that **half of the array cannot contain the answer**.

That's why Binary Search works.

---

# Why Binary Search?

Suppose

```text
nums = [1,3,5,6]

target = 2
```

Initially

```text
Start          End

1 3 5 6

    Mid
```

Middle is

```text
3
```

Question:

Is

```text
2
```

greater than

```text
3?
```

No.

Therefore,

everything on the **right side** can be ignored.

We reduced the search space by half.

---

# 🔍 Algorithm

### Step 1

Initialize

```python
start = 0
end = len(nums)-1
```

---

### Step 2

Repeat while

```python
start <= end
```

---

### Step 3

Find middle

```python
mid = (start + end)//2
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

If

```python
nums[mid] < target
```

Search the right half.

```python
start = mid + 1
```

---

### Step 6

Else

Search the left half.

```python
end = mid - 1
```

---

### Step 7

If the loop finishes,

return

```python
start
```

This is the insertion position.

---

# ⭐ Why Do We Return `start`?

This is the most important concept in this problem.

Many beginners ask:

> "If the target wasn't found, why does `start` become the answer?"

Let's understand.

---

## Example

```text
nums = [1,3,5,6]

target = 2
```

Initially

```text
start = 0

end = 3
```

---

### First Iteration

```text
mid = 1

nums[mid] = 3
```

Since

```text
2 < 3
```

Move left

```python
end = mid-1
```

Now

```text
start = 0

end = 0
```

---

### Second Iteration

```text
mid = 0

nums[mid] = 1
```

Since

```text
2 > 1
```

Move right

```python
start = mid+1
```

Now

```text
start = 1

end = 0
```

Loop ends because

```text
start > end
```

Question:

Where should

```text
2
```

go?

Exactly at

```text
Index 1
```

And notice

```text
start = 1
```

That is why

```python
return start
```

works.

---

## Another Example

```text
nums = [1,3,5,6]

target = 7
```

Eventually

```text
start = 4

end = 3
```

Loop ends.

Insert at

```text
Index 4
```

Exactly where

```text
start
```

is pointing.

---

## Memory Trick

Think of

```text
start
```

as

> **"The first possible place where the target can exist."**

If the target isn't found,

that place becomes its insertion position.

---

# ✅ Python Solution

```python
class Solution:

    def searchInsert(self, nums, target):

        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return start
```

---

# 📝 Line-by-Line Explanation

### Initialize pointers

```python
start = 0
end = len(nums)-1
```

Search the whole array.

---

### Find middle

```python
mid = (start+end)//2
```

Divide the search space into two halves.

---

### Target Found

```python
if nums[mid] == target:
    return mid
```

Return immediately.

---

### Target Bigger

```python
start = mid+1
```

Ignore the left half.

---

### Target Smaller

```python
end = mid-1
```

Ignore the right half.

---

### Target Not Found

```python
return start
```

Return insertion position.

---

# 📖 Complete Dry Run

Input

```text
nums = [1,3,5,6]

target = 2
```

### Iteration 1

```text
start = 0

end = 3

mid = 1

nums[mid] = 3
```

```text
2 < 3
```

Move left

```text
end = 0
```

---

### Iteration 2

```text
start = 0

end = 0

mid = 0

nums[mid] = 1
```

```text
2 > 1
```

Move right

```text
start = 1
```

---

Loop ends

```text
start = 1

end = 0
```

Return

```text
1
```

Correct.

---

# ⚠️ Common Mistakes

### ❌ Returning `end`

Many beginners write

```python
return end
```

Wrong.

Example

```text
nums=[1,3]

target=2
```

End becomes

```text
0
```

Correct answer

```text
1
```

Always return

```python
start
```

---

### ❌ Using

```python
while start < end
```

This skips checking the last remaining element.

Always write

```python
while start <= end
```

---

### ❌ Forgetting

```python
mid = (start+end)//2
```

Using

```python
/
```

returns a float.

Use

```python
//
```

for integer division.

---

# 🐍 Pythonic Explanation

## Integer Division

```python
mid = (start+end)//2
```

`//`

means **floor division**.

Example

```python
7//2
```

Output

```text
3
```

---

## len()

```python
len(nums)
```

Returns the number of elements.

Example

```python
nums=[1,3,5,6]
```

```python
len(nums)
```

returns

```text
4
```

---

# ⏱ Complexity

## Time

Every iteration removes half of the array.

```text
n

↓

n/2

↓

n/4

↓

n/8

↓

1
```

Time Complexity

```text
O(log n)
```

---

## Space

Only three variables are used.

```text
start

end

mid
```

Space Complexity

```text
O(1)
```

---

# 🎯 Interview Pattern

Whenever you hear

- Sorted Array
- Search
- Insert Position
- Lower Bound

Think

```text
Binary Search
```

---

# 🧠 Memory Trick

```text
Sorted Array

↓

Binary Search

↓

Found?

↓

YES → Return Mid

↓

NO

↓

Return Start
```

---

# 📚 Key Learnings

- Binary Search works only because the array is sorted.
- Every comparison removes half of the search space.
- If the target exists, return its index.
- If it doesn't exist, `start` always points to the correct insertion position.
- Time Complexity is **O(log n)**.
- Space Complexity is **O(1)**.
# ✅ Q98. LeetCode 35 – Search Insert Position

## 📌 Problem Statement

You are given a **sorted array** of distinct integers and a target value.

Your task is to:

- Return the **index** if the target exists.
- If it does **not** exist, return the **index where it should be inserted** so that the array remains sorted.

---

## Example 1

```text
Input

nums = [1,3,5,6]
target = 5

Output

2
```

Explanation

```text
Index

0 1 2 3

Array

1 3 5 6
    ↑
Target = 5

Already exists at index 2.
```

---

## Example 2

```text
Input

nums = [1,3,5,6]
target = 2

Output

1
```

Explanation

```text
Current Array

1 3 5 6

Insert 2 here

1 2 3 5 6
```

So answer is

```text
1
```

---

## Example 3

```text
Input

nums = [1,3,5,6]
target = 7
```

Output

```text
4
```

Because

```text
1 3 5 6 7
        ↑
```

It should be inserted after the last element.

---

# 🧠 Beginner Intuition

A beginner's first thought might be:

> "I'll start from the first element and compare every number."

Example

```text
nums = [1,3,5,6]

target = 2
```

Compare

```text
1

↓

3

↓

Stop
```

Since

```text
2 < 3
```

Insert before 3.

This works.

But what if the array contains

```text
1,000,000 elements?
```

Worst case

```text
1,000,000 comparisons
```

Time Complexity

```text
O(n)
```

Can we do better?

Yes.

The array is already **sorted**, which is the biggest hint.

---

# 💡 Key Observation

Notice the array is sorted.

```text
1 3 5 6
```

When we check the middle element,

we immediately know that **half of the array cannot contain the answer**.

That's why Binary Search works.

---

# Why Binary Search?

Suppose

```text
nums = [1,3,5,6]

target = 2
```

Initially

```text
Start          End

1 3 5 6

    Mid
```

Middle is

```text
3
```

Question:

Is

```text
2
```

greater than

```text
3?
```

No.

Therefore,

everything on the **right side** can be ignored.

We reduced the search space by half.

---

# 🔍 Algorithm

### Step 1

Initialize

```python
start = 0
end = len(nums)-1
```

---

### Step 2

Repeat while

```python
start <= end
```

---

### Step 3

Find middle

```python
mid = (start + end)//2
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

If

```python
nums[mid] < target
```

Search the right half.

```python
start = mid + 1
```

---

### Step 6

Else

Search the left half.

```python
end = mid - 1
```

---

### Step 7

If the loop finishes,

return

```python
start
```

This is the insertion position.

---

# ⭐ Why Do We Return `start`?

This is the most important concept in this problem.

Many beginners ask:

> "If the target wasn't found, why does `start` become the answer?"

Let's understand.

---

## Example

```text
nums = [1,3,5,6]

target = 2
```

Initially

```text
start = 0

end = 3
```

---

### First Iteration

```text
mid = 1

nums[mid] = 3
```

Since

```text
2 < 3
```

Move left

```python
end = mid-1
```

Now

```text
start = 0

end = 0
```

---

### Second Iteration

```text
mid = 0

nums[mid] = 1
```

Since

```text
2 > 1
```

Move right

```python
start = mid+1
```

Now

```text
start = 1

end = 0
```

Loop ends because

```text
start > end
```

Question:

Where should

```text
2
```

go?

Exactly at

```text
Index 1
```

And notice

```text
start = 1
```

That is why

```python
return start
```

works.

---

## Another Example

```text
nums = [1,3,5,6]

target = 7
```

Eventually

```text
start = 4

end = 3
```

Loop ends.

Insert at

```text
Index 4
```

Exactly where

```text
start
```

is pointing.

---

## Memory Trick

Think of

```text
start
```

as

> **"The first possible place where the target can exist."**

If the target isn't found,

that place becomes its insertion position.

---

# ✅ Python Solution

```python
class Solution:

    def searchInsert(self, nums, target):

        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return start
```

---

# 📝 Line-by-Line Explanation

### Initialize pointers

```python
start = 0
end = len(nums)-1
```

Search the whole array.

---

### Find middle

```python
mid = (start+end)//2
```

Divide the search space into two halves.

---

### Target Found

```python
if nums[mid] == target:
    return mid
```

Return immediately.

---

### Target Bigger

```python
start = mid+1
```

Ignore the left half.

---

### Target Smaller

```python
end = mid-1
```

Ignore the right half.

---

### Target Not Found

```python
return start
```

Return insertion position.

---

# 📖 Complete Dry Run

Input

```text
nums = [1,3,5,6]

target = 2
```

### Iteration 1

```text
start = 0

end = 3

mid = 1

nums[mid] = 3
```

```text
2 < 3
```

Move left

```text
end = 0
```

---

### Iteration 2

```text
start = 0

end = 0

mid = 0

nums[mid] = 1
```

```text
2 > 1
```

Move right

```text
start = 1
```

---

Loop ends

```text
start = 1

end = 0
```

Return

```text
1
```

Correct.

---

# ⚠️ Common Mistakes

### ❌ Returning `end`

Many beginners write

```python
return end
```

Wrong.

Example

```text
nums=[1,3]

target=2
```

End becomes

```text
0
```

Correct answer

```text
1
```

Always return

```python
start
```

---

### ❌ Using

```python
while start < end
```

This skips checking the last remaining element.

Always write

```python
while start <= end
```

---

### ❌ Forgetting

```python
mid = (start+end)//2
```

Using

```python
/
```

returns a float.

Use

```python
//
```

for integer division.

---

# 🐍 Pythonic Explanation

## Integer Division

```python
mid = (start+end)//2
```

`//`

means **floor division**.

Example

```python
7//2
```

Output

```text
3
```

---

## len()

```python
len(nums)
```

Returns the number of elements.

Example

```python
nums=[1,3,5,6]
```

```python
len(nums)
```

returns

```text
4
```

---

# ⏱ Complexity

## Time

Every iteration removes half of the array.

```text
n

↓

n/2

↓

n/4

↓

n/8

↓

1
```

Time Complexity

```text
O(log n)
```

---

## Space

Only three variables are used.

```text
start

end

mid
```

Space Complexity

```text
O(1)
```

---

# 🎯 Interview Pattern

Whenever you hear

- Sorted Array
- Search
- Insert Position
- Lower Bound

Think

```text
Binary Search
```

---

# 🧠 Memory Trick

```text
Sorted Array

↓

Binary Search

↓

Found?

↓

YES → Return Mid

↓

NO

↓

Return Start
```

---

# 📚 Key Learnings

- Binary Search works only because the array is sorted.
- Every comparison removes half of the search space.
- If the target exists, return its index.
- If it doesn't exist, `start` always points to the correct insertion position.
- Time Complexity is **O(log n)**.
- Space Complexity is **O(1)**.
# ✅ Q100. Count Occurrences of an Element in a Sorted Array

## 📌 Problem Statement

You are given a **sorted array** and a target element.

Your task is to find **how many times the target appears** in the array.

---

## Example 1

```text
Input

nums = [1,2,2,2,3,4,5]

target = 2

Output

3
```

Explanation

```text
Index

0 1 2 3 4 5 6

Array

1 2 2 2 3 4 5
  ↑     ↑
First   Last
```

The target appears

```text
3 times
```

---

## Example 2

```text
Input

nums = [1,3,5,7]

target = 2

Output

0
```

Since the target doesn't exist.

---

# 🧠 Beginner Intuition

A beginner would probably do this:

Traverse the entire array.

Whenever the target is found,

increase a counter.

```python
count = 0

for num in nums:
    if num == target:
        count += 1
```

Works perfectly.

But...

Time Complexity

```text
O(n)
```

Can we do better?

Yes.

The array is already **sorted**.

---

# 💡 Key Observation

Look carefully.

```text
1 2 2 2 2 3 4 5
```

All occurrences of

```text
2
```

are together.

That means if we know

- First occurrence
- Last occurrence

then we automatically know the count.

---

# ⭐ Main Idea

Instead of counting one by one,

find

```text
First Index

↓

Last Index
```

Then

```text
Count

=

Last - First + 1
```

---

# Why "+1"?

Suppose

```text
Index

0 1 2 3

Array

2 2 2 2
```

First

```text
0
```

Last

```text
3
```

If we calculate

```text
3 - 0

=

3
```

Is that correct?

No.

There are actually

```text
4
```

elements.

So

```text
Count

=

Last - First + 1
```

becomes

```text
3 - 0 + 1

=

4
```

Correct.

---

## Another Example

```text
Index

0 1 2 3 4 5

Array

1 2 2 2 3 4
```

First

```text
1
```

Last

```text
3
```

Count

```text
3 - 1 + 1

=

3
```

Correct.

---

# 🔍 Algorithm

### Step 1

Find the first occurrence using Binary Search.

---

### Step 2

If the first occurrence is

```text
-1
```

Return

```text
0
```

because the target doesn't exist.

---

### Step 3

Find the last occurrence using Binary Search.

---

### Step 4

Return

```python
last - first + 1
```

---

# ✅ Python Solution

```python
class Solution:

    def countOccurrences(self, nums, target):

        first = self.findIndex(nums, target, True)

        if first == -1:
            return 0

        last = self.findIndex(nums, target, False)

        return last - first + 1


    def findIndex(self, nums, target, findFirst):

        start = 0
        end = len(nums) - 1

        ans = -1

        while start <= end:

            mid = (start + end) // 2

            if nums[mid] == target:

                ans = mid

                if findFirst:
                    end = mid - 1

                else:
                    start = mid + 1

            elif nums[mid] < target:

                start = mid + 1

            else:

                end = mid - 1

        return ans
```

---

# 📝 Line-by-Line Explanation

### Find First

```python
first = self.findIndex(nums, target, True)
```

Find the left boundary.

---

### Check

```python
if first == -1:
    return 0
```

If the target doesn't exist,

there is no need to find the last occurrence.

Return

```text
0
```

immediately.

---

### Find Last

```python
last = self.findIndex(nums, target, False)
```

Find the right boundary.

---

### Calculate Count

```python
return last - first + 1
```

Use the formula.

---

# 📖 Complete Dry Run

Input

```text
nums = [1,2,2,2,3,4]

target = 2
```

---

## Find First

Binary Search returns

```text
1
```

---

## Find Last

Binary Search returns

```text
3
```

---

## Count

```text
3 - 1 + 1

=

3
```

Answer

```text
3
```

---

# 📖 Dry Run 2

Input

```text
nums = [1,3,5,7]

target = 2
```

Find First

```text
-1
```

Immediately return

```text
0
```

No second Binary Search is needed.

---

# 🔍 Visualization

```text
Array

1 2 2 2 2 3 4

  ↑     ↑

First   Last
```

Distance

```text
Last - First

↓

Number of gaps
```

To include both ends,

add

```text
+1
```

---

# ⚠️ Common Mistakes

### ❌ Forgetting +1

Wrong

```python
last - first
```

Correct

```python
last - first + 1
```

---

### ❌ Performing the second Binary Search even when target doesn't exist

Wrong

```python
last = findLast(...)
```

If first is

```text
-1
```

simply return

```text
0
```

---

### ❌ Using Linear Search

Works

but

Time Complexity

```text
O(n)
```

Binary Search is much faster.

---

# 🐍 Pythonic Explanation

## Reusing Functions

Notice

```python
findIndex(...)
```

is reused.

Instead of writing

```python
findFirst()

findLast()
```

we simply change one boolean.

This avoids duplicate code.

---

## Why Return Early?

```python
if first == -1:
    return 0
```

This is called an

```text
Early Return
```

If we already know the answer,

there is no reason to continue.

It makes the code faster and cleaner.

---

# ⏱ Complexity

First Binary Search

```text
O(log n)
```

Second Binary Search

```text
O(log n)
```

Total

```text
O(log n)
```

Space

```text
O(1)
```

---

# 🎯 Interview Pattern

Whenever you hear

- Count Occurrences
- Frequency in Sorted Array
- Number of Times Appears

Think

```text
Find First

+

Find Last

↓

Last - First + 1
```

---

# 🧠 Memory Trick

```text
Need Count?

↓

Find First

↓

Find Last

↓

Last - First + 1
```

---

# 🔄 Relationship Between Q99 and Q100

Notice something interesting.

### Q99 asks:

```text
Return

[First, Last]
```

### Q100 asks:

```text
Return

Last - First + 1
```

So **Q100 is simply an extension of Q99**.

If you know how to solve **LeetCode 34 (Q99)**,

then **Count Occurrences** is just one extra line:

```python
count = last - first + 1
```

---

# 📚 Key Learnings

- Since the array is sorted, all occurrences are together.
- We don't need to count each occurrence manually.
- Find the first and last occurrence using Binary Search.
- If the element doesn't exist, return `0`.
- Otherwise, use the formula:

```text
Count = Last - First + 1
```

- Time Complexity is **O(log n)**.
- Space Complexity is **O(1)**.