# Conditions (if/elif/else) (Q11–Q20)

# Q:11. Check if a number is positive, negative, or zero.
user_input = float(input("Enter a number: "))
if user_input > 0:
    print("The number is positive")
elif user_input < 0:
    print("The number is negative")
else:
    print("The number is zero")


print("********************************************")
# Q:12. Input marks; print "Passed" if ≥50, else "Failed".
marks = float(input("Enter your marks: "))
if marks >= 50:
    print("Passed")
else:
    print("Failed")


print("********************************************")
# Q:13. Find the largest of three numbers using if/elif/else.
num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))
num3 = float(input("Enter the third number :"))

# largest = max(num1, num2, num3)
# print("The largest number is", largest)
# Or 

if num1 >= num2 and num1 >= num3:
    print("The largest number is", num1)
elif num2 >= num1 and num2>= num3:
    print("The largest number is", num2)
else:
    print("The largest number is", num3)


print("********************************************")


# Q:14. Input age. Print: Child (age <13), Teen (13–19), Adult (20+).
user_age = float(input("Enter you age: "))
if user_age < 13:
    print("Child")
elif  13 <= user_age <= 19:
    print("Teen")
else:
    print("adult")

    

print("********************************************")
# Q:15. Check whether a number is even or odd using `%`.
num_checking = int(input("Enter a number: "))
if num_checking % 2 == 0:
    print(f"The {num_checking} is even.")
else:
    print(f"The {num_checking} is odd")


print("********************************************")
# Q:16. Input two subjects' marks. Print: “Both Passed”, “One Passed”, or “None Passed”.
sub1 = float(input("Enter marks of subject1: "))
sub2 = float(input("Enter marks of subject2: "))
if sub1 >= 50 and sub2 >= 50:
    print("Both passed")
elif sub1 >= 50 or sub2 >= 50:
    print("One Passed")
else:
    print("None Passed")

# or other way
# if sub1 > 50 and sub2 > 50:
#     print("Both Passed")
# elif (sub1 > 50 and sub2 <= 50) or (sub1 <= 50 and sub2 > 50):
#     print("One Passed")
# else:
#     print("None Passed")



"""
There are 3 types of triangles based on side lengths:

Triangle Type	Condition
Equilateral	All three sides are equal (a == b == c)
Isosceles	Exactly two sides are equal (a == b or b == c or a == c)
Scalene	All three sides are different (a != b != c)
"""
print("********************************************")

# Q:17. Classify a triangle as Equilateral, Isosceles, or Scalene using its sides.
a = float(input("Enter length of side A: "))
b = float(input("Enter length of side B: "))
c = float(input("Enter length of side C: "))
if a == b == c:
    print("The triangle is Equilateral")
elif a == b or b == c or a == c:
    print("The triangle is Isosceles")
else:
    print("The triangle is Scalene")

"""
a == b == c: All sides are equal → Equilateral

a == b or b == c or a == c: Only two sides are equal → Isosceles

Else: No sides are equal → Scalene

Input (a, b, c)	Output
5, 5, 5	Equilateral
6, 6, 4	Isosceles
3, 4, 5	Scalene

"""


print("********************************************")
# Q:18. Input a number. Print "Fizz" if divisible by 3, "Buzz" if 5, "FizzBuzz" if both.

# Take user input and convert it to an integer
user_input_check = int(input("Enter a number: "))

# First condition: divisible by both 3 and 5
if user_input_check % 3 == 0 and user_input_check % 5 == 0:
    print("FizzBuzz")

# Second: divisible only by 3
elif user_input_check % 3 == 0:
    print("Fizz")

# Third: divisible only by 5
elif user_input_check % 5 == 0:
    print("Buzz")

# If none of the above conditions are true
else:
    print("Not divisible by 3 or 5")


print("********************************************")
# Q:19. Input temperature. Print: Freezing (<0), Cold (0–15), Moderate (16–30), Hot (>30).

# Ask the user to enter temperature and convert to float (to allow decimal values)
temp = float(input("Enter the temperature: "))

if temp < 0:
    print("Freezing")
elif 0 <= temp  <= 15:
    print("Cold")
elif 16 <= temp <= 30:
    print("Moderate")
elif temp > 30:
    print("Hot")
else:
    print("Out of tolerance!")

# Q:20. Validate username and password: Username ≥5 chars, Password has 1 digit and 1 special char.
user_name = input("Enter your username: ")
user_password = input("Enter your password: ")

# Check username length
if len(user_name) >= 5:  # Username should be 5 or more characters
    # Now check password conditions
    has_digit = any(char.isdigit() for char in user_password)
     # True if any character is a digit
    has_special = any(not char.isalnum() for char in user_password)
    # True if any character is NOT a letter or digit → i.e., special character

    if has_digit and has_special: # Both conditions true?
        print("Login successful")
    else:
        print("Password must contain at least 1 digit and 1 special character.")
else:
    print("Username must be at least 5 characters long.")



"""
if = check something

else = if not

elif = else if (extra check)

== = equals

!= = not equal

> = greater than

< = less than

>= = greater or equal

<= = less or equal

and = both true

or = one true

not = opposite

Must use **:** after if`

Indent block after if

Works with bool: True / False

Can put if inside if (nested)

No curly braces in Python

Can compare strings too

if "a" in "apple": → True

Conditions = brain of your code 🧠
"""