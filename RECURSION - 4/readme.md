# DAY 62 - MATHS & RECURSION

# Q80. Count Primes (Sieve of Eratosthenes)

## Problem

Print all prime numbers from **2 to n**.

Example

```text
Input

20

Output

2 3 5 7 11 13 17 19
```

---

## DSA Way

```python
class Solution:
    def countPrimes(self, n):

        if n < 2:
            return []

        # Initially assume every number is prime
        isPrime = [True] * (n + 1)

        # 0 and 1 are not prime
        isPrime[0] = isPrime[1] = False

        i = 2

        while i * i <= n:

            if isPrime[i]:

                # Mark all multiples of i as non-prime
                j = i * i

                while j <= n:
                    isPrime[j] = False
                    j += i

            i += 1

        ans = []

        for i in range(2, n + 1):
            if isPrime[i]:
                ans.append(i)

        return ans
```

---

## Dry Run

Input

```text
20
```

Initially

```text
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

T T T T T T T T T  T  T  T  T  T  T  T  T  T  T
```

Start with

```text
2
```

Mark multiples

```text
4 6 8 10 12 14 16 18 20

↓

False
```

Next

```text
3
```

Mark

```text
9 12 15 18

↓

False
```

Next

```text
4

Already False

Skip
```

Next

```text
5
```

Now

```text
5 × 5 = 25

>

20

Stop
```

Remaining True

```text
2 3 5 7 11 13 17 19
```

---

## Why start from `i * i`?

Suppose

```text
i = 5
```

Multiples are

```text
5

10

15

20

25
```

Notice

```text
10

=

2×5
```

already marked by **2**.

```text
15

=

3×5
```

already marked by **3**.

```text
20

=

4×5
```

already marked by **4**.

So we begin from

```text
25
```

to avoid repeating work.

---

## Complexity

```text
Time  : O(n log(log n))

Space : O(n)
```
---
## LEETCODE PROBLEM:

```python
class Solution:
    def countPrimes(self, n):

        if n <= 2:
            return 0

        # Assume every number is prime
        isPrime = [True] * n

        # 0 and 1 are not prime
        isPrime[0] = False
        isPrime[1] = False

        i = 2

        while i * i < n:

            if isPrime[i]:

                j = i * i

                while j < n:
                    isPrime[j] = False
                    j += i

            i += 1

        count = 0

        for i in range(2, n):
            if isPrime[i]:
                count += 1

        return count
```
---
---

## Pythonic Way ⭐

```python
def countPrimes(n):

    if n < 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):

        if sieve[i]:
            sieve[i * i:n + 1:i] = [False] * len(sieve[i * i:n + 1:i])

    return [i for i in range(2, n + 1) if sieve[i]]
```

---

## Pythonic Explanation

### `n ** 0.5`

Computes square root.

Example

```python
16 ** 0.5
```

↓

```text
4.0
```

---

### List Slicing

```python
sieve[start:end:step]
```

Example

```python
arr=[0,1,2,3,4,5,6,7,8]

arr[2:9:2]
```

Output

```text
2 4 6 8
```

---

### List Comprehension ⭐

```python
[i for i in range(10)]
```

Produces

```text
[0,1,2,3,4,5,6,7,8,9]
```

It is a compact way to create lists.

---

# Q81. Square Root

---

# A. Brute Force

## DSA Way

```python
class Solution:
    def sqrtBrute(self, x):

        i = 0

        while i * i <= x:
            i += 1

        return i - 1
```

---

## Dry Run

```text
x = 20

0²

1²

2²

3²

4²

5²

25 > 20

Answer = 4
```

---

## Complexity

```text
Time  : O(√n)

Space : O(1)
```

---

# B. Binary Search (Optimal)

## DSA Way

```python
class Solution:
    def mySqrt(self, x):

        if x < 2:
            return x

        left = 1
        right = x // 2
        ans = 1

        while left <= right:

            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                ans = mid
                left = mid + 1

            else:
                right = mid - 1

        return ans
```

---

## Dry Run

Input

```text
20
```

```text
left=1

right=10

↓

mid=5

25>20

↓

right=4

↓

mid=2

4<20

↓

left=3

↓

mid=3

9<20

↓

left=4

↓

mid=4

16<20

↓

Answer=4
```

---

## Complexity

```text
Time  : O(log n)

Space : O(1)
```

---

## Pythonic Way ⭐

```python
import math

def mySqrt(x):
    return math.isqrt(x)
```

---

## Pythonic Explanation

### New Function: `math.isqrt()`

Returns the integer square root.

Example

```python
math.isqrt(20)
```

Output

```text
4
```

Unlike

```python
20 ** 0.5
```

which gives

```text
4.472135...
```

`isqrt()` returns only the integer part.

---

# Q82. Pow(x, n)

---

# A. Brute Force

## DSA Way

```python
class Solution:
    def myPow(self, x, n):

        ans = 1

        power = abs(n)

        for _ in range(power):
            ans *= x

        if n < 0:
            return 1 / ans

        return ans
```

---

## Dry Run

```text
2³

↓

1×2

↓

2×2

↓

4×2

↓

8
```

---

## Complexity

```text
Time  : O(n)

Space : O(1)
```

---

# B. Binary Exponentiation (Optimal)

## DSA Way

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

## Dry Run

```text
2¹⁰

↓

2⁵

↓

2²

↓

2¹

↓

2

↑

4

↑

32

↑

1024
```

---

## Complexity

```text
Time  : O(log n)

Space : O(log n)
```

---

## Pythonic Way ⭐

```python
def myPow(x, n):
    return x ** n
```

or

```python
def myPow(x, n):
    return pow(x, n)
```

---

## Pythonic Explanation

### `**`

Exponentiation operator.

```python
2 ** 5
```

↓

```text
32
```

---

### `pow()`

Built-in power function.

```python
pow(2,5)
```

↓

```text
32
```

Both also support negative powers.

Example

```python
2 ** -3
```

↓

```text
0.125
```

---

# Comparison

| Problem      | Brute Force         | Optimal               |
| ------------ | ------------------- | --------------------- |
| Count Primes | Check every number  | Sieve of Eratosthenes |
| Square Root  | Linear Search       | Binary Search         |
| Power        | O(n) Multiplication | Binary Exponentiation |

---

# Key Learnings

1. Sieve marks multiples of every prime as non-prime.
2. Start marking from `i²` because smaller multiples are already processed.
3. Binary Search can find the square root efficiently.
4. Binary Exponentiation reduces the exponent by half each recursion.
5. List Comprehensions provide a concise way to create lists.
6. `math.isqrt()` returns the integer square root directly.

---

# Interview Tips

## Sieve Pattern

```python
isPrime = [True] * (n + 1)
```

Mark multiples

```python
j = i * i

while j <= n:
    isPrime[j] = False
    j += i
```

---

## Binary Search Pattern

```python
while left <= right:

    mid = (left + right) // 2
```

Use whenever the search space is sorted or monotonic.

---

## Binary Exponentiation Pattern

```python
half = solve(x, n // 2)

if n % 2 == 0:
    return half * half

return half * half * x
```

---

# Python Functions / Concepts Learned Today

```python
math.isqrt()

List Comprehension

List Slicing

pow()

**

n ** 0.5
```
