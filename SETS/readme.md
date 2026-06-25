# DAY 53 - SETS, MAPS & HASHING IN PYTHON

# Q63. Jewels and Stones

## Problem

Given two strings:

* **jewels** → characters representing jewels.
* **stones** → characters representing stones you have.

Return the number of stones that are also jewels.

Example:

```text
Jewels = "aA"
Stones = "aAAbbbb"

Output = 3
```

---

## DSA Way

```python
class Solution(object):
    def numJewelsInStones(self, jewels, stones):

        s = set()

        for ch in jewels:
            s.add(ch)

        count = 0

        for ch in stones:
            if ch in s:
                count += 1

        return count
```

---

## Dry Run

Input

```text
Jewels = "aA"
Stones = "aAAbbbb"
```

Set

```text
{'a','A'}
```

Traverse Stones

```text
a ✔
A ✔
A ✔
b ✖
b ✖
b ✖
b ✖
```

Answer

```text
3
```

---

## Complexity

```text
Time  : O(n + m)

Space : O(n)
```

where

* n = jewels
* m = stones

---

## Pythonic Way

```python
class Solution(object):
    def numJewelsInStones(self, jewels, stones):

        jewels = set(jewels)

        return sum(ch in jewels for ch in stones)
```

---

# Q65. Happy Number

## Definition

A Happy Number eventually becomes **1** after repeatedly replacing the number by the sum of the squares of its digits.

If the process repeats forever, it is **not** a Happy Number.

Example:

```text
19

1² + 9² = 82

8² + 2² = 68

6² + 8² = 100

1² + 0² + 0² = 1

Happy Number
```

---

## DSA Way

```python
class Solution(object):

    def isHappy(self, n):

        visited = set()

        while True:

            total = 0

            while n > 0:

                digit = n % 10

                total += digit * digit

                n //= 10

            if total == 1:
                return True

            if total in visited:
                return False

            visited.add(total)

            n = total
```

---


## Dry Run

Input

```text
19
```

Iterations

```text
19 -> 82

82 -> 68

68 -> 100

100 -> 1
```

Output

```text
True
```

---
---

## Pythonic Way
```python
    def isHappy(self, n):
        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)

            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1
```

---

## Why Set?

Without a Set:

```text
4

16

37

58

89

145

42

20

4

16

37

...
```

The sequence loops forever.

The Set detects repeated values.

---

## Complexity

```text
Time  : O(log n)

Space : O(log n)
```

---

# Python Dictionary (Equivalent of JavaScript Map)

## Definition

A Dictionary stores data in **key : value** pairs.

It is the Python equivalent of JavaScript's **Map**.

---

## Creating Dictionary

```python
mp = {}
```

or

```python
mp = dict()
```

---

## Adding Elements

```python
mp["name"] = "Alice"

mp["age"] = 25

mp[True] = "booleanKey"
```

---

## Output

```python
print(mp)
```

```text
{
'name':'Alice',
'age':25,
True:'booleanKey'
}
```

---

## Access Value

```python
print(mp["name"])
```

Output

```text
Alice
```

---

## Using get()

```python
print(mp.get("age"))
```

Output

```text
25
```

---

## Check Key Exists

```python
print("age" in mp)
```

Output

```text
True
```

Equivalent to

```javascript
map.has(key)
```

---

## Delete Key

```python
del mp["age"]
```

Output

```python
print(mp)
```

```text
{'name':'Alice',True:'booleanKey'}
```

---

## Loop Through Dictionary

```python
for key,value in mp.items():
    print(key,"=>",value)
```

Output

```text
name => Alice

True => booleanKey
```

---

## Length

```python
print(len(mp))
```

Equivalent

```javascript
map.size
```

---

## Clear Dictionary

```python
mp.clear()
```

Output

```python
{}
```

---

# JavaScript Map vs Python Dictionary

| JavaScript     | Python            |
| -------------- | ----------------- |
| new Map()      | {} / dict()       |
| set(key,value) | dict[key] = value |
| get(key)       | dict[key] / get() |
| has(key)       | key in dict       |
| delete(key)    | del dict[key]     |
| size           | len(dict)         |
| clear()        | clear()           |

---

# Useful Dictionary Operations

## Frequency Count

```python
arr = [1,2,1,3,2,1]

freq = {}

for num in arr:

    freq[num] = freq.get(num,0) + 1

print(freq)
```

Output

```text
{
1:3,
2:2,
3:1
}
```

---

## Count Characters

```python
s = "banana"

freq = {}

for ch in s:

    freq[ch] = freq.get(ch,0) + 1

print(freq)
```

Output

```text
{
'b':1,
'a':3,
'n':2
}
```

---

# Key Learnings

1. Set stores only unique values.
2. Membership checking in Set takes O(1).
3. Dictionary stores key-value pairs.
4. Dictionary is Python's equivalent of JavaScript Map.
5. `dict.get(key, default)` avoids checking whether a key exists before updating it.
6. Set is useful for detecting duplicate or repeated values.
7. Dictionary is useful for frequency counting.

---

# Interview Tips

## Set

Used for:

* Remove duplicates
* Membership checking
* Cycle detection
* Happy Number
* Jewels and Stones

Example

```python
visited = set()

if value in visited:
```

---

## Dictionary

Used for:

* Frequency Count
* Hash Map Problems
* Two Sum
* Character Count
* Group Anagrams

Pattern

```python
freq = {}

freq[key] = freq.get(key,0) + 1
```

This is one of the most important patterns in DSA and appears in many LeetCode problems.

---

# Python Functions Learned Today

```python
set()

add()

in

len()

clear()

dict()

get()

items()

del
```