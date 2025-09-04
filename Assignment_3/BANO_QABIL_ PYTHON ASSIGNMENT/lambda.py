# Section G: Lambda Functions (Real-Life + Interview Qs)

#Q:71. Lambda to check even/odd.

# 1. Basic Lambda for Even/Odd
# Lambda function to check if a number is even or odd
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd" # % is modulo ope
print(check_even_odd(10))  # Test with 10 → Output: Even
print(check_even_odd(7))   # Test with 7 → Output: Odd


print("***************************************************")

#2. Lambda inside map() for a list
# numbers = [1, 2, 3, 4, 5, 6]  # list of numbers

# # Using lamda + map to get even/odd for each number in list
# result = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", numbers))
# print(result)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']


#3. Lambda inside filter() (filter even numbers only)
# numbers = [1, 2, 3, 4, 5, 6, 7]

# # Using lambda + filter to get only even numbers
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  #Output: [2, 4, 6]


# #4. Lambda inside filter() (filter odd numbers only)
# numbers = [1, 2, 3, 4, 5, 6]

# # Using lambda + filter to get only odd numbers
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))  
# print(odd_numbers)  # Output: [1, 3, 5]


#5.Lambda with reduce() (count even and odd numbers)
# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6]

# # Using lambda + reduce to count even numbers
# even_count = reduce(lambda acc, x: acc + (x % 2 == 0), numbers, 0)  
# print(even_count)  # Output: 3



#6. Lambda inside a dictionary (classic trick)
# check = {
#     0: lambda: "Even", # Key 0 -> Even
#     1: lambda: "Odd" # Key 1 -> Odd
# }

# num  = 15
# print(check[num % 2]())   # Output: Odd


#7. Inline lambda without variable (direct call)
# print((lambda x: "Even" if x % 2 == 0 else "Odd")(22))  # Output: Even



# Q:72. Lambda with map() → double numbers.
# 1. Basic Lambda with map() to double numbers

numbers = [1, 2, 3, 4, 5]  # List of numbers to double

# Using Lambda with map to double each number
doubled_numbers = list(map(lambda x: x * 2, numbers))
# map(lambda x: x*2, numbers) → applies lambda to each element in numbers
# lambda x: x*2 → anonymous function, multiplies x by 2
# list() → converts map object to list for readable output

print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]


print("***************************************************")



#2. Inline Lambda with map() without assigning to a variable
# numbers = [10, 20, 30]

# # Directly printing doubled numbers using map and lambda
# print(list(map(lambda x: x * 2, numbers)))  
# # list(map(...)) → converts map object to list
# # lambda x: x*2 → doubles each element in numbers


#3.Using map() with a separate lambda variable
# numbers = [5, 10, 15]

# # Define lambda separately
# double = lambda x: x * 2  # lambda x: x*2 → doubles input x

# # Apply map() with lambda variable
# doubled_numbers = list(map(double, numbers))  
# # map(double, numbers) → applies double lambda to each element in numbers
# print(doubled_numbers)  # Output: [10, 20, 30]


#4.Using map() with lambda + additional operations
# numbers = [1, 2, 3, 4]

# # Double numbers and add 1 using lambda
# double_plus_one = list(map(lambda x: x * 2 + 1, numbers))
# # x*2 + 1 → doubles and then adds 1
# print(double_plus_one)  # Output: [3, 5, 7, 9]

#5.Lambda with map() and user input numbers
# Taking multiple numbers as input
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# # input() → takes input from user as string
# # .split() → splits string into list of strings
# # map(int, ...) → converts each string to integer
# # list() → converts map object to list

# # Doubling numbers
# doubled_numbers = list(map(lambda x: x * 2, numbers))
# print("Doubled numbers:", doubled_numbers)


#6.Using map() with lambda + filter() (double only even numbers)
# numbers = [1, 2, 3, 4, 5, 6]

# # First filter even numbers, then double using lambda
# doubled_even_numbers = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
# # filter(lambda x: x%2==0, numbers) → keeps only even numbers
# # map(lambda x: x*2, ...) → doubles each even number
# print(doubled_even_numbers)  # Output: [4, 8, 12]



#7.Using dictionary + lambda + map() trick
# numbers = [1, 2, 3]

# # Using dictionary to choose operation
# operations = {
#     "double": lambda x: x * 2,
#     "triple": lambda x: x * 3
# }

# # Apply map with selected operation
# doubled_numbers = list(map(operations["double"], numbers))
# print(doubled_numbers)  # Output: [2, 4, 6]






# Q:73. Lambda with filter() → select emails ending with `.edu`.
# 1. Basic Lambda + filter() for .edu emails
# List of email addresses
emails = ["john@gmail.com", "alice@university.edu", "bob@college.edu", "jane@yahoo.com"]

# Using filter() with lambda to select emails ending with '.edu'
edu_emails = list(filter(lambda x: x.endswith(".edu"), emails))
# filter(lambda x: x.endswith(".edu"), emails) → keeps only emails where lambda returns True
# lambda x: x.endswith(".edu") → anonymous function, checks if string ends with '.edu'
# list() → converts filter object to list for readable output

print(edu_emails)  # Output: ['alice@university.edu', 'bob@college.edu']
print("***************************************************")



#2.Inline Lambda + filter() without variable
# emails = ["prof@mit.edu", "student@gmail.com", "teacher@harvard.edu"]

# # Directly printing filtered .edu emails
# print(list(filter(lambda x: x.endswith(".edu"), emails)))
# list(filter(...)) → converts filter object to list
# lambda x: x.endswith(".edu") → checks for '.edu' ending




# #3.Lambda variable + filter()
# emails = ["sam@stanford.edu", "tom@gmail.com", "lisa@oxford.edu"]

# # Define lambda separately
# is_edu = lambda email: email.endswith(".edu")  # lambda email: email.endswith(".edu") → returns True if email ends with '.edu'

# # Apply filter with lambda variable
# edu_emails = list(filter(is_edu, emails))  
# print(edu_emails)  # Output: ['sam@stanford.edu', 'lisa@oxford.edu']


#4.Using filter() + map() → get usernames of .edu emails
# emails = ["alice@mit.edu", "bob@gmail.com", "carol@harvard.edu"]

# # Filter .edu emails, then extract usernames (before @)
# usernames = list(map(lambda x: x.split("@")[0], filter(lambda x: x.endswith(".edu"), emails)))  
# # filter(lambda x: x.endswith(".edu"), emails) → keeps only .edu emails
# # map(lambda x: x.split("@")[0], ...) → splits email by '@' and takes first part (username)
# print(usernames)  # Output: ['alice', 'carol']



#5.Using list comprehension + lambda (alternate)
# emails = ["john@princeton.edu", "kate@gmail.com", "mike@yale.edu"]

# # List comprehension with lambda for filtering .edu emails
# edu_emails = [email for email in emails if (lambda x: x.endswith(".edu"))(email)]  
# # (lambda x: x.endswith(".edu"))(email) → calls lambda for each email
# print(edu_emails)  # Output: ['john@princeton.edu', 'mike@yale.edu']



#6.User input + filter() + lambda
# Take emails as input separated by space
# emails = input("Enter emails separated by space: ").split()  
# # input() → takes string input
# # .split() → splits string into list

# # Filter emails ending with '.edu'
# edu_emails = list(filter(lambda x: x.endswith(".edu"), emails))  
# print("Emails ending with .edu:", edu_emails)



# #7. Dictionary trick + filter() (check type of domain)
# emails = ["anna@mit.edu", "peter@gmail.com", "lucas@harvard.edu"]

# # Define domain check functions in dictionary
# check_domain = {
#     "edu": lambda x: x.endswith(".edu"),
#     "com": lambda x: x.endswith(".com")
# }

# # Filter only .edu emails
# edu_emails = list(filter(check_domain["edu"], emails))  
# print(edu_emails)  # Output: ['anna@mit.edu', 'lucas@harvard.edu']





# Q:74. Lambda with reduce() → product of list

#1. Basic Lambda + reduce() for product
from functools import reduce  # Import reduce function from functools module

numbers = [1, 2, 3, 4, 5]  # List of numbers whose product we want

# Using reduce() with lambda to calculate product

product = reduce(lambda x, y: x * y, numbers)
# lambda x, y: x*y → anonymous function multiplies two numbers
# reduce(lambda x, y: x*y, numbers) → applies lambda cumulatively to the list
# Step: (((1*2)*3)*4)*5 → final product

print(product)  # Output: 120
print("***************************************************")






#2.Lambda variable + reduce()
# numbers = [2, 3, 4]

# # lambda separately
# multiply = lambda a, b: a * b # a*b -> multiplies two numbers

# # Use reduce with Lambda variable
# product = reduce(multiply, numbers)
# print(product)  # Output: 24


# 3.Inline reduce() + lambda without variable
# numbers = [5, 6, 2]

# # Directly calculate product using reduce and inline lambda
# print(reduce(lambda x, y: x * y, numbers)) # output: 60



#4.Reduce() + lambda + starting value (optional)
# numbers = [1, 2, 3, 4]

# # Provide initial value 1
# product = reduce(lambda x, y: x * y, numbers, 1)
# # Third argument (1) → initial value of accumulator

# print(product)  #output: 24



# 5.Product of numbers using user input + reduce() + lambda

# ke numbers from user separated by space
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# # input() → string input
# # .split() → splits into list of strings
# # map(int, ...) → converts each string to integer
# # list() → converts map object to list

# # Calculate product
# product = reduce(lambda x, y: x * y, numbers)
# print("Product:", product)



# 6.Reduce() + lambda + filter() → product of only even numbers
# numbers = [1, 2, 3, 4, 5, 6]

# # Filter even numbers and then multiply
# even_product = reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 0, numbers))  
# # filter(lambda x: x%2==0, numbers) → keeps only even numbers
# # reduce(lambda x,y: x*y, ...) → multiplies all filtered numbers
# print(even_product)  # Output: 48 (2*4*6)


#7.Dictionary + lambda + reduce() trick (choose operation)
# numbers = [1, 2, 3, 4]

# # Dictionary to select operation
# operations = {
#     "product": lambda x, y: x * y,
#     "sum": lambda x, y: x + y
# }

# # Use reduce with dictionary operation
# product = reduce(operations["product"], numbers)
# print(product)  # Output: 24







# Q:75. Lambda to extract first character of each word.
# Using map() with lambda (basic way)

words = ["Python", "Lambda", "Function", "Map"]  # List of words

# Using map() with lambda to get first character of each word
first_chars = list(map(lambda x: x[0], words))
# lambda x: x[0] → anonymous function that takes first character of x
# map(lambda x: x[0], words) → applies lambda to each word in list
# list() → converts map object to list for easy reading

print(first_chars)  # Output: ['P', 'L', 'F', 'M']

print("***************************************************")


# 2.Lambda variable + map()
# words = ["Apple", "Banana", "Cherry"]
# # Define lambda separately
# get_first = lambda word: word[0]  # word[0] → first character of word
# # Apply map with lambda variable
# first_chars = list(map(get_first, words))  
# print(first_chars)  # Output: ['A', 'B', 'C']



#3.Inline lambda without assignment (direct call with map)

# words = ["Dog", "Elephant", "Fox"]

# # Directly using map + lambda inside print
# print(list(map(lambda x: x[0], words)))  
# # lambda x: x[0] → anonymous function, x[0] is first character
# # list(map(...)) → converts map object to list



#4.Using list comprehension + lambda
# words = ["Giraffe", "Horse", "Iguana"]

# # List comprehension with lambda
# first_chars = [(lambda x: x[0])(word) for word in words]  
# # (lambda x: x[0])(word) → calls lambda on each word
# print(first_chars)  # Output: ['G', 'H', 'I']



#5.Using filter trick (optional creative way)

# Although filter is not intended for extracting characters, we can creatively filter only non-empty words and then extract first character using lambda:


# words = ["Jackal", "", "Kangaroo"]

# # Filter non-empty words and get first character
# first_chars = list(map(lambda x: x[0], filter(lambda x: x != "", words)))  
# # filter(lambda x: x!="", words) → keeps only non-empty words
# # map(lambda x:x[0], ...) → takes first character
# print(first_chars)  # Output: ['J', 'K']






#Q:76. Lambda to sort employees by salary.
#1.Using sorted() with inline lambda (basic way)

# List of employees, each represented as a dictionary
employees = [
    {"name": "Alice", "salary": 5000},
    {"name": "Bob", "salary": 7000},
    {"name": "Charlie", "salary": 6000}
]
# Sort employees by salary using lambda
sorted_employees = sorted(employees, key=lambda x: x["salary"])
# lambda x: x["salary"] → anonymous function, extracts 'salary' from each employee
# sorted(..., key=...) → sorts the list based on the key provided (salary)
# Returns a new sorted list, original list remains unchanged


print(sorted_employees)
# Output: [{'name': 'Alice', 'salary': 5000}, {'name': 'Charlie', 'salary': 6000}, {'name': 'Bob', 'salary': 7000}]
print("***************************************************")



#2.Lambda variable + sorted()
# Define lambda separately
# get_salary = lambda emp: emp["salary"] # extracts salary from employee dictionary

# #Sort employees using lambda variable
# sorted_employees = sorted(employees, key=get_salary)

# print(sorted_employees)
# # Output: same as above



#3.Sort in descending order using lambda

# Sort employees by salary descending
# sorted_employees_desc = sorted(employees, key=lambda x: x["salary"], reverse=True)
# # reverse=True → sorts from highest to lowest
# print(sorted_employees_desc)
# # Output: [{'name': 'Bob', 'salary': 7000}, {'name': 'Charlie', 'salary': 6000}, {'name': 'Alice', 'salary': 5000}]




#4.Using itemgetter from operator module (alternative with lambda optional)
# from operator import itemgetter  # Import itemgetter function

# # Sort using itemgetter (alternative to lambda)
# sorted_employees = sorted(employees, key=itemgetter("salary"))
# # itemgetter("salary") → returns a function that extracts 'salary' from dictionary
# print(sorted_employees)
# # Output: same as method 1





# 5. Using list.sort() method with lambda (in-place sorting)
# Copy employees list to avoid modifying original
# employees_copy = employees.copy()

# # Sort in-place using list.sort() with lambda
# employees_copy.sort(key=lambda x: x["salary"])
# # list.sort() → sorts list in place (modifies original list)
# print(employees_copy)
# # Output: [{'name': 'Alice', 'salary': 5000}, {'name': 'Charlie', 'salary': 6000}, {'name': 'Bob', 'salary': 7000}]





# Q:77. Lambda to filter only premium users.
# Using filter() with inline lambda (basic way)
# List of users, each represented as a dictionary
users = [
    {"name": "Alice", "premium": True},
    {"name": "Bob", "premium": False},
    {"name": "Charlie", "premium": True}
]


# Filter only premium users using lambda
premium_users = list(filter(lambda x: x["premium"], users))  
# lambda x: x["premium"] → anonymous function returning True if user is premium
# filter(lambda x: ..., users) → keeps only users where lambda returns True
# list() → converts filter object into a list

print(premium_users)  
# # Output: [{'name': 'Alice', 'premium': True}, {'name': 'Charlie', 'premium': True}]

print("***************************************************")

#2.Lambda variable + filter()
# Define lambda separately
# is_premium = lambda user: user["premium"]  # returns True if user is premium

# # Apply filter using lambda variable
# premium_users = list(filter(is_premium, users))  
# print(premium_users)
# # Output: [{'name': 'Alice', 'premium': True}, {'name': 'Charlie', 'premium': True}]




# # 3.Inline lambda + map() → get names of premium users
# # Get only names of premium users
# premium_names = list(map(lambda x: x["name"], filter(lambda x: x["premium"], users)))
# # filter(lambda x: x["premium"], users) → keeps only premium users
# # map(lambda x: x["name"], ...) → extracts the 'name' of each premium user
# print(premium_names)  
# # Output: ['Alice', 'Charlie']


#4.Using list comprehension + lambda
# List comprehension with lambda
# premium_users = [user for user in users if (lambda x: x["premium"])(user)]
# # (lambda x: x["premium"])(user) → calls lambda for each user
# print(premium_users)
# # Output: [{'name': 'Alice', 'premium': True}, {'name': 'Charlie', 'premium': True}]




# #5.Using dictionary + lambda trick
# # Dictionary to represent user types
# user_type_check = {
#     "premium": lambda x: x["premium"],
#     "regular": lambda x: not x["premium"]
# }

# # Filter premium users using dictionary + lambda
# premium_users = list(filter(user_type_check["premium"], users))
# print(premium_users)
# # Output: [{'name': 'Alice', 'premium': True}, {'name': 'Charlie', 'premium': True}]




# Q:78. Lambda with sorted() → sort by last name.
# 1.Basic sorted() with inline lambda (ascending order)
names = ["Alice Smith", "Bob Johnson", "Charlie Brown"]

# # Sort names by last name using lambda
sorted_names = sorted(names, key=lambda x: x.split()[-1])
# lambda x: x.split()[-1] → anonymous function splits full name by space and takes last word (last name)
# # sorted(..., key=...) → sorts list based on key provided (last name)
print(sorted_names)
# # Output: ['Charlie Brown', 'Bob Johnson', 'Alice Smith']

print("***************************************************")


#2.Lambda variable + sorted()
# Define lambda separately
# get_last_name = lambda full_name: full_name.split()[-1]  # returns last word from full name

# # Sort using lambda variable
# sorted_names = sorted(names, key=get_last_name)
# print(sorted_names)
# Output: same as above



#3.Sort in descending order by last name
# Sort names by last name descending
# sorted_names_desc = sorted(names, key=lambda x: x.split()[-1], reverse=True)
# # reverse=True → sorts from Z to A
# print(sorted_names_desc)
# # Output: ['Alice Smith', 'Bob Johnson', 'Charlie Brown']



# 4. Using list.sort() method with lambda (in-place sorting)
# # Copy names list to avoid modifying original
# names_copy = names.copy()

# # In-place sorting using list.sort() with lambda
# names_copy.sort(key=lambda x: x.split()[-1])
# # list.sort() → sorts the list in place
# print(names_copy)
# # Output: ['Charlie Brown', 'Bob Johnson', 'Alice Smith']


#5.Using itemgetter for last name (alternative, requires splitting first)
# from operator import itemgetter  # import itemgetter

# Convert names into list of [first_name, last_name]
# split_names = [name.split() for name in names]  
# split() → splits each full name into [first_name, last_name]

# Sort by last name using itemgetter
# sorted_split_names = sorted(split_names, key=itemgetter(1))  
# # itemgetter(1) → selects second element (last name) as key
# # sorted(...) → returns sorted list

# # Join first and last names back into full names
# sorted_names = [" ".join(name) for name in sorted_split_names]
# print(sorted_names)
# # Output: ['Charlie Brown', 'Bob Johnson', 'Alice Smith']

"""
Details in simple words:

itemgetter(index_or_key) → returns a callable function.

When called on a sequence (like list or tuple), it returns the item at the given index.

When called on a dictionary, it returns the value for the given key.

Useful as a key function in sorted() instead of writing a lambda.

✅ Summary: itemgetter is a shortcut for lambda x: x[index_or_key].
"""





#Q:79. Lambda to format phone numbers.
#1.Using map() + inline lambda (basic way)
# List of phone numbers as strings (10 digits each)
numbers = ["1234567890", "9876543210"]

# # Format numbers as (XXX) XXX-XXXX using lambda + map
# formatted_numbers = list(map(lambda x: f"({x[:3]}) {x[3:6]}-{x[6:]}", numbers))
# # lambda x: f"({x[:3]}) {x[3:6]}-{x[6:]}" → anonymous function
# # x[:3] → first 3 digits (area code)
# # x[3:6] → next 3 digits
# # x[6:] → remaining 4 digits
# # map(lambda x: ..., numbers) → applies lambda to each number in list
# # list(...) → converts map object to list for readable output

# print(formatted_numbers)
# # Output: ['(123) 456-7890', '(987) 654-3210']



# 2.Lambda variable + map()
# Define lambda separately
# format_number = lambda num: f"({num[:3]}) {num[3:6]}-{num[6:]}"
# # num[:3] → first 3 digits
# # num[3:6] → next 3 digits
# # num[6:] → last 4 digits

# # Apply map using lambda variable
# formatted_numbers = list(map(format_number, numbers))
# print(formatted_numbers)
# # Output: same as above



#3.Using list comprehension + lambda
# List comprehension with lambda
# formatted_numbers = [(lambda x: f"({x[:3]}) {x[3:6]}-{x[6:]}")(num) for num in numbers]
# # (lambda x: ...)(num) → calls lambda for each number
# print(formatted_numbers)
# # Output: ['(123) 456-7890', '(987) 654-3210']



#4.Using user input + lambda + map()
# Take phone numbers from user input, separated by space
# numbers = input("Enter phone numbers separated by space: ").split()
# # input() → reads string from user
# # .split() → converts string into list of number strings

# # Format phone numbers
# formatted_numbers = list(map(lambda x: f"({x[:3]}) {x[3:6]}-{x[6:]}", numbers))
# print("Formatted numbers:", formatted_numbers)




#5. Using function + lambda inside map()
# # Define a function to format phone numbers
# def format_numbers(nums):
#     return list(map(lambda x: f"({x[:3]}) {x[3:6]}-{x[6:]}", nums))
#     # map applies lambda to each number in list

# # Call function
# formatted_numbers = format_numbers(numbers)
# print(formatted_numbers)





# Q:80. Lambda to filter all `.jpg` files.
# 1. Using filter() + inline lambda (basic way)
# List of files with different extensions
files = ["image1.jpg", "document.pdf", "photo.jpg", "notes.txt"]

# # Filter only .jpg files using lambda
jpg_files = list(filter(lambda x: x.endswith(".jpg"), files))
# # lambda x: x.endswith(".jpg") → anonymous function returns True if string ends with '.jpg'
# # filter(...) → keeps only elements where lambda returns True
# # list(...) → converts filter object to list for readable output

print(jpg_files)
# # Output: ['image1.jpg', 'photo.jpg']
print("***************************************************")



#2.Lambda variable + filter()
# Define lambda separately
# is_jpg = lambda filename: filename.endswith(".jpg")  # checks if file ends with '.jpg'

# # Apply filter using lambda variable
# jpg_files = list(filter(is_jpg, files))
# print(jpg_files)
# # Output: same as above


# 3.Using list comprehension + lambda
# List comprehension with lambda
# jpg_files = [f for f in files if (lambda x: x.endswith(".jpg"))(f)]
# # (lambda x: x.endswith(".jpg"))(f) → calls lambda for each file f
# print(jpg_files)
# # Output: ['image1.jpg', 'photo.jpg']


# 4. Using map() + lambda + conditional (creative way)
# Map lambda to mark .jpg files and then filter None
# jpg_files = list(filter(None, map(lambda x: x if x.endswith(".jpg") else None, files)))
# # map(lambda x: x if x.endswith(".jpg") else None, files) → returns filename if .jpg else None
# # filter(None, ...) → removes None values
# print(jpg_files)
# # Output: ['image1.jpg', 'photo.jpg']


#5. Using function + lambda + filter()
# Define a function to filter .jpg files
# def get_jpg_files(file_list):
#     return list(filter(lambda f: f.endswith(".jpg"), file_list))
#     # filter applies lambda to keep only .jpg files

# jpg_files = get_jpg_files(files)
# print(jpg_files)







# Interview Qs:
# 81. Difference between lambda and def function?
# 82. Limitations of lambda functions?


# =========================================================
# 81. Difference between lambda and def function
# =========================================================

"""
Lambda Function vs Def Function:

1. Definition:
   - lambda: Anonymous, small, one-line function without a name.
   - def: Named function, can contain multiple lines and statements.

2. Syntax:
   - lambda: lambda arguments: expression
     Example: square = lambda x: x**2
   - def: def function_name(arguments):
              statements
     Example:
         def square(x):
             return x**2

3. Usage:
   - lambda: Used for small, throwaway functions, often with map(), filter(), reduce(), sorted()
   - def: Used for reusable, larger, multi-line functions.

4. Return:
   - lambda: Implicitly returns the result of the expression.
   - def: Explicitly returns using return statement.

5. Readability:
   - lambda: Less readable if complex.
   - def: More readable and maintainable.

6. Statements:
   - lambda: Can only contain expressions, no statements like loops, if-else (except ternary)
   - def: Can have multiple statements, loops, conditionals, etc.

"""

# =========================================================
# 82. Limitations of lambda functions
# =========================================================

"""
Limitations of Lambda Functions in Python:

1. Single Expression:
   - Lambda can contain only one expression, no multiple statements.
   Example (Invalid):
       lambda x: x+=1; print(x)  # ❌ Not allowed

2. No Assignment:
   - Cannot assign values or create variables inside lambda.
   Example:
       lambda x: y=2+x  # ❌ Not allowed

3. Limited Readability:
   - Complex logic makes lambda hard to read and debug.

4. Cannot contain loops or multiple conditions:
   - Only single expression is allowed.
   Example:
       lambda x: [i for i in range(x)]  # allowed (list comprehension is expression)
       lambda x: for i in range(x): i   # ❌ Not allowed

5. No Annotations or Docstrings:
   - Lambda functions cannot have type hints or docstrings for explanation.

6. Difficult for Recursion:
   - Lambda functions are not ideal for recursion or self-referencing complex logic.

7. Debugging Limitations:
   - Errors inside lambda can be harder to trace compared to def functions.

"""











# =========================================================
# Map, Filter, Reduce – Easy Explanation
# =========================================================

"""
1️⃣ map(function, iterable)
- Purpose: Apply a function to every item in a list (or any iterable) and return a new map object.
- Key point: Transforms each element in the iterable.
- Returns: map object (use list() to see as list)

Example:
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))  
# squares each number → [1, 4, 9, 16]

---

2️⃣ filter(function, iterable)
- Purpose: Select items from a list (or iterable) where the function returns True.
- Key point: Filters elements based on a condition.
- Returns: filter object (use list() to see as list)

Example:
numbers = [1, 2, 3, 4]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  
# keeps only even numbers → [2, 4]

---

3️⃣ reduce(function, iterable)
- Purpose: Apply a function cumulatively to the items in a list to reduce them to a single value.
- Key point: Combines elements step by step.
- Requires: from functools import reduce

Example:
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)  
# multiplies all numbers → 1*2*3*4 = 24

---

✅ Summary in simple words:
- map → transforms every element.
- filter → selects elements that satisfy a condition.
- reduce → combines elements into a single result.
"""
