# 📘 Day80_Q95_Quick_Sort.md

# ✅ Q95. Quick Sort

## Definition

Quick Sort is a **Divide and Conquer** sorting algorithm.

It works by:

1. Choosing a **Pivot** element.
2. Placing the pivot in its correct sorted position.
3. Putting all smaller elements to the left.
4. Putting all greater elements to the right.
5. Repeating the same process recursively on the left and right parts.

---

# Example

```text
Input

[18,5,3,40,10,30]

Output

[3,5,10,18,30,40]
```

---

# Why Do We Need Quick Sort?

Suppose we have

```text
[18,5,3,40,10,30]
```

Instead of comparing every element with every other element (like Bubble Sort),

Quick Sort divides the problem into smaller pieces.

Think of it like arranging students around a class monitor.

The monitor (pivot) stands in the correct place.

Students shorter than the monitor stand on the left.

Students taller stand on the right.

Now both groups repeat the same process with their own monitor.

Eventually everyone reaches the correct position.

---

# Intuition

Imagine arranging books.

Choose one book.

Put all smaller books on the left.

Put all larger books on the right.

Now do the same with both piles.

Eventually every pile contains only one book.

The books are sorted.

---

# What is Divide and Conquer?

Divide and Conquer means

```text
Big Problem

↓

Break into Smaller Problems

↓

Solve Smaller Problems

↓

Combine Answers
```

Quick Sort divides

```text
Array

↓

Left Half

Pivot

Right Half
```

Then recursively sorts the left and right halves.

---

# Important Term : Pivot

A Pivot is a special element.

It is used to divide the array.

Example

```text
18 5 3 40 10 30

Pivot = 30
```

Everything smaller than 30 goes left.

Everything larger goes right.

---

# Why Do We Choose the Last Element?

Many implementations choose

```python
pivot = arr[high]
```

because

- Easy to implement.
- Doesn't require extra memory.
- Makes partition logic simple.

Other pivot choices are also possible:

- First element
- Middle element
- Random element
- Median of Three

---

# Python Solution

```python
class Solution:

    def quickSort(self, arr):

        self.sort(arr, 0, len(arr)-1)

        return arr


    def sort(self, arr, low, high):

        if low < high:

            pivotIndex = self.partition(arr, low, high)

            self.sort(arr, low, pivotIndex-1)

            self.sort(arr, pivotIndex+1, high)


    def partition(self, arr, low, high):

        pivot = arr[high]

        i = low - 1

        for j in range(low, high):

            if arr[j] < pivot:

                i += 1

                arr[i], arr[j] = arr[j], arr[i]

        i += 1

        arr[i], arr[high] = arr[high], arr[i]

        return i
```

---

# Line-by-Line Explanation

## Step 1

```python
pivot = arr[high]
```

Choose the last element as pivot.

Example

```text
18 5 3 40 10 30

Pivot = 30
```

---

## Step 2

```python
i = low - 1
```

### ❓Why low-1?

This is one of the most confusing parts for beginners.

Think of `i` as

> **"The last position where a smaller element has been placed."**

Initially,

no smaller element has been found.

So

```text
i

↓

-1
```

Meaning

```text
No smaller elements yet.
```

---

# Example

Array

```text
18 5 3 40 10 30
```

Pivot

```text
30
```

Initially

```text
i = -1

j = 0
```

---

### j = 0

```text
18 < 30

Yes
```

Increase i

```text
i = 0
```

Swap

```text
18 with 18
```

Nothing changes.

---

### j = 1

```text
5 < 30

Yes
```

Increase i

```text
i = 1
```

Swap

```text
5 with 5
```

---

### j = 2

```text
3 < 30

Yes
```

Increase i

```text
i = 2
```

---

### j = 3

```text
40 < 30

No
```

Do nothing.

---

### j = 4

```text
10 < 30

Yes
```

Increase

```text
i = 3
```

Swap

```text
40

↓

10
```

Array becomes

```text
18 5 3 10 40 30
```

---

Loop ends.

Increase i

```text
i = 4
```

Swap

```text
40

30
```

Final

```text
18 5 3 10 30 40
```

Pivot is now exactly where it belongs.

---

# Why Do We Swap?

Whenever we find a smaller element,

we want all smaller elements to stay together.

So we swap it to the next available position.

Without swapping,

small and large elements would remain mixed.

---

# Why Does Pivot End Up Correct?

After the loop,

everything before `i`

is smaller than the pivot.

Everything after `i`

is larger than the pivot.

So swapping the pivot into position `i+1`

puts it exactly where it belongs.

It never needs to move again.

---

# Complete Dry Run

Input

```text
18 5 3 40 10 30
```

Pivot

```text
30
```

After partition

```text
18 5 3 10 |30| 40
```

Now recursively sort

Left

```text
18 5 3 10
```

Right

```text
40
```

Left becomes

```text
3 5 10 18
```

Right already sorted.

Final

```text
3 5 10 18 30 40
```

---

# Recursion Tree

```text
18 5 3 40 10 30

↓

18 5 3 10 |30| 40

↓

3 5 |10| 18

↓

3 |5|

↓

Sorted
```

---

# Why Recursion?

Once the pivot reaches its correct position,

the left and right halves become independent.

Sorting the left half never affects the right half.

So we solve them separately.

---

# Complexity

## Best Case

Every pivot divides the array equally.

```text
Time

O(n log n)
```

---

## Average Case

Most partitions are balanced.

```text
O(n log n)
```

---

## Worst Case

Example

```text
1 2 3 4 5
```

Choosing the last element

creates

```text
4

3

2

1
```

instead of

```text
2

2
```

Time becomes

```text
O(n²)
```

---

# Space Complexity

Because of recursion,

```text
Average

O(log n)

Worst

O(n)
```

---

# Stable or Not?

Quick Sort is

```text
❌ Not Stable
```

Equal elements may change their original order.

---

# Pythonic Way

Python already provides

```python
arr.sort()
```

or

```python
sorted(arr)
```

Internally Python uses

```text
Timsort
```

instead of Quick Sort because it performs better on real-world data.

However,

Quick Sort is still one of the most important interview algorithms.

---

# Pythonic Explanation

## New Syntax

```python
arr[i], arr[j] = arr[j], arr[i]
```

This swaps two numbers.

Instead of

```python
temp = arr[i]
arr[i] = arr[j]
arr[j] = temp
```

Python allows swapping in one line.

---

## New Function

```python
range(low, high)
```

Notice

```python
high
```

is excluded.

Example

```python
range(2,6)
```

Produces

```text
2 3 4 5
```

The pivot is at `high`, so we don't compare it with itself.

---

# ❓ Why does the loop run until `high-1`?

The loop is:

```python
for j in range(low, high):
```

A beginner might wonder:

> Why don't we loop till `high`?

Because

```python
pivot = arr[high]
```

The pivot is already chosen.

If we compare it with itself,

```text
30 < 30
```

is always false.

It serves no purpose.

So we stop one index before the pivot.

---

# Common Mistakes

❌ Using

```python
i = low
```

instead of

```python
low-1
```

---

❌ Forgetting the final pivot swap.

---

❌ Recursing on

```python
pivotIndex
```

instead of

```python
pivotIndex-1
```

and

```python
pivotIndex+1
```

---

# Interview Tips

Whenever you hear

- Divide and Conquer
- In-place Sorting
- Fast Average Sorting

Think

```text
Quick Sort
```

Remember

```text
Choose Pivot

↓

Partition

↓

Recursively Sort Left

↓

Recursively Sort Right
```

---

# Comparison

| Algorithm | Best | Average | Worst | Stable |
|-----------|------|----------|--------|---------|
| Bubble Sort | O(n²) | O(n²) | O(n²) | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | ❌ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | ✅ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | ❌ |

---

# Key Learnings

- Quick Sort is a Divide and Conquer algorithm.
- Pivot divides the array.
- Smaller elements move left.
- Larger elements move right.
- Pivot reaches its final position after partition.
- Recursion sorts the remaining parts.
- Average complexity is O(n log n).
- Worst case occurs when partitions become highly unbalanced.

---

# Memory Trick

```text
Choose Pivot

↓

Partition

↓

Pivot Fixed

↓

Sort Left

↓

Sort Right

↓

Done
```