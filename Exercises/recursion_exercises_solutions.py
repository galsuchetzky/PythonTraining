# Write a recursive function to calculate the nth Fibonacci number.

"""
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers. The
sequence starts with 0 and 1, so the 0th Fibonacci number is 0 and the 1st Fibonacci number is 1.
A recursive solution to calculate the nth Fibonacci number is as follows below. This function uses recursion to
calculate the nth Fibonacci number. If n is 0 or 1, the function returns the appropriate value. Otherwise,
it calls itself twice with n-1 and n-2 as arguments and adds the results.
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Write a recursive function to calculate the sum of the digits in a number.

"""
To calculate the sum of the digits in a number, we can use recursion to add the last digit to the sum of the digits 
in the rest of the number. This function uses the modulo operator to get the last digit of the number, adds it to 
the sum of the digits in the rest of the number (which is calculated by integer dividing the number by 10), 
and returns the result.
"""


def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


# Write a recursive function to calculate the sum of the first n natural numbers.

"""
The sum of the first n natural numbers can be calculated using a recursive formula that adds n to the sum of the 
first n-1 natural numbers. This function checks if n is equal to 1. If it is, it returns 1. Otherwise, it adds n to 
the sum of the first n-1 natural numbers (which is calculated by calling itself with n-1 as the argument) and 
returns the result.
"""


def sum_naturals(n):
    if n == 1:
        return 1
    else:
        return n + sum_naturals(n - 1)


# Write a recursive function to calculate the factorial of a number.

"""
The factorial of a number is the product of all positive integers up to and including that number. This function 
checks if n is equal to 0. If it is, it returns 1 (since 0! is defined as 1). Otherwise, it multiplies n by the 
factorial of n-1 (which is calculated by calling itself with n-1 as the argument) and returns the result.
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Write a recursive function to find the GCD (Greatest Ccommon Divisor) of two numbers.

"""
The greatest common divisor (GCD) of two numbers is the largest positive integer that divides both numbers without a 
remainder. A recursive solution to find the GCD of two numbers is as follows below. This function checks if b is 
equal to 0. If it is, it returns a (since a is the GCD of a and 0). Otherwise, it calls itself with b as the first 
argument and a % b as the second argument. This calculates the remainder of a divided by b and recursively calls the 
function with b and the remainder as the arguments, until b is equal to 0 (which means that a is the GCD).
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Write a recursive function to reverse a string.

"""
To reverse a string, we can use recursion to swap the first and last characters of the string and reverse the 
remaining substring. This function checks if the length of the string is 0. If it is, it returns the empty string. 
Otherwise, it concatenates the last character of the string with the result of calling itself with the string minus 
the last character as the argument, effectively reversing the string.
"""


def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


# Write a recursive function to find the length of a linked list.

"""
A linked list is a data structure in which each node points to the next node in the list. To find the length of a 
linked list using recursion, we can traverse the list by following the next pointers until we reach the end of the 
list. This function checks if the head of the linked list is None. If it is, it returns 0 (since the length of an 
empty list is 0). Otherwise, it adds 1 to the length of the rest of the list (which is calculated by calling itself 
with the next node as the argument) and returns the result.  
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def list_length(head):
    if head is None:
        return 0
    else:
        return 1 + list_length(head.next)


# Write a recursive function to find the maximum element in an array.

"""
To find the maximum element in an array using recursion, we can compare the first element of the array to the 
maximum element in the rest of the array. This function checks if the length of the array is 1. If it is, it returns 
the first (and only) element of the array. Otherwise, it compares the first element of the array to the maximum 
element in the rest of the array (which is calculated by calling itself with the slice of the array from the second 
element to the end as the argument) and returns the larger value.
"""


def max_element(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], max_element(arr[1:]))


# Write a recursive function to calculate the power of a number.

"""
The power of a number is the product of multiplying a number by itself a certain number of times. This function 
checks if exponent is equal to 0. If it is, it returns 1 (since any number to the power of 0 is 1). Otherwise, 
it multiplies the base by the power of the base to the exponent-1 (which is calculated by calling itself with the 
base and exponent-1 as the arguments) and returns the result.
"""


def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


# Write a recursive function to check if a string is a palindrome.

"""
A palindrome is a string that reads the same forwards and backwards. To check if a string is a palindrome using 
recursion, we can compare the first and last characters of the string and recursively check if the remaining 
substring is also a palindrome. This function checks if the length of the string is less than 2. If it is, 
it returns True (since any single-character string is a palindrome). If the first and last characters of the string 
are not equal, it returns False (since the string is not a palindrome). Otherwise, it calls itself with the 
substring from the second character to the second-to-last character as the argument and returns the result.
"""


def is_palindrome(s):
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
