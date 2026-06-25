# DAY 55 - BITWISE SHIFT OPERATORS & BIT MANIPULATION IN PYTHON

# Bitwise Shift Operators

## 1. Left Shift (`<<`)

### Definition

Left Shift moves all bits to the left.

Each left shift multiplies the number by **2**.

### Example

```python
x = 5

print(x << 1)
```

Output

```text
10
```

### Binary Explanation

```text
5

101

Shift Left by 1

1010

=

10
```

Example

```python
print(5 << 2)
```

Binary

```text
101

↓

10100

=

20
```

Because

```text
5 × 2² = 20
```

---

## 2. Right Shift (`>>`)

### Definition

Right Shift moves all bits to the right.

Each right shift divides the number by **2** (floor division).

### Example

```python
x = 8

print(x >> 1)
```

Output

```text
4
```

Binary

```text
1000

↓

100

=

4
```

Another Example

```python
print(20 >> 2)
```

Binary

```text
10100

↓

00101

=

5
```

Because

```text
20 ÷ 2² = 5
```

---

# Q70. Swap Two Numbers Without Third Variable (Using XOR)

## DSA Way

```python
a = 5
b = 7

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
```

Output

```text
7 5
```

---

## Dry Run

Initially

```text
a = 5

101

b = 7

111
```

Step 1

```python
a = a ^ b
```

```text
101

111

↓

010

a = 2
```

Now

```text
a = 2

b = 7
```

Step 2

```python
b = a ^ b
```

```text
010

111

↓

101

b = 5
```

Now

```text
a = 2

b = 5
```

Step 3

```python
a = a ^ b
```

```text
010

101

↓

111

a = 7
```

Final

```text
a = 7

b = 5
```

---

## Pythonic Way ⭐

```python
a = 5
b = 7

a, b = b, a

print(a, b)
```

Output

```text
7 5
```

### Explanation

This is called **Tuple Unpacking**.

Python first creates a temporary tuple.

```python
(b, a)
```

becomes

```python
(7,5)
```

Then assigns

```python
a = 7

b = 5
```

No extra variable is required.

This is the preferred Python way.

---

# Q71. Check Even or Odd (Using Bitwise AND)

## DSA Way

```python
def isEven(num):

    return (num & 1) == 0


print(isEven(4))

print(isEven(7))
```

Output

```text
True

False
```

---

## Why does `num & 1` work?

Every even number ends with **0** in binary.

Example

```text
4

100
```

```text
100

001

↓

000
```

Result

```text
0
```

Odd Number

```text
7

111

001

↓

001

=

1
```

Hence

```python
(num & 1) == 0
```

means

```text
Even
```

---

## Pythonic Way

The DSA solution is already the Pythonic way.

There is no shorter or better alternative.

---

# Q72. Check if Number is Power of 2

## DSA Way

```python
def isPowerOfTwo(num):

    return num > 0 and (num & (num-1)) == 0


print(isPowerOfTwo(8))

print(isPowerOfTwo(10))
```

Output

```text
True

False
```

---

## Why does this work?

Power of 2

```text
1

1

2

10

4

100

8

1000

16

10000
```

Notice

Every power of 2 has only **one 1**.

Subtract 1

```text
1000

↓

0111
```

Now AND them

```text
1000

0111

↓

0000
```

Result

```text
0
```

Example

```text
8

1000

7

0111

1000 & 0111

↓

0000
```

---

Not Power of 2

```text
10

1010

9

1001

1010

1001

↓

1000
```

Result

```text
8

≠ 0
```

Hence

```text
False
```

---

## Pythonic Way

The DSA solution itself is already the Pythonic way.

---

# Bitwise Operator Summary

| Operator | Meaning          |
| -------- | ---------------- |
| &        | AND              |
| |        | OR               |
| ^        | XOR              |
| <<       | Left Shift (×2)  |
| >>       | Right Shift (÷2) |

---

# JavaScript → Python

| JavaScript | Python |
| ---------- | ------ |
| <<         | <<     |
| >>         | >>     |
| &          | &      |
| |          | |      |
| ^          | ^      |

Bitwise operators are exactly the same in Python.

---

# Pythonic Feature Learned Today

## Tuple Unpacking

Instead of

```python
temp = a
a = b
b = temp
```

Python allows

```python
a, b = b, a
```

### How it works

Python first creates

```python
(b, a)
```

Example

```python
a = 10
b = 20
```

Python internally thinks

```python
(20,10)
```

Then assigns

```python
a = 20

b = 10
```

This is called **Tuple Packing and Unpacking**.

---

# Key Learnings

1. `<<` multiplies by powers of 2.
2. `>>` divides by powers of 2.
3. XOR can swap two numbers without a temporary variable.
4. `(num & 1)` checks if a number is even or odd.
5. `(num & (num-1)) == 0` checks whether a number is a power of two.
6. Python uses tuple unpacking for swapping variables.

---

# Interview Tips

## Swap

Interview

```python
a = a ^ b
b = a ^ b
a = a ^ b
```

Python

```python
a, b = b, a
```

---

## Even or Odd

```python
num & 1
```

Very common in bit manipulation problems.

---

## Power of Two

Remember this pattern

```python
num > 0 and (num & (num-1)) == 0
```

This appears in many LeetCode Bit Manipulation problems.

---

# Python Functions / Concepts Learned Today

```python
<<

>>

^

&

Tuple Unpacking

a, b = b, a
```