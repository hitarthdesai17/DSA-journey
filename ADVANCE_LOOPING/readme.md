"""1. ISBN Number
Description: An ISBN (International Standard Book Number) is a unique 10-digit
number assigned to books. The ISBN is valid if the sum of its digits, each
multiplied by its position (1 to 10), is divisible by 11.
Example:
7 Input: 020131452
7 Output: Invalid ISBN
7 Explanation: The sum of the digits multiplied by their positions is not
divisible by 11V
7 Input: 0471958697
7 Output: Valid ISBN
7 Explanation: (0×1 + 4×2 + 7×3 + ... + 7×10) is divisible by 11.
Hint: Use a loop to multiply each digit by its respective position and check
divisibility by 11."""

Solution : 

"""2. HCF/GCD
Description: The Highest Common Factor (HCF) or Greatest Common Divisor
(GCD) of two numbers is the largest number that divides both numbers
without leaving a remainder.
Example:
7 Input: a = 12, b = 18,
7 Output: '
7 Explanation: Factors of 12: {1,2,3,4,6,12}, Factors of 18: {1,2,3,6,9,18}.
Common factors: {1,2,3,6}. The highest is 6.
Hint: Use the Euclidean algorithm: GCD(a, b) = GCD(b, a % b)."""

"""3. Harshad Number
Description: A number is a Harshad number if it is divisible by the sum of its
digits.
Example\
P Input: 18
P Output: Harshad Numbea
P Explanation: Sum of digits (1 + 8) = 9, and 18 is divisible by 9.
Hint: Extract digits using modulo (%) and integer division (//)."""

"""4. Perfect Square
Description: A number is a perfect square if it is the square of an integer.
Example\
P Input: 2X
P Output: Perfect SquarN
P Explanation: 5 × 5 = 25.
Hint: Use sqrt(N), check if it’s an integer."""

"""5. Abundant Number
Description: A number is abundant if the sum of its proper divisors is greater
than the number itself.
Example\
P Input: 1
P Output: Abundant Numbea
P Explanation: Proper divisors: 1, 2, 3, 4, 6 → Sum = 16 (greater than 12).
Hint: Use a loop to find proper divisors."""

"""6. Fibonacci Series using Loop
Description: Print Fibonacci series up to N terms using a loop.
Example/
b Input: N = (
b Output: 0, 1, 1, 2, 3, 5
Hint: Use a loop and store previous two numbers."""

"""7. Find Numbers with Exactly X Divisors (Java)
Description: Find numbers that have exactly X divisors.
Example/
b Input: X = O
b Output: 4, 9, 25, 4
b Explanation: These numbers have exactly three divisors.
Hint: Use prime factorization."""

"""8. Prime Factors in Java
Description: Find all prime factors of a number.
Example/
b Input: 3h
b Output: 2, 3, 5
Hint: Use division method."""

"""9. Calculate Area using Switch Statement
Description: Find the area of a circle, rectangle, or triangle using switch.
Example(
& Input: Choice = Circle, Radius = M
& Output: Area = 78.5
Hint: Use switch with case statements."""

"""10. Neon Number
Description: A number where the sum of digits of its square equals the
number itself.
Example(
& Input: 
& Output: Neon Numbe;
& Explanation: 92 = 81, sum of digits = 9.
Hint: Find square, sum digits, compare."""

"""11. Sum of Even Indexed Fibonacci Numbers
Description: Find the sum of Fibonacci numbers at even indices up to the 2Nth
Fibonacci number.
Example(
& Input: N = 
& Output: 33
Hint: Use a loop and maintain a sum for even-indexed elements."""

"""12. Find the Largest Digit in a Number
Description: Find the largest digit in a given number.
Example5
i Input: 5482.
i Output: 9
Hint: Extract digits using modulo (% 10) and compare."""

"""13. Find LCM of Two Numbers
Description: Find the Least Common Multiple (LCM) of two numbers.
Example5
i Input: a = 12, b = 1S
i Output: 60
Hint: LCM can be found using the formula: LCM(a, b) = (a × b) / GCD(a, b)."""

"""14. Find the Sum of Even Digits in a Number
Description: Find the sum of all even digits in a given number.
Example5
i Input: 2382
i Output: 14
Hint: Extract digits using % 10, check if even (digit % 2 == 0), add to sum."""

"""15. Number of Days in a Month
Description: Find the number of days in a given month and year (to handle leap
years).
Example
 Input: Month = 2, Year = 202
 Output: 29
Hint: Use conditions
 31 Days: Jan, Mar, May, Jul, Aug, Oct, Dec$
 30 Days: Apr, Jun, Sep, Nov$
 February: 28 or 29 (check for leap year using year % 4 == 0 but not year %
100 != 0 unless year % 400 == 0)."""