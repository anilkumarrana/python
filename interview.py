"""
Python Coding Interview Problems
---------------------------------
This file is a workspace for solving the following coding problems.

BASIC:
1. Reverse a String
2. Palindrome Check
3. Factorial of a Number
4. Find the Largest Element
5. FizzBuzz

INTERMEDIATE:
6. Two Sum Problem
7. Find Duplicates
8. Anagram Detection
9. Fibonacci Sequence (Memoization)
10. Merge Sorted Lists

ADVANCED:
11. Reverse a Linked List (In-place)
12. Valid Parentheses (Balanced Brackets)
13. Tree Traversal (BFS/DFS)
14. Longest Substring Without Repeating Characters
15. Knapsack Problem (DP)
"""

# START CODING HERE

def reverse_string(s: str) -> str:
    # TODO: Implement without using slicing or reversed()
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def is_palindrome(s: str) -> bool:
    # TODO: Implement palindrome check
    s_cleaned = "".join([char.lower() for char in s if char.isalnum()])
    reversed_s = s_cleaned[::-1]
    return s_cleaned == reversed_s

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def find_largest(nums: list) -> int:
    if not nums:
        raise ValueError("List is empty")
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)