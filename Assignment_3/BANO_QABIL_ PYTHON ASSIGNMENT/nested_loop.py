# Section C: Nested Loops (Real-World + Interview Qs)
"""
What is a Nested Loop?

A nested loop means: one loop runs inside another loop.

Think of it like:

Outer loop = rows

Inner loop = columns

👉 So the outer loop controls how many times the whole process repeats, and the inner loop controls the details inside each step.

🔹 Real-World Examples

Classroom seating

Outer loop: Rows of benches

Inner loop: Students sitting in each bench

Clock

Outer loop: Hours (1–12)

Inner loop: Minutes (0–59)

Shopping Mall

Outer loop: Floors

Inner loop: Shops on each floor

🔹 Python Example 1: Multiplication Table (classic)
for i in range(1, 4):        # Outer loop → rows
    for j in range(1, 4):    # Inner loop → columns
        print(i * j, end=" ")
    print()   # Move to next row


📌 Output:

1 2 3
2 4 6
3 6 9
"""


# Q:23. Print all seat numbers in cinema (Rows A–C, Seats 1–5 → A1, A2...).
# Cinema Seat Generator

# rows = ["A", "B", "C"]          # Define rows
# seats = range(1, 6)             # Define seats (1–5)
# for row in rows:                 # Outer loop → rows
#     for seat in seats:           # Inner loop → seats
#         print(f"{row}{seat}", end=" ")  # Print seat number
#     print()  # Move to next row                             


# Other ways
# Way 2: Using while loops
# rows = ["A", "B", "C"] # rows defined
# seats = range(1, 6)  # seats defined
# i = 0
# while i < len(rows):          # outer loop for rows
#     j = 1                     # start seat count at 1
#     while j <= 5:             # inner loop for seats
#         print(f"{rows[i]}{j}", end=" ")  # print seat
#         j += 1                # next seat
#     print()                   # next row
#     i += 1   


# Way:3 Using List Comprehension
# rows = ["A", "B", "C"]
# seats = range(1, 6)

# all_seats = [f"{row}{seat}" for row in rows for seat in seats]
# # f"{row}{seat}" → combine row+seat
# # for row in rows → outer loop
# # for seat in seats → inner loop
# print(all_seats)  # prints as list
# for row in rows:
#     print(" ".join(f"{row}{seat}" for seat in seats))
#     # " ".join([...]) → join items with spaces


# Way:4 Using itertools.product
# import itertools
# rows = ["A", "B", "C"]
# seats = range(1, 6)
# # for row, seat in itertools.product(rows, seats):
# #     print(f"{row}{seat}", end=" ")
# for row in rows:
#     for seat in seats:
#         print(f"{row}{seat}", end=" ")
#     print()

"""
What is itertools?

itertools is a Python standard library module (comes built-in with Python).

It provides fast, memory-efficient tools for handling iterators (things you can loop over).

Instead of writing complicated nested loops, itertools gives you ready-made functions.

Think of it like a toolbox for loops and combinations.

🔹 Why use itertools?

Saves code → Write less, do more.

Memory-efficient → Creates results on the fly (lazy evaluation), doesn’t store everything in memory at once.

Readable → Instead of 3 nested loops, just one line with itertools.product.

Useful in real life → Combinations, permutations, grouping, infinite sequences, etc.
"""



#Way5: Dictionary Mapping (row → seats)
# rows = ["A", "B", "C"]
# seats = range(1, 6)

# seat_map = {row: [f"{row}{seat}" for seat in seats] for row in rows}
# # dictionary comprehension → row : list of seats

# print(seat_map)

# -------------------------------
#  3: Print row by row
# # -------------------------------
# for row, seat_list in seat_map.items():
#     print(" ".join(seat_list))



# Q:24. Generate all shirt–pant combinations from 2 lists.
# list1 = ["Red Shirt", "Blue Shirt"]
# list2 = ["Black Pant", "White Pant"]
# for shirt in list1:
#     for pant in list2:
#         print(f"{shirt} + {pant}")  



# Other ways
# -------------------------------
# #  1: Define lists
# # -------------------------------
# shirts = ["Red", "Blue"]       # list of shirts
# pants = ["Black", "White"]     # list of pants


# # -------------------------------
# #  2: Outer loop (shirts)
# # -------------------------------
# for shirt in shirts:           # for → keyword, shirt = "Red", then "Blue"
#     print(shirt)               # just checking shirt values


# # -------------------------------
# #  3: Add inner loop (pants)
# # -------------------------------
# for shirt in shirts:               # outer loop for shirts
#     for pant in pants:             # inner loop for pants
#         print(pant)                # print pant values


# # -------------------------------
# #  4: Combine shirt + pant
# # -------------------------------
# for shirt in shirts:               # take one shirt
#     for pant in pants:             # match with every pant
#         print(f"{shirt} - {pant}") # print combination
#     print()                        # move to next line after all pants



# 2: Using while 

# shirts = ["Red", "Blue"]
# pants = ["Black", "White"]
# i = 0
# while i < len(shirts):             # outer loop
#     j = 0
#     while j < len(pants):          # inner loop
#         print(f"{shirts[i]} - {pants[j]}")
#         j += 1                     # move to next pant
#     i += 1    



# 3: List Comprehension
# shirts = ["Red", "Blue"]
# pants = ["Black", "White"]

# combinations = [f"{s} - {p}" for s in shirts for p in pants]
# # s → shirt, p → pant
# # for s in shirts → outer loop
# # for p in pants → inner loop

# print(combinations)


# 4: Using itertools.product
# import itertools

# shirts = ["Red", "Blue"]
# pants = ["Black", "White"]

# # -------------------------------
# #  2: Use product()
# # -------------------------------
# for s, p in itertools.product(shirts, pants):
#     print(f"{s} - {p}")



# 5: Dictionary Mapping (Optional Creative Way)
# shirts = ["Red", "Blue"]
# pants = ["Black", "White"]

# shirt_pant_map = {s: [f"{s} - {p}" for p in pants] for s in shirts}
# # dictionary: shirt → all pant combinations

# # -------------------------------
# #  2: Print combinations
# # -------------------------------
# for shirt, combos in shirt_pant_map.items():
#     for combo in combos:
#         print(combo)



#Q:25. Print every minute from 12:00 → 12:10.
# for hour in range(12, 13):          # Outer loop → hours
#     for minute in range(0, 11):     # Inner loop → minutes
#         print(f"{hour}:{minute:02}")
#         # :02 → pad with 0 if single digit (e.g. 1 →
#         # 01, 2 → 02)
# # Output:
# # 12:00


# Other ways
# hour = 12  # : Initialize hour as 12
# minute = 0  # : Initialize minute as 0

# : Loop until minute reaches 11 (exclusive, stops at 10)
# while minute <= 10:
#     print(f"{hour}:{minute:02d}")  # : Print current time with 2-digit minutes
#     minute += 1  # : Increment minute by 1
# # : End of While Loop Approach

# hour = 12  # : Initialize hour as 12
# minute = 0  # : Initialize minute as 0



# # : Loop until minute reaches 11 (exclusive, stops at 10)
# while minute <= 10:
#     print(f"{hour}:{minute:02d}")  # : Print current time with 2-digit minutes
#     minute += 1  # : Increment minute by 1
# # : End of While Loop Approach


# : Start of List Comprehension Approach
# [print(f"12:{m:02d}") for m in range(11)]  # : Generate and print times in one line



# Using Function + Yield (Generator)
# ----------------------------------------------------
# : Start of Generator Approach
# def time_generator():  # : Define generator function
#     for m in range(11):  # : Loop minutes 0-10
#         yield f"12:{m:02d}"  # : Yield formatted string instead of printing

# for t in time_generator():  # : Iterate over generator
#     print(t)  # : Print generated time
# # : End of Generator Approach


# from datetime import datetime, timedelta  # : Import datetime and timedelta classes

# start = datetime(2025, 1, 1, 12, 0)  # : Set starting time as 12:00
# for i in range(11):  # : Loop 11 times
#     time = start + timedelta(minutes=i)  # : Add i minutes to starting time
#     print(time.strftime("%H:%M"))  # : Format and print hour:minute
# # : End of Datetime Approach



# Using Map Function
# ----------------------------------------------------
# : Start of Map Approach
# def format_minute(m):  # : Define formatter function
#     return f"12:{m:02d}"  # : Return formatted string

# list(map(lambda m: print(format_minute(m)), range(11)))  # : Apply map to print times
# # : End of Map Approach



# import itertools  # : Import itertools

# for minute in itertools.count(start=0, step=1):  # : Infinite counter starting at 0
#     if minute > 10:  # : Stop at minute 10
#         break  # : Exit loop
#     print(f"12:{minute:02d}")  # : Print current time
# # : End of itertools Approach




#Q:26. Nested loop to show timetable: Days 1–3, Slots Morning/Evening.
# days = [1, 2, 3]                 # Define days
# slots = ["Morning", "Evening"]    # Define slots
# for day in days:                  # Outer loop → days
#     for slot in slots:            # Inner loop → slots
#         print(f"Day {day} - {slot}")    
#     print()  # Move to next day
# # Output:   
# # Day 1 - Morning
# # Day 1 - Evening


# Other ways
# Using while Loop (Nested)
# days = [1, 2, 3]  # : Define list of days
# slots = ["Morning", "Evening"]  # : Define list of slots

# i = 0  # : Day index start
# while i < len(days):  # : Outer while loop for days
#     print(f"Day {days[i]}")  # : Print current day
#     j = 0  # : Slot index start
#     while j < len(slots):  # : Inner while loop for slots
#         print(f" - {slots[j]}")  # : Print current slot
#         j += 1  # : Move to next slot
#     i += 1  # : Move to next day


# Using Dictionary of Days → Slots
# timetable = {1: ["Morning", "Evening"],
#              2: ["Morning", "Evening"],
#              3: ["Morning", "Evening"]}  # : Map each day to slots

# # : Loop through dictionary
# for day, slots in timetable.items():
#     print(f"Day {day}")  # : Print current day
#     for slot in slots:  # : Loop over slots
#         print(f" - {slot}")  # : Print slot


# Using List Comprehension
# days = [1, 2, 3]  # : Define days
# slots = ["Morning", "Evening"]  # : Define slots

# # : Generate all combinations
# timetable = [(day, slot) for day in days for slot in slots]

# # : Print results
# for day, slot in timetable:
#     print(f"Day {day} - {slot}")


# Using itertools.product
# from itertools import product  # : Import product function

# days = [1, 2, 3]  # : Define days
# slots = ["Morning", "Evening"]  # : Define slots

# # : Use product to generate combinations
# for day, slot in product(days, slots):
#     print(f"Day {day} - {slot}")  # : Print combination






#Q:27. Print seating chart for bus (Rows 1–3, Seats A–D).
# rows = [1, 2, 3]                # Define rows
# seats = ["A", "B", "C", "D"]  # Define seats
# for row in rows:
#     for seat in seats:
#         print(f"Row {row} - Seat {seat}")
#     print()  # Move to next row
# # Output:
# # Row 1 - Seat A
# # Row 1 - Seat B


# 2. Using While Loop
# row = 1  # : Start from row 1
# while row <= 3:  # : Continue until row 3
#     seat_index = 0  # : Reset seat index for each row
#     while seat_index < 4:  # : Loop over 4 seats
#         seat = chr(65 + seat_index)  # : Convert number to letter (A–D)
#         print(f"Row {row} Seat {seat}")  # : Print seat
#         seat_index += 1  # : Move to next seat
#     row += 1  # : Move to next row


# 3. Using List Comprehension
# rows = range(1, 4)
# seats = ["A", "B", "C", "D"]
# # seating_chart = [f"Row {r} Seat {s}" for r in rows for s in seats]
# # for entry in seating_chart:
# #     print(entry)
# [print(f"Row {row} Seat {seat}")  for row in rows for seat in seats ]# prints as list


# 4. Using itertools.product
# import itertools

# rows = range(1, 4)  # : Define rows
# seats = ['A', 'B', 'C', 'D']  # : Define seats

# # : Use product to generate row-seat pairs
# for row, seat in itertools.product(rows, seats):
#     print(f"Row {row} Seat {seat}")  # : Print seat


# 5. Storing Chart in a List (Beginner Data Structure Use)
# : Start of List Storage Approach
# rows = range(1, 4)  # : Rows 1–3
# seats = ['A', 'B', 'C', 'D']  # : Seats A–D

# seating_chart = []  # : Empty list to store chart

# # : Create seating chart
# for row in rows:
#     for seat in seats:
#         seating_chart.append(f"Row {row} Seat {seat}")

# # : Print chart
# for seat in seating_chart:
#     print(seat)
# # : End of List Storage Approach


#Q:28. Print a Tic-Tac-Toe 3×3 board.
# for row in range(3):            # Outer loop → rows
#     for col in range(3):        # Inner loop → columns
#         print(f"({row}, {col})", end=" ")  # Print cell coordinates
#     print()  # Move to next row
# # Output:
# # (0, 0) (0, 1) (0, 2)


# Other ways
# : Start of Simple Print Approach

# print("Tic-Tac-Toe Board")  # : Title for clarity
# print("-------------")      # : Top border
# print("|   |   |   |")      # : First row
# print("-------------")      # : Separator
# print("|   |   |   |")      # : Second row
# print("-------------")      # : Separator
# print("|   |   |   |")      # : Third row
# print("-------------")      # : Bottom border

# : Start of Loop Approach

# print("Tic-Tac-Toe Board (Loop)")  # : Title

# for row in range(3):  # : Loop for 3 rows
#     print("-------------")          # : Print row separator
#     print("|   |   |   |")          # : Print empty row
# print("-------------")              # : Final bottom border

# # : End of Loop Approach



# print("Tic-Tac-Toe Board (Loop)")  # Commit: Title

# for row in range(3):  # Commit: Loop for 3 rows
#     print("-------------")          # Commit: Print row separator
#     print("|   |   |   |")          # Commit: Print empty row
# print("-------------")              # Commit: Final bottom border


# print("Tic-Tac-Toe Board (Nested Loop)")  # Commit: Title

# for row in range(3):        # Commit: Outer loop for rows
#     print("-------------")   # Commit: Print border before each row
#     for col in range(3):    # Commit: Inner loop for 3 cells
#         print("|   ", end="")  # Commit: Print each cell with border
#     print("|")              # Commit: End the row with right border
# print("-------------")       # Commit: Bottom border

# 4: Using List Representation
# Commit: Start of List Representation Approach

# print("Tic-Tac-Toe Board (List)")  # Commit: Title

# board = [[" " for _ in range(3)] for _ in range(3)]  # Commit: Create 3×3 grid

# for row in board:                          # Commit: Loop through rows
#     print("-------------")                  # Commit: Border before row
#     print("| " + " | ".join(row) + " |")    # Commit: Join cells with |
# print("-------------")                      # Commit: Bottom border



# 29. Print a star pyramid pattern.
# rows = 5                          # Number of rows
# for i in range(rows):            # Outer loop → rows
#     for j in range(rows - i - 1):  # Inner loop → spaces
#         print(" ", end="")         # Print space
#     for k in range(2 * i + 1):     # Inner loop → stars
#         print("*", end="")         # Print star
#     print()  # Move to next row



# rows = 5  # Number of rows in the pyramid

# for i in range(1, rows + 1):
#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")
#     # Print stars
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()  # New line after each row


# Using string multiplication
# rows = 5

# for i in range(1, rows + 1):
#     spaces = " " * (rows - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)

# Using str.center()
# rows = 5
# for i in range(1, rows + 1):
#     stars = "*" * (2 * i - 1)
#     print(stars.center(2 * rows - 1))  # Center stars in the width of the base


# Using recursion
# def print_pyramid(n, row=1):
#     if row > n:
#         return
#     spaces = " " * (n - row)
#     stars = "*" * (2 * row - 1)
#     print(spaces + stars)
#     print_pyramid(n, row + 1)

# print_pyramid(5)


# Using while loop
# rows = 5
# i = 1

# while i <= rows:
#     print(" " * (rows - i) + "*" * (2 * i - 1))
#     i += 1


# Using List Comprehension + join
# Commit: Pyramid using list comprehension
# rows = 5

# [print(" " * (rows - i) + "*" * (2 * i - 1)) for i in range(1, rows + 1)]





# Q:30. Nested loop to find all team pairs from player list.
# players = ["Asad", "Ameer", "Sameer", "Wasim"]
# # Outer loop: each player
# for i in range(len(players)):
#     # Inner loop: next players (avoid duplicates & self)
#     for j in range(i + 1, len(players)):
#         print(players[i], "vs", players[j])


# Direct Nested Loop with Condition

# for p1 in players:              # pick first player
#     for p2 in players:          # pick second player
#         if p1 != p2:            # avoid same player
#             if players.index(p1) < players.index(p2):  # avoid duplicates
#                 print(p1, "vs", p2)


# Using itertools.combinations
# import itertools
# # combinations gives all unique 2-player groups
# for pair in itertools.combinations(players, 2):
#     print(pair[0], "vs", pair[1])

# List Comprehension
# pairs = [(players[i], players[j]) 
#          for i in range(len(players)) 
#          for j in range(i+1, len(players))]

# print(pairs)


# While Loop Version
# i = 0
# while i < len(players):
#     j = i + 1
#     while j < len(players):
#         print(players[i], "vs", players[j])
#         j += 1
#     i += 1






# Q:31. Generate full multiplication tables from 2–5.
# for i in range(2, 6):       # Tables 2 to 5
#     print(f"\n--- Table of {i} ---")
#     for j in range(1, 11):  # Multipliers 1 to 10
#         print(f"{i} x {j} = {i*j}")


# While Loops
# i = 2
# while i <= 5: # Tables 2 to 5
#     print(f"\n--- Table of {i} ---")
#     j = 1
#     while j <= 10:  # Multipliers 1 to 10
#         print(f"{i} x {j} = {i * j}")
#         j += 1
#     i += 1



# List Comprehension (Flat List)
# One-liner style
# tables = [f"{i} x {j} = {i*j}" for i in range(2, 6) for j in range(1, 11)]
# print("\n".join(tables))


# Dictionary of Tables
# Store each table in dictionary
# tables = {i: [f"{i} x {j} = {i*j}" for j in range(1, 11)] for i in range(2, 6)}

# for k, v in tables.items():
#     print(f"\n--- Table of {k} ---")
#     print("\n".join(v))


# Function-based Approach
# Function to generate one table
# def multiplication_table(n):
#     return [f"{n} x {j} = {n*j}" for j in range(1, 11)]

# for i in range(2, 6):
#     print(f"\n--- Table of {i} ---")
#     print("\n".join(multiplication_table(i)))


# itertools.product
# import itertools

# # Cartesian product of tables and multipliers
# for i, j in itertools.product(range(2, 6), range(1, 11)):
#     print(f"{i} x {j} = {i*j}")

# Using map()
# map with lambda
# for i in range(2, 6):
#     print(f"\n--- Table of {i} ---")
#     list(map(lambda j: print(f"{i} x {j} = {i*j}"), range(1, 11)))





#Q:32. Print shopping categories and their products.
# shopping_categories = ["Fruits", "Vegetables", "Dairy"]
# products = ["Apple", "Banana", "Carrot", "Milk", "Cheese"]
# for i in shopping_categories:
#     for j in products:
#         print(f"{i} - {j}")
#     print()  # Move to next category



# Categories with products
# categories = {
#     "Fruits": ["Apple", "Banana", "Mango"],
#     "Vegetables": ["Carrot", "Potato", "Tomato"],
#     "Dairy": ["Milk", "Cheese", "Butter"]
# }

# # Loop through dictionary
# for category, products in categories.items():  
#     print(f"🛒 Category: {category}")   # Commit: Print category name
#     for product in products:  
#         print(f"   - {product}")        # Commit: Print each product under category




# Using dict + Index Numbers
# Commit: Create dictionary of categories with lists
# categories = {
#     "Fruits": ["Apple", "Banana", "Mango"],
#     "Vegetables": ["Carrot", "Potato", "Tomato"],
#     "Dairy": ["Milk", "Cheese", "Butter"]
# }

# # Commit: Enumerate categories for numbering
# for idx, (category, products) in enumerate(categories.items(), start=1):  
#     print(f"{idx}. {category}")   # Commit: Print numbered category
#     for p_idx, product in enumerate(products, start=1):  
#         print(f"   {idx}.{p_idx} {product}")  # Commit: Number each product




# Using zip with Separate Lists
# categories = ["Fruits", "Vegetables", "Dairy"]
# products = [
#     ["Apple", "Banana", "Mango"],
#     ["Carrot", "Potato", "Tomato"],
#     ["Milk", "Cheese", "Butter"]
# ]

# for category, product_list in zip(categories, products):
#     print(f"[Category] {category}")  
#     for product in product_list:
#         print(f"   - {product}")


# Using itertools.product (Advanced but useful)
# import itertools

# # Commit: Create dict of categories
# categories = {
#     "Fruits": ["Apple", "Banana"],
#     "Dairy": ["Milk", "Butter"]
# }

# # Commit: Cartesian product - all category-product pairs
# for category, products in categories.items():
#     for combo in itertools.product([category], products):
#         print(combo)  # Commit: Prints (Category, Product) pairs



# Way 5: Using List Comprehension
# categories = {
#     "Fruits": ["Apple", "Banana"],
#     "Vegetables": ["Carrot", "Potato"]
# }

# # Commit: Flatten structure into tuples
# pairs = [(cat, product) for cat, products in categories.items() for product in products]

# # Commit: Print pairs
# for category, product in pairs:
#     print(f"{category} -> {product}")





# Interview Qs:
# 33. Time complexity of nested loops?
# 34. When would you replace nested loops with list comprehensions?


"""
3. Time Complexity of Nested Loops?

👉 Definition in easy words:
Time complexity means how many times your code runs compared to the size of input.

Single loop:

for i in range(n):
    print(i)


Runs n times → O(n).

Nested loop:

for i in range(n):
    for j in range(n):
        print(i, j)


Outer loop → runs n times.

Inner loop → runs n times for each outer loop.

Total = n × n = n²

👉 So complexity = O(n²) (quadratic).

💡 General rule:

k nested loops → O(nᵏ)

Example: 3 nested loops = O(n³).

🔑 Interview punchline:
Nested loops multiply their complexities. That’s why they get slower quickly as n grows.




34. When would you replace nested loops with list comprehensions?

👉 List comprehensions are a Python shortcut to make lists in one line instead of using nested loops.

Example with nested loops:
pairs = []
for x in [1, 2, 3]:
    for y in [4, 5]:
        pairs.append((x, y))
print(pairs)

Same with list comprehension:
pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5]]
print(pairs)


👉 When to replace?

✅ If the nested loop is only for building a list.

✅ If readability improves (short and clear).

❌ If logic is complex (more conditions, many steps), keep normal loops for clarity.

🌟 Super Simple Analogy

Nested loops = step-by-step recipe → detailed but long.

List comprehension = shortcut recipe → same dish, fewer words.

✨ Final short interview answer:

Nested loop time complexity is multiplicative, e.g., O(n²) for two loops.

List comprehensions are best when you just need to build a list in a compact, Pythonic way; they replace nested loops when readability is improved, but not when logic is too complex.

"""