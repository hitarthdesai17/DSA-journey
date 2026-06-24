# DAY 47 - STRINGS IN PYTHON

## Introduction to Strings

A string is a sequence of characters used to represent text.

Strings can be enclosed in:

```python
'Hello'
"Hello"
'''Hello'''
```

Strings are immutable, meaning characters cannot be changed after creation.

Example:

```python
s = "hello"
s[0] = "H"   # Error
```

---

# String Methods (JavaScript → Python)

| JavaScript           | Python                  |
| -------------------- | ----------------------- |
| str.length           | len(str)                |
| slice(start,end)     | str[start:end]          |
| substring(start,end) | str[start:end]          |
| substr(start,length) | str[start:start+length] |
| toUpperCase()        | upper()                 |
| toLowerCase()        | lower()                 |
| concat()             | +                       |
| trim()               | strip()                 |
| indexOf()            | find()                  |
| lastIndexOf()        | rfind()                 |
| includes()           | in                      |
| startsWith()         | startswith()            |
| endsWith()           | endswith()              |
| replace()            | replace()               |
| replaceAll()         | replace()               |
| split()              | split()                 |
| charAt(i)            | str[i]                  |
| charCodeAt(i)        | ord(str[i])             |

---

# Examples

## Length

```python
s = "Hello"
print(len(s))
```

Output:

```text
5
```

---

## Uppercase

```python
s = "hello"
print(s.upper())
```

Output:

```text
HELLO
```

---

## Lowercase

```python
s = "HELLO"
print(s.lower())
```

Output:

```text
hello
```

---

## Trim Spaces

```python
s = "   hello   "
print(s.strip())
```

Output:

```text
hello
```

---

## Contains

```python
s = "hello"

print("ell" in s)
```

Output:

```text
True
```

---

## Character at Index

```python
s = "hello"

print(s[1])
```

Output:

```text
e
```

---

## ASCII / Unicode Value

```python
print(ord('A'))
```

Output:

```text
65
```

Convert ASCII back to character:

```python
print(chr(65))
```

Output:

```text
A
```

---

# Q35. Accept a String and Print Each Character on a New Line

## DSA Way

```python
s = input("Enter a string: ")

for i in range(len(s)):
    print(s[i])
```

### Output

Input:

```text
hello
```

Output:

```text
h
e
l
l
o
```

---

## Pythonic Way

```python
s = input("Enter a string: ")

for ch in s:
    print(ch)
```

---

# Q36. Accept a String and Print It in Reverse Order

## DSA Way

```python
s = input("Enter a string: ")

reversed_str = ""

for i in range(len(s)-1,-1,-1):
    reversed_str += s[i]

print(reversed_str)
```

Input:

```text
hello
```

Output:

```text
olleh
```

---

## Pythonic Way

```python
s = input()

print(s[::-1])
```

### Explanation

```python
s[start:end:step]
```

Reverse string:

```python
s[::-1]
```

Meaning:

```text
Start from end
Move backwards
Take every character
```

---

# Convert String to List

```python
s = "hello"

arr = list(s)

print(arr)
```

Output:

```text
['h', 'e', 'l', 'l', 'o']
```

---

# Join Characters into String

```python
arr = ['h','e','l','l','o']

s = "".join(arr)

print(s)
```

Output:

```text
hello
```

---

# Count Character Frequency

```python
s = "banana"

print(s.count('a'))
```

Output:

```text
3
```

---

# Find Index of Substring

```python
s = "banana"

print(s.find("na"))
```

Output:

```text
2
```

---

# Useful String Operations for DSA

Length

```python
len(s)
```

Reverse String

```python
s[::-1]
```

Uppercase

```python
s.upper()
```

Lowercase

```python
s.lower()
```

Split String

```python
s.split()
```

Join String

```python
"".join(arr)
```

Character to ASCII

```python
ord(ch)
```

ASCII to Character

```python
chr(num)
```

---

# Interview Tips

1. Strings are immutable.
2. Use indexing to access characters.

```python
s[i]
```

3. Use slicing for substring operations.

```python
s[start:end]
```

4. Reverse string quickly.

```python
s[::-1]
```

5. Convert string to list when modifications are required.

```python
list(s)
```

6. Convert list back to string.

```python
"".join(arr)
```

7. Frequently used functions:

```python
len()
upper()
lower()
strip()
find()
replace()
split()
join()
ord()
chr()
```

These operations are heavily used in:

* Reverse String
* Palindrome
* Anagram
* String Compression
* Frequency Count
* Longest Common Prefix
* Character Manipulation Problems
# Q37. Check if String is Palindrome (Two Pointer)

### DSA Way

```python
def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

print(isPalindrome("madam"))
print(isPalindrome("hello"))
```

### Output

```text
True
False
```

### Dry Run

```text
madam

m == m ✔
a == a ✔

Palindrome
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

### Interview Tip

This is the standard Two Pointer approach used in many palindrome problems.

---

# Q38. Toggle Each Alphabet Using ASCII Values

### DSA Way

```python
def toggleCase(s):
    result = ""

    for ch in s:
        ascii_val = ord(ch)

        if 65 <= ascii_val <= 90:
            result += chr(ascii_val + 32)

        elif 97 <= ascii_val <= 122:
            result += chr(ascii_val - 32)

        else:
            result += ch

    return result

print(toggleCase("AcgDfD"))
```

### Output

```text
aCGdFd
```

### ASCII Range

```text
A-Z -> 65 to 90
a-z -> 97 to 122
```

### Pythonic Way

```python
def toggleCase(s):
    return s.swapcase()

print(toggleCase("AcgDfD"))
```

### Complexity

```text
Time  : O(n)
Space : O(n)
```

---

# Q39. Count Words with Given Prefix

### DSA Way

```python
def countPrefix(words,pref):
    count = 0

    for word in words:
        if word.startswith(pref):
            count += 1

    return count

print(countPrefix(
    ["pay","attention","practice","attend"],
    "at"
))
```

### Output

```text
2
```

### Pythonic Way

```python
def countPrefix(words,pref):
    return sum(
        word.startswith(pref)
        for word in words
    )
```

### Complexity

```text
Time  : O(n)
Space : O(1)
```

---

# Q40. Capitalize First and Last Character of Each Word

Input

```text
hello bhai kya haal chaal
```

Output

```text
HellO BhaI KyA HaaL ChaaL
```

### DSA Way

```python
s = "hello bhai kya haal chaal"

ans = ""

arrStr = s.split()

for word in arrStr:

    if len(word) <= 2:
        ans += word.upper() + " "

    else:
        ans += (
            word[0].upper()
            + word[1:-1]
            + word[-1].upper()
            + " "
        )

print(ans)
```

### Output

```text
HellO BhaI KyA HaaL ChaaL
```

### Explanation

For

```text
hello
```

```text
h -> H
ello -> same
o -> O
```

Result

```text
HellO
```

### Complexity

```text
Time  : O(n)
Space : O(n)
```

---

# Useful String Functions Used Today

### ASCII Value

```python
ord('A')
```

Output

```text
65
```

---

### Character from ASCII

```python
chr(65)
```

Output

```text
A
```

---

### Starts With

```python
word.startswith("at")
```

---

### Uppercase

```python
s.upper()
```

---

### Lowercase

```python
s.lower()
```

---

### Toggle Case

```python
s.swapcase()
```

---

### Split String

```python
s.split()
```

---

# Key Learnings

1. Strings are immutable.
2. Use Two Pointers for palindrome problems.
3. Use `ord()` and `chr()` for ASCII-based questions.
4. `startswith()` is useful for prefix questions.
5. `split()` converts a sentence into words.
6. `[::-1]` is the easiest way to reverse a string in Python.
7. `swapcase()` is the Pythonic way to toggle case.

---

# Interview Tips

### Reverse String

```python
s[::-1]
```

### Palindrome

```python
left = 0
right = len(s)-1
```

### ASCII Conversion

```python
ord(ch)
chr(num)
```

### Prefix Check

```python
word.startswith(prefix)
```

These concepts frequently appear in:

* Valid Palindrome
* Reverse String
* Reverse Words in a String
* Longest Common Prefix
* String Compression
* Anagram Problems
* Character Frequency Problems
