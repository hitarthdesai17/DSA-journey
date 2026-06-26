# DAY 56 - STACK MEMORY & RECURSION IN PYTHON

# Stack Memory

## Definition

Stack is a **Linear Data Structure** that follows the **LIFO (Last In, First Out)** principle.

The last element inserted is the first one removed.

---

## What is Stored in Stack?

Python Stack stores:

* Function Calls (Call Stack)
* Local Variables
* Function Parameters

Unlike JavaScript, Python objects are generally created on the heap, while references and function frames are managed on the call stack.

---

# Call Stack

## Definition

The **Call Stack** keeps track of all active function calls.

Whenever a function is called,

* It is **Pushed** onto the stack.
* After the function finishes,
* It is **Popped** from the stack.

---

## Example

```python
def greet():
    print("Hello")

greet()
```

Call Stack

```text
Start

main()

↓

greet()

↓

print()

↓

print() finishes

↓

greet() finishes

↓

main() finishes
```

Output

```text
Hello
```

---

# Primitive Variables

Example

```python
a = 10
b = a

a = 20

print(a)
print(b)
```

Output

```text
20
10
```

## Explanation

Python integers are immutable.

When

```python
b = a
```

the value of `a` is assigned to `b`.

Changing `a` later does **not** change `b`.

---

# Recursion

## Definition

Recursion is a technique where a function **calls itself** to solve a smaller version of the same problem.

Every recursive call is pushed onto the **Call Stack**.

---

## Two Important Parts

### 1. Base Case

Stops the recursion.

Without a base case,

the function will call itself forever until a **RecursionError** occurs.

---

### 2. Recursive Call

Calls the same function with a smaller problem.

---

# Q73. Print "Hello World" N Times

## DSA Way

```python
def printHello(n):

    if n == 0:
        return

    print("Hello World")

    printHello(n-1)


printHello(5)
```

---

## Dry Run

Input

```text
5
```

Call Stack

```text
printHello(5)

↓

Hello World

↓

printHello(4)

↓

Hello World

↓

printHello(3)

↓

Hello World

↓

printHello(2)

↓

Hello World

↓

printHello(1)

↓

Hello World

↓

printHello(0)

↓

Return
```

Output

```text
Hello World
Hello World
Hello World
Hello World
Hello World
```

---

## Complexity

```text
Time  : O(n)

Space : O(n)
```

Space is **O(n)** because every recursive call occupies one stack frame.

---

## Pythonic Way ⭐

```python
def printHello(n):

    for _ in range(n):
        print("Hello World")
```

---

## Pythonic Explanation

### New Feature: `_`

```python
for _ in range(5):
    print("Hello")
```

The variable `_` means:

> "I don't need this variable."

Instead of

```python
for i in range(5):
```

we write

```python
for _ in range(5):
```

because `i` is never used.

This is a Python convention.

---

### New Function: `range()`

```python
range(5)
```

Produces

```text
0
1
2
3
4
```

The loop runs **5 times**.

---

# Q74. Print N to 1 Using Recursion

## DSA Way

```python
def printNumbers(n):

    if n == 0:
        return

    print(n)

    printNumbers(n-1)


printNumbers(5)
```

---

## Dry Run

```text
printNumbers(5)

↓

Print 5

↓

printNumbers(4)

↓

Print 4

↓

printNumbers(3)

↓

Print 3

↓

printNumbers(2)

↓

Print 2

↓

printNumbers(1)

↓

Print 1

↓

printNumbers(0)

↓

Return
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

## Complexity

```text
Time  : O(n)

Space : O(n)
```

---

## Pythonic Way ⭐

```python
def printNumbers(n):

    print(*range(n,0,-1), sep="\n")
```

---

## Pythonic Explanation

### New Feature: `range(start, stop, step)`

Earlier you learned

```python
range(5)
```

Now

```python
range(n,0,-1)
```

means

```text
Start = n

Stop before 0

Step = -1
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

### New Feature: `*` (Unpacking Operator)

```python
numbers = [1,2,3]

print(*numbers)
```

Output

```text
1 2 3
```

Without `*`

```python
print(numbers)
```

Output

```text
[1, 2, 3]
```

The `*` operator **unpacks** the list into separate values.

---

### New Parameter: `sep`

Normally

```python
print(1,2,3)
```

Output

```text
1 2 3
```

because the default separator is a space.

If we write

```python
print(1,2,3, sep="\n")
```

Output

```text
1
2
3
```

Every value is printed on a new line.

---

# Recursion vs Loop

| Loop                         | Recursion                                         |
| ---------------------------- | ------------------------------------------------- |
| Uses iteration               | Function calls itself                             |
| Uses less memory             | Uses Call Stack                                   |
| Faster                       | Slightly slower                                   |
| Easier for simple repetition | Better for recursive problems like Trees & Graphs |

---

# Key Learnings

1. Stack follows **LIFO**.
2. Every function call is stored in the **Call Stack**.
3. Every recursive call creates a new stack frame.
4. A recursive function must always have a **Base Case**.
5. `range(start, stop, step)` allows forward and backward iteration.
6. `_` is used when a loop variable is not needed.
7. `*` unpacks a list into separate arguments.
8. `sep="\n"` prints each argument on a new line.

---

# Interview Tips

## Recursion Pattern

```python
def recursion(n):

    if base_case:
        return

    # Work

    recursion(smaller_problem)
```

Always identify:

* Base Case
* Recursive Call
* Smaller Problem

---

# Python Functions / Concepts Learned Today

```python
range()

range(start, stop, step)

_

*

sep

Recursion

Call Stack
```
