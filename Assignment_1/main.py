# ASSIGNMENT 1 (Python)
# Variables & Data Types (Q1–Q10)

# Q# 1. Create a variable `student_name`, assign your name, and print its type.
# declare a variable
student_name = "Waqar Ali"
# its type 
print("Type of student_name: ",type(student_name)) # <class 'str'>

print("***********************************************")

# Q:2 Store your age in a variable. Multiply it by 2 and print the result.
# declare a age variable
my_age = 18
# multiply by 2
my_age *=2
# print its value
print(my_age)
# print("Double age is:", my_age * 2)


print("***********************************************")

# Q:3. Create three variables with an integer, a string, and a float. Print their types.

# declare three variables
num = 22
# a string
string_name = "Khan"
# A float
float_num = 22.2

# Printing their types
print("The type of ",num ," is ",type(num))
print("The type of ",string_name ," is ",type(string_name))
print("The type of ",float_num ," is ",type(float_num))

# print("Type of num:", type(num))
# print("Type of string_name:", type(string_name))
# print("Type of float_num:", type(float_num))

print("***********************************************")

# Q:4. Convert the integer `55` to a string and concatenate with " is a number".
# coverting '55'

coverted_num  = 55
# Concatenation and converting number to string
result = str(coverted_num) + " is a number."
print(result)

print("***********************************************")

# Q:5.Input two numbers, print their sum and the type of the result. 
# Getting two numbers as input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Sum of two numbers
result = num1 + num2
# printing sum of two numbers and its type 
print(f"The sum of {num1} and {num2} is",result,"\ntype of result is " ,type(result))
# print(f"The sum of {num1} and {num2} is {result}")
# print("Type of result:", type(result))

print("***********************************************")

# Q:6. Assign `a = "5"` (string) and `b = 3`. Add them correctly and explain the result.

# Assigning values 
a = "5"   # a is a string
b = 3     # b is an integer
# Convert 'a' to integer before adding
result = int(a) + b
print(f"The sum of {a} + {b} is ",result)



print("***********************************************")
# Q:7. Swap values of two variables without a third variable.
# Declare a variable
x = 10
y = 20
print(f"Before the swapping: the value of x is {x} and the value of y is {y}")
# Swap them without using third variable
x,y = y, x
# print them 
print(f"After the swapping: the value of x is {x} and the value of y is {y}")


print("***********************************************")
# Q:8. What is the type and output of: `result = 3 + 4.0 + True`? 
result = 3 + 4.0 + True #The output 8.0
print("The answer of this (3 + 4.0 + True) expression is ",result)
print("Type of result:", type(result))         # float

print("***********************************************")

# Q:9.Input a float number and print if it’s an integer (without using `int()`).
"""
To check if a float number is an integer without using int(), you can use the .is_integer() method in Python.
.is_integer() → Returns True if the float has no decimal part (like 5.0).
"""

user_input = float(input("Enter a float number: "))
if user_input.is_integer():
    print("It is an integer")
else:
    print("It is not an integer")


print("***********************************************")
# Q:10. Use `isinstance()` to check whether an input is float or integer.
# eval() automatically converts the input to its correct type (like int, float, etc.).

nums = eval(input("enter a number: "))
if isinstance(nums, int):
    print("It's an integer.")
elif isinstance(nums, float):
    print("It's a float.")
else:
    print("It's something else.")



"""



 Variables & Data Types – Key Points
Store values in memory.

No type declaration needed.

Common types: int, float, str, bool.

Use type() to check type.

Strings use quotes: "text".

Numbers support +, -, *, /, etc.

input() gets user input.

Use int(), float() to convert.

Boolean: True / False.

None means no value.
"""