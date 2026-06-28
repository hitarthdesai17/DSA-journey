# ✅ Q87. Maximum Subarray (LeetCode 53)

## Problem

Given an integer array `nums`, find the **contiguous subarray** (containing at least one element) which has the **largest sum**, and return its sum.

---

## Example 1

```text
Input:
nums = [-2,1,-3,4,-1,2,1,-5,4]

Output:
6

Explanation:
The subarray [4,-1,2,1] has the largest sum = 6
```

---

## Example 2

```text
Input:
nums = [1]

Output:
1
```

---

## Example 3

```text
Input:
nums = [5,4,-1,7,8]

Output:
23
```

---

# Method 1 : Kadane's Algorithm (Optimal)

## DSA Solution (Python)

```python
class Solution:
    def maxSubArray(self, nums):

        maximum = float("-inf")
        currentSum = 0

        for num in nums:

            currentSum += num

            maximum = max(maximum, currentSum)

            if currentSum < 0:
                currentSum = 0

        return maximum
```

---

# Algorithm

### Step 1

Create two variables.

```python
maximum = float("-inf")
currentSum = 0
```

* `currentSum` stores the current subarray sum.
* `maximum` stores the best answer found so far.

---

### Step 2

Traverse the array.

```python
currentSum += num
```

Add every number to the running sum.

---

### Step 3

Update the answer.

```python
maximum = max(maximum, currentSum)
```

If the current subarray is better than the previous best,
update the answer.

---

### Step 4

If the running sum becomes negative

```python
if currentSum < 0:
    currentSum = 0
```

discard it.

Why?

Because adding a negative sum to future numbers only decreases the future total.

---

### Step 5

Return the maximum sum.

---

# Dry Run

Input

```text
[-2,1,-3,4,-1,2,1,-5,4]
```

| Current Number | Current Sum | Maximum |
| -------------- | ----------: | ------: |
| -2             |          -2 |      -2 |
| Reset          |           0 |      -2 |
| 1              |           1 |       1 |
| -3             |          -2 |       1 |
| Reset          |           0 |       1 |
| 4              |           4 |       4 |
| -1             |           3 |       4 |
| 2              |           5 |       5 |
| 1              |           6 |       6 |
| -5             |           1 |       6 |
| 4              |           5 |       6 |

Final Answer

```text
6
```

---

# Why Reset When Sum Becomes Negative?

Suppose

```text
Current Sum = -5
```

Next number

```text
10
```

If we continue

```text
-5 + 10 = 5
```

Instead, starting a new subarray

```text
10
```

is clearly better.

So whenever

```python
currentSum < 0
```

we discard the old subarray.

---

# Complexity

```text
Time  : O(n)

Space : O(1)
```

---

# Method 2 : Brute Force

## Python Solution

```python
class Solution:
    def maxSubArray(self, nums):

        maximum = float("-inf")

        for i in range(len(nums)):

            currentSum = 0

            for j in range(i, len(nums)):

                currentSum += nums[j]

                maximum = max(maximum, currentSum)

        return maximum
```

---

# Algorithm

1. Start every subarray from index `i`.
2. Extend it until the end.
3. Calculate every subarray sum.
4. Store the maximum.

---

# Dry Run

```text
nums = [2,-1,3]
```

Subarrays

```text
[2]

Sum = 2

Maximum = 2
```

```text
[2,-1]

Sum = 1
```

```text
[2,-1,3]

Sum = 4

Maximum = 4
```

```text
[-1]

Sum = -1
```

```text
[-1,3]

Sum = 2
```

```text
[3]

Sum = 3
```

Answer

```text
4
```

---

# Complexity

```text
Time  : O(n²)

Space : O(1)
```

---

# ⭐ Pythonic Way

```python
class Solution:
    def maxSubArray(self, nums):

        currentSum = maximum = nums[0]

        for num in nums[1:]:

            currentSum = max(num, currentSum + num)

            maximum = max(maximum, currentSum)

        return maximum
```

---

# Pythonic Explanation

## New Function : `float("-inf")`

Represents negative infinity.

Example

```python
maximum = float("-inf")
```

It is smaller than every integer.

Useful when we don't know the minimum possible answer.

Example

```python
nums = [-5,-2,-10]
```

If we initialize

```python
maximum = 0
```

the answer becomes wrong because every element is smaller than 0.

Using

```python
float("-inf")
```

avoids this problem.

---

## New Function : `max()`

Returns the larger value.

Example

```python
max(5,8)
```

Output

```text
8
```

---

## List Slicing

```python
nums[1:]
```

Returns every element after index 0.

Example

```python
nums = [5,3,2,1]
```

```python
nums[1:]
```

returns

```text
[3,2,1]
```

---

# Why This Pythonic Version Works

Instead of writing

```python
currentSum += num

if currentSum < 0:
    currentSum = 0
```

we directly decide

```python
currentSum = max(
    num,
    currentSum + num
)
```

Two choices exist:

Option 1

Start a new subarray

```text
num
```

Option 2

Continue the previous subarray

```text
currentSum + num
```

Whichever is larger becomes the new current sum.

---

# Dry Run (Pythonic)

Input

```text
[-2,1,-3,4,-1,2,1]
```

Current

```text
current = -2
maximum = -2
```

Number = 1

```text
max(1,-1)

↓

1
```

Current

```text
1
```

Maximum

```text
1
```

Number = -3

```text
max(-3,-2)

↓

-2
```

Current

```text
-2
```

Maximum

```text
1
```

Number = 4

```text
max(4,2)

↓

4
```

Current

```text
4
```

Maximum

```text
4
```

Continue...

Final Answer

```text
6
```

---

# Comparison

| Method             | Time  | Space |
| ------------------ | ----- | ----- |
| Brute Force        | O(n²) | O(1)  |
| Kadane's Algorithm | O(n)  | O(1)  |
| Pythonic Kadane    | O(n)  | O(1)  |

---

# Key Learnings

* Kadane's Algorithm is a Dynamic Programming / Greedy technique.
* Negative running sums are discarded because they reduce future sums.
* `float("-inf")` is useful when arrays can contain only negative numbers.
* The Pythonic version chooses between:

  * Starting a new subarray.
  * Extending the existing subarray.
* Both Kadane implementations have the same complexity.

---

# Interview Tip

Whenever you see:

* Maximum contiguous sum
* Largest contiguous subarray
* Maximum running sum

Think of **Kadane's Algorithm** first.

It is the optimal solution with:

```text
Time  : O(n)

Space : O(1)
```


# ✅ Q88. Majority Element (LeetCode 169)

## Problem

Given an array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than** `⌊n / 2⌋` times.

You may assume that the majority element always exists.

---

## Example 1

```text
Input:
nums = [3,2,3]

Output:
3
```

---

## Example 2

```text
Input:
nums = [2,2,1,1,1,2,2]

Output:
2
```

---

# Method 1 : Boyer-Moore Voting Algorithm (Optimal)

## DSA Solution (Python)

```python
class Solution:
    def majorityElement(self, nums):

        candidate = nums[0]
        count = 1

        for i in range(1, len(nums)):

            if count == 0:
                candidate = nums[i]
                count = 1

            elif nums[i] == candidate:
                count += 1

            else:
                count -= 1

        return candidate
```

---

# Algorithm

### Step 1

Choose the first element as the candidate.

```python
candidate = nums[0]
count = 1
```

---

### Step 2

Traverse the array.

If

```python
count == 0
```

choose a new candidate.

---

### Step 3

If the current element equals the candidate

```python
count += 1
```

because we found another occurrence.

---

### Step 4

Otherwise

```python
count -= 1
```

because a different element cancels one occurrence of the candidate.

---

### Step 5

Return the candidate.

---

# Why Does This Work?

Imagine every occurrence of the majority element fights with one occurrence of every other element.

Example

```text
2 2 1 1 1 2 2
```

Pair them.

```text
2 ✖ 1

2 ✖ 1

2 ✖ 1
```

Remaining

```text
2
```

The majority element always survives because it appears **more than half** the time.

---

# Dry Run

Input

```text
nums = [2,2,1,1,1,2,2]
```

| i | Current | Candidate | Count | Action                  |
| - | ------- | --------- | ----: | ----------------------- |
| 0 | 2       | 2         |     1 | Initialize              |
| 1 | 2       | 2         |     2 | Same → Count++          |
| 2 | 1       | 2         |     1 | Different → Count--     |
| 3 | 1       | 2         |     0 | Different → Count--     |
| 4 | 1       | 1         |     1 | Count=0 → New Candidate |
| 5 | 2       | 1         |     0 | Different → Count--     |
| 6 | 2       | 2         |     1 | Count=0 → New Candidate |

Final Answer

```text
2
```

---

# Visual Explanation

```
2 2 1 1 1 2 2

↓

2 2
1 1
1
2 2

↓

Cancel pairs

↓

2 survives

↓

Answer = 2
```

---

# Complexity

```text
Time  : O(n)

Space : O(1)
```

---

# Method 2 : HashMap (Dictionary)

## Python Solution

```python
class Solution:
    def majorityElement(self, nums):

        freq = {}

        majority = len(nums) // 2

        for num in nums:

            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            if freq[num] > majority:
                return num
```

---

# Algorithm

1. Create a dictionary.
2. Count frequency of every number.
3. As soon as any frequency becomes greater than `n//2`,
   return it.

---

# Dry Run

Input

```text
nums = [3,2,3]
```

Dictionary

```
{}
```

Insert 3

```
{3:1}
```

Insert 2

```
{3:1,2:1}
```

Insert 3

```
{3:2,2:1}
```

Since

```text
2 > 3//2

↓

2 > 1
```

Answer

```text
3
```

---

# Complexity

```text
Time  : O(n)

Space : O(n)
```

---

# ⭐ Pythonic Way 1

Using `collections.Counter`

```python
from collections import Counter

class Solution:
    def majorityElement(self, nums):

        
```

---

# Pythonic Explanation

## New Module : `Counter`

`Counter` counts the frequency of every element automatically.

Example

```python
from collections import Counter

nums = [1,1,2,2,2,3]

print(Counter(nums))
```

Output

```text
Counter({
2:3,
1:2,
3:1
})
```

Instead of writing

```python
freq = {}
```

and updating it manually,

`Counter` does it in one line.

---

## New Function : `max()`

Normally

```python
max([5,8,3])
```

returns

```text
8
```

But here

```python
max(count, key=count.get)
```

works differently.

Suppose

```python
count = {
2:5,
1:2,
3:1
}
```

Python checks

```python
count.get(2)

↓

5
```

```python
count.get(1)

↓

2
```

```python
count.get(3)

↓

1
```

Largest frequency

```text
5
```

belongs to

```text
2
```

So

```python
max(count, key=count.get)
```

returns

```text
2
```

---

## New Parameter : `key=`

`key` tells Python **how to compare values**.

Example

```python
words = ["apple","banana","cat"]

print(max(words, key=len))
```

Output

```text
banana
```

Python compared the **length** instead of alphabetical order.

Similarly

```python
max(count, key=count.get)
```

compares frequencies.

---

# ⭐ Pythonic Way 2

```python
from collections import Counter

class Solution:
    def majorityElement(self, nums):

        return Counter(nums).most_common(1)[0][0]
```

---

# Pythonic Explanation

## New Function : `most_common()`

Returns elements in descending order of frequency.

Example

```python
Counter([1,1,1,2,2,3]).most_common()
```

Output

```text
[(1,3),
 (2,2),
 (3,1)]
```

If we only need the most frequent

```python
Counter(nums).most_common(1)
```

Output

```text
[(2,4)]
```

The result is a list.

Index

```python
[0]
```

gives

```text
(2,4)
```

Again

```python
[0]
```

gives

```text
2
```

Hence

```python
Counter(nums).most_common(1)[0][0]
```

returns the majority element.

---

# Comparison

| Method                | Time | Space |
| --------------------- | ---- | ----- |
| Boyer-Moore Voting    | O(n) | O(1)  |
| HashMap               | O(n) | O(n)  |
| Counter + max         | O(n) | O(n)  |
| Counter + most_common | O(n) | O(n)  |

---

# Key Learnings

* Boyer-Moore is the optimal interview solution.
* The majority element survives pairwise cancellation because it appears more than `n/2` times.
* Dictionaries (HashMaps) are useful for frequency counting.
* `Counter` is Python's built-in frequency counter.
* `max(key=...)` lets Python compare using custom criteria.
* `most_common()` returns elements sorted by frequency.

---

# Interview Tips

If the problem guarantees that a majority element **always exists**:

✅ Use **Boyer-Moore Voting Algorithm**.

If the problem asks for frequencies or **doesn't guarantee** a majority element:

✅ Use a **HashMap (Dictionary)** or **Counter**.

# ✅ Q89. Best Time to Buy and Sell Stock (LeetCode 121)

## Problem

You are given an array `prices` where `prices[i]` is the price of a stock on the `iᵗʰ` day.

You want to maximize your profit by choosing:

* One day to **buy**
* One **later** day to sell

Return the maximum profit you can achieve.

If no profit is possible, return `0`.

---

## Example 1

```text
Input:
prices = [7,1,5,3,6,4]

Output:
5

Explanation:

Buy at price 1

Sell at price 6

Profit = 6 - 1 = 5
```

---

## Example 2

```text
Input:
prices = [7,6,4,3,1]

Output:
0

Explanation:

Prices only decrease.

No profit is possible.
```

---

# Method 1 : Track Minimum Price + Maximum Profit (Optimal)

## DSA Solution (Python)

```python
class Solution:
    def maxProfit(self, prices):

        minPrice = float("inf")
        maxProfit = 0

        for price in prices:

            minPrice = min(minPrice, price)

            profit = price - minPrice

            maxProfit = max(maxProfit, profit)

        return maxProfit
```

---

# Algorithm

### Step 1

Initialize

```python
minPrice = float("inf")
maxProfit = 0
```

* `minPrice` stores the lowest stock price seen so far.
* `maxProfit` stores the best profit found.

---

### Step 2

Traverse the array.

For every price,

update the minimum price.

```python
minPrice = min(minPrice, price)
```

---

### Step 3

Calculate today's profit.

```python
profit = price - minPrice
```

---

### Step 4

Update the answer.

```python
maxProfit = max(maxProfit, profit)
```

---

### Step 5

Return the maximum profit.

---

# Dry Run

Input

```text
prices = [7,1,5,3,6,4]
```

| Price | Minimum Price | Profit | Maximum Profit |
| ----: | ------------: | -----: | -------------: |
|     7 |             7 |      0 |              0 |
|     1 |             1 |      0 |              0 |
|     5 |             1 |      4 |              4 |
|     3 |             1 |      2 |              4 |
|     6 |             1 |      5 |              5 |
|     4 |             1 |      3 |              5 |

Answer

```text
5
```

---

# Visual Explanation

```text
Day

1  2  3  4  5  6

Price

7  1  5  3  6  4

↓

Lowest price

1

↓

Sell later at

6

↓

Profit

6-1 = 5
```

---

# Why Does This Work?

At every day we ask two questions.

### Question 1

What is the cheapest stock I have seen so far?

```python
minPrice = min(minPrice, price)
```

---

### Question 2

If I sell today,

how much profit will I make?

```python
profit = price - minPrice
```

We repeat this for every day.

The largest profit becomes the answer.

---

# Another Dry Run

Input

```text
prices = [2,4,1]
```

Initially

```text
minPrice = ∞

maxProfit = 0
```

---

Price = 2

```text
minPrice = 2

profit = 0

maxProfit = 0
```

---

Price = 4

```text
minPrice = 2

profit = 2

maxProfit = 2
```

---

Price = 1

```text
minPrice = 1

profit = 0

maxProfit = 2
```

Answer

```text
2
```

---

# What If Prices Only Decrease?

Example

```text
prices = [7,6,5,4]
```

Profit

```text
0

0

0

0
```

Answer

```text
0
```

Because we never find a profitable selling day.

---

# Complexity

```text
Time  : O(n)

Space : O(1)
```

---

# Brute Force Method

## Python Solution

```python
class Solution:
    def maxProfit(self, prices):

        maximum = 0

        for i in range(len(prices)):

            for j in range(i + 1, len(prices)):

                maximum = max(maximum,
                              prices[j] - prices[i])

        return maximum
```

---

# Algorithm

1. Buy on every possible day.
2. Sell on every later day.
3. Calculate every possible profit.
4. Return the maximum.

---

# Dry Run

Input

```text
prices = [7,1,5]
```

Possible profits

```text
Buy 7

Sell 1

Profit = -6
```

```text
Buy 7

Sell 5

Profit = -2
```

```text
Buy 1

Sell 5

Profit = 4
```

Maximum

```text
4
```

---

# Complexity

```text
Time  : O(n²)

Space : O(1)
```

---

# ⭐ Pythonic Way

```python
class Solution:
    def maxProfit(self, prices):

        minPrice = float("inf")

        maxProfit = 0

        for price in prices:

            minPrice = min(minPrice, price)

            maxProfit = max(
                maxProfit,
                price - minPrice
            )

        return maxProfit
```

This is the same algorithm but written more compactly.

---

# Pythonic Explanation

## New Function : `float("inf")`

Represents positive infinity.

Example

```python
minimum = float("inf")
```

Initially,

every number is smaller than infinity.

So,

```python
minimum = min(minimum, number)
```

works correctly.

Example

```python
minimum = float("inf")

minimum = min(minimum,7)

↓

7
```

---

## New Function : `min()`

Returns the smaller value.

Example

```python
min(5,2)
```

Output

```text
2
```

---

## New Function : `max()`

Returns the larger value.

Example

```python
max(5,9)
```

Output

```text
9
```

---

# Why Use `float("inf")`?

Suppose we write

```python
minPrice = 0
```

Then

```text
price = 5

profit = 5-0 = 5
```

This is incorrect because we never bought the stock for ₹0.

Instead,

```python
minPrice = float("inf")
```

ensures that the first price automatically becomes the minimum.

---

# Comparison

| Method              | Time  | Space |
| ------------------- | ----- | ----- |
| Brute Force         | O(n²) | O(1)  |
| Track Minimum Price | O(n)  | O(1)  |
| Pythonic            | O(n)  | O(1)  |

---

# Key Learnings

* Keep track of the minimum price seen so far.
* Calculate today's profit using that minimum.
* Update the answer whenever a larger profit is found.
* `float("inf")` is useful when searching for minimum values.
* `min()` and `max()` simplify the code.
* The buying day must always come before the selling day.

---

# Interview Tips

Whenever you hear:

* Maximum Profit
* Buy once, Sell once
* Best time to buy stock

Think:

```text
Track Minimum Price

+

Track Maximum Profit
```

This gives the optimal solution.

```text
Time  : O(n)

Space : O(1)
```