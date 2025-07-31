"""
Interview & Conceptual (Q39–Q50)
38. 39. What’s the difference between mutable and immutable types? Give examples.
39. 40. Explain the difference between `is` and `==` in Python.
40. 41. Can you change values in a tuple? Why or why not?
41. 42. Explain how `elif` works. Can it exist without `if`?
42. 43. What happens when accessing a non-existent dictionary key? How to avoid it?
43. Why are strings immutable in Python? What are the benefits?
44. 46. Difference between `list.copy()` and using `=` assignment? Show example.
45. 47. Can a tuple contain mutable items? Give a code example.
46. 48. What is the difference between `in` when used in a list vs a dictionary?
47. 49. Explain shallow copy vs deep copy with a list example.
48. 50. What is the output of:
x = [1, 2, 3]
y = x
y.append(4)
print(x)
Explain the result.
"""

# Python Interview Questions (Q39–Q50) with Explanations & Examples

# Mutable vs Immutable Types
# Mutable: Can be changed after creation (e.g., list, dict, set)
# Immutable: Cannot be changed after creation (e.g., int, str, tuple)
# 39. Mutable vs Immutable Types
# Mutable = changeable (list, dict); Immutable = unchangeable (int, str, tuple)
mutable_list = [1, 2]; mutable_list.append(3)  # ✅ Allowed
immutable_str = "hi"  # "hi" stays unchanged, new string is made if modified
immutable_str += "!"  # Still immutable, creates a new object

print("*****************************************************")


# == checks value equality, is checks object identity (same memory).
# 40. 'is' vs '=='
a = [1]; b = [1]
print(a == b)  # ✅ True, values are equal
print(a is b)  # ❌ False, different objects in memory
c = a
print(c is a)  # ✅ True, same object
print("*****************************************************")
# 41. Can tuple values change?
# No, because tuples are immutable. Their structure can't be altered.
t = (1, 2)
# t[0] = 5  # ❌ Error: 'tuple' object does not support item assignment

print("*****************************************************")
# 42. 'elif' usage
# elif = "else if". It must follow an if. Cannot exist alone.
# It is used when you want to check multiple conditions.
# It must come after if — it cannot be used alone.
x = 0
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
# Note: `elif` cannot exist without an `if` before it

print("*****************************************************")

# 43. Non-existent dictionary key
# Raises KeyError. Avoid with .get() or in.
# Accessing a missing key directly gives a KeyError.
# You can avoid this using:
# in keyword: check if key exists
# .get() method: safely returns None or default value


d = {"a": 1}
print(d.get("b"))      # ✅ None, avoids error
print("b" in d)        # ✅ False, key not present
# print(d["age"])           # ❌ KeyError
print("*****************************************************")
# 44. Why strings are immutable
# Immutability ensures thread-safety, memory efficiency (string interning), and predictability.z
# Immutable strings allow memory optimization, safe sharing, and hashability
s = "cat"
# s[0] = "b"  # ❌ Error: string does not support item assignment
name = "Ali"
# name[0] = "B"   ❌ Error: can't modify string


print("*****************************************************")
# 45. list.copy() vs =
# list.copy() creates a new list; (= points to same list.)
a = [1, 2]
b = a           # Same object, changes affect both
b.append(3)
print("a after b.append:", a)  # [1, 2, 3]

a = [1, 2]
c = a.copy()    # New object
c.append(4)
print("a after c.append:", a)  # [1, 2]

print("*****************************************************")

# 46. Tuple with mutable items
# Yes. Tuples can't change, but their items can if they are mutable.
t = ([1, 2], "hi")
t[0].append(3)  # ✅ Allowed: list inside tuple is mutable
print("Mutable in tuple:", t)  # ([1, 2, 3], 'hi')

# Yes. A tuple itself is immutable, but it can contain mutable elements (like a list), and those can be changed.
t = ([1, 2], "hi")
t[0].append(3)    # Allowed: modifying list inside tuple
print(t)          # ([1, 2, 3], 'hi')


print("*****************************************************")
# 47. 'in' for list vs dict
# List: Checks value.
# Dict: Checks keys only.
# In a list, in checks values.
# In a dictionary, in checks keys only.

print("apple" in ["apple", "banana"])       # ✅ True (value check)
print("apple" in {"apple": 1, "b": 2})      # ✅ True (key check)
print(1 in {"apple": 1})                    # ❌ False (1 is a value, not a key)

print("*****************************************************")
# 48. Shallow vs Deep Copy
# Shallow copy: Copies top-level only.
# Deep copy: Recursively copies all levels.
# Shallow Copy: Copies outer list only — inner lists still refer to the original.
# Deep Copy: Recursively copies everything — makes full duplicate.
import copy
lst1 = [[1], [2]]
shallow = lst1.copy()           # Top-level copy only
deep = copy.deepcopy(lst1)      # Fully independent copy

lst1[0].append(9)
print("Shallow copy:", shallow)  # [[1, 9], [2]]
print("Deep copy:", deep)        # [[1], [2]]

print("*****************************************************")
# 49. x = [1, 2, 3]; y = x; y.append(4); print(x)
#  y and x point to same list, so changes affect both.
x = [1, 2, 3]
y = x
y.append(4)
print("Final x:", x)  # [1, 2, 3, 4] – y and x point to same object
