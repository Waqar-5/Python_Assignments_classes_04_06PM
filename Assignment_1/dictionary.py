# Dictionaries (Q33–Q38)

# Q:33. Create dictionary `student` with keys: `name`, `age`, `grade`. Print all key-value pairs.

# Create the dictionary
student = {
    "name": "Ali",
    "age" : 22,
    "grade" : "A"
}

# print(student.items())

# .items():
# This method gives all key-value pairs in the dictionary

# Print all key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

print("*******************************************************")


# Q:34. Add new key `subject` to the dictionary. Print updated dictionary.
# Original dictionary
print("Original dictionary: ", student)
# Add new key 'subject'

student["subject"] = "English"

# Print updated dictionary
print("after adding new key subject: ",student)

print("******************************************")

# Q:35. Search for a key. If found, print the value.

# Key to search
key_to_search = "grade"

# Check if key exists and print the value
if key_to_search in student:
    # print(f"{key_to_search}: {student["grade"]}")  #student["grade"]  # gives you "A"
    print(f"{key_to_search}: {student[key_to_search]}") #student[key_to_search]  # also gives "A" because key_to_search = "grade"
else:
    print("Key '{key_to_search}' not found.")


print("******************************************")
# Q:36. Create dictionary of 3 students and their marks. Calculate average.
# Dictionary of students and their marks
student_marks = {
    "Ali": 75,
    "Sara": 85,
    "Zara": 90
}

# Step 1: Add all the marks
total_marks = sum(student_marks.values())

# Step 2: Count number of students
number_of_students = len(student_marks)

# Step 3: Calculate average
average = total_marks / number_of_students

# Step 4: Print the result
print("Average marks:", average)
"""
 Explanation in Easy Words:
sum(student_marks.values()): adds all the marks (75 + 85 + 90)

len(student_marks): counts the students (3)

total / count: gives the average
"""

print("******************************************")



# Q:37. Given items and prices in a dictionary, input a budget and list affordable items.
# PART 1: Input a budget and list affordable items
items = {
    "Pen": 20,
    "Notebook": 50,
    "Bag": 500,
    "Pencil": 10,
    "Eraser": 5,
}

# Ask user for their budget
budget = int(input("Enter your budget: "))

# Find and print affordable items
print("You can afford:")
for item, price in items.items():
    if price <= budget:
        print(f"- {item}: Rs {price}")


print("*********************************************************")

#  Print students scoring ≥50 and count how many failed
# Given:
# marks = {"Ali": 45, "Sara": 70, "Shayan": 65, "Osama": 30}
# Print students scoring ≥50.
# Count how many failed.



marks = {"Ali": 45, "Sara": 70, "Shayan": 65, "Osama": 30}
print("Students scoring 50 or more:")
for name, mark in marks.items():
    if mark >= 50:
        print(f"- {name}: {mark}")

# Count how many failed (marks < 50)
failed_count = 0
for mark in marks.values():
    if mark < 50:
        failed_count += 1

print(f"\nTotal students who failed: {failed_count}")




"""
Dictionaries in Python – Must-Know Short Lines
{} = dictionary

Key → value pair

Example: {"name": "Ali", "age": 20}

Keys must be unique

Values can repeat

dict() = built-in function

Access: mydict["key"]

Add new: mydict["new"] = value

Change: mydict["key"] = new_value

Delete: del mydict["key"]

Check key: "name" in mydict

mydict.keys() → all keys

mydict.values() → all values

mydict.items() → key-value pairs

Loop: for k, v in mydict.items():

Use with input() for menus/forms

Nested dict = dict inside dict

Keys can be strings, numbers, or tuples

get() avoids errors → mydict.get("key")

Fast lookup – better than list for search


"""
