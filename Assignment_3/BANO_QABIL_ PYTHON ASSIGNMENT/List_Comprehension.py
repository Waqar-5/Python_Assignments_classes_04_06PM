# Section H: List Comprehension (Real-Life + Interview Qs)


#Q:83. Generate roll numbers `[BSE-1, BSE-2, ..., BSE-50]`.
# Way 1: Using a simple for
# Initialize an empty list to store roll numbers
roll_numbers = []  # roll_numbers -> variable name holding the list

# Loop from 1 to 50
for i in range(1, 50): # for -> loop keyword, i -> loop variable, range(1, 51) -> generates numbers 1 to 50
    roll = "BSE-" + str(i) # "BSE-" -> string prefix, str(i) -> convert number i to string, + -> concatenate strings
    roll_numbers.append(roll)  # append() -> list method to add element at the end


# Print the final list
print(roll_numbers)  # print() -> outputs the list to console


print("***********************************************")




# Way 2: Using List Comprehension
# Create a list of roll numbers in a single line using list comprehension
# roll_numbers = ["BSE-" + str(i) for i in range(1, 51)]
# # ["BSE-" + str(i) ...] -> generate each roll number string
# # for i in range(1, 51) -> iterate i from 1 to 50
# # roll_numbers -> variable storing the list

# print(roll_numbers)  # print list to console

# print("***********************************************")
# Way 3: Using map function
# Define a function to format the roll number
# def format_roll(n):  # def -> define function, n -> function parameter
#     return "BSE-" + str(n)  # return the formatted string

# # Use map to apply function to numbers 1 to 50
# roll_numbers = list(map(format_roll, range(1, 51)))  
# # map(format_roll, range(1, 51)) -> applies function to each number
# # list() -> converts map object to list

# print(roll_numbers)  # print the list


# print("*****************************************************")
# Way 4: Using lambda with map
# Use lambda (anonymous function) with map

# roll_numbers = list(map(lambda x: "BSE-" + str(x), range(1, 51)))  

# # lambda x: "BSE-" + str(x) -> function to create roll number string
# # map(...) -> apply function to each element in range
# # list() -> convert map object to list

# print(roll_numbers)  # output the list


# print("********************************************")
# Way 5: Using f-string in List Comprehension
# f-strings -> formatted string literals, very clean way

# roll_numbers = [f"BSE-{i}" for i in range(1, 51)]  

# # f"BSE-{i}" -> directly inserts i into string
# # for i in range(1, 51) -> loop from 1 to 50

# print(roll_numbers)  # display the result






#Q:84. Extract vowels from string.
# Way 1: Using simple for loop and if condition
# Input string
text = "Hello World"  # text -> variable storing the string

# Define vowels
vowels = "aeiouAEIOU"  # vowels -> string containing all vowel characters

# Initialize empty list to store extracted vowels
extracted = []  # extracted -> list to hold vowels found

# Loop through each character in text
for char in text: # for -> loop keyword, char -> current character, in -> keyword to iterate over text
    if char in vowels:  # if -> condition, char in vowels -> checks if char is a vowel
        extracted.append(char)  # append() -> add char to list

print(extracted)  # print() -> display extracted vowels


# print("***************************************************")


# Way 2: Using List Comprehension
# extracted = [char for char in text if char in vowels]  
# # [char ...] -> each character to include in list
# # for char in text -> iterate over each character
# # if char in vowels -> only include if char is a vowel

# print(extracted)  # output vowels

# print("*****************************************************")


# Way 3: Using filter() and lambda
# filter() -> filters elements based on function, lambda x -> anonymous function

# extracted = list(filter(lambda x: x in vowels, text))  

# # lambda x: x in vowels -> returns True if x is a vowel
# # list() -> convert filter object to list

# print(extracted)  # print vowels


# print("*******************************************************")
# # Way 4: Using re module (Regular Expressions)
# import re  # import -> load module, re -> regular expression module

# text = "Hello World"

# # re.findall() -> find all matches in string
# extracted = re.findall(r"[aeiouAEIOU]", text)  
# # r"[aeiouAEIOU]" -> regex pattern to match vowels
# # extracted -> list of matched vowels

# print(extracted)  # display the result



# print("**********************************************************")
# Way 5: Using set() to get unique vowels

# Use set to extract unique vowels
# extracted = list(set([char for char in text if char in vowels]))  
# # [char for char in text if char in vowels] -> list of vowels
# # set() -> remove duplicates
# # list() -> convert set back to list

# print(extracted)  # print unique vowels

# print("***********************************************")
# Way 6: Using for loop with string concatenation
# text = "Hello World"
# vowels = "aeiouAEIOU"

# extracted = ""  # initialize empty string

# for char in text:  # iterate through each character
#     if char in vowels:  # check if character is vowel
#         extracted += char  # concatenate vowel to extracted string

# print(extracted)  # print vowels as string



print("*********************************************")
#Q:85. Get only words starting with “S” from list.
# Way 1: Using simple for loop and if condition
# Define a list of words

words = ["Sun", "Moon", "Star", "Sky", "Earth"]

# Initialize empty list to store words starting with 'S'
s_words = [] # s_words -> list to hold matching words

# Loop through each word in the list
for word in words:  # for -> loop keyword, word -> current element, in -> iterate over words
    if word.startswith("S"):  # if -> condition, word.startswith("S") -> checks if word begins with "S"
        s_words.append(word)  # append() -> add word to s_words list

print(s_words)  # print() -> display result


# print("***********************************************")
# Way 2: Using List Comprehension
# List comprehension to get words starting with 'S'

# s_words = [word for word in words if word.startswith("S")]

# # [word ...] -> include word in new list
# # for word in words -> loop through each element in words
# # if word.startswith("S") -> condition to filter words

# print(s_words)  # display filtered list


# print("***************************************************")
# Way 3: Using filter() with lambda
# filter() -> filters elements based on function, lambda -> anonymous function

# s_words = list(filter(lambda w: w.startswith("S"), words))
# # lambda w: w.startswith("S") -> returns True if w starts with "S"
# # list() -> convert filter object to list

# print(s_words)  # output result



# print("******************************************************")
# Way 4: Using for loop and string slicing
# for word in words:  # iterate each word
#     if word[0] == "S":  # word[0] -> first character, check if it is 'S'
#         s_words.append(word)  # add to list

# print(s_words)  # print the resu


# print("*********************************************")
# Way 5: Using map() and conditional inside list comprehension

# Use map to process words, then filter using list comprehension

# s_words = [w for w in map(str, words) if w.startswith("S")]  

# map(str, words) -> ensures each element is string
# [w ...] -> list comprehension to select words starting with 'S'

# print(s_words)  # display filtered words

# print("**************************************************")
# Way 6: Using re module (Regular Expressions)
# import re  # import regular expression module


# # re.match() -> matches pattern at the start of string
# s_words = [w for w in words if re.match(r"^S", w)]  
# # r"^S" -> regex pattern: ^ = start of string, S = character 'S'
# # list comprehension to filter matching words

# print(s_words)  # output words starting with 'S'


print("****************************************************")
#Q:86. Flatten nested list using comprehension.

# Way 1: Simple nested list comprehension (1-level nesting)
# Define a nested list

nested_list = [[1, 2], [3, 4], [5, 6]]  

# nested_list -> variable storing list of lists

# Flatten list using list comprehension

flat_list = [item for sublist in nested_list for item in sublist]  

# [item ...] -> each element to include in flattened list
# for sublist in nested_list -> iterate through each inner list
# for item in sublist -> iterate through each element inside inner list

print(flat_list)  # print() -> output flattened list


print("************************************************")
# Way 2: Using double for loop in comprehension with string lists
# nested_list = [["a", "b"], ["c", "d"], ["e", "f"]]

# # Flatten nested string list
# flat_list = [char for sublist in nested_list for char in sublist]  
# # char -> individual element in inner list
# # sublist -> each inner list
# # nested_list -> main outer list

# print(flat_list)  # display result



# print("**********************************************************")
# Way 3: Flatten using comprehension with condition
# nested_list = [[1, 2], [3, 4], [5, 6]]

# # Only flatten even numbers
# flat_list = [item for sublist in nested_list for item in sublist if item % 2 == 0]  
# # if item % 2 == 0 -> include only even numbers

# print(flat_list)  # output [2, 4, 6]



# print("******************************************************")
# Way 4: Using comprehension with str() conversion
# nested_list = [[1, 2], [3, 4], [5, 6]]

# # Flatten list and convert each element to string
# flat_list = [str(item) for sublist in nested_list for item in sublist]  
# # str(item) -> convert element to string

# print(flat_list)  # output ['1', '2', '3', '4', '5', '6']


# print("*************************************************")
# Way 5: Flatten mixed types (numbers + strings) safely
# nested_list = [[1, "a"], [2, "b"], [3, "c"]]

# # Flatten and convert all elements to string
# flat_list = [str(item) for sublist in nested_list for item in sublist]  
# # ensures all types can be combined in one flat list

# print(flat_list)  # output ['1', 'a', '2', 'b', '3', 'c']

# print("********************************************")
# Way 6: Flatten 1-level nested list using itertools.chain in comprehension style
# from itertools import chain  # import chain function from itertools module

# nested_list = [[1, 2], [3, 4], [5, 6]]

# # Flatten using chain
# flat_list = [item for item in chain(*nested_list)]  
# # chain(*nested_list) -> unpack inner lists and iterate over all elements

# print(flat_list)  # output [1, 2, 3, 4, 5, 6]



# print("********************************************")
# 87. Create dictionary {word: length} from list of words.
# Way 1: Using simple for loop
# Define a list of words
words = ["apple", "banana", "cherry", "date"]  
# words -> variable holding list of strings

# Initialize empty dictionary
word_lengths = {}  # word_lengths -> dictionary to store word: length pairs

# Loop through each word
for word in words:  # for -> loop keyword, word -> current element, in -> iterate over list
    word_lengths[word] = len(word)  # len(word) -> length of the string, assign to dictionary key

print(word_lengths)  # print() -> display dictionary

print("****************************************************")

# Way 2: Using Dictionary Comprehension
# Create dictionary using comprehension

# word_lengths = {word: len(word) for word in words}  

# # {key: value for element in iterable} -> dictionary comprehension
# # word -> key, len(word) -> value

# print(word_lengths)  # output dictionary

# print("**************************************************")
# Way 3: Using dict() and zip()

# Calculate lengths

# lengths = [len(word) for word in words]  

# list comprehension to get lengths of each word

# Create dictionary by zipping words and lengths

# word_lengths = dict(zip(words, lengths))  

# zip(words, lengths) -> pairs word with its length
# dict() -> convert pairs to dictionary

# print(word_lengths)  # display result


# print("**************************************")
# Way 4: Using map() and dict()

# map() -> applies a function to each element, lambda -> anonymous function
# pairs = map(lambda w: (w, len(w)), words)  
# # lambda w: (w, len(w)) -> create tuple (word, length)

# word_lengths = dict(pairs)  # convert map object of tuples to dictionary

# print(word_lengths)  # output dictionary


# print("****************************************")
# Way 5: Using fromkeys() with a loop
# fromkeys() -> creates dictionary with keys and a single default value
# word_lengths = dict.fromkeys(words, 0)  
# # initially set all lengths to 0

# for word in word_lengths:  # iterate over dictionary keys
#     word_lengths[word] = len(word)  # update length of each word

# print(word_lengths)  # display dictionary


# print("*******************************************************")
# Way 6: Using enumerate() (less common, just for variety)
# Use enumerate to get index (optional) and word
# word_lengths = {word: len(word) for index, word in enumerate(words)}  
# # enumerate(words) -> returns (index, word), index not used here
# # dictionary comprehension assigns word -> len(word)

# print(word_lengths)  # output dictionary

# print("*************************************************")

#Q:88. Extract domain names from emails.
# Way 1: Using split() method
# Define a list of email addresses
emails = ["alice@example.com", "bob@test.org", "charlie@mydomain.net"]  
# emails -> variable holding list of strings

# Initialize empty list to store domain names
domains = []  # domains -> list to store extracted domains

# Loop through each email
for email in emails:  # for -> loop keyword, email -> current string, in -> iterate over emails
    domain = email.split("@")[1]  # split("@") -> splits string at '@', [1] -> takes domain part
    domains.append(domain)  # append() -> add domain to domains list

print(domains)  # print() -> output list of domains



# print("*************************************")
# Way 2: Using List Comprehension
# Extract domains in a single line

# domains = [email.split("@")[1] for email in emails]  

# email.split("@")[1] -> get domain part
# for email in emails -> iterate through each email

# print(domains)  # output domains

# print("*****************************************")

# Way 3: Using partition() method
# domains = [email.partition("@")[2] for email in emails]  
# # email.partition("@") -> splits into tuple (before, separator, after)
# # [2] -> take the 'after' part, which is the domain

# print(domains)  # display domain names


# print("*******************************************8")
# Way 4: Using split() and map()
# map() applies a function to each email
# domains = list(map(lambda e: e.split("@")[1], emails))  
# # lambda e: e.split("@")[1] -> function to extract domain
# # list() -> convert map object to list

# print(domains)  # output domains


# print("*****************************************")
# Way 5: Using re module (Regular Expressions)
# import re  # import re module for regular expressions

# # re.findall() -> finds matches of pattern
# domains = [re.findall(r'@(.+)', email)[0] for email in emails]  
# # r'@(.+)' -> regex pattern: '@' followed by one or more characters
# # [0] -> get the matched domain string from list returned by findall()

# print(domains)  # display domains


# print("*****************************************")
# # Way 6: Using split() and unpacking

# # Use walrus operator to assign domain while iterating
# domains = [(domain := email.split("@")[1]) for email in emails]  
# # domain := email.split("@")[1] -> assigns domain while returning it
# # list comprehension collects the domain into a list

# print(domains)  # output ['example.com', 'test.org', 'mydomain.net']


print("*******************************************")

# Q:89. Create list of even numbers from 1–100.
# Initialize empty list to store even numbers
list_even_100 = []  # list_even_100 -> variable holding list of even numbers, [] -> empty list

# Loop from 1 to 99
for i in range(1, 101):  # for -> loop keyword, i -> loop variable, range(1, 100) -> generates numbers 1 to 99
    if i % 2 == 0:  # if -> condition, i % 2 -> remainder when i is divided by 2, == 0 -> checks if i is even
        list_even_100.append(i)  # append() -> list method to add i to the list

# Print the final list
print(list_even_100)  # print() -> output the list of even numbers


print("********************************************")
# Way 2: Using List Comprehension
# # Create even numbers list using comprehension
# even_numbers = [i for i in range(1, 101) if i % 2 == 0]  
# # [i ...] -> each number i included if condition is True
# # for i in range(1, 101) -> iterate from 1 to 100
# # if i % 2 == 0 -> only include even numbers

# print(even_numbers)  # output list


# print("**********************************")
# Way 3: Using range() with step
# Use range(start, stop, step) to get even numbers directly

# even_numbers = list(range(2, 101, 2))  

# # range(2, 101, 2) -> start at 2, stop before 101, step 2 to get evens
# # list() -> convert range object to list

# print(even_numbers)  # display the lis


# print("****************************************")
# Way 4: Using filter() and lambda

# Create numbers from 1 to 100
# numbers = range(1, 101)  # range object from 1 to 100

# # Use filter() with lambda to get even numbers
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  
# # lambda x: x % 2 == 0 -> function returning True if number is even
# # filter() -> keeps only numbers where lambda returns True
# # list() -> convert filter object to list

# print(even_numbers)  # output list of even numbers


# print("******************************************")
# Way 5: Using while loop
# Initialize variables
# i = 1  # start from 1
# even_numbers = []  # list to store even numbers

# # Loop until 100
# while i <= 100:  # while -> loop while condition is True
#     if i % 2 == 0:  # check if i is even
#         even_numbers.append(i)  # add to list
#     i += 1  # increment i

# print(even_numbers)  # display result


# print("*****************************************")
# Way 7: Using map() and range
# Multiply by 2 to get even numbers
# even_numbers = list(map(lambda x: x*2, range(1, 51)))  
# # range(1, 51) -> numbers 1 to 50
# # lambda x: x*2 -> double each number to get even numbers
# # list() -> convert map object to list

# print(even_numbers)  # display even numbers



# print("********************************")
# Way 6: Using numpy (if installed)
# import numpy as np  # import numpy module

# # Use numpy.arange to generate even numbers
# even_numbers = np.arange(2, 101, 2).tolist()  
# # np.arange(2, 101, 2) -> numbers from 2 to 100 with step 2
# # .tolist() -> convert numpy array to Python list

# print(even_numbers)  # output list



# print("************************************************")
#Q:90. Filter transactions above 100,000 PKR.
# Way 1: Using for loop and if

# List of transaction amounts in PKR
transactions = [50000, 120000, 75000, 200000, 95000, 150000]  
# transactions -> variable storing list of numbers
# Initialize empty list to store filtered transactions
high_transactions = []  # high_transactions -> list to hold amounts above 100,000

# Loop through each transaction
for amount in transactions:  # for -> loop keyword, amount -> current element, in -> iterate over transactions
    if amount > 100000:  # if -> condition, amount > 100000 -> checks if amount exceeds 100,000
        high_transactions.append(amount)  # append() -> add amount to list

print(high_transactions)  # print() -> output filtered transactions


# print("*******************************************")
# Way 2: Using List Comprehension
# Filter transactions in a single line

# high_transactions = [amount for amount in transactions if amount > 100000]  
# # [amount ...] -> include amount in new list
# # for amount in transactions -> iterate through transactions
# # if amount > 100000 -> condition to include only amounts above 100,000

# print(high_transactions)  # output list

# print("**************************************")
# Way 3: Using filter() and lambda
# filter() -> filters elements based on a function

# high_transactions = list(filter(lambda x: x > 100000, transactions))  
# # lambda x: x > 100000 -> anonymous function returning True if x > 100,000
# # filter() -> keeps only elements where lambda returns True
# # list() -> convert filter object to list

# print(high_transactions)  # output filtered amounts


# print("*****************************************")
# Way 4: Using numpy array (if installed)
# import numpy as np  # import numpy module

# transactions_array = np.array(transactions)  # convert list to numpy array
# high_transactions = transactions_array[transactions_array > 100000].tolist()  
# # transactions_array > 100000 -> boolean mask
# # [ ... ] -> select elements where condition is True
# # .tolist() -> convert numpy array back to Python list

# print(high_transactions)  # display result



# print("******************************************")
# Way 5: Using for loop with continue
# high_transactions = []  # initialize empty list

# for amount in transactions:  # iterate each transaction
#     if amount <= 100000:  # check if amount is not above 100,000
#         continue  # skip to next iteration
#     high_transactions.append(amount)  # add only amounts above 100,000

# print(high_transactions)  # output filtered transactions



# print("********************************************")
# Way 6: Using map() + conditional in comprehension
# Map each amount to itself if > 100000 else None, then filter None
# high_transactions = [x for x in map(lambda y: y if y > 100000 else None, transactions) if x is not None]  
# # map(lambda y: ...) -> apply function to each element
# # x is not None -> keep only valid amounts

# print(high_transactions)  # output result


print("****************************************")

#Q:91. Extract hashtags from tweets.

# Way 1: Using for loop and split()
# List of sample tweets
tweets = [
    "Loving the new features! #Python #Coding",
    "Machine Learning is amazing! #AI #ML",
    "Good morning everyone! #Sunshine #HappyDay"
]  
# tweets -> variable holding list of strings

# Initialize empty list to store hashtags
hashtags = []  # hashtags -> list to collect hashtags

# Loop through each tweet
for tweet in tweets:  # for -> loop keyword, tweet -> current string, in -> iterate over tweets
    # Split tweet into words
    words = tweet.split()  # split() -> splits string into list of words by spaces
    for word in words:  # iterate each word
        if word.startswith("#"):  # if -> condition, word.startswith("#") -> checks if word is a hashtag
            hashtags.append(word)  # append() -> add hashtag to list

print(hashtags)  # print() -> output list of hashtags



# print("*********************************************")
# Way 2: Using List Comprehension
# Extract hashtags in one line

# hashtags = [word for tweet in tweets for word in tweet.split() if word.startswith("#")]  
# # tweet.split() -> splits tweet into words
# # for word in tweet.split() -> iterate each word
# # if word.startswith("#") -> include only hashtags

# print(hashtags)  # display result


# print("*****************************************")
# Way 3: Using filter() and lambda
# hashtags = []

# for tweet in tweets:  # iterate tweets
#     # filter words starting with #
#     tweet_hashtags = list(filter(lambda w: w.startswith("#"), tweet.split()))  
#     # filter() -> keeps elements where lambda returns True
#     # lambda w: w.startswith("#") -> returns True if word is hashtag
#     hashtags.extend(tweet_hashtags)  # extend() -> add all elements of tweet_hashtags to hashtags

# print(hashtags)  # output all hashtags




# print("**********************************************")
# Way 4: Using re module (Regular Expressions)
# import re  # import regular expression module

# hashtags = []  # initialize empty list

# for tweet in tweets:  # iterate each tweet
#     # re.findall() -> find all patterns in string
#     tweet_hashtags = re.findall(r"#\w+", tweet)  
#     # r"#\w+" -> regex pattern: '#' followed by one or more word characters
#     hashtags.extend(tweet_hashtags)  # extend() -> add all found hashtags to list

# print(hashtags)  # display hashtags


# print("****************************************")
# Way 5: Using Nested List Comprehension with re
# import re

# # Flatten and extract hashtags from all tweets
# hashtags = [tag for tweet in tweets for tag in re.findall(r"#\w+", tweet)]  
# # re.findall(r"#\w+", tweet) -> returns list of hashtags in tweet
# # tag -> each hashtag, included in final list

# print(hashtags)  # output result

# print("*****************************************")
# Way 6: Using map() + filter()
# import re

# # Map each tweet to list of hashtags
# hashtags_lists = list(map(lambda t: re.findall(r"#\w+", t), tweets))  
# # lambda t: re.findall(...) -> extract hashtags from single tweet
# # map() -> apply function to each tweet, returns list of lists

# # Flatten the list of lists
# hashtags = [tag for sublist in hashtags_lists for tag in sublist]  
# # nested comprehension to flatten list

# print(hashtags)  # display all hashtags


print("******************************************")
#Q:92. List comprehension for seat numbers A1–C5.

# Way 1: Simple Nested List Comprehension
# Generate seat numbers using list comprehension
seat_numbers = [f"{row}{col}" for row in "ABC" for col in range(1, 6)]  
# f"{row}{col}" -> formatted string combining row and column
# for row in "ABC" -> iterate over letters A, B, C (rows)
# for col in range(1, 6) -> iterate over numbers 1 to 5 (columns)
# [ ... ] -> creates list of all combinations

print(seat_numbers)  # print() -> display seat numbers


# print("******************************************")
# # Way 2: Using Nested for Loops
# seat_numbers = []  # initialize empty list

# for row in "ABC":  # iterate rows A, B, C
#     for col in range(1, 6):  # iterate columns 1 to 5
#         seat = f"{row}{col}"  # combine row and column
#         seat_numbers.append(seat)  # append seat to list

# print(seat_numbers)  # display result


# print("*************************************")
# # Way 3: Using map() and itertools.product
# from itertools import product  # import product to create all combinations

# # product("ABC", range(1,6)) -> Cartesian product of rows and columns
# seat_numbers = list(map(lambda x: f"{x[0]}{x[1]}", product("ABC", range(1, 6))))  
# # lambda x: f"{x[0]}{x[1]}" -> combine tuple (row, col) into string
# # list() -> convert map object to list

# print(seat_numbers)  # output seat numbers


# print("***************************************")
# Way 4: Using for loop + f-string in append


# seat_numbers = []  # initialize empty list

# for row in "ABC":  # loop through rows
#     for col in range(1, 6):  # loop through columns
#         seat_numbers.append(f"{row}{col}")  # append formatted string directly

# print(seat_numbers)  # display list



# print("************************************")
# Way 5: Using join() inside List Comprehension

# Generate seat numbers by joining row and column
# seat_numbers = ["".join([row, str(col)]) for row in "ABC" for col in range(1, 6)]  
# # "".join([row, str(col)]) -> combines row and column as string
# # for row in "ABC" -> iterate rows
# # for col in range(1, 6) -> iterate columns

# print(seat_numbers)  # display seats










# Interview Qs:
# 93. When to prefer list comprehension over loops?
# 94. Can list comprehensions replace map/filter?

"""
93. When to prefer list comprehension over loops?

- Use list comprehension when you want to **create a new list** from an existing iterable in a **concise and readable way**.
- Preferred for **simple transformations** or **filtering** where one line is enough.
- Advantages:
    1. **Readability**: Clear and expressive, easier to understand than multiple lines of loop code.
    2. **Conciseness**: Converts multi-line loops into a single line.
    3. **Performance**: Slightly faster than traditional for-loops due to internal optimization.
- Not recommended when:
    1. The logic is **very complex** with multiple conditions or nested loops.
    2. You need **side effects** (e.g., printing or modifying external variables) instead of creating a list.
"""

"""
94. Can list comprehensions replace map/filter?

- **Yes, list comprehensions can replace map() and filter() in most cases** because:
    1. map(function, iterable) -> applies a function to each element
        - Equivalent list comprehension: [function(x) for x in iterable]
    2. filter(function, iterable) -> selects elements where function returns True
        - Equivalent list comprehension: [x for x in iterable if function(x)]
- Advantages of using list comprehension over map/filter:
    1. **More readable**: Combines mapping and filtering in a single line.
    2. **Supports inline conditions** easily, unlike map which only transforms.
    3. **No need for lambda** for simple transformations.
- Example:
    - map: squared = list(map(lambda x: x**2, numbers))
    - list comprehension equivalent: squared = [x**2 for x in numbers]
    - filter: evens = list(filter(lambda x: x%2==0, numbers))
    - list comprehension equivalent: evens = [x for x in numbers if x%2==0]
"""
