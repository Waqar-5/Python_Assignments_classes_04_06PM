# Section D: Functions + Loops (Real-Life + Interview Qs)
# Q:35. Function to count how many `.pdf` files are in a list.
files = ['document.pdf', 'image.png', 'report.pdf', 'notes.txt']
def count_pdf_files(file_list):
    count = 0
    for file in file_list:
        if file.endswith('.pdf'):
            count += 1
    return count
# Example usage:
# files = ['document.pdf', 'image.png', 'report.pdf', 'notes.txt']
print(count_pdf_files(files))  # Output: 2


print("***********************************************************")

# Q:36. Function to check username availability.
existing_usernames = ['user1', 'admin', 'guest']
def is_username_available(username, existing_usernames):
    return username not in existing_usernames
# Example usage:
print(is_username_available('newuser', existing_usernames))  # Output: True
print(is_username_available('admin', existing_usernames))    # Output: False




print("***********************************************************")
#Q:37. Function to return longest word in a sentence.
sentence = "Hello world! Welcome to Python programming."
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
# Example usage:
print(longest_word(sentence))  # Output: programming.




print("***********************************************************")
#Q:38. Function that checks if string is palindrome using loop.
word = "racecar"
def is_palindrome(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True
# Example usage:
print(is_palindrome(word))  # Output: True




print("***********************************************************")
#Q:39. Function that prints multiplication table.
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Example usage:
multiplication_table(5)



print("***********************************************************")
# Q:40.Function to simulate dice roll until 6 appears.
import random
def roll_until_six():
    roll = 0
    while roll != 6:
        roll = random.randint(1, 6)
        print(f"Rolled: {roll}")
    print("Got a 6! Stopping.")
# Example usage:
roll_until_six()  # Output: Rolls until a 6 is rolled.



print("***********************************************************")
# Q:41. Function to filter products under given price.
products = [{'name': 'Laptop', 'price': 800}, {'name': 'Mouse', 'price': 20}, {'name': 'Keyboard', 'price': 50}]
def filter_products_by_price(products, max_price):
    affordable_products = []
    for product in products:
        if product['price'] < max_price:
            affordable_products.append(product)
    return affordable_products
# Example usage:
print(filter_products_by_price(products, 100))  # Output: [{'name': 'Mouse', 'price': 20}, {'name': 'Keyboard', 'price': 50}]





print("***********************************************************")
#Q:42. Function that masks all passwords in list.
passwords = ['mypassword', '123456', 'adminpass']
def mask_passwords(password_list):
    masked = []
    for password in password_list:
        masked.append('*' * len(password))
    return masked
# Example usage:
print(mask_passwords(passwords))  # Output: ['**********




print("***********************************************************")
#Q:43. Function to count frequency of words in sentence.
sentence = "hello world hello"
def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
# Example usage:
print(word_frequency(sentence))  # Output: {'hello': 2, 'world':




print("***********************************************************")
# 44. Function to extract hashtags from social media post.
post = "Loving the #sunshine and #beach vibes! #summer"
def extract_hashtags(post):
    words = post.split()
    hashtags = []
    for word in words:
        if word.startswith('#'):
            hashtags.append(word)
    return hashtags
# Example usage:
print(extract_hashtags(post))  # Output: ['#sunshine', '#beach', '#summer']






# Other ways do above questions:

# -------------------------------
# 35. Function to count how many `.pdf` files are in a list
# -------------------------------

# Approach 1: Using a for loop
# def count_pdfs_loop(file_list):
#     count = 0  # Initialize counter
#     for file in file_list:  # Loop through each file in list
#         if file.endswith(".pdf"):  # Check if file ends with .pdf
#             count += 1  # Increment counter if yes
#     return count  # Return final count

# # Approach 2: Using list comprehension
# def count_pdfs_lc(file_list):
#     return sum(1 for file in file_list if file.endswith(".pdf"))  # Count .pdf using comprehension

# # -------------------------------
# # 36. Function to check username availability
# # -------------------------------

# # Approach 1: Using simple loop
# def check_username(username, existing_usernames):
#     for user in existing_usernames:  # Loop through existing usernames
#         if user.lower() == username.lower():  # Case-insensitive check
#             return False  # Username taken
#     return True  # Username available

# # Approach 2: Using `in` operator
# def check_username_in(username, existing_usernames):
#     return username.lower() not in [user.lower() for user in existing_usernames]  # Return True if not in list

# # -------------------------------
# # 37. Function to return longest word in a sentence
# # -------------------------------

# # Approach 1: Using split and loop
# def longest_word_loop(sentence):
#     words = sentence.split()  # Split sentence into words
#     longest = ""  # Initialize longest word
#     for word in words:  # Loop through words
#         if len(word) > len(longest):  # Compare lengths
#             longest = word  # Update longest
#     return longest  # Return longest word

# # Approach 2: Using max with key
# def longest_word_max(sentence):
#     return max(sentence.split(), key=len)  # Max by word length

# # -------------------------------
# # 38. Function that checks if string is palindrome using loop
# # -------------------------------

# # Approach 1: Using two pointers
# def is_palindrome_loop(s):
#     s = s.lower().replace(" ", "")  # Normalize string
#     left, right = 0, len(s) - 1  # Initialize pointers
#     while left < right:  # Loop until pointers meet
#         if s[left] != s[right]:  # Compare characters
#             return False  # Not palindrome
#         left += 1
#         right -= 1
#     return True  # Palindrome

# # Approach 2: Using reversed string
# def is_palindrome_reverse(s):
#     s_clean = s.lower().replace(" ", "")  # Normalize
#     return s_clean == s_clean[::-1]  # Compare with reversed

# # -------------------------------
# # 39. Function that prints multiplication table
# # -------------------------------

# # Approach 1: Using for loop
# def multiplication_table(n):
#     for i in range(1, 11):  # 1 to 10
#         print(f"{n} x {i} = {n*i}")  # Print each multiplication

# # Approach 2: Using list comprehension and join
# def multiplication_table_lc(n):
#     table = [f"{n} x {i} = {n*i}" for i in range(1, 11)]  # List of strings
#     print("\n".join(table))  # Join and print

# # -------------------------------
# # 40. Function to simulate dice roll until 6 appears
# # -------------------------------
# import random  # Import random module

# def roll_until_six():
#     count = 0  # Count number of rolls
#     while True:  # Infinite loop
#         roll = random.randint(1, 6)  # Roll dice
#         print(f"Rolled: {roll}")  # Print roll
#         count += 1  # Increment roll count
#         if roll == 6:  # Stop when 6 appears
#             break
#     print(f"Total rolls to get 6: {count}")  # Print total rolls

# # -------------------------------
# # 41. Function to filter products under given price
# # -------------------------------

# # Approach 1: Using loop
# def filter_products_loop(products, max_price):
#     result = []  # Initialize result list
#     for product, price in products.items():  # Loop through dictionary
#         if price <= max_price:  # Check price
#             result.append(product)  # Add to result
#     return result  # Return list

# # Approach 2: Using dictionary comprehension
# def filter_products_dc(products, max_price):
#     return [p for p, price in products.items() if price <= max_price]  # List comprehension

# # -------------------------------
# # 42. Function that masks all passwords in list
# # -------------------------------

# # Approach 1: Using loop
# def mask_passwords_loop(passwords):
#     masked = []  # Initialize list
#     for pw in passwords:  # Loop through passwords
#         masked.append("*" * len(pw))  # Mask with *
#     return masked

# # Approach 2: Using list comprehension
# def mask_passwords_lc(passwords):
#     return ["*" * len(pw) for pw in passwords]  # Mask in one line

# # -------------------------------
# # 43. Function to count frequency of words in sentence
# # -------------------------------

# # Approach 1: Using loop and dictionary
# def word_frequency_loop(sentence):
#     freq = {}  # Empty dict
#     for word in sentence.split():  # Loop words
#         word = word.lower()  # Normalize
#         if word in freq:
#             freq[word] += 1
#         else:
#             freq[word] = 1
#     return freq

# # Approach 2: Using collections.Counter
# from collections import Counter
# def word_frequency_counter(sentence):
#     words = sentence.lower().split()  # Lowercase and split
#     return Counter(words)  # Return Counter dict

# # -------------------------------
# # 44. Function to extract hashtags from social media post
# # -------------------------------

# # Approach 1: Using loop
# def extract_hashtags_loop(post):
#     hashtags = []  # Empty list
#     for word in post.split():  # Loop through words
#         if word.startswith("#"):  # Check if word is hashtag
#             hashtags.append(word)  # Add to list
#     return hashtags

# # Approach 2: Using list comprehension
# def extract_hashtags_lc(post):
#     return [word for word in post.split() if word.startswith("#")]  # One line extraction

# # Approach 3: Using regex
# import re
# def extract_hashtags_regex(post):
#     return re.findall(r"#\w+", post)  # Find all hashtags using regex

# # ===============================
# # Example usage
# # ===============================
# if __name__ == "__main__":
#     # Test PDF counter
#     files = ["a.pdf", "b.doc", "c.pdf", "d.txt"]
#     print(count_pdfs_loop(files), count_pdfs_lc(files))

#     # Test username check
#     users = ["Alice", "Bob", "Charlie"]
#     print(check_username("bob", users), check_username_in("dave", users))

#     # Test longest word
#     sentence = "Python is amazing for learning"
#     print(longest_word_loop(sentence), longest_word_max(sentence))

#     # Test palindrome
#     print(is_palindrome_loop("Madam"), is_palindrome_reverse("Racecar"))

#     # Test multiplication table
#     multiplication_table(5)
#     multiplication_table_lc(3)

#     # Test dice roll
#     roll_until_six()

#     # Test product filter
#     products = {"apple": 100, "banana": 40, "mango": 150}
#     print(filter_products_loop(products, 100))
#     print(filter_products_dc(products, 100))

#     # Test password masking
#     passwords = ["1234", "password", "secret"]
#     print(mask_passwords_loop(passwords))
#     print(mask_passwords_lc(passwords))

#     # Test word frequency
#     test_sentence = "Python is fun and Python is easy"
#     print(word_frequency_loop(test_sentence))
#     print(word_frequency_counter(test_sentence))

#     # Test hashtag extraction
#     post = "Loving #Python and #AI development #100DaysOfCode"
#     print(extract_hashtags_loop(post))
#     print(extract_hashtags_lc(post))
#     print(extract_hashtags_regex(post))
#     # End of showcase




# Interview Qs:
# 45. Difference between `return` and `print` in functions?
# 46. Can functions in Python return multiple values?

"""
45. Difference between return and print in functions

Conceptual Difference:

Feature	return	print
Purpose	Sends a value back to the caller of function	Displays output to the console
Usage	Can be used in further calculations or stored	Only shows information, cannot be used
End of function	Ends function execution when executed	Function continues after printing
Multiple values	Can return multiple values (tuple, list, etc.)	Prints multiple values, but does not pass them

Example 1: Using print vs return

# Using print
def add_print(a, b):
    print(a + b)  # Output is only displayed
result = add_print(5, 10)  # Prints 15
print("Result:", result)  # None, because function didn't return

# Using return
def add_return(a, b):
    return a + b  # Output is returned
result = add_return(5, 10)  # Returns 15
print("Result:", result)  # Prints 15


Explanation:

print just displays 15, but you cannot use it for calculations.

return allows storing value in a variable and using it elsewhere.

Example 2: Return ends the function

def test_return(x):
    return x
    print("This will never run")  # After return, function stops

def test_print(x):
    print(x)
    print("This will still run")  # Function continues after print

46. Can functions in Python return multiple values?

✅ Yes! Python functions can return multiple values using tuples, lists, or dictionaries.

Approach 1: Return multiple values as a tuple (most common)

def get_name_age():
    name = "Waqar"
    age = 22
    return name, age  # Returns as tuple automatically

n, a = get_name_age()  # Unpacking tuple
print("Name:", n)
print("Age:", a)


Approach 2: Return values as a list

def get_scores():
    return [90, 80, 70]  # Return a list
scores = get_scores()
print("Scores:", scores)


Approach 3: Return values as a dictionary

def get_person_info():
    return {"name": "Ali", "age": 25, "city": "Karachi"}  # Return dict
info = get_person_info()
print("Name:", info["name"])
print("Age:", info["age"])
print("City:", info["city"])


Approach 4: Using *args and tuple for dynamic multiple returns

def sum_product(a, b):
    return a+b, a*b  # Return sum and product
s, p = sum_product(5, 6)
print("Sum:", s)
print("Product:", p)


Key Notes:

You can return as many values as you want.

Returning multiple values allows flexible function outputs.

Using print here instead of return won’t allow unpacking or storing values.
"""