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



# Q#4: Display all product prices from a list with “PKR” appended.
# prices = [100, 250, 399, 500, 1200]
# for price in prices:
#     print(f"{price} PKR")

#2. Using list comprehension (one-liner)
# [print(f"{price} PKR") for price in prices]

#3. Using map() with lambda
# list(map(lambda p: print(f"{p} PKR"), prices))


#4. Using while loop
# i = 0;
# while i < len(prices):
#     print(f"{prices[i]} PKR")
#     i += 1


# 5. Using for loop with index (range)
# for i in range(len(prices)):
#     print(f"{prices[i]} PKR")

#6. Using enumerate()
# for idx, price in enumerate(prices, start=1):
    # print(f"{idx}. {price} PKR")
# Adds numbering automatically.


#7. Using map() to create a formatted list
# formatted_prices = list(map(lambda p: f"{p} PKR", prices))
# print(formatted_prices)

# 8.Using join()
# print("\n".join([f"{price} PKR" for price in prices]))

#9. Using for loop with continue (example if we skip prices < 300)
# for price in prices:
    # if price < 300:
    #     continue
    # print(f"{price} PKR")

#10. Using pandas (advanced / professional)
# import pandas as pd

# df = pd.DataFrame(prices, columns=["Price"])
# df["Price"] = df["Price"].astype(str) + " PKR"
# print(df.to_string(index=False))


#Q:5. Loop through contacts and mask their phone number except last 4 digits.
# contacts = [
#     {"name": "Ali", "phone": "03123456789"},
#     {"name": "Sara", "phone": "03339876543"},
#     {"name": "Waqar", "phone": "03001234567"}
# ]

# for contact in contacts:
#     phone = contact["phone"]
#     masked = "*" * (len(phone) - 4) + phone[-4:]
#     print(f"{contact['name']}: {masked}")


#1. Using String Slicing
# contacts = ["03001234567", "03451239876", "03111234555"]
# for phone in contacts:
#     masked = "*" * (len(phone) - 4) + phone[-4:]
#     print(masked)


# 2. Using String rjust()
# for number in contacts:
#     masked = number[-4:].rjust(len(number), "*")
#     print(masked)

# 3. Using str.replace() with Loop
# for number in contacts:
#     masked = number
#     for i in range(len(number) - 4):
#         masked = masked.replace(number[i], "*", 1)
#     print(masked)


# 4. Using Regex (re.sub)
# import re

# for number in contacts:
#     masked = re.sub(r".(?=.{4})", "*", number)
#     print(masked)

# 5. Using map() and Conditional Join
# for number in contacts:
#     masked = "".join(map(lambda i: "*" if i < len(number) - 4 else number[i], range(len(number))))
#     print(masked)

# 6. Using enumerate()
# for number in contacts:
#     masked = "".join("*" if idx < len(number) - 4 else digit for idx, digit in enumerate(number))
#     print(masked)


# 7. Using format() (custom padding)
# for number in contacts:
#     masked = "{:*>11}".format(number[-4:])  # assuming phone length = 11
#     print(masked)


# 8. Using str.zfill() Trick
# for number in contacts:
#     masked = ("*" * (len(number) - 4) + number[-4:]).zfill(len(number))
#     print(masked)



# 9. Using ljust() (opposite of rjust)
# for number in contacts:
#     masked = number[-4:].rjust(len(number), "*")  # same as #2 but can use ljust for reversed cases
#     print(masked)


# 10. Using Function for Reuse
# def mask_number(number, mask="*"):
#     return mask * (len(number) - 4) + number[-4:]

# for number in contacts:
#     print(mask_number(number))


# Q:6. Loop through a list of transactions and print those above 50,000 PKR.
# 1. Using a simple for loop + if
# transactions = [2000, 340000, 40000, 20000, 50000, 450000, 200000]
# for i in transactions:
#     if i > 50000:
#         print(f"{i} PKR")

# 2. Using List Comprehension
# print([f"{i} PKR" for i in transactions if i > 50000])

# 3. Using filter() with lambda
# high_transactions = filter(lambda x: x > 50000, transactions)
# for i in high_transactions:
#     print(f"{i} PKR")

# 4.Using enumerate() (if you also want index)
# for i, t in enumerate(transactions):
#     if t > 50000:
#         # print(f"Transaction #{i}: {t} PKR")
#         print(f"Transaction #{i + 1}: {t} PKR")

# 5. Using map() + filter() (Functional style)
# result = map(lambda x: f"{x} PKR", filter(lambda x: x > 50000, transactions))
# print(list(result))


# 6. Using any() to check if such transactions exist
# if any(t > 50000 for t in transactions):
#     print("Transactions above 50,000 PKR found!")


#7. Using all() to check if all are above 50,000
# if all(t > 50000 for t in transactions):
#     print("All transactions are above 50,000 PKR")
# else:
#     print("Not all transactions are above 50,000 PKR")

# 8.Using while loop
# i = 0
# while i < len(transactions):
#     if transactions[i] > 50000:
#         print(f"{transactions[i]} PKR")
#     i += 1


#9. Using list(filter(...)) directly
# print(list(filter(lambda t: t > 50000, transactions)))


# 10. Using NumPy (when dealing with huge datasets)
# import numpy as np
# arr = np.array(transactions)
# print(arr[arr > 50000])   # Prints only those above 50,000




# Q:7. Print all words from a sentence in reverse order.
# 1.Using a for loop (manual reversal)
# sentence = "I am happy"
# words = sentence.split()

# reversed_words = []

# for i in range(len(words) -1, -1, -1): # loop backwards
#     reversed_words.append(words[i])
# print(" ".join(reversed_words))   # Output: Python love I


# 2: Using split() + [::-1] (Pythonic way)
# sentence = "I love Python"

# # Step 1: Split sentence into words → ['I', 'love', 'Python']
# words = sentence.split()

# # Step 2: Reverse the list of words
# reversed_words = words[::-1]

# # Step 3: Join back into a string
# result = " ".join(reversed_words)

# print(result)   # Output: Python love I


# 3.Using split() + reversed()
# sentence = "I love Python"

# reversed() returns an iterator, not a list
# reversed_words = reversed(sentence.split())

# result = " ".join(reversed_words)
# print(result)   # Output: Python love I



#4. Using while loop

# words = sentence.split()

# i = len(words) - 1
# reversed_words = []
# while i >= 0:
#     reversed_words.append(words[i])
#     i -= 1

# print(" ".join(reversed_words))   # Output: Python love I


# 5: Using stack (LIFO concept)
# words = sentence.split()

# stack = []
# for word in words:
#     stack.append(word)

# reversed_words = []
# while stack:
#     reversed_words.append(stack.pop())   # LIFO pop

# print(" ".join(reversed_words))   # Output: Python love I


#6. Using list comprehension

# words = sentence.split()

# reversed_words = [words[i] for i in range(len(words)-1, -1, -1)]

# print(" ".join(reversed_words))   # Output: Python love I


# 7.Using recursion
# def reverse_words(words):
#     if len(words) == 0:
#         return []
#     return [words[-1]] + reverse_words(words[:-1])

# sentence = "I love Python"
# words = sentence.split()
# result = " ".join(reverse_words(words))

# print(result)   # Output: Python love I


# 8. Using collections.deque (double-ended queue)
# from collections import deque


# words = sentence.split()

# dq = deque(words)
# reversed_words = []

# while dq:
#     reversed_words.append(dq.pop())

# print(" ".join(reversed_words))   # Output: Python love I


# 9.Using reduce() from functools
# from functools import reduce

# words = sentence.split()

# result = reduce(lambda x, y: y + " " + x, words)
# print(result)   # Output: Python love I

# 10. Using one-liner Pythonic style

# print(" ".join(sentence.split()[::-1]))   # Output: Python love I




# Q:8. Loop through a shopping cart and print “Out of stock” if quantity = 0.
# shopping_cart = [
#     {"item": "Laptop", "quantity": 2},
#     {"item": "Phone", "quantity": 0},
#     {"item": "Headphones", "quantity": 5},
#     {"item": "Charger", "quantity": 0}
# ]

#1. Simple for loop with if
# Loop through each product in shopping_cart
# import sys
# sys.stdout.reconfigure(encoding='utf-8')
# for product in shopping_cart:
#      # Check if product quantity is 0
#     if product["quantity"] == 0:
#         print(product["item"], "→ Out of stock")  # Print with item name
#         # print(product["item"], "\u2192 Out of stock")  # Unicode arrow
        


# 2. Using range(len(...))
# Loop using index with range() function
# for i in range(len(shopping_cart)):
#     # Access product by index
#     product = shopping_cart[i]
#     # check if quantity is 0
#     if product["quantity"] == 0:
#         print(product["item"], "=> Out of stock")


# 3.Using enumerate() for index + value

# Loop with enumerate() → gives both index and product
# for index, product in enumerate(shopping_cart):
#     if product["quantity"] == 0:
#         print(f"Index {index}: {product['item']} -> Out of stock")



# 4.List comprehension (inline filtering)
# List comprehension → collects out of stock items
# out_of_stock = [p["item"] for p in shopping_cart if p["quantity"] == 0]
# # Print each out of stock item

# for item in out_of_stock:
#     print(item, "-> Out of stock")



# 5. Using filter() function
# Use filter() to get only items with quantity == 0
# out_of_stock_items = filter(lambda p: p["quantity"] == 0, shopping_cart)

# # Loop through the filtered result
# for product in out_of_stock_items:
#     print(product["item"], "-> Out of stock")


# 6. Using zip() with item names and quantities

# Extract names and quantities separately
# items = [p["item"] for p in shopping_cart]
# quantities = [p["quantity"] for p in shopping_cart]

# # Use zip to pair each item with its quantity
# for item, qyt in zip(items, quantities):
#     if qyt == 0:
#         print(item, "-> Out of stock")


# 9. Print all pending tasks from a to-do list.

# todo_list = [
#     {"title": "Buy groceries", "status": "pending"},
#     {"title": "Pay bills", "status": "done"},
#     {"title": "Finish assignment", "status": "pending"},
#     {"title": "Call mom", "status": "in-progress"},
#     {"title": "Book tickets", "status": "PENDING"},
    
# ]
# 1.Simple for-loop + normalize status (most common)
# for i in todo_list:
#     # Normalize status to lower-case so 'Pending', 'PENDING' also count
#     status = i["status"].strip().lower()
#     if status == "pending":
#         print(i["title"], "-> pending")

# 2. For-loop with a helper set of “pending-like” statuses

# pending_labels = {"pending", "todo", "not-started", "open"}
# for t in todo_list:
#     if t["status"].strip().lower() in pending_labels:
#         print(t["title"], "-> pending")


# 3. List comprehension to collect pending, then print
# pending = [t for t in todo_list if t["status"].strip().lower() == "done"]
# pending = [t for t in todo_list if t["status"].strip().lower() == "pending"]
# for t in pending:
#     # print(t["title"], "-> done")
#     print(t["title"], "-> pending")



# 4.filter() + lambda

# pending_iter = filter(lambda t: t["status"].strip().lower() == "pending", todo_list)
# for t in pending_iter:
#     print(t["title"], "-> pending")



# 5.enumerate() (if you also want the index)
# for i, t in enumerate(todo_list, start=1):
#     if t["status"].strip().lower() == "pending":
#         print(f"{i}. {t['title']} -> pending")


# 6. Index-based loop (range/len)
# for i in range(len( todo_list )):
#     if  todo_list [i]["status"].strip().lower() == "pending":
#         print( todo_list [i]["title"], "-> pending")


#7. while-loop (classic style)
# i = 0
# while i < len(todo_list):
#     if todo_list[i]["status"].strip().lower() == "pending":
#         print(todo_list[i]["title"], "-> pending")
#     i += 1



# 8.Reusable function (cleanest for real projects)

# def print_pending(todo_list, pending_labels=("pending",)):
#     # Convert tuple to set once for fast membership checks
#     labels = {s.lower() for s in pending_labels}
#     for t in todo_list:
#         if t.get("status", "").strip().lower() in labels:
#             print(t.get("title", "<no title>"), "-> pending")

# print_pending(todo_list)  # default looks for "pending" only
# # print_pending(tasks, pending_labels=("pending", "open", "todo"))



# Q#10: Print first 5 notifications from a list.
# notifications list
# notifications = [
#     "New message from Ali",
#     "Your order has been shipped",
#     "Password change successful",
#     "Meeting at 3 PM",
#     "Assignment due tomorrow",
#     "Update available for your app",
#     "New follower request",
#     "Low battery warning"
# ]


# 1. Using for loop with range
# Loop only over the first 5 indexes (0 to 4)
# for i in range(5):
#     print(notifications[i])  # print notification at index i



# 2. Using for loop directly with slicing
# Loop only over the first 5 elements using slicing

# for notification in notifications[:5]:
#     print(notification)  # Print each
# notifications[:5] slices list from index 0 to 4.

# 3. Using while loop

# Start index at 0
# i = 0

# # Run loop until index is less than 5
# while i < 5:
#     print(notifications[i]) # print notification at index i
#     i += 1 # Increase index by 1




#4. Using enumerate with condition
# enumerate gives index + value
# for index, notification in enumerate(notifications):
#     if index < 5: # Print only if index is less than 5
#         print(notification)

# 5. Using itertools.islice (Pythonic way)
# import itertools  # Import itertools module

# # islice allows slicing while iterating
# for notification in itertools.islice(notifications, 5): # islice(list, stop=5)
#     print(notification)


# 6. Using list comprehension
# Create a list of first 5 notifications and print them
# [print(notification) for notification in notifications[:5]]


# 7. Using map() function
# Use map with slicing
# list(map(print, notifications[:5]))  # map applies print to each element




# 11. Explain difference between `for item in list:` and `for i in range(len(list)):`
"""11. Difference between for item in list: and for i in range(len(list)):

🔹 Style 1: for item in list:

Directly loops over each element.

You don’t care about the index.

Pythonic, clean, more readable.

fruits = ["apple", "banana", "cherry"]

# Looping directly over elements
for fruit in fruits:   # fruit takes values: "apple", "banana", "cherry"
    print(fruit)       # ✅ Clean, readable


🔹 Style 2: for i in range(len(list)):

Loops over index numbers from 0 to len(list)-1.

You need the index to access elements or do index-based operations.

fruits = ["apple", "banana", "cherry"]

# Looping using index
for i in range(len(fruits)):   # i takes values: 0, 1, 2
    print(i, fruits[i])        # prints index + element


✅ Key Points / Interview-Ready Comparison:

for item in list: → best when you just need values.

for i in range(len(list)): → best when you need both index & value.

If you need both index and value together, Python gives enumerate() (preferred way).

for i, fruit in enumerate(fruits):
    print(i, fruit)   # Cleaner than range(len(list))


👉 Interview Tip: Say that enumerate is the most Pythonic when both index & value are needed."""


# 12. How does Python handle iterators internally in for loops?
"""When you write:

for item in my_list:
    print(item)


🔎 What actually happens inside Python:

Python calls iter(my_list) → creates an iterator object.

Then it repeatedly calls next(iterator) to get each element.

When the iterator is exhausted, it raises StopIteration.

The for loop catches that exception and exits gracefully.

💡 Example using iterator manually (what for does behind the scenes):

fruits = ["apple", "banana", "cherry"]

# Step 1: Create iterator
it = iter(fruits)

# Step 2: Fetch elements using next()
print(next(it))  # apple
print(next(it))  # banana
print(next(it))  # cherry

# Step 3: If you call again, StopIteration will be raised
# print(next(it))  # ❌ StopIteration


✅ Key Points (easy to memorize for interview):

A for loop in Python = iter() + repeated next() calls.

It stops automatically when StopIteration is raised.

This makes for loops work not only on lists, but on any iterable (lists, tuples, sets, dicts, files, generators)."""

# Quick Interview Answer:

# "for item in list: is used to directly get values, while for i in range(len(list)): is index-based looping. In real projects, enumerate is preferred when both index and value are needed.

# Internally, Python’s for loop converts the iterable into an iterator using iter(), then repeatedly calls next() until StopIteration is raised, which makes it work for any iterable, not just lists."