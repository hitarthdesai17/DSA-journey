# DAY 52 - FREQUENCY ARRAY, ANAGRAMS & SETS IN PYTHON

# Q61. Frequency of Each Character (Using Bitmap / Integer Array)

## DSA Way

```python
def charFrequency(s):

    freq = [0] * 123     # ASCII values

    for ch in s:
        freq[ord(ch)] += 1

    for i in range(97, 123):   # a-z
        if freq[i] > 0:
            print(f"{chr(i)} : {freq[i]}")

charFrequency("character")
```

### Output

```text
a : 2
c : 2
e : 1
h : 1
r : 2
t : 1
```

---

## Dry Run

Input

```text
character
```

ASCII values:

```text
c -> 99
h -> 104
a -> 97
r -> 114
a -> 97
c -> 99
t -> 116
e -> 101
r -> 114
```

Frequency Array:

```text
freq[97]  = 2
freq[99]  = 2
freq[101] = 1
freq[104] = 1
freq[114] = 2
freq[116] = 1
```

---

## Complexity

```text
Time  : O(n)
Space : O(1)
```

(ASCII size is fixed)

---

## Pythonic Way

```python
from collections import Counter

s = "character"

freq = Counter(s)

for ch,count in freq.items():
    print(ch,":",count)
```

### Output

```text
c : 2
h : 1
a : 2
r : 2
t : 1
e : 1
```

---

# Q62. Check Two Strings Are Anagram Or Not (Using Frequency Array)

## Definition

Two strings are Anagrams if:

* Both strings have the same characters.
* Frequency of every character is the same.

Example:

```text
arc  -> car
state -> taste
night -> thing
```

All are Anagrams.

---

## DSA Way

```python
def isAnagram(str1,str2):

    if len(str1) != len(str2):
        return False

    freq = [0] * 123

    for ch in str1:
        freq[ord(ch)] += 1

    for ch in str2:
        freq[ord(ch)] -= 1

    for i in range(97,123):
        if freq[i] != 0:
            return False

    return True


print(isAnagram("arc","car"))
print(isAnagram("state","taste"))
print(isAnagram("night","thing"))
print(isAnagram("apple","papel"))
print(isAnagram("test","rest"))
```

### Output

```text
True
True
True
True
False
```

---

## Dry Run

Input:

```text
arc
car
```

Frequency after first string:

```text
a = 1
r = 1
c = 1
```

Frequency after second string:

```text
c = 0
a = 0
r = 0
```

All frequencies become zero.

Result:

```text
True
```

---

## Complexity

```text
Time  : O(n)
Space : O(1)
```

---

## Pythonic Way

```python
from collections import Counter

def isAnagram(str1,str2):
    return Counter(str1) == Counter(str2)

print(isAnagram("arc","car"))
```

---

# Python Set

## Definition

A Set is a collection of unique elements.

Duplicate values are automatically removed.

---

## Creating a Set

```python
s = set()
```

---

## Adding Elements

```python
s.add(1)
s.add(2)
s.add(3)
s.add(2)

print(s)
```

Output

```text
{1, 2, 3}
```

Notice:

```text
2 is added only once
```

---

## Checking Existence

```python
print(2 in s)
print(5 in s)
```

Output

```text
True
False
```

Equivalent to JavaScript:

```javascript
set.has(2)
```

---

## Removing Elements

```python
s.remove(2)

print(s)
```

Output

```text
{1, 3}
```

---

## Loop Through Set

```python
for item in s:
    print(item)
```

Output

```text
1
3
```

---

## Length of Set

```python
print(len(s))
```

Output

```text
2
```

Equivalent to:

```javascript
set.size
```

---

## Clear Set

```python
s.clear()

print(s)
```

Output

```text
set()
```

---

# JavaScript Set vs Python Set

| JavaScript | Python   |
| ---------- | -------- |
| new Set()  | set()    |
| add()      | add()    |
| has()      | in       |
| delete()   | remove() |
| size       | len(set) |
| clear()    | clear()  |

---

# Useful Set Operations

## Union

```python
a = {1,2,3}
b = {3,4,5}

print(a | b)
```

Output

```text
{1,2,3,4,5}
```

---

## Intersection

```python
a = {1,2,3}
b = {3,4,5}

print(a & b)
```

Output

```text
{3}
```

---

## Difference

```python
a = {1,2,3}
b = {3,4,5}

print(a - b)
```

Output

```text
{1,2}
```

---

# Interview Tips

## Frequency Array

Remember:

```python
ord(ch)
chr(num)
```

Used for:

* Character Frequency
* Anagram Problems
* ASCII Manipulation

---

## Anagram Pattern

```python
freq = [0] * 123

for ch in str1:
    freq[ord(ch)] += 1

for ch in str2:
    freq[ord(ch)] -= 1
```

If all values become zero:

```python
return True
```

---

## Set Pattern

Used for:

* Remove Duplicates
* Unique Elements
* Membership Checking

Example:

```python
if x in s:
```

Time Complexity:

```text
O(1)
```

which is much faster than:

```python
if x in arr:
```

which takes:

```text
O(n)
```

---

# Key Learnings

1. Frequency Array stores count of characters using ASCII values.
2. `ord()` converts character → ASCII.
3. `chr()` converts ASCII → character.
4. Anagrams can be solved using a Frequency Array.
5. Sets store only unique values.
6. Membership checking in Set is O(1).
7. Sets are heavily used in DSA and LeetCode problems.
