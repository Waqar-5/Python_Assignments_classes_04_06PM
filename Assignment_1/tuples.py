# Tuples (Q28–Q32)
# Q:28. Create a tuple of 5 countries. Try changing the 2nd country and observe what happens.
# Q:28. Create a tuple of 5 countries. Try changing the 2nd country and observe what happens.

# Step 1: Create a tuple of 5 countries
countries = ("Pakistan", "China", "Iran", "Thailand", "Australia", "Pakistan")

# Step 2: Try to print the tuple
print("Original tuple:", countries)

# Step 3: Try to change the second country (index 1)
# This line will cause an error because tuples are immutable
# countries[1] = "Japan"  # ❌ Not allowed

print("****************************************")
# Q:29. Print the last two countries using slicing.

print("Original tuple:", countries)

# Using slicing to get the last two elements
last_two = countries[-2:]  # This means: from second last to end

# Print the result
print("Last two countries:", last_two)


print("*************************************************")
# Q:30. Count how many times "Pakistan" appears in a tuple.

# Print original tuple
print("Original tuple:", countries)

# Use count() to count "Pakistan"
count_pakistan = countries.count("Pakistan")

# Print the count
print("Counting 'Pakistan' in countries tuple:", count_pakistan)



print("*************************************************")
# Q:31. Given: `t = (1, 2, 3, [4, 5])`. Add 6 to the list inside the tuple and explain the result.
t = (1, 2, 3, [4, 5])
print("Original tuple: ", t)
t[3].append(6)   # ✅ append 6 to the list inside the tuple
print("Updated tuple:", t)

"""
t = (1, 2, 3, [4, 5], [6,7])
t[4].append(8)   # ✅ append 6 to the list inside the tuple
print("Updated tuple:", t)
"""

print("********************************************************")
# Q:32. Convert tuple `(1, 2, 3)` to string "1-2-3" using `join()`.
num_tuple = (1, 2, 3)
print("Original tuple : ", num_tuple)
# Convert each number to string using map(), then join with '-'
converted_string = "-".join(map(str, num_tuple))

print("After converting tuple to string and joining:", converted_string)





"""

 Tuples – Key Points
Immutable (can't change).

Use round brackets ().

Access with index: t[0].

Faster than lists.

Store mixed data.

Support .count() and .index().

Used for fixed data (like dates).

Can loop through.

Takes less memory.

One item tuple: (5,) (don’t forget comma).




From my side
# tuples.py

Awesome Things Every Developer Should Know About Tuples in Python

# 1️⃣ Tuples are Immutable
example = (1, 2, 3)
# example[0] = 10  ❌ Error: Tuples can't be changed after creation

# 2️⃣ Tuples can store mixed data types
mixed = (1, "hello", 3.14, True)

# 3️⃣ You can create a tuple without parentheses (Python adds them)
implicit = 1, 2, 3  # Still a tuple

# 4️⃣ A single-item tuple must have a comma
single = (5,)  # ✅ tuple
not_a_tuple = (5)  # ❌ this is just an int

# 5️⃣ Tuples are faster than lists (good for fixed data)
import timeit
print("List time:", timeit.timeit(stmt="[1,2,3,4,5]", number=1000000))
print("Tuple time:", timeit.timeit(stmt="(1,2,3,4,5)", number=1000000))

# 6️⃣ You can unpack tuples
a, b, c = (10, 20, 30)
print("Unpacked:", a, b, c)

# 7️⃣ Use tuples to swap values quickly
x, y = 5, 10
x, y = y, x
print("Swapped:", x, y)

# 8️⃣ Tuples support all common operations: indexing, slicing, len, count, index
t = (10, 20, 30, 10)
print("Index 1:", t[1])         # 20
print("Slice:", t[1:3])         # (20, 30)
print("Count of 10:", t.count(10))
print("Index of 30:", t.index(30))

# 9️⃣ Tuples can be nested
nested = (1, (2, 3), (4, (5, 6)))
print("Nested tuple:", nested[2][1])  # 6

# 🔟 Tuples are hashable (can be keys in dictionaries)
key = (1, 2)
my_dict = {key: "value"}
print("Value from tuple key:", my_dict[(1, 2)])

# 1️⃣1️⃣ You can convert between list and tuple
lst = [1, 2, 3]
tup = tuple(lst)
back_to_list = list(tup)
print("Tuple:", tup, "List again:", back_to_list)

# 1️⃣2️⃣ Use tuples when returning multiple values from a function
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([5, 2, 8, 1])
print("Min:", low, "Max:", high)

"""