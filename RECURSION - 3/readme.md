# DAY 61 - RECURSION (PART 3) & GCD

# Q77. Sum of Digits

## Problem

Given a number, return the sum of all its digits.

Example

```text
Input

891

Output

18
```

Because

```text
8 + 9 + 1 = 18
```

---

## DSA Way

```python
class Solution:
    def sumOfDigits(self, n):

        if n == 0:
            return 0

        return (n % 10) + self.sumOfDigits(n // 10)
```

---

## Dry Run

Input

```text
891
```

Call Stack

```text
sumOfDigits(891)

↓

1 + sumOfDigits(89)

↓

1 + 9 + sumOfDigits(8)

↓

1 + 9 + 8 + sumOfDigits(0)

↓

1 + 9 + 8 + 0

↓

18
```

---

## Complexity

```text
Time  : O(d)

Space : O(d)
```

`d` = Number of digits.

---

## Pythonic Way ⭐

```python
def sumOfDigits(n):
    return sum(map(int, str(n)))
```

---

## Pythonic Explanation

### New Function: `str()`

Converts a number into a string.

Example

```python
str(891)
```

Output

```text
"891"
```

---

### New Function: `map()`

Applies a function to every element.

Example

```python
map(int, "891")
```

Internally

```text
int('8')

int('9')

int('1')
```

Produces

```text
8 9 1
```

---

### Combined

```python
sum(map(int, str(891)))
```

becomes

```text
sum([8,9,1])

↓

18
```

---

# Q78. Reverse Digits

## Problem

Reverse a number.

Example

```text
891

↓

198
```

---

## DSA Way

```python
class Solution:
    def reverseNumber(self, n, rev=0):

        if n == 0:
            return rev

        return self.reverseNumber(
            n // 10,
            rev * 10 + (n % 10)
        )
```

---

## Dry Run

```text
891

rev=0

↓

89

rev=1

↓

8

rev=19

↓

0

rev=198

↓

198
```

---

## Complexity

```text
Time  : O(d)

Space : O(d)
```

---

## Pythonic Way ⭐

```python
def reverseNumber(n):
    return int(str(n)[::-1])
```

---

## Pythonic Explanation

### String Slicing

You already learned slicing.

Now

```python
[::-1]
```

means

```text
Start

↓

End

↓

Step = -1
```

So

```python
"891"[::-1]
```

becomes

```text
198
```

---

### Why `int()`?

Because

```python
str(n)[::-1]
```

returns

```text
"198"
```

which is a string.

We convert it back.

```python
int("198")
```

↓

```text
198
```

---

# Q79. GCD (Greatest Common Divisor)

## Definition

The **Greatest Common Divisor (GCD)** is the largest number that divides both numbers.

Example

```text
GCD(12,18)

Factors of 12

1 2 3 4 6 12

Factors of 18

1 2 3 6 9 18

Greatest Common Factor

6
```

---

# A. Brute Force

## DSA Way

```python
class Solution:
    def gcdBruteForce(self, a, b, i):

        if a % i == 0 and b % i == 0:
            return i

        return self.gcdBruteForce(a, b, i - 1)
```

Call

```python
obj.gcdBruteForce(a, b, min(a,b))
```

---

## Dry Run

```text
a=12

b=18

↓

i=12

↓

11

↓

10

↓

9

↓

8

↓

7

↓

6

↓

Both divisible

↓

Answer = 6
```

---

## Complexity

```text
Time  : O(min(a,b))

Space : O(min(a,b))
```

---

# B. Subtraction Method

## DSA Way

```python
class Solution:
    def gcdSubtraction(self, a, b):

        if a == b:
            return a

        if a > b:
            return self.gcdSubtraction(a - b, b)

        return self.gcdSubtraction(a, b - a)
```

---

## Dry Run

```text
12,18

↓

12,6

↓

6,6

↓

Answer = 6
```

---

## Complexity

```text
Time  : O(max(a,b))

Space : O(max(a,b))
```

---

# C. Euclidean Algorithm (Optimal)

## DSA Way

```python
class Solution:
    def gcdEuclidean(self, a, b):

        if b == 0:
            return a

        return self.gcdEuclidean(b, a % b)
```

---

## Dry Run

Input

```text
12,18
```

Calls

```text
gcd(12,18)

↓

gcd(18,12)

↓

gcd(12,6)

↓

gcd(6,0)

↓

6
```

Output

```text
6
```

---

## Why does it work?

Important Formula

```text
GCD(a,b)

=

GCD(b,a%b)
```

Example

```text
GCD(18,12)

↓

18%12

↓

6

↓

GCD(12,6)

↓

12%6

↓

0

↓

GCD(6,0)

↓

6
```

---

## Complexity

```text
Time  : O(log(max(a,b)))

Space : O(log(max(a,b)))
```

---

## Pythonic Way ⭐

```python
import math

def gcd(a, b):
    return math.gcd(a, b)
```

---

## Pythonic Explanation

### New Library: `math`

Python provides many mathematical functions.

Import it

```python
import math
```

---

### New Function: `math.gcd()`

Returns the Greatest Common Divisor.

Example

```python
math.gcd(12,18)
```

Output

```text
6
```
# 📘 Recursion & Math Algorithms (Python)

This repository contains solutions for common recursion and mathematics problems with:

* ✅ DSA / Interview Approach
* ⭐ Pythonic Approach
* 📝 Algorithm
* 🔍 Dry Run
* ⏱️ Time & Space Complexity

---

# 1️⃣ Power Function `pow(x, n)`

## Problem

Given a number `x` and an integer `n`, compute:

```text
xⁿ
```

Examples

```text
Input:
x = 2
n = 5

Output:
32
```

```text
Input:
x = 2
n = -3

Output:
0.125
```

---

## DSA Approach (Binary Exponentiation)

```python
class Solution:

    def myPow(self, x, n):

        if n < 0:
            return 1 / self.solve(x, -n)

        return self.solve(x, n)

    def solve(self, x, n):

        if n == 0:
            return 1

        if n == 1:
            return x

        half = self.solve(x, n // 2)

        if n % 2 == 0:
            return half * half

        return half * half * x
```

---

## Algorithm

1. If power is negative, convert it to positive.
2. Base Case:

   * `n == 0 → 1`
   * `n == 1 → x`
3. Solve only half of the exponent.
4. If exponent is even:

```text
xⁿ = (xⁿᐟ²)²
```

5. If exponent is odd:

```text
xⁿ = (xⁿᐟ²)² × x
```

---

## Dry Run

Input

```text
x = 2
n = 10
```

Calls

```text
solve(10)

↓

solve(5)

↓

solve(2)

↓

solve(1)

↓

2

↑

4

↑

32

↑

1024
```

Output

```text
1024
```

---

## Complexity

```text
Time  : O(log n)

Space : O(log n)
```

---

## ⭐ Pythonic Way

```python
def myPow(x, n):
    return x ** n
```

or

```python
def myPow(x, n):
    return pow(x, n)
```

### Explanation

* `**` is Python's exponent operator.
* `pow()` is Python's built-in power function.

---

# 📘 Find Greatest Common Divisor of Array (LeetCode)

## Problem

Given an integer array `nums`, return the **Greatest Common Divisor (GCD)** of the **smallest** and **largest** element in the array.

### Example 1

```text
Input:
nums = [2,5,6,9,10]

Output:
2
```

Explanation

```text
Smallest = 2
Largest  = 10

GCD(2,10) = 2
```

---

### Example 2

```text
Input:
nums = [7,5,6,8,3]

Output:
1
```

Explanation

```text
Smallest = 3
Largest  = 8

GCD(3,8) = 1
```

---

# DSA Approach

## Step 1

Find the minimum and maximum element of the array.

## Step 2

Use the **Euclidean Algorithm** to calculate their GCD.

---
---
## Alternate 
```python
class solution:
    def findGCD(self,nums):
        a=min(nums)
        b=max(nums)
        while b:
            a,b=b,a%b
        return a
```
---
## Python Solution

```python
class Solution:
    def findGCD(self, nums):

        minimum = min(nums)
        maximum = max(nums)

        return self.gcd(minimum, maximum)

    def gcd(self, a, b):

        if b == 0:
            return a

        return self.gcd(b, a % b)
```

---

# Algorithm

1. Find the smallest element using `min()`.
2. Find the largest element using `max()`.
3. Apply the Euclidean Algorithm:

```text
GCD(a,b) = GCD(b,a%b)
```

4. Continue until `b` becomes `0`.
5. Return `a`.

---

# Dry Run

Input

```text
nums = [2,5,6,9,10]
```

Find

```text
minimum = 2
maximum = 10
```

Now calculate

```text
gcd(2,10)

↓

gcd(10,2)

↓

gcd(2,0)

↓

Answer = 2
```

---

# Another Dry Run

Input

```text
nums = [3,6,9,12]
```

Find

```text
minimum = 3
maximum = 12
```

Calculate

```text
gcd(3,12)

↓

gcd(12,3)

↓

gcd(3,0)

↓

Answer = 3
```

---

# Why Euclidean Algorithm Works

Important Formula

```text
GCD(a,b) = GCD(b,a%b)
```

Example

```text
GCD(18,12)

↓

18 % 12 = 6

↓

GCD(12,6)

↓

12 % 6 = 0

↓

GCD(6,0)

↓

6
```

Each recursive call reduces the problem size, making it much faster than checking every possible divisor.

---

# Complexity

Finding minimum element

```text
O(n)
```

Finding maximum element

```text
O(n)
```

Euclidean Algorithm

```text
O(log(max(nums)))
```

Overall

```text
Time  : O(n)

Space : O(log(max(nums)))
```

Since scanning the array dominates the runtime, the overall complexity is **O(n)**.

---

# ⭐ Pythonic Way

```python
import math

class Solution:
    def findGCD(self, nums):
        return math.gcd(min(nums), max(nums))
```

---

# Pythonic Explanation

### `min(nums)`

Returns the smallest element.

Example

```python
min([2,5,6,9,10])
```

Output

```text
2
```

---

### `max(nums)`

Returns the largest element.

Example

```python
max([2,5,6,9,10])
```

Output

```text
10
```

---

### `math.gcd(a, b)`

Returns the Greatest Common Divisor of two numbers.

Example

```python
math.gcd(2,10)
```

Output

```text
2
```

Python internally uses the optimized **Euclidean Algorithm**.

---

# Key Learnings

* The problem asks for the GCD of the **minimum** and **maximum** elements only.
* Use the Euclidean Algorithm for an efficient GCD calculation.
* `min()` and `max()` each scan the array once.
* `math.gcd()` is Python's built-in implementation of the Euclidean Algorithm.

---

# Interview Tip

When you see **GCD** in a coding interview:

* Avoid checking every divisor (brute force).
* Think of the Euclidean Algorithm immediately.

```python
if b == 0:
    return a

return gcd(b, a % b)
```

This recursive pattern is the standard and most efficient solution.


---

# Comparison

| Method      | Time Complexity  |
| ----------- | ---------------- |
| Brute Force | O(min(a,b))      |
| Subtraction | O(max(a,b))      |
| Euclidean   | O(log(max(a,b))) |
| math.gcd()  | O(log(max(a,b))) |

---

# Key Learnings

1. Sum of digits can be solved using recursion or string conversion.
2. Reverse digits uses an accumulator (`rev`) during recursion.
3. `map()` applies a function to every element.
4. `[::-1]` reverses a string or list.
5. GCD is the largest common divisor of two numbers.
6. Euclidean Algorithm is the fastest recursive method for finding GCD.
7. `math.gcd()` is Python's built-in implementation.

---

# Interview Tips

## Digit Recursion Pattern

```python
last_digit = n % 10

remaining = n // 10
```

This pattern is used in:

* Sum of Digits
* Reverse Number
* Count Digits
* Product of Digits
* Armstrong Number

---

## Euclidean Algorithm Pattern

```python
if b == 0:
    return a

return gcd(b, a % b)
```

This is one of the most frequently asked recursion problems.

---

# Python Functions / Concepts Learned Today

```python
str()

map()

int()

[::-1]

math.gcd()
```
