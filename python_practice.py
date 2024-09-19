"""
This module demonstrates various control structures in Python.

Control Structures:
1. Conditional Statements:
    - if, elif, else: Used to execute code based on conditions.
2. Loops:
    - for: Iterates over a sequence (like a list, tuple, dictionary, set, or string).
    - while: Repeats a block of code as long as a condition is true.
3. Loop Control Statements:
    - break: Exits the loop prematurely.
    - continue: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
    - pass: Does nothing; acts as a placeholder.
4. Exception Handling:
    - try, except, finally: Used to handle exceptions (errors) in the code.
"""

#######               Python if statment          ###########

# The 'if' statement is used for conditional execution.
# It allows the program to execute certain code only if a specified condition is true.
# Syntax:
# if condition:
#     # code to execute if condition is true
#
# Example:
# if x > 0:
#     print("x is positive")
#
# In this example, the print statement will only execute if the variable 'x' is greater than 0.

# Ternaryt operator
# Syntax:
age = input("Enter your age: ")
price = 10 if int(age) < 18 else 20
print(price)


# i want to learn about for loop in python
# The 'for' loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
# Syntax:
# for variable in sequence:
#     # code to execute for each item in the sequence

# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Iterating over a string
for letter in "Python":
    print(letter)

# Example 3: Using range() to generate a sequence of numbers
for i in range(5):
    print(i)

# Example 4: Iterating over a dictionary
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
for student, grade in student_grades.items():
    print(f"{student}: {grade}")
    


