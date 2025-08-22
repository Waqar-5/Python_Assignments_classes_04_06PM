# Section A: For Loop (Real-Life + Interview Qs)

# Q#1. Print all file names in a given list of files.
# List of file names
# files = ["report.pdf", "data.csv", "image.png", "notes.txt", "presentation.pptx"]

# Print all file names
# print("List of files: ")
# for file in files:
#     print(file)

# or 
# print("List of files:\n" + "\n".join(files))
# or 

# Using map()
# list(map(print, files))

# or 
# Using while loop
# i = 0
# while i < len(files):
#     print(files[i])
#     i += 1

# or 
# Using List Comprehension (one-liner)
# [print(f) for f in files]



# Q: 2. Print each student’s name from a list with roll numbers.
# List of students (roll number, name)
# students = [
#     (1, "Ali"),
#     (2, "Aliza"),
#     (3, "Ameer"),
#     (4, "AliGul"),
#     (5, "Sameer")
# ]
# print("Student Names:")
# for roll, name in students:
#     print(roll, ")",name)



# or 
# [print(roll ,")", name) for roll, name in students]

# or 

# print(students[0][1])   # [0] → first tuple, [1] → name

# for student in students:
#     print(student[1])   # index 1 = name


# or 
# for roll, name in students:
#     print(f"{roll} - {name}")

# or 
# Using Index Access
# for student in students:
#     print(student[0], "-", student[1])


# or 
# 1. Simple for loop with tuple unpacking (cleanest way)
# for roll, name in students:
#     print(f"{roll} - {name}")


# 2. Using Index Access
# for student in students:
#     print(student[0], "-", student[1])

# 3. Using enumerate() (adds index automatically)
# for i, student in enumerate(students, start=1):
#     print(i, "-", student[1])  #student[0] → roll number, student[1] → name.
# enumerate gives you a counter along with the data.
# enumerate() returns (index, value) for each element in a list.

# start=1 → index starts from 1 instead of 0.

# student[1] → prints name.



# 4. Using map() with lambda
# list(map(lambda s: print(s[0], "-", s[1]), students))
# map() applies a function to each element of a list.

# lambda s: print(s[0], "-", s[1]) → prints roll and name for each tuple.

# Wrapping in list() executes it immediately in Python 3.



# 5 List Comprehension (one-liner)
# [print(roll, "-", name) for roll, name in students]




# 6. Using join() for Pretty Printing
# print("\n".join([f"{roll} - {name}" for roll, name in students]))



# 7. Using dict Instead of Tuples
# students_dict = {
#     1: "Ali",
#     2: "Aliza",
#     3: "Ameer",
#     4: "AliGul",
#     5: "Sameer"
# }


# for roll, name in students_dict.items():
#     print(f"{roll} - {name}")
# Dictionary key:value → roll:name.
# .items() → returns (key, value) pairs.



# 8. Using while Loop
# i = 0
# while i < len(students):
#     print(students[i][0], "-", students[i][1])
#     i += 1




#9. Using zip() (if roll numbers & names are separate lists)
# rolls = [1, 2, 3, 4, 5]
# names = ["Ali", "Aliza", "Ameer", "AliGul", "Sameer"]

# for roll, name in zip(rolls, names):
#     print(f"{roll} - {name}")
# zip(rolls, names) → pairs each roll with its corresponding name.



# 10. Using pandas (advanced & professional way 📊)
# import pandas as pd

# df = pd.DataFrame(students, columns=["Roll", "Name"])
# print(df.to_string(index=False))

# pd.DataFrame() → creates a table (rows & columns).
# to_string(index=False) → prints table nicely without extra index.


# Q#3: Loop through an email list and print only those ending with `@gmail.com`.
# emails = [
#     "ali@gmail.com",
#     "sara@yahoo.com",
#     "waqar@gmail.com",
#     "ayesha@hotmail.com",
#     "sameer@gmail.com"
# ]

# 1️ Using simple for loop and str.endswith()
# for email in emails:
#     if email.endswith("@gmail.com"):
#         print(email)
# # email.endswith("@gmail.com") → checks if string ends with @gmail.com.
# print("***************************************************")


# 2. Using list comprehension
# [print(email) for email in emails if email.endswith("@gmail.com")]



# 3.Using filter() with lambda
# gmail_emails = filter(lambda e: e.endswith("@gmail.com"), emails)
# for email in gmail_emails:
#     print(email)
# filter() returns an iterator with only emails ending with @gmail.com.

# 4.Using map() with condition inside
# list(map(lambda e: print(e) if e.endswith("@gmail.com") else None, emails))


# 5.Using while loop

# i = 0
# while i < len(emails):
#     if emails[i].endswith("@gmail.com"):
#         print(emails[i])
#     i += 1


# 6.Using for loop with continue
# for email in emails:
#     if not email.endswith("@gmail.com"):
#         continue
#     print(email)



# 7.Using re module (regular expressions)
# import re

# for email in emails:
#     if re.search(r"@gmail\.com$", email):
#         print(email)
# @gmail\.com$ → matches Gmail at the end of string.

# Useful if pattern matching becomes more complex.

# 8. Using pandas (advanced, tabular)

# import pandas as pd

# df = pd.DataFrame(emails, columns=["Email"])
# gmail_emails = df[df["Email"].str.endswith("@gmail.com")]
# print(gmail_emails.to_string(index=False))


# 9. Using zip() if you have multiple listsnames = ["Ali", "Sara", "Waqar", "Ayesha", "Sameer"]
# names = ["Ali", "Sara", "Waqar", "Ayesha", "Sameer"]
# for name, email in zip(names, emails):
#     if email.endswith("@gmail.com"):
#         print(f"{name}: {email}")


# 10.Using enumerate()
# for i, email in enumerate(emails, start=1):
#     if email.endswith("@gmail.com"):
#         print(f"{i}. {email}")



#Q#4: Display all product prices from a list with “PKR” appended.
prices = [100, 250, 399, 500, 1200]
# for price in prices:
#     print(f"{price} PKR")

#2. Using list comprehension (one-liner)
# [print(f"{price} PKR") for price in prices]

#3. Using map() with lambda
list(map(lambda p: print(f"{p} PKR"), prices))