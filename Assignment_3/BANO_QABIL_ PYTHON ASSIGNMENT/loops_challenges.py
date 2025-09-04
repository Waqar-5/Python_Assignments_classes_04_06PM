# Section E: Real-World Looping Challenges



#Q:47. Loop through employee salaries, print only above average.
# Sample employee salaries
salaries = [30000, 50000, 40000, 60000, 35000, 45000]

average_salary = sum(salaries) / len(salaries)
print(f"Average Salary: {average_salary}\n")

# # -----------------------------
# # Method 1: Using basic for loop
# # -----------------------------
# print("Method 1: Using basic for loop")
# for salary in salaries:
#     # Commit: Check if salary is above average
#     if salary > average_salary:
#         print(salary)  # Commit: Print salary above average

# print("\n")


# -----------------------------
# Method 2: Using for loop with index
# -----------------------------
# print("Method 2: Using for loop with index")
# for i in range(len(salaries)):
#     # Commit: Access salary using index
#     if salaries[i] > average_salary:
#         print(salaries[i])  # Commit: Print salary above average

# print("\n")

# -----------------------------
# Method 3: Using while loop
# -----------------------------
# print("Method 3: Using while loop")
# i = 0
# while i < len(salaries):
#     # Commit: Compare salary with average
#     if salaries[i] > average_salary:
#         print(salaries[i])  # Commit: Print salary above average
#     i += 1

# print("\n")

# Method 4: Using list comprehension
# # -----------------------------
# print("Method 4: Using list comprehension")
# above_avg_salaries = [s for s in salaries if s > average_salary]
# # Commit: List comprehension creates a new list of salaries above average
# print(above_avg_salaries)

# print("\n")


# Method 5: Using filter() function
# -----------------------------
# print("Method 5: Using filter() function")
# def is_above_average(salary):
#     # Commit: Function to check if salary is above average
#     return salary > average_salary

# filtered_salaries = filter(is_above_average, salaries)
# # Commit: filter() returns an iterator, convert to list to print
# print(list(filtered_salaries))

# print("\n")



# -----------------------------
# Method 6: Using enumerate
# # -----------------------------
# print("Method 6: Using enumerate")
# for index, salary in enumerate(salaries):
#     # Commit: enumerate gives both index and value
#     if salary > average_salary:
#         print(f"Employee {index + 1} Salary: {salary}")

# # =========================================================
# # End of Program
# # =========================================================




print("***********************************************************")
#Q:48. Loop through list of student grades, print pass/fail.
grades = [85, 42, 76, 90, 58, 33, 67]

# Define pass mark
pass_mark = 50
print(f"Passing Mark: {pass_mark}")

# # Method 1: Using basic for loop
print("Method 1: Using basic for loop")
for grade in grades:
    # Compare grade with pass mark
    if grade >=  pass_mark:
        print(f"Grade: {grade} - Pass")  #Print Pass
    else:
        print(f"Grade: {grade} - Fail")  #Print Fail

print("\n")


# Method 2: Using for loop with index
# print("Method 2: Using for loop with index")
# for i in range(len(grades)):
#     # Access grade using index
#     if grades[i] >= pass_mark:
#         print(f"Student {i + 1} Grade {grades[i]:} - Pass")  # Print Pass
#     else:
#         print(f"Student {i + 1} Grade {grades[i]:} - Fail")
# print("\n")


# Method 3: Using while loop
# print("Method 3: Using while loop")
# i = 0
# while i < len(grades):
#     #compare grade with pass mark
#     if grades[i] >= pass_mark:
#         print(f"Grade: {grades[i]} - Pass")  #Print Pass
#     else:
#         print(f"Grade: {grades[i]} - Fail")
#     i += 1

# print("\n")



# Method 4: Using list comprehension
# print("Method 4: Using list comprehension")
# # create a list of pass/fail status using comprehension
# pass_fail = [f"Pass" if grade >= pass_mark else "Fail" for grade in grades]
# # print the list of pass/fail status
# print(pass_fail)

# Method 5: Using map() function
# print("Method 5: Using map() function")
# def check_pass_fail(grade):
#     # Commit: Function to determine pass/fail
#     return "Pass" if grade >= pass_mark else "Fail"

# status_list = list(map(check_pass_fail, grades))
# # Commit: map() applies function to all grades
# print(status_list)
# print("\n")

# Method 6: Using enumerate
# print("Method 6: Using enumerate")
# for index, grade in enumerate(grades):
#     # Commit: Track student index and grade
#     result = "Pass" if grade >= pass_mark else "Fail"
#     print(f"Student {index + 1}: Grade {grade} - {result}")




print("***********************************************************")
#Q:49. Remove duplicates from list manually (without set).
numbers = [1, 2, 3, 2, 4, 3, 5, 1, 6, 4]
print(f"Original List: {numbers}\n")

# Method 1: Using for loop and new list
print("Method 1: Using for loop and new list")
unique_numbers = []  # New list to store unique numbers
for num in numbers:
    # Check if number is not already in unique_numbers
    if num not in unique_numbers:
        unique_numbers.append(num)  # Add unique number to list
print(f"Unique List: {unique_numbers}\n")


# Method 2: Using while loop
# print("Method 2: Using while loop")

# numbers_copy = numbers.copy() # Copy original list to avoid modifying it during iteration
# i = 0
# while i < len(numbers_copy):
#     # remove duplicates after the first reference
#     j = i+ 1
#     while j < len(numbers_copy):
#         if numbers_copy[i] == numbers_copy[j]:
#             numbers_copy.pop(j)  # Remove duplicate
#         else:
#             j += 1
#     i += 1
# print(f"Unique List: {numbers_copy}\n")


# Method 3: Using dictionary keys (manual)
# print("Method 3: Using dictionary keys")
# unique_dict = {}  # Dictionary to maintain unique keys
# for num in numbers:
#     unique_dict[num] = True  # Key added only once automatically
# unique_list = list(unique_dict.keys())  # Commit: Convert keys back to list
# print(unique_list, "\n")


# Method 4: Using list comprehension
# print("Method 4: Using list comprehension")
# unique_list_lc = []
# [unique_list_lc.append(num) for num in numbers if num not in unique_list_lc]  # Commit: Append only if not present
# print(unique_list_lc, "\n")

# Method 5: Using enumerate
# print("Method 5: Using enumerate")
# unique_enum_list = []
# for index, num in enumerate(numbers):
#     # Commit: Check if first occurrence index matches current index
#     if num not in unique_enum_list:
#         unique_enum_list.append(num)
# print(unique_enum_list, "\n")




print("***********************************************************")
#Q:50. Flatten a nested list using loop.
nested_list = [[1, 2], [3, 4, 5], [6], [7, 8, 9]]
print(f"Original Nested List: {nested_list}\n")

# Method 1: Using nested for loop
print("Method 1: Using nested for loop")
flat_list = [] # Empty list to store flattened elements
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)  # Append each element of sublist
print(flat_list, "\n")



# Method 2: Using while loop
# print("Method 2: Using while loop")
# flat_list_while = []
# i = 0
# while i < len(nested_list):
#     j = 0
#     while j < len(nested_list[i]):
#         flat_list_while.append(nested_list[i][j])  # Commit: Append element
#         j += 1
#     i += 1
# print(flat_list_while, "\n")


# # Method 3: Using list comprehension
# print("Method 3: Using list comprehension")
# flat_list_lc = [item for sublist in nested_list for item in sublist]  # Commit: Flatten nested list elegantly
# print(flat_list_lc, "\n")



#  Method 4: Using extend() in for loop
# print("Method 4: Using extend() in for loop")
# flat_list_extend = []
# for sublist in nested_list:
#     flat_list_extend.extend(sublist)  # Commit: extend() adds all elements of sublist at once
# print(flat_list_extend, "\n")


# Method 5: Using enumerate
# print("Method 5: Using enumerate")
# flat_list_enum = []
# for index, sublist in enumerate(nested_list):
#     # Commit: Track index if needed for debugging
#     for item in sublist:
#         flat_list_enum.append(item)  # Commit: Append each item
# print(flat_list_enum, "\n")



print("***********************************************************")
#Q:51. Loop to validate email addresses (must contain `@`).
emails = ["waqar@gmail.com", "john.doe.com", "alice@", "bob@example.com", "notanemail"]

# Method 1: Using basic for loop
print("Method 1: Using basic for loop")
for email in emails:
    # check if '@' is present in email
    if '@' in email:
        print(f"{email} is VALID")
    else:
        print(f"{email} is INVALID")
print("\n")

# Method 2: Using for loop with index
# print("Method 2: Using for loop with index")
# for i in range(len(emails)):
#     #  Access email using index
#     if '@' in emails[i]:
#         print(f"Email {i+1}: {emails[i]} is VALID")
#     else:
#         print(f"Email {i+1}: {emails[i]} is INVALID")

# print("\n")


# Method 3: Using while loop
# print("Method 3: Using while loop")
# i = 0
# while i < len(emails):
#     #  Compare each email for '@'
#     if '@' in emails[i]:
#         print(f"{emails[i]} is VALID")
#     else:
#         print(f"{emails[i]} is INVALID")
#     i += 1

# print("\n")



# Method 4: Using list comprehension
# print("Method 4: Using list comprehension")
# Create a list of validation results
# validation_results = [f"{email} is VALID" if '@' in email else f"{email} is INVALID" for email in emails]
# print(validation_results)

# print("\n")


# Method 5: Using enumerate
# print("Method 5: Using enumerate")
# for index, email in enumerate(emails):
#     # Track email index for clarity
#     result = "VALID" if '@' in email else "INVALID"
#     print(f"Email {index+1}: {email} - {result}")

# print("\n")



print("***********************************************************")
#Q:52. Count number of urgent messages in chat logs.

chat_logs = [
    "Please send the report",
    "This is urgent, reply ASAP",
    "Meeting at 5 PM",
    "Urgent: Server is down",
    "Lunch time",
    "We have an urgent issue to fix"
]


# Method 1: Using basic for loop
print("Method 1: Using basic for loop")
urgent_count = 0 # Initialize counter
for message in chat_logs:
    # Check if 'urgent' is in message (case-sensitive)
    if "urgent" in message.lower():
        urgent_count += 1  # Increment cpunter if urgent
print(f"Number of urgent message: {urgent_count}\n")



# # Method 2: Using for loop with index
# print("Method 2: Using for loop with index")
# urgent_count_index = 0
# for i in range(len(chat_logs)):
#     # access message by index
#     if "urgent" in chat_logs[i].lower():
#         urgent_count_index += 1 
# print(f"Number of urgent message: {urgent_count_index}\n")


# # Method 3: Using while loop
# print("Method 3: Using while loop")
# urgent_count_while = 0
# i= 0
# while i < len(chat_logs):
#     # Check message content
#     if "urgent" in chat_logs[i].lower():
#         urgent_count_while += 1
#     i += 1
# print(f"Number of urgent message:  {urgent_count_while}\n")



# Method 4: Using list comprehension
# print("Method 4: Using list comprehension")
# # Create a list of urgent messages
# urgent_messages = [msg for msg in chat_logs if "urgent" in msg.lower()]
# # Count the list length
# print(f"Number of urgent messages: {len(urgent_messages)}\n")

# Method 5: Using enumerate
# print("Method 5: Using enumerate")
# urgent_count_enum = 0
# for index, message in enumerate(chat_logs):
#     # Track index if needed for debugging
#     if "urgent" in message.lower():
#         urgent_count_enum += 1
# print(f"Number of urgent messages: {urgent_count_enum}\n")





print("***********************************************************")

#Q:53. Loop to show only Pakistani contacts (+92).
# Sample contact list
contacts = [
    "+923001234567",
    "+19876543210",
    "+923456789012",
    "+441234567890",
    "+921234567890"
]
# Method 1: Using basic for loop
print("Method 1: Using basic for loop")
for contact in contacts:
    # check if contact status with '+92'
    if contact.startswith("+92"):
        print(contact)  # print Pakistani contact
print("\n")


# Method 2: Using for loop with index
# print("Method 2: Using for loop with index")
# for i in range(len(contacts)):
#     # Access contact using index
#     if contacts[i].startswith("+92"):
#         print(contacts[i]) # print Pakistani contact
# print("\n")

# Method 3: Using while loop
# print("Method 3: Using while loop")
# i = 0
# while i < len(contacts):
#     # Compare each contact for '+92' prefix
#     if contacts[i].startswith("+92"):
#         print("Pakistani Phone Number: ",contacts[i])
#     i += 1  
# print("\n")

# Method 4: Using list comprehension
# print("Method 4: Using list comprehension")
# # Filter contacts starting with "+92"
# pakistani_contacts = [c for c in contacts if c.startswith("+92")]
# print(pakistani_contacts)

# print("\n")


# Method 5: Using enumerate

# print("Method 5: Using enumerate")
# for index, contact in enumerate(contacts):
#     # Commit: Track index and check prefix
#     if contact.startswith("+92"):
#         print(f"Contact {index + 1}: {contact}")  # Commit: Print Pakistani contact with index



# Initialize an empty list to store Pakistani contacts manually
# pakistani_contacts = []

# # Loop through each contact manually
# for contact in contacts:
#     # Manually check first three characters to see if they match '+92'
#     if contact[0] == "+" and contact[1] == "9" and contact[2] == "2":
#         pakistani_contacts.append(contact)  # Add to manual list

# # Display the manually filtered Pakistani contacts
# print("Pakistani Contacts (+92):")
# for contact in pakistani_contacts:
#     print(contact)



print("***********************************************************")

#Q:54. Simulate inventory reduction when order placed.


# # Sample inventory: product name and quantity
inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20
}

# Sample orders: product name and quantity ordered
orders = [
    {"product": "Apples", "quantity": 5},
    {"product": "Oranges", "quantity": 10},
    {"product": "Bananas", "quantity": 15},
    {"product": "Apples", "quantity": 20},
]

# Method 1: Using basic for loop
print("Method 1: Using basic for loop")
for order in orders:
    product = order["product"]
    qty_ordered = order["quantity"]
    # Check if product exists in inventory
    if product in inventory:
        # reduce inventory quantity
        inventory[product] -= qty_ordered
        print(f"{qty_ordered} {product} ordered, remaining: {inventory[product]}")
print("\n")


# # Method 2: Using for loop with index
# print("Method 2: Using for loop with index")
# for i in range(len(orders)):
#     product = orders[i]["product"]
#     qty_ordered = orders[i]["quantity"]
#     if product in inventory:
#         inventory[product] -= qty_ordered
#         print(f"{qty_ordered} {product} ordered, remaining: {inventory[product]}")
# print("\n")



# Method 3: Using while loop
# print("Method 3: Using while loop") # indicate method
# i = 0 # initialize index
# while i < len(orders): # loop until all orders are processed
#     product = orders[i]["product"] # Get product
#     qty_ordered = orders[i]["quantity"] # get quantity
#     if product in inventory: # check inventory
#         inventory[product] -= qty_ordered # reduce inventory
#         print(f"{qty_ordered} {product} ordered, remaining: {inventory[product]}")  # Display updated inventory
#     i += 1
# print("\n")


# Method 4: Using enumerate
# print("Method 4: Using enumerate") 
# for index, order in enumerate(orders): # Loop with index  using enumerate
#     product = order["product"] # extract product
#     qty_ordered = order["quantity"] # extract quantity
#     if product in inventory: # check inventory
#         inventory[product] -= qty_ordered # reduce inventory
#         print(f"Order {index + 1}: {qty_ordered} {product} ordered, remaining: {inventory[product]}")   #Display updated inventory with order number
# print("\n")  # Line break

# Method 5: Using list comprehension (for simulation printing)

# print("Method 5: Using list comprehension for simulation")  # 

# [  #  Start list comprehension for side-effect printing
#     print(f"{order['quantity']} {order['product']} ordered, remaining: {inventory.update({order['product']: inventory[order['product']] - order['quantity']}) or inventory[order['product']]}")  # Update inventory and print remaining
#     for order in orders  # Loop through each order
# ]

# print("\n")  # Line break




print("***********************************************************")

#Q:55. Loop through doctor profiles and print specialists only.

# Sample doctor profiles
doctors = [
    {"name": "Dr. Ahmed", "specialist": True},
    {"name": "Dr. Sara", "specialist": False},
    {"name": "Dr. Ameer", "specialist": True},
    {"name": "Dr. Hina", "specialist": False},
    {"name": "Dr. Sameer", "specialist": True}
]

# Method 1: Using basic for loop
print("Method 1: Using basic for loop")
for doctor in doctors: # loop through each doctor
    if doctor["specialist"]: # check if doctor is a specialist
        print(f"{doctor['name']} is a specialists")  # Print specialist doctor
print("\n")


# Method 2: Using for loop with index
# print("Method 2: Using for loop with index") 
# for i in range(len(doctors)): # loop through doctors using index
#     if doctors[i]["specialist"]: # check if doctor is a specialist
#         print(f"{doctors[i]['name']} is a specialist") # Print specialist doctor
# print("\n")




# Method 3: Using while loop

# print("Method 3: Using while loop")
# i = 0  # Commit: Initialize index
# while i < len(doctors):  # Commit: Loop until all doctors are checked
#     if doctors[i]["specialist"]:  # Commit: Check if doctor is a specialist
#         print(f"{doctors[i]['name']} is a specialist")  # Commit: Print specialist doctor
#     i += 1  # Commit: Increment index
# print("\n")



# Method 4: Using enumerate

# print("Method 4: Using enumerate")
# for index, doctor in enumerate(doctors):  # Commit: Loop with index tracking
#     if doctor["specialist"]:  # Commit: Check specialist status
#         print(f"Doctor {index + 1}: {doctor['name']} is a specialist")  # Commit: Print with index
# print("\n")



# # Method 5: Using list comprehension
# print("Method 5: Using list comprehension")
# specialists = [doctor["name"] for doctor in doctors if doctor["specialist"]]  # Commit: Create list of specialist names
# print(specialists)  # Commit: Print all specialists
# print("\n")




print("***********************************************************")
#Q:56. Loop through dictionary of courses per student.
students_courses = {
    "Ali": ["Math", "Physics", "Chemistry"],
    "Sara": ["Biology", "English"],
    "Usman": ["Math", "Computer Science"],
}

# Method 1: Using basic for loop (keys)
print("Method 1: Using basic for loop (keys)")
for student in students_courses: #  Loop through dictionary keys
    courses = students_courses[student] # get courses for student
    print(f"{student} is enrolled in: {courses}")  # Print student and their courses
print("\n")


# # Method 2: Using for loop with .items()
# print("Method 2: Using for loop with .items()")
# for student, courses in students_courses.items():  # Loop through key-value pairs
#     print(f"{student} is enrolled in: {courses}")  # Print student and their courses
# print("\n")


# Method 3: Using for loop with index (list of keys)

# print("Method 3: Using for loop with index")
# student_keys = list(students_courses.keys())  # Convert dictionary keys to list
# for i in range(len(student_keys)):  # Loop using index
#     student = student_keys[i]  # Get student by index
#     courses = students_courses[student]  # Get their courses
#     print(f"{student} is enrolled in: {courses}")  #  Print
# print("\n")



# Method 4: Using while loop

# print("Method 4: Using while loop")
# student_keys = list(students_courses.keys())  #  Convert keys to list
# i = 0  #  Initialize index
# while i < len(student_keys):  #  Loop until all students are processed
#     student = student_keys[i]  #  Get student name
#     courses = students_courses[student]  #  Get courses
#     print(f"{student} is enrolled in: {courses}")  #  Print student and courses
#     i += 1  #  Increment index
# print("\n")



# Method 5: Using enumerate

# print("Method 5: Using enumerate")
# for index, (student, courses) in enumerate(students_courses.items()):  # Commit: Loop through items with index
#     print(f"Student {index + 1}: {student} is enrolled in: {courses}")  # Commit: Print with index
# print("\n")



# Method 6: Using list comprehension
# print("Method 6: Using list comprehension")
# # Create a list of formatted strings for all students and courses
# students_info = [f"{student} is enrolled in: {courses}" for student, courses in students_courses.items()]
# print(students_info)  # Print the list
# print("\n")



# Interview Qs:
# 57. How do you iterate over both keys and values in dictionary?
# 58. How to break out of multiple nested loops in Python?


"""
57. How do you iterate over both keys and values in a dictionary?

Definition / Answer (Interview-Ready):

In Python, dictionaries store data as key-value pairs. To iterate over both keys and values simultaneously, the most Pythonic way is to use the .items() method, which returns a view of key-value pairs. Each pair can be unpacked in a loop.

Example:

student_scores = {"Ali": 90, "Sara": 85, "Usman": 78}

for student, score in student_scores.items():  # .items() gives key-value pairs
    print(f"{student} scored {score}")


Output:

Ali scored 90
Sara scored 85
Usman scored 78


Additional Notes (Optional for Interview):

You can also loop over .keys() for keys and .values() for values separately, but .items() is preferred for both.

Use enumerate() with .items() if you need a counter while iterating.

58. How to break out of multiple nested loops in Python?

Definition / Answer (Interview-Ready):

Python does not provide a direct way to break multiple nested loops with a single break. However, there are clean and professional ways to exit all loops when a condition is met:

1. Using a Flag Variable:

found = False
for i in range(1, 5):
    for j in range(1, 5):
        if i * j == 6:
            found = True
            break  # Break inner loop
    if found:
        break  # Break outer loop


2. Using a Function and return (Pythonic way):

def find_product():
    for i in range(1, 5):
        for j in range(1, 5):
            if i * j == 6:
                return (i, j)  # Immediately exit all loops

result = find_product()
print("Found:", result)


3. Using Exception (Advanced):

class BreakLoops(Exception):
    pass

try:
    for i in range(1, 5):
        for j in range(1, 5):
            if i * j == 6:
                raise BreakLoops
except BreakLoops:
    print("Exited all loops")


Key Notes for Interview:

Flag variable: Simple and readable; works in most scenarios.

Function with return: Cleanest Pythonic approach; exits all loops immediately.

Custom Exception: Use for complex nested loops or when loops are deep inside multiple functions.

💡 Tips for answering in an interview:

Start with a short definition.

Give a small code example.

Mention alternative approaches briefly.

Highlight Pythonic or clean methods to sh

"""