# Section F: Interview-Style String Challenges


#Q:59. Remove duplicate characters from string (no set).
#  Initialize the input string
# text = "programming"

# #  Create an empty string to store unique characters
# result = ""

# #  Start iterating through each character in the input string
# for char in text:
#     #  Check if the current character is NOT already in the result
#     if char not in result:
#         #  Append the unique character to the result string
#         result += char

# #  Print the final string after removing duplicates
# print(result)  # Output: "progamin"


# Method 2: Using a list instead of string
# unique_chars = []

# for char in text:
#     if char not in unique_chars:
#         unique_chars.append(char)

# result = "".join(unique_chars)
# print(result)  # Output: "progamin"

# Method 3: Using a dictionary to preserve order
# unique_dict = {}  # Empty dictionary

# for char in text:
#     unique_dict[char] = True  # Duplicate keys overwritten

# result = "".join(unique_dict.keys())
# print(result)  # Output: "progamin"
# Dictionaries in Python 3.7+ preserve insertion order.


# Method 4: Using list comprehension with index check
# result = "".join([char for i, char in enumerate(text) if char not in text[:i]])
# print(result)  # Output: "progamin"




#Q:60. Find first non-repeated character in string.
# string = "togther";
# string = "Togther";

#  Create an empty dictionary to store character counts
# char_count = {}

# # Iterate through each character to count its occurrences
# for char in string:
#     # Increment the count if character exists, else set it to 1
#     char_count[char] = char_count.get(char, 0) + 1

# # Iterate through string to find the first non-repeated character
# for char in string:
#      # Check if the character count is exactly 1
#     if char_count[char] == 1:
#         # Print the first non-repeated character and exit loop
#         print(char)  # Output: "p"
#         break



# Method 2: Using count() method
# Iterate through each character in the string
# for char in string:
#     # check if the character appears only once in the string
#     if string.count(char) == 1:
#         # Print the first non-reapted character and break
#         print(char)
#         break


# Method 3: Using Ordered Dictionary (Python 3.7+)
# from collections import OrderedDict

# Create an ordered dictionary to count character occurrences
# char_count = OrderedDict()

# # Populate the dictionary with counts
# for char in text:
#     char_count[char] = char_count.get(char, 0) + 1

# # Find the first non-repeated character preserving order
# for char, count in char_count.items():
#     # check if count is 1
#     if count == 1:
#         # Print the first non-repeated character
#         print(char)  # Output: "p"
#         break


# Method 4: Using a set to track seen duplicates
#  Initialize the input string
# text = "programming"

# #  Initialize sets for seen characters and duplicates
# seen = set()
# duplicates = set()

# #  Iterate over each character
# for char in text:
#     #  If character already seen, add to duplicates
#     if char in seen:
#         duplicates.add(char)
#     else:
#         #  If character not seen, add to seen
#         seen.add(char)

# #  Iterate again to find first character not in duplicates
# for char in text:
#     if char not in duplicates:
#         # Print the first non-repeated character
#         print(char)  # Output: "p"
#         break



# Q:61. Rotate string left (`abc` → `bca`).
# sorted_str = "abc"

# #  Rotate left by 1 using slicing
# rotated = sorted_str[1:] + sorted_str[0]

# # Print the rotated string
# print(rotated) # Output: "bca"


# Method 2: Using loop (manual shifting)
# Convert string into list for easy shifting
# chars = list(sorted_str)

# # Store the first character separately
# first_char = chars[0]

# # shift each character one position left
# for i in range(len(chars) - 1):
#     chars[i] = chars[i + 1]

# # Place the first character at the end
# chars[i] = first_char

# # Join the list back into a string
# rotated = "".join(chars)


# # Print the rotated string
# print(rotated)  # Output: "bca"



# Method 3: Using string concatenation + slicing loop

#  Define how many positions to rotate (1 for left rotation)
# n = 1

# Rotate using slicing based on n
# rotated = sorted_str[n:] + sorted_str[:n]

#  Print rotated string
# print(rotated)  # Output: "bca"


# Method 4: Using collections.deque
# from collections import deque  #Import deque from collections module


# #  Convert to deque for efficient rotations
# dq = deque(sorted_str)

# #  Rotate left by 1 (negative = left, positive = right)
# dq.rotate(-1)


# #  Join back into string
# rotated = "".join(dq)

# # Print the rotated string
# print(rotated)  # Output: "bca"


"""
Step 1: What is collections?

collections is a built-in Python module.

It provides specialized data structures beyond the basic list, tuple, dict, and set.

Examples: deque, Counter, OrderedDict, defaultdict, namedtuple.

🔎 Step 2: What is deque?

deque stands for Double-Ended Queue.

It is like a list, but optimized for fast appending and popping from both ends (left and right).

Normal Python lists are slow when inserting/removing from the left (because elements shift).

deque makes this O(1) time complexity (constant time).

🔎 Step 3: Why deque is useful here?

We use deque for string rotation because:

It has a built-in method .rotate(k)

k > 0 → rotate right
/
k < 0 → rotate left

This makes rotation super simple and efficien
"""


# Method 5: Using slicing inside a function
# Define a function to rotate left by given positions
# def rotate_left(s, n=1):
#     return s[n:] + s[:n]

# # Commit: Call function with text
# text = "abc"
# rotated = rotate_left(text, 1)

# # Commit: Print the rotated string
# print(rotated)  # Output: "bca"





# Method 1: Manual Counting with Loop
#Q:62. Compress string (`aaabb` → `a3b2`).

# Initialize the input string
# text = "aaabb"

# Create empty string to store compressed result
# compressed = ""

# Initialize count = 1 (for first character)
# count = 1

# # loop through string from index 1 to end
# for i in range(1, len(text)):
#     # If curreny char == previous char, increment count
#     if text[i] == text[i - 1]:
#         count += 1
#     else:
#         # Append previous char + count to result
#         compressed += text[i - 1] + str(count)
#         #  Reset count for new character
#         count = 1
    
# #  Append the last char + count after loop ends
# compressed += text[-1] + str(count)

# # print Compressed result
# print(compressed)


# Method 2: Using While Loop

# text = "aaabb"
# # Create empty string for result
# compressed = ""

# # start index at 0
# i = 0

# # loop until end of string
# while i < len(text):
#     # count current character occurrence
#     count = 1
#     while i + 1 < len(text) and text[i] == text[i + 1]:
#         count += 1
#         i += 1
#     # Add char + count to result
#     compressed += text[i] + str(count)
#     i += 1

# # print compressed string
# print(compressed)



# Method 3: Using itertools.groupby
# from itertools import groupby

# # Initialize the input string
# text = "aaabb"

# # Use groupby to group same consecutive characters
# compressed = "".join(char + str(len(list(group))) for char, group in groupby(text))

# # Print compressed string
# print(compressed)  # Output: "a3b2"
"""
What is itertools.groupby?

groupby groups consecutive identical elements in an iterable.

👉 Easy definition:
“It bundles same-neighboring items together into groups.”
"""




# Method 4: Function for Reuse

# Define a function to compress string
# def compress_string(s):
#     compressed = ""
#     count = 1
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             compressed += s[i - 1] + str(count)
#             count = 1
#     compressed += s[-1] + str(count)
#     return compressed
# # Call function
# print(compress_string("aaabb"))  # Output: "a3b2"



# Method 5: Dictionary (Not Ordered Correctly, but Demonstration)


#  Initialize the input string
# text = "aaabb"

# # Use dictionary to count total characters (not compression, but frequency)
# char_count = {}

# for char in text:
#     char_count[char] = char_count.get(char, 0) + 1

# # Join into a compressed-style string
# compressed = "".join(k + str(v) for k, v in char_count.items())

# print(compressed)  # 







#Q:63. Reverse words in sentence without slicing.
# Method 1: Using split() and manual loop (build reversed list)
# Initialize the input sentence
sentence = "I love Python"

# # Split sentence into list of words
# words = sentence.split()

# # Create empty list to store reversed words
# reversed_words = []

# # Iterate backwards using range
# for i in range(len(words) -1, -1, -1):
#     reversed_words.append(words[i])

# # join the reversed list into a string
# result = " ".join(reversed_words)

# print(result)  #Python love I


# Method 2: Using reversed() built-in

# splite into words
# words = sentence.split()

# # Use reversed() to reverse order of words
# reversed_words = list(reversed(words))


# # Join into final string
# result = " ".join(reversed_words)

# #  Print result
# print(result)  # Output: "Python love I"



# Method 3: Using Stack (LIFO principle)
# Split into words
# words = sentence.split()

# # Create empty list for reversed words
# reversed_words = []

# # while there are words left, pop from end
# while words:
#     reversed_words.append(words.pop())

# # Join into final string
# result = " ".join(reversed_words)

# print(result)  # Output: "Python love I"



# Method 4: Using Recursion
#  Define recursive function
# def reverse_words(words):
#     #  Base case - if only one word, return it
#     if len(words) == 1:
#         return words[0]
#     #  Recursive case - last word + recursion on rest
#     return words[-1] + " " + reverse_words(words[:-1])

# #  Initialize sentence
# sentence = "I love Python"

# #  Split into words
# words = sentence.split()

# #  Call recursive function
# result = reverse_words(words)

# #  Print result
# print(result)  # Output: "Python love I"


# Method 5: Using collections.deque
# from collections import deque

# # Initialize sentence


# # Split into words
# words = sentence.split()

# # Convert into deque
# dq = deque(words)

# #  Create empty list for reversed order
# reversed_words = []

# #  Pop from right until empty
# while dq:
#     reversed_words.append(dq.pop())

# #  Join into string
# result = " ".join(reversed_words)

# #  Print result
# print(result)  # Output: "Python love I"


# Full form: LIFO = Last In, First Out





#Q:64. Count uppercase vs lowercase letters.
# Method 1: Using isupper() and islower()
#  Initialize input string
text = "Hello World Python"

# # Initialize counters
# upper_count = 0
# lower_count = 0

# # Iterate through each character in string
# for char in text:
#     # check if character is uppercase
#     if char.isupper():
#         upper_count += 1
#     # check if character is lowercase
#     elif char.islower():
#         lower_count += 1
    
# #  Print results
# print("Text: ", text)
# print("Uppercase:", upper_count)   # Output: 3
# print("Lowercase:", lower_count)   # Output: 12



# Method 2: Using List Comprehension + sum()

# Count uppercase letters using comprehension
# upper_count = sum(1 for char in text if char.isupper()) 


# # Count lowercase letters using comprehension
# lower_count = sum(1 for char in text if char.islower())

# # Print results
# print("Text: ", text)
# print("Uppercase:", upper_count)   # Output: 3
# print("Lowercase:", lower_count)   # Output: 12


# Method 3: Using ASCII values (ord())
# Initialize counters
# upper_count = 0
# lower_count = 0

# # Loop through each character
# for char in text:
#     code = ord(char) # get ASCII code
#     # check if in uppercase range A-Z
#     if 65 <= code <= 90:
#         upper_count += 1
#     # Check if in lowercase range a-z
#     elif 97 <= code <= 122:
#         lower_count += 1

# #  Print results
# print("Text ==> ", text)
# print("Uppercase:", upper_count)   # Output: 3
# print("Lowercase:", lower_count)   #


# Method 4: Using filter()
#  Filter uppercase letters
# upper_count = len(list(filter(str.isupper, text)))

# # Filter lowercase letters
# lower_count = len(list(filter(str.islower, text)))

# #  Print results
# print("Text: ", text)
# print("Uppercase:", upper_count)   # Output: 3
# print("Lowercase:", lower_count)   # Output: 12


# Method 5: Using collections.Counter
# from collections import Counter        # ✅ Import Counter to keep track of counts like a dictionary
# counts = Counter({"upper": 0, "lower": 0})   # ✅ Initialize keys 'upper' & 'lower' with 0

# text = "Hello World Python"            # ✅ Define input text

# for char in text:                      # ✅ Loop through each character
#     if char.isupper():                 # ✅ If character is uppercase
#         counts["upper"] += 1           # ✅ Increase uppercase counter
#     elif char.islower():               # ✅ If character is lowercase
#         counts["lower"] += 1           # ✅ Increase lowercase counter

# print("text: ", text)                  # ✅ Print original text
# print("Uppercase:", counts["upper"])   # ✅ Print uppercase count
# print("Lowercase:", counts["lower"])   # ✅ Print lowercase count





#Q:65. Validate password (min 8 chars, at least 1 digit).
# Method 1: Using Simple Loop
# password = "Hello123" #password -> variable storing user password
# is_valid = True  #is_valid -> flag (True by default)

# if len(password) < 8: #checks total length of string
#     is_valid = False #set invalid if less than 8 chars


# has_digit = False #flag to track digits
# for char in password:  #loop through each character
#     if char.isdigit():  #check if character is digit
#         has_digit = True #set flag True
#         break #exit loop early (optimization
# if not has_digit:  #invert condition (if no digit found)
#     is_valid = False #set overall flag False

# print("Password Valid? : ", is_valid) #output result


# Method 2: Using Any + Loop
# is_valid = len(password) >= 8 and any(ch.isdigit() for ch in password)  
# #  len(password) >= 8 -> length condition
# #  any(...) -> checks if at least one True exists
# #  ch.isdigit() -> check each character if digit
# #  for ch in password -> loop through password chars

# print("Password Valid?", is_valid)              #  show result


# Method 3: Using Regular Expression (re)


# import re                                       #  import re -> regex library

# password = "Secret99"                           #  test password

# pattern = r"^(?=.*\d).{8,}$"                    #  ^ -> start of string
#                                                 #  (?=.*\d) -> must contain digit
#                                                 #  .{8,} -> at least 8 chars
#                                                 #  $ -> end of string

# is_valid = bool(re.match(pattern, password))    #  re.match -> apply regex
#                                                 #  bool -> convert result to True/False

# print("Password Valid?", is_valid)              #  display validation



# Method 4: Using filter()


# password = "Abcdefg9"                           #  define password

# digits = list(filter(str.isdigit, password))    #  filter -> keep only digits
#                                                 #  str.isdigit -> check digits
#                                                 #  list -> convert filter object to list
# is_valid = len(password) >= 8 and len(digits) > 0  
# #  len(password) >= 8 -> length check
# #  len(digits) > 0 -> at least 1 digit present

# print("Password Valid?", is_valid)              #  print result


# Method 5: Using any() + Generator Expression

# password = "MyPass123"                          # password string

# is_valid = len(password) >= 8 and any(ch.isdigit() for ch in password)  
# # len(password) >= 8 -> check length
# # any(...) -> at least one digit required
# # ch.isdigit() -> checks digit for each char
# # for ch in password -> generator expression

# print("Password Valid?", is_valid)              # final result






# 66. Find duplicate words in paragraph.
# Method 1: Using Dictionary (manual counting)
# text = "Python is great and Python is easy to learn and Python is popular"   #  text -> input paragraph
# words = text.lower().split()
# freq = {}

# for w in words:
#     freq[w] = freq.get(w, 0) + 1

# duplicates = [w for w, c in freq.items() if c > 1]

# print("Text: ", text)
# print("Duplicates: ", duplicates)


# Method 2: Using collections.Counter

# from collections import Counter                                               #  import Counter


# words = text.lower().split()                                                  # split words

# count = Counter(words)                                                        # Counter -> count each word
# duplicates = [w for w, c in count.items() if c > 1]                           # keep only repeated

# print("Text: ", text)  
# print("Duplicates:", duplicates)  





# # Method 3: Using set() (track seen words)
# words = text.lower().split()                                                  #  split into words

# seen = set()                                                                  #  seen -> already visited
# dupes = set()                                                                 #  dupes -> store duplicates

# for w in words:                                                               #  loop over words
#     if w in seen:                                                             #  if word already in seen
#         dupes.add(w)                                                          #  add to duplicates
#     else:
#         seen.add(w)                                                           #  first time add to seen

# print("Duplicates:", list(dupes))  


# Method 4: Using List Comprehension + count()
# words = text.lower().split()                                                  #  split

# duplicates = list(set([w for w in words if words.count(w) > 1]))              # c count(w) -> count each word, set() -> unique

# print("Duplicates:", duplicates) 


# Method 5: Regex (find words)
# import re                                                                     #  import regex

# text = "Python is great and Python is easy to learn and Python is popular"    #  input
# words = re.findall(r'\w+', text.lower())                                      #  \w+ -> extract words

# from collections import Counter                                               #  Counter
# count = Counter(words)                                                        #  count words
# duplicates = [w for w, c in count.items() if c > 1]                           #  keep repeated

# print("Duplicates:", duplicates)                





#Q:67. Count frequency of vowels.
# Method 1: Using Dictionary (manual loop)
text = "Python Programming is Awesome"
# vowels = "aeiou"
# freq = {}

# for char in text.lower():
#     if char in vowels:
#         freq[char] = freq.get(char, 0) + 1

# print("text: ", text)
# print("Vowel Frequency:", freq)  



# Method 2: Using collections.Counter
# from collections import Counter                #  import Counter

# vowels = "aeiou"                               #  vowel list
# count = Counter(ch for ch in text.lower() if ch in vowels)  
# #  generator -> only vowels
# #  Counter -> count them

# print("Vowel Frequency:", dict(count))         #  show result



# # Method 3: Using defaultdict
# from collections import defaultdict            #  import defaultdict


# vowels = "aeiou"                               #  vowel list
# freq = defaultdict(int)                        #  auto-create keys with int(0)

# for ch in text.lower():                        #  loop through chars
#     if ch in vowels:                           #  check vowel
#         freq[ch] += 1                          #  increase count

# print("Vowel Frequency:", dict(freq))          #  convert to dict & show


# # Method 4: Using filter()
# vowels = "aeiou"                               #  vowels
# filtered = list(filter(lambda ch: ch.lower() in vowels, text))  
# #  filter -> keep only vowels
# #  lambda -> condition for vowel
# #  list -> convert to list

# from collections import Counter                #  use Counter
# print("Vowel Frequency:", dict(Counter(filtered)))  
# #  count vowels




# # Method 5: Using Regex
# import re                                      #  regex

# text = "Python Programming is Awesome"        #  input
# vowels = re.findall(r'[aeiou]', text.lower())  #  findall -> extract vowels

# from collections import Counter                # Counter
# print("Vowel Frequency:", dict(Counter(vowels)))  # result


# # Method 6: Using List Comprehension
# vowels = "aeiou"                               # vowels
# freq = {v: text.lower().count(v) for v in vowels if v in text.lower()}  
# # dict comprehension
# # text.count(v) -> count each vowel

# print("Vowel Frequency:", freq)                # show output







# Method 1: Sorting
# Q:68. Check if two strings are anagrams.

# s1, s2 = "listen", "silent"                 #  two strings
# is_anagram = sorted(s1) == sorted(s2)       #  sorted() -> sort letters, compare lists
# print("Anagram?", is_anagram)               #  True if same




# # Method 2: Using collections.Counter
# from collections import Counter              # import Counter

# s1, s2 = "listen", "silent"                 # two strings
# is_anagram = Counter(s1) == Counter(s2)     # Counter -> counts each char
# print("Anagram?", is_anagram)               # print result



# Method 3: Manual Dictionary Counting
# s1, s2 = "listen", "silent"                 #  strings

# def count_chars(word):                       #  define function
#     freq = {}                                #  empty dict
#     for ch in word:                          #  loop chars
#         freq[ch] = freq.get(ch, 0) + 1       #  count char
#     return freq                              #  return dict

# is_anagram = count_chars(s1) == count_chars(s2)   #  compare dicts
# print("Anagram?", is_anagram)               #  show result



# Method 4: Using defaultdict
# from collections import defaultdict          # commit: import defaultdict

# s1, s2 = "listen", "silent"                 #  input

# def char_count(word):                        #  define helper
#     d = defaultdict(int)                     #  auto 0 values
#     for ch in word:                          #  loop
#         d[ch] += 1                           #  increase
#     return d                                 #  return

# is_anagram = char_count(s1) == char_count(s2)  #  compare dicts
# print("Anagram?", is_anagram)               #  result



# Method 5: Using Sets + Count (slower, but simple)
# s1, s2 = "listen", "silent"                 # input
# is_anagram = len(s1) == len(s2) and all(s1.count(ch) == s2.count(ch) for ch in set(s1))  
# # len(s1)==len(s2) -> length same
# # all(...) -> check every char
# # .count -> compare counts
# print("Anagram?", is_anagram)               # final result



# Method 6: Regex (remove non-letters, then compare)
# import re                                    # commit: regex

# s1, s2 = "Listen!!", "Silent..."            # commit: messy strings

# clean1 = "".join(sorted(re.findall(r'[a-z]', s1.lower())))  
# # re.findall -> only letters
# # .lower() -> ignore case
# # sorted -> sort

# clean2 = "".join(sorted(re.findall(r'[a-z]', s2.lower())))  
# # clean second word

# is_anagram = clean1 == clean2                # compare
# print("Anagram?", is_anagram)                # output


# # Method 7: Using all() + zip (compare sorted directly)
# s1, s2 = "listen", "silent"                 #  strings
# is_anagram = len(s1) == len(s2) and all(x == y for x, y in zip(sorted(s1), sorted(s2)))  
# #  len -> same length
# #  zip -> pair chars
# #  all -> check all equal
# print("Anagram?", is_anagram)               #  







# Interview Qs:
# 69. Difference between immutable (string, tuple) vs mutable (list, dict)?
# 70. Why strings are immutable in Python?
"""
===========================================================
Q69. Difference between Immutable vs Mutable in Python
===========================================================

🔹 Immutable Objects
- Cannot be changed after creation.
- If "modified", Python actually creates a new object.
- Examples: str, tuple, int, float, frozenset

Example:
    s = "hello"
    print(id(s))        # memory id before
    s = s + " world"    # new object created
    print(id(s))        # different id → proves immutability

🔹 Mutable Objects
- Can be changed in place without creating new object.
- Examples: list, dict, set

Example:
    lst = [1, 2, 3]
    print(id(lst))      # memory id before
    lst.append(4)       # modifies same list
    print(id(lst))      # same id → proves mutability

🔹 Key Differences Table
-----------------------------------------------------------
| Feature             | Immutable (str, tuple) | Mutable (list, dict) |
|----------------------|-------------------------|-----------------------|
| Can change in place? | ❌ No                  | ✅ Yes                |
| Memory efficiency   | New object each change  | Same object reused    |
| Safe for hashing    | ✅ Yes (dict keys)      | ❌ No (not hashable)  |
| Examples            | str, tuple, int        | list, dict, set       |
-----------------------------------------------------------

===========================================================
Q70. Why Strings are Immutable in Python?
===========================================================

🔹 1. Memory efficiency (string interning)
    - Python reuses same string objects.
    - Example:
        a = "hello"
        b = "hello"
        print(a is b)   # True → both share memory
    - If mutable, changing `a` would also change `b`.

🔹 2. Hashability (dictionary keys, set elements)
    - Strings must be hashable for dict/set usage.
    - If mutable, hash would change → dict keys break.

🔹 3. Thread-safety
    - Strings are used everywhere.
    - If mutable, multiple threads could cause bugs.
    - Immutability ensures safe shared usage.

🔹 4. Security & Reliability
    - Strings store critical info (file paths, identifiers).
    - If mutable, they could be altered by mistake/malware.

🔹 5. Simplicity in implementation
    - Immutable strings allow Python to optimize internally.

===========================================================
✅ One-Line Interview Answer
Strings are immutable in Python because it makes them 
memory efficient, hashable, thread-safe, and reliable.
===========================================================

Quick Demo:
    s = "hello"
    print(id(s))        # before
    s += " world"
    print(id(s))        # new id → new object created
"""
