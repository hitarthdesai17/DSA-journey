# DAY 54 - HASH MAP PROBLEMS & BITWISE OPERATORS IN PYTHON

# Q67. Two Sum

## Problem

Given an integer array `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

Example

```text
nums = [2,7,11,15]
target = 9

Output:
[0,1]
```

---

# Approach 1 - Brute Force

```python
class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                if nums[i] + nums[j] == target:
                    return [i,j]

        return []
```

### Complexity

```text
Time  : O(n²)

Space : O(1)
```

---

# Approach 2 - Hash Map (Optimal)

```python
class Solution:
    def twoSum(self, nums, target):

        numMap = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in numMap:
                return [numMap[complement], i]

            numMap[nums[i]] = i

        return []
```

### Dry Run

Input

```text
nums = [2,7,11,15]
target = 9
```

Initially

```text
{}
```

Iteration 1

```text
Current = 2

Complement = 7

7 not found

Store

{
2:0
}
```

Iteration 2

```text
Current = 7

Complement = 2

Found

Return

[0,1]
```

### Complexity

```text
Time  : O(n)

Space : O(n)
```

---

# Q68. First Letter Appears Twice

## Problem

Return the first character that appears twice.

Example

```text
Input

abccbaacz

Output

c
```

---

# Approach 1 - Set

```python
class Solution:
    def repeatedCharacter(self,s):

        seen = set()

        for ch in s:

            if ch in seen:
                return ch

            seen.add(ch)

        return None
```

### Complexity

```text
Time  : O(n)

Space : O(n)
```

---

# Approach 2 - Dictionary (Frequency Count)

```python
class Solution:
    def repeatedCharacter(self,s):

        freq = {}

        for ch in s:

            freq[ch] = freq.get(ch,0) + 1

            if freq[ch] == 2:
                return ch

        return None
```

### Explanation

Dictionary stores

```text
Character → Frequency
```

Example

```text
abccba
```

Dictionary becomes

```text
{
'a':2,
'b':2,
'c':2
}
```

The first character whose frequency becomes **2** is returned.

---

# Complexity

```text
Time  : O(n)

Space : O(n)
```

---

# Q69. Sort the People

## Problem

Sort names according to heights in descending order.

Example

```text
Names

["Alice","Bob","Charlie"]

Heights

[165,180,175]

Output

["Bob","Charlie","Alice"]
```

---

# DSA Way (Dictionary)

```python
class Solution:
    def sortPeople(self,names,heights):

        mp = {}

        for i in range(len(names)):
            mp[heights[i]] = names[i]

        heights.sort(reverse=True)

        ans = []

        for h in heights:
            ans.append(mp[h])

        return ans
```

---

# Pythonic Way ⭐

```python
class Solution:
    def sortPeople(self,names,heights):

        people = zip(heights,names)

        people = sorted(people,reverse=True)

        return [name for height,name in people]
```

---

### Complexity

```text
Time  : O(n log n)

Space : O(n)
```

---

# Decimal to Binary

## Process

1. Divide number by 2.
2. Store remainder.
3. Continue until quotient becomes 0.
4. Reverse the remainders.

Example

```text
10

10 ÷ 2 = 5  remainder 0

5 ÷ 2 = 2   remainder 1

2 ÷ 2 = 1   remainder 0

1 ÷ 2 = 0   remainder 1

Reverse

1010
```

---

# Python

```python
n = 10

print(bin(n))
```

Output

```text
0b1010
```

Only Binary

```python
print(bin(n)[2:])
```

Output

```text
1010
```

---

# Binary to Decimal

Example

```text
1010

1×2³

0×2²

1×2¹

0×2⁰

=

8+0+2+0

=

10
```

Python

```python
binary = "1010"

print(int(binary,2))
```

Output

```text
10
```

---

# Bitwise Operators

## AND (&)

Returns **1** only if both bits are **1**.

Example

```python
a = 5
b = 3

print(a & b)
```

Binary

```text
5

101

3

011

--------

001
```

Output

```text
1
```

---

## OR (|)

Returns **1** if at least one bit is **1**.

```python
a = 5
b = 3

print(a | b)
```

Binary

```text
101

011

-----

111
```

Output

```text
7
```

---

## XOR (^)

Returns **1** when bits are different.

```python
a = 5
b = 3

print(a ^ b)
```

Binary

```text
101

011

-----

110
```

Output

```text
6
```

---

# Summary

| Operator | Meaning               |
| -------- | --------------------- |
| &        | Both bits must be 1   |
| |        | At least one bit is 1 |
| ^        | Bits are different    |

---

# JavaScript → Python Conversion

| JavaScript   | Python      |
| ------------ | ----------- |
| new Map()    | {}          |
| map.set(k,v) | dict[k] = v |
| map.get(k)   | dict[k]     |
| map.has(k)   | k in dict   |
| map.size     | len(dict)   |
| new Set()    | set()       |
| set.has(x)   | x in set    |
| set.add(x)   | set.add(x)  |

---

# Key Learnings

1. Hash Map reduces Two Sum from **O(n²)** to **O(n)**.
2. Set is useful for duplicate detection.
3. Dictionary is useful for frequency counting.
4. `dict.get(key,0)` is a common Python pattern.
5. `zip()` combines multiple lists.
6. `sorted()` returns a new sorted list.
7. `bin()` converts decimal to binary.
8. `int(binary,2)` converts binary to decimal.
9. Bitwise operators work on binary representations of numbers.

---

# Interview Tips

## Hash Map Pattern

```python
mp = {}

for i in range(len(nums)):

    complement = target - nums[i]

    if complement in mp:
        return [mp[complement],i]

    mp[nums[i]] = i
```

---

## Frequency Pattern

```python
freq = {}

for x in arr:

    freq[x] = freq.get(x,0) + 1
```

---

## Set Pattern

```python
visited = set()

if value in visited:
    ...
```

---

## Python Functions Learned Today

```python
set()

dict()

zip()

sorted()

sort(reverse=True)

bin()

int(binary,2)
```
