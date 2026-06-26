# DAY 60 - RECURSION (PART 2)

# Q74. Print Numbers 1 to N and N to 1 using Recursion

## A. Print 1 to N

### DSA Way

```python
class Solution:
    def print1ToN(self, n):

        if n == 0:
            return

        self.print1ToN(n - 1)

        print(n)
```

---

### Dry Run

Input

```text
n = 5
```

Call Stack

```text
print1ToN(5)

↓

print1ToN(4)

↓

print1ToN(3)

↓

print1ToN(2)

↓

print1ToN(1)

↓

print1ToN(0)

↓

Return

↓

Print 1

↓

Print 2

↓

Print 3

↓

Print 4

↓

Print 5
```

Output

```text
1
2
3
4
5
```

---

### Complexity

```text
Time  : O(n)

Space : O(n)
```

---

### Pythonic Way ⭐

```python
def print1ToN(n):
    print(*range(1, n + 1), sep="\n")
```

---

### Pythonic Explanation

### `range(1, n+1)`

Creates numbers starting from **1** up to **n**.

Example

```python
range(1,6)
```

Produces

```text
1 2 3 4 5
```

---

### `*`

Unpacks all values.

Without

```python
print(range(1,6))
```

Output

```text
range(1, 6)
```

With

```python
print(*range(1,6))
```

Output

```text
1 2 3 4 5
```

---

### `sep="\n"`

Changes separator from space to newline.

---

# B. Print N to 1

## DSA Way

```python
class Solution:
    def printNTo1(self, n):

        if n == 0:
            return

        print(n)

        self.printNTo1(n - 1)
```

---

### Dry Run

```text
Print 5

↓

Print 4

↓

Print 3

↓

Print 2

↓

Print 1
```

Output

```text
5
4
3
2
1
```

---

### Complexity

```text
Time  : O(n)

Space : O(n)
```

---

### Pythonic Way ⭐

```python
def printNTo1(n):
    print(*range(n, 0, -1), sep="\n")
```

---

### Pythonic Explanation

```python
range(start, stop, step)
```

Example

```python
range(5,0,-1)
```

Produces

```text
5
4
3
2
1
```

---

# Algorithm

### Print 1 → N

```text
Base Case

↓

Move Down

↓

Print while Returning
```

---

### Print N → 1

```text
Base Case

↓

Print

↓

Move Down
```

---

# Q75. Sum of First N Numbers

## DSA Way

```python
class Solution:
    def sumN(self, n):

        if n == 0:
            return 0

        return n + self.sumN(n - 1)
```

---

### Dry Run

```text
sumN(5)

↓

5 + sumN(4)

↓

5 + 4 + sumN(3)

↓

5 + 4 + 3 + sumN(2)

↓

5 + 4 + 3 + 2 + sumN(1)

↓

5 + 4 + 3 + 2 + 1 + sumN(0)

↓

15
```

---

### Complexity

```text
Time  : O(n)

Space : O(n)
```

---

### Pythonic Way ⭐

```python
def sumN(n):
    return sum(range(1, n + 1))
```

---

### Pythonic Explanation

### New Function: `sum()`

Adds all values in an iterable.

Example

```python
sum([1,2,3,4])
```

Output

```text
10
```

---

### Combined

```python
sum(range(1,n+1))
```

Example

```python
sum(range(1,6))
```

becomes

```text
1+2+3+4+5

↓

15
```

---

# Q75. Factorial

## DSA Way

```python
class Solution:
    def factorial(self, n):

        if n == 0:
            return 1

        return n * self.factorial(n - 1)
```

---

### Dry Run

```text
factorial(5)

↓

5 × factorial(4)

↓

5 × 4 × factorial(3)

↓

5 × 4 × 3 × factorial(2)

↓

5 × 4 × 3 × 2 × factorial(1)

↓

5 × 4 × 3 × 2 × 1

↓

120
```

---

### Complexity

```text
Time  : O(n)

Space : O(n)
```

---

### Pythonic Way ⭐

```python
import math

def factorial(n):
    return math.factorial(n)
```

---

### Pythonic Explanation

### New Library: `math`

Python provides a built-in **math** library.

```python
import math
```

imports it.

---

### New Function: `math.factorial()`

Returns factorial directly.

Example

```python
math.factorial(5)
```

Output

```text
120
```

---

# Q76. Fibonacci Series

## A. Print First N Terms

### DSA Way

```python
class Solution:
    def fibonacciSeries(self, n, a=0, b=1):

        if n == 0:
            return

        print(a)

        self.fibonacciSeries(n-1, b, a+b)
```

---

### Dry Run

Input

```text
5
```

Output

```text
0
1
1
2
3
```

---

### Complexity

```text
Time  : O(n)

Space : O(n)
```

---

### Pythonic Way ⭐

```python
def fibonacciSeries(n):

    a, b = 0, 1

    for _ in range(n):
        print(a)
        a, b = b, a + b
```

---

### Pythonic Explanation

### Tuple Assignment

```python
a, b = b, a+b
```

Python first creates

```text
(new_b, new_a+b)
```

then assigns both together.

Example

```text
a=2

b=3

↓

a,b=b,a+b

↓

a=3

b=5
```

No temporary variable is required.

---

# B. Find nth Fibonacci Number

## DSA Way

```python
class Solution:
    def fibonacciNth(self, n):

        if n == 0:
            return 0

        if n == 1:
            return 1

        return self.fibonacciNth(n-1) + self.fibonacciNth(n-2)
```

---

### Dry Run

```text
fib(5)

↓

fib(4)+fib(3)

↓

3+2

↓

5
```

Output

```text
5
```

---

### Complexity

```text
Time  : O(2ⁿ)

Space : O(n)
```

---

### Pythonic Way ⭐

```python
def fibonacciNth(n):

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a+b

    return a
```

---

### Pythonic Explanation

Each iteration moves to the next Fibonacci number.

Example

```text
a=0
b=1

↓

1 1

↓

1 2

↓

2 3

↓

3 5

↓

5 8
```

After `n` iterations,

`a` stores the **nth Fibonacci number**.

---

# Key Learnings

1. Printing before recursion gives **N → 1**.
2. Printing after recursion gives **1 → N**.
3. Every recursive function needs a **Base Case**.
4. Sum and Factorial are classic recursion problems.
5. Fibonacci recursion has overlapping subproblems.
6. Iterative Fibonacci is much faster than recursive Fibonacci.
7. `sum()` quickly adds iterable elements.
8. `math.factorial()` is the built-in factorial function.
9. Tuple assignment (`a, b = b, a+b`) is the preferred Python way to update multiple variables.

---

# Interview Tips

## Recursion Template

```python
if base_case:
    return

# Work

return recursive_call(smaller_problem)
```

Always identify:

* Base Case
* Recursive Call
* Smaller Problem

---

# Python Functions / Concepts Learned Today

```python
sum()

math.factorial()

range(start, stop, step)

Tuple Assignment

a, b = b, a+b
```