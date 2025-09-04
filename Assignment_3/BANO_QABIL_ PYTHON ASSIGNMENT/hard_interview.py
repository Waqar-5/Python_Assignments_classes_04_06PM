# Section I: Hard Interview Questions



#Q:95. Implement your own `range()` using generator.

# Version 1: Basic generator with start, stop, step
# Define a generator function named my_range
def my_range(start, stop, step=1):  # 'start' is where counting begins, 'stop' is where it ends (exclusive), 'step' is increment
    current = start  # initialize a variable 'current' with starting value
    while current < stop:  # loop while current is less than stop
        yield current  # yield returns value and pauses function (generator behavior)
        current += step  # increment current by step
        
# Example usage:
for i in my_range(1, 10, 2):  # loop through our generator
    print(i)  # print each 


# print("********************************************************")

# Version 2: Support negative steps
# def my_range_v2(start, stop, step=1):  # generator function definition
#     current = start  # set current to start value
#     if step == 0:  # check if step is zero
#         raise ValueError("step must not be zero")  # error if step is zero
#     if step > 0:  # positive step case
#         while current < stop:  # continue as long as current < stop
#             yield current  # yield current value
#             current += step  # increment
#     else:  # negative step case
#         while current > stop:  # continue as long as current > stop
#             yield current  # yield current
#             current += step  # increment by negative step (actually decrement)
# for i in my_range_v2(10, 0, -2):  # negative step example
#     print(i)  # prints 10, 8, 6, 4, 2



# Version 3: Single argument (like built-in range)
# def my_range_v3(*args):  # accepts variable number of arguments
#     # Determine start, stop, step based on number of args
#     if len(args) == 1:  # only stop is given
#         start = 0  # start defaults to 0
#         stop = args[0]  # stop is first argument
#         step = 1  # default step is 1
#     elif len(args) == 2:  # start and stop given
#         start, stop = args  # unpack values
#         step = 1  # default step
#     elif len(args) == 3:  # start, stop, step given
#         start, stop, step = args  # unpack all three
#     else:  # invalid usage
#         raise TypeError("my_range expected 1-3 arguments, got {}".format(len(args)))  # error message
#     current = start  # initialize current
#     if step == 0:  # check step
#         raise ValueError("step must not be zero")  # raise error
#     if step > 0:  # positive step
#         while current < stop:  # loop condition
#             yield current  # yield current
#             current += step  # increment
#     else:  # negative step
#         while current > stop:  # loop condition
#             yield current  # yield current
#             current += step  # increment by negative
# for i in my_range_v3(5):  # only stop
#     print(i)  # prints 0,1,2,3,4



# Version 4: Using itertools.count internally
# from itertools import count  # import count (infinite iterator)

# def my_range_v4(start, stop, step=1):  # generator function
#     if step == 0:  # validate step
#         raise ValueError("step cannot be zero")  # raise error
#     for i in count(start, step):  # infinite count starting from start
#         if (step > 0 and i >= stop) or (step < 0 and i <= stop):  # break condition
#             break  # stop iteration
#         yield i  # yield current value
# for i in my_range_v4(2, 10, 3):  # prints 2, 5, 8
#     print(i)





print("********************************************************")
#Q:96. Write your own `enumerate()` logic with loop.
# Version 1: Basic for-loop
def my_enumerate(iterable, start=0): # define generator function, start index default 0
    index = start # initialize index variable with start value
    for element in iterable: # loop through each element in iterable
        yield index, element   # yield a tuple (index, element) lazily
        index += 1 # increment index by 1


# Usage example
print("=== Versiob 1 ===")
fruits = ['apple', 'banana', 'cherry']  # sample list
for idx, val in my_enumerate(fruits, 1):  # loop using generator, start index 1
    print(idx, val)  # print index and element





# # Version 2: While loop

# def my_enumerate_v2(iterable, start=0):  # define generator function
#     index = start  # initialize index variable
#     i = 0  # initialize counter for while loop
#     while i < len(iterable):  # loop while counter less than length of iterable
#         yield index, iterable[i]  # yield index and current element
#         index += 1  # increment index
#         i += 1  # increment counter

# # Usage example
# print("\n=== Version 2 ===")
# for idx, val in my_enumerate_v2(['a', 'b', 'c']):  # loop with while-based generator
#     print(idx, val)  # print index and element


# # Version 3: Using iter() and next()

# def my_enumerate_v3(iterable, start=0):  # define generator function
#     it = iter(iterable)  # get iterator from iterable
#     index = start  # initialize index variable
#     while True:  # infinite loop
#         try:  
#             element = next(it)  # get next element from iterator
#             yield index, element  # yield index and element
#             index += 1  # increment index
#         except StopIteration:  # catch StopIteration when iterator ends
#             break  # exit the loop

# # Usage example
# print("\n=== Version 3 ===")
# for idx, val in my_enumerate_v3(['x', 'y', 'z'], 5):  # loop using next(), start index 5
#     print(idx, val)  # print index and element


# # Version 4: One-line generator expression

# def my_enumerate_v4(iterable, start=0):  # define generator function
#     return ((i + start, val) for i, val in zip(range(len(iterable)), iterable))  
#     # zip index range with iterable, create tuples (index + start, value)

# # Usage example
# print("\n=== Version 4 ===")
# for idx, val in my_enumerate_v4(['p', 'q', 'r']):  # loop using one-line generator
#     print(idx, val)  # print index and element


print("*******************************************************")
#Q:97. Reverse dictionary {key: value} → {value: key}.

# Version 1: Using dictionary comprehension
def reverse_dict_v1(d): # define a function named reverse_dict_v1 with parameter d (dictionary)
    return {v: k for k, v in d.items()}  # create new dictionary: value becomes key, key becomes value

# Usage example
print("=== Version 1 ===")
original_dict = {'a': 1, 'b': 2, 'c': 3}  # sample dictionary
reversed_dict = reverse_dict_v1(original_dict)  # call reverse function
print(reversed_dict)  # print reversed dictionary




# # Version 2: Using loop and assignment

# def reverse_dict_v2(d):  # define function with dictionary parameter
#     reversed_d = {}  # create empty dictionary
#     for key, value in d.items():  # loop through each key, value in dictionary items
#         reversed_d[value] = key  # assign value as key, key as value in new dictionary
#     return reversed_d  # return reversed dictionary

# # Usage example
# print("\n=== Version 2 ===")
# reversed_dict2 = reverse_dict_v2({'x': 10, 'y': 20, 'z': 30})  # call function
# print(reversed_dict2)  # print result


# # Version 3: Using zip()

# def reverse_dict_v3(d):  # define function
#     keys = d.keys()  # get dictionary keys
#     values = d.values()  # get dictionary values
#     return dict(zip(values, keys))  # zip values with keys and convert to dictionary

# # Usage example
# print("\n=== Version 3 ===")
# reversed_dict3 = reverse_dict_v3({'apple': 'red', 'banana': 'yellow', 'cherry': 'red2'})
# print(reversed_dict3)


# # Version 4: Using map() and dict()

# def reverse_dict_v4(d):  # define function
#     return dict(map(lambda kv: (kv[1], kv[0]), d.items()))  
#     # map each key-value tuple to (value, key) and convert to dictionary

# # Usage example
# print("\n=== Version 4 ===")
# reversed_dict4 = reverse_dict_v4({'p': 5, 'q': 6, 'r': 7})  # call function
# print(reversed_dict4)


# # Version 5: Using dictionary update in loop

# def reverse_dict_v5(d):  # define function
#     reversed_d = {}  # initialize empty dictionary
#     for k, v in d.items():  # loop through items
#         reversed_d.update({v: k})  # update new dictionary with {value: key}
#     return reversed_d  # return reversed dictionary

# # Usage example
# print("\n=== Version 5 ===")
# reversed_dict5 = reverse_dict_v5({'one': 1, 'two': 2, 'three': 3})  # call function
# print(reversed_dict5)



print("*********************************************")
#Q:98. Find all unique pairs in list that sum to target.
# Version 1: Using nested loops
def unique_pairs_v1(lst, target):  # define function with parameters lst (list) and target (int)
    pairs = []  # initialize empty list to store pairs
    for i in range(len(lst)):  # loop through list indices
        for j in range(i + 1, len(lst)):  # loop through remaining indices after i
            if lst[i] + lst[j] == target:  # check if sum of two elements equals target
                pair = tuple(sorted((lst[i], lst[j])))  # create sorted tuple (smaller, larger)
                if pair not in pairs:  # check uniqueness
                    pairs.append(pair)  # add pair to list
    return pairs  # return list of unique pairs

# Usage example
print("=== Version 1 ===")
numbers = [1, 2, 3, 4, 3, 2]  # sample list
target = 5  # target sum
print(unique_pairs_v1(numbers, target))  # print result





# # Version 2: Using set to track seen numbers

# def unique_pairs_v2(lst, target):  # define function
#     seen = set()  # initialize set to track numbers
#     output = set()  # initialize set to store unique pairs
#     for num in lst:  # loop through each number in list
#         complement = target - num  # calculate complement that sums to target
#         if complement in seen:  # check if complement exists in seen set
#             output.add(tuple(sorted((num, complement))))  # add sorted pair to output
#         seen.add(num)  # add current number to seen set
#     return list(output)  # convert output set to list and return

# # Usage example
# print("\n=== Version 2 ===")
# print(unique_pairs_v2([1, 2, 3, 4, 3, 2], 5))  # example call


# # Version 3: Using dictionary to track complements

# def unique_pairs_v3(lst, target):  # define function
#     d = {}  # initialize empty dictionary
#     pairs = set()  # initialize set to store unique pairs
#     for num in lst:  # loop through each number
#         complement = target - num  # calculate complement
#         if complement in d:  # check if complement seen before
#             pairs.add(tuple(sorted((num, complement))))  # add sorted pair to set
#         d[num] = True  # mark current number as seen
#     return list(pairs)  # convert set to list and return

# # Usage example
# print("\n=== Version 3 ===")
# print(unique_pairs_v3([1, 2, 3, 4, 3, 2], 5))  # example call


# # Version 4: Using itertools.combinations

# from itertools import combinations  # import combinations function

# def unique_pairs_v4(lst, target):  # define function
#     pairs = set()  # initialize set to store unique pairs
#     for a, b in combinations(lst, 2):  # generate all 2-element combinations
#         if a + b == target:  # check if sum equals target
#             pairs.add(tuple(sorted((a, b))))  # add sorted pair to set
#     return list(pairs)  # convert set to list and return

# # Usage example
# print("\n=== Version 4 ===")
# print(unique_pairs_v4([1, 2, 3, 4, 3, 2], 5))  # example call


# # Version 5: Using list comprehension

# def unique_pairs_v5(lst, target):  # define function
#     return list({tuple(sorted((lst[i], lst[j])))  # create set of sorted tuples
#                  for i in range(len(lst))  # loop over all indices i
#                  for j in range(i + 1, len(lst))  # loop over indices after i
#                  if lst[i] + lst[j] == target})  # check sum equals target

# # Usage example
# print("\n=== Version 5 ===")
# print(unique_pairs_v5([1, 2, 3, 4, 3, 2], 5))  # example call


print("*********************************************")
# 99. Check balanced parentheses using loop.
# Version 1: Using simple counter for ()

def is_balanced_v1(s):  # define function with string parameter s
    count = 0  # initialize counter to 0
    for char in s:  # loop through each character in string
        if char == '(':  # if character is opening parenthesis
            count += 1  # increment counter
        elif char == ')':  # if character is closing parenthesis
            count -= 1  # decrement counter
        if count < 0:  # if counter goes negative
            return False  # parentheses are not balanced
    return count == 0  # return True if all opened parentheses are closed

# Usage example
print("=== Version 1 ===")
print(is_balanced_v1("((()))"))  # True
print(is_balanced_v1("(()"))     # False




# # Version 2: Using stack with list

# def is_balanced_v2(s):  # define function
#     stack = []  # initialize empty list as stack
#     for char in s:  # loop through each character
#         if char == '(':  # opening parenthesis
#             stack.append(char)  # push to stack
#         elif char == ')':  # closing parenthesis
#             if not stack:  # if stack is empty
#                 return False  # unbalanced
#             stack.pop()  # pop last opening parenthesis
#     return not stack  # True if stack empty (balanced)

# # Usage example
# print("\n=== Version 2 ===")
# print(is_balanced_v2("((()()))"))  # True
# print(is_balanced_v2("())("))      # False


# # Version 3: Using dictionary for multiple types (), {}, []

# def is_balanced_v3(s):  # define function
#     stack = []  # initialize empty stack
#     pairs = {'(': ')', '{': '}', '[': ']'}  # dictionary mapping opening to closing
#     for char in s:  # loop through each character
#         if char in pairs:  # if char is opening bracket
#             stack.append(char)  # push to stack
#         elif char in pairs.values():  # if char is closing bracket
#             if not stack:  # stack empty
#                 return False  # unbalanced
#             last = stack.pop()  # pop last opening bracket
#             if pairs[last] != char:  # check if types match
#                 return False  # not balanced
#     return not stack  # True if stack empty

# # Usage example
# print("\n=== Version 3 ===")
# print(is_balanced_v3("({[]})"))  # True
# print(is_balanced_v3("({[})]"))  # False


# # Version 4: Using counter only for multiple types with separate counters

# def is_balanced_v4(s):  # define function
#     paren = 0  # counter for ()
#     curly = 0  # counter for {}
#     square = 0  # counter for []
#     for char in s:  # loop through each character
#         if char == '(': paren += 1
#         elif char == ')': paren -= 1
#         elif char == '{': curly += 1
#         elif char == '}': curly -= 1
#         elif char == '[': square += 1
#         elif char == ']': square -= 1
#         if paren < 0 or curly < 0 or square < 0:  # if any counter negative
#             return False  # unbalanced
#     return paren == 0 and curly == 0 and square == 0  # all counters zero

# # Usage example
# print("\n=== Version 4 ===")
# print(is_balanced_v4("{[()]}"))   # True
# print(is_balanced_v4("{[(])}"))   # False


# # Version 5: Using stack with loop and break

# def is_balanced_v5(s):  # define function
#     stack = []  # initialize empty stack
#     pairs = {'(': ')', '{': '}', '[': ']'}  # mapping opening to closing
#     for char in s:  # loop through each character
#         if char in pairs:  # opening
#             stack.append(char)  # push to stack
#         elif char in pairs.values():  # closing
#             if not stack or pairs[stack.pop()] != char:  # check top matches
#                 return False  # unbalanced
#     return not stack  # balanced if stack empty

# # Usage example
# print("\n=== Version 5 ===")
# print(is_balanced_v5("({[]})"))  # True
# print(is_balanced_v5("({[})]"))  # False




print("*******************************************")
#Q:100. Implement a basic menu-driven system (1=Add, 2=Delete, 3=Exit).

# Version 1: Using while loop and if-elif-else
def menu_v1(): # define function menu_v1
    items = [] # initialize empty list to store items
    while True: # infinite loop for menu
        print("\nMenu:")  # print menu header
        print("1. Add")  # option 1
        print("2. Delete")  # option 2
        print("3. Exit")  # option 3
        choice = input("Enter choice: ") # take input from user

        if choice == "1": # if choice is 1
            item = input("Enter item to add: ") # ask item to add
            items.append(item)  #add item to list
            print(f"Item added: {item}")  # print confirmation
        elif choice == "2": # if choice is 2
            item = input("Enter item to delete: ") #ask item to delete
            if item in items: # check if item exists
                items.remove(item) # remove item from list
                print(f"Item deleted: {item}")  # print confirmation
            else: #item not found
                print(f"{item} not found") # print error
        elif choice == "3": # if choice is 3
            print("Exiting...") # print exit message
            break # exit loop
        else:
            print("Invalid choice")  # print error


# Usage example
menu_v1()





# # Version 2: Using dictionary of functions

# def add_item(items):  # define add function
#     item = input("Enter item to add: ")  # input item
#     items.append(item)  # add to list
#     print(f"Item added: {item}")  # print confirmation

# def delete_item(items):  # define delete function
#     item = input("Enter item to delete: ")  # input item
#     if item in items:  # check if item exists
#         items.remove(item)  # remove item
#         print(f"Item deleted: {item}")  # confirmation
#     else:  # not found
#         print(f"{item} not found")  # error

# def exit_menu(items):  # define exit function
#     print("Exiting...")  # print message
#     exit()  # terminate program

# def menu_v2():  # define menu function
#     items = []  # initialize empty list
#     options = {'1': add_item, '2': delete_item, '3': exit_menu}  # map choice to functions
#     while True:  # infinite loop
#         print("\nMenu:\n1. Add\n2. Delete\n3. Exit")  # print menu
#         choice = input("Enter choice: ")  # take input
#         if choice in options:  # if valid choice
#             options[choice](items)  # call corresponding function
#         else:  # invalid choice
#             print("Invalid choice")  # print error

# # Usage example
# # menu_v2()


# # Version 3: Using match-case (Python 3.10+)

# def menu_v3():  # define function
#     items = []  # empty list
#     while True:  # infinite loop
#         print("\nMenu:\n1. Add\n2. Delete\n3. Exit")  # menu
#         choice = input("Enter choice: ")  # input choice
#         match choice:  # match choice
#             case '1':  # add
#                 item = input("Enter item to add: ")  # input item
#                 items.append(item)  # append
#                 print(f"Item added: {item}")  # print confirmation
#             case '2':  # delete
#                 item = input("Enter item to delete: ")  # input item
#                 if item in items:  # check exists
#                     items.remove(item)  # remove
#                     print(f"Item deleted: {item}")  # confirmation
#                 else:  # not found
#                     print(f"{item} not found")  # error
#             case '3':  # exit
#                 print("Exiting...")  # exit message
#                 break  # break loop
#             case _:  # default
#                 print("Invalid choice")  # invalid input

# # Usage example
# # menu_v3()




print("*********************************************")
#Q:101. Print JSON-like dictionary with nested loop.
# Version 1: Nested for loops

# Sample nested dictionary
sample_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30},
    "person3": {"name": "Charlie", "age": 35}
}


def print_nested_v1(d):  # define function with dictionary parameter d
    for key, value in d.items():  # outer loop through key, value pairs
        print(f"{key}:")  # print outer key
        for inner_key, inner_value in value.items():  # inner loop through nested dictionary
            print(f"  {inner_key}: {inner_value}")  # print inner key and value with indentation

# Usage example
print("=== Version 1 ===")
print_nested_v1(sample_dict)




# # Version 2: Using recursion

# def print_nested_v2(d, indent=0):  # define function with dictionary and indent level
#     for key, value in d.items():  # loop through dictionary items
#         print("  " * indent + str(key) + ":")  # print key with indentation
#         if isinstance(value, dict):  # check if value is a dictionary
#             print_nested_v2(value, indent + 1)  # recursive call with increased indentation
#         else:  # value is not a dictionary
#             print("  " * (indent + 1) + str(value))  # print value with indentation

# # Usage example
# print("\n=== Version 2 ===")
# print_nested_v2(sample_dict)


# # Version 3: Using json module for pretty print

# import json  # import json module

# def print_nested_v3(d):  # define function
#     print(json.dumps(d, indent=2))  # use json.dumps to pretty print with 2-space indentation

# # Usage example
# print("\n=== Version 3 ===")
# print_nested_v3(sample_dict)


# # Version 4: Using dictionary comprehension with nested loops (formatted)

# def print_nested_v4(d):  # define function
#     for key, value in d.items():  # outer loop
#         print(f"{key}:")  # print outer key
#         [print(f"  {k}: {v}") for k, v in value.items()]  # inner loop using list comprehension to print inner items

# # Usage example
# print("\n=== Version 4 ===")
# print_nested_v4(sample_dict)


# # Version 5: Flatten and print with nested loops

# def print_nested_v5(d):  # define function
#     for outer_key in d:  # loop through outer dictionary keys
#         print(f"{outer_key}:")  # print outer key
#         for inner_key in d[outer_key]:  # loop through inner dictionary keys
#             print(f"  {inner_key}: {d[outer_key][inner_key]}")  # print inner key and value

# # Usage example
# print("\n=== Version 5 ===")
# print_nested_v5(sample_dict)


print("******************************************")
# Sample user credentials dictionary
users = {
    "alice": "pass123",  # username: password
    "bob": "secret",     # username: password
    "charlie": "abc123"  # username: password
}

# Version 1: Basic if-else
def login_v1(user_dict):  # define function with dictionary parameter
    username = input("Enter username: ")  # input username
    password = input("Enter password: ")  # input password
    if username in user_dict:  # check if username exists
        if user_dict[username] == password:  # check if password matches
            print("Login successful")  # success message
        else:  # password incorrect
            print("Incorrect password")  # error message
    else:  # username not found
        print("Username not found")  # error message

# Usage example
login_v1(users)







# # Version 2: Using loop for multiple attempts
# def login_v2(user_dict, attempts=3):  # define function with attempts parameter
#     for _ in range(attempts):  # loop for number of attempts
#         username = input("Enter username: ")  # input username
#         password = input("Enter password: ")  # input password
#         if username in user_dict and user_dict[username] == password:  # valid credentials
#             print("Login successful")  # success
#             return True  # exit function
#         else:  # invalid credentials
#             print("Invalid username or password")  # error message
#     print("Exceeded attempts. Login failed.")  # exceeded attempts message
#     return False  # login failed

# # Usage example
# # login_v2(users)

# # Version 3: Using try-except

# def login_v3(user_dict):  # define function
#     username = input("Enter username: ")  # input username
#     password = input("Enter password: ")  # input password
#     try:  # try block
#         if user_dict[username] == password:  # check credentials
#             print("Login successful")  # success
#         else:  # password incorrect
#             print("Incorrect password")  # error
#     except KeyError:  # username not in dictionary
#         print("Username not found")  # error message

# # Usage example
# # login_v3(users)


# # Version 4: Using dictionary get()

# def login_v4(user_dict):  # define function
#     username = input("Enter username: ")  # input username
#     password = input("Enter password: ")  # input password
#     if user_dict.get(username) == password:  # get returns None if username not found
#         print("Login successful")  # success
#     else:  # invalid credentials
#         print("Invalid username or password")  # error message

# # Usage example
# # login_v4(users)


# # Version 5: Using while loop for retry until success or exit

# def login_v5(user_dict):  # define function
#     while True:  # infinite loop
#         username = input("Enter username: ")  # input username
#         password = input("Enter password: ")  # input password
#         if username in user_dict and user_dict[username] == password:  # valid credentials
#             print("Login successful")  # success message
#             break  # exit loop
#         else:  # invalid credentials
#             print("Invalid username or password")  # error message
#         retry = input("Try again? (y/n): ")  # ask to retry
#         if retry.lower() != 'y':  # if not yes
#             print("Exiting login.")  # exit message
#             break  # exit loop

# # Usage example
# login_v5(users)



print("**********************************************************")
# Q:103. Implement word frequency counter without using collections.



# Version 1: Using dictionary and for loop

# Sample text
text = "hello world hello python world hello"

def word_freq_v1(text):  # define function with parameter text
    freq = {}  # initialize empty dictionary to store frequencies
    words = text.split()  # split text into list of words
    for word in words:  # loop through each word
        if word in freq:  # check if word already in dictionary
            freq[word] += 1  # increment count
        else:  # word not in dictionary
            freq[word] = 1  # initialize count to 1
    return freq  # return frequency dictionary

# Usage example
print("=== Version 1 ===")
print(word_freq_v1(text))  # print word frequencies


# # Version 2: Using dictionary get() method

# def word_freq_v2(text):  # define function
#     freq = {}  # empty dictionary
#     for word in text.split():  # loop through words
#         freq[word] = freq.get(word, 0) + 1  # get current count or 0 and increment
#     return freq  # return dictionary

# # Usage example
# print("\n=== Version 2 ===")
# print(word_freq_v2(text))  # print result


# # Version 3: Using set to iterate unique words

# def word_freq_v3(text):  # define function
#     freq = {}  # empty dictionary
#     words = text.split()  # split text into words
#     unique_words = set(words)  # get unique words
#     for word in unique_words:  # loop through unique words
#         freq[word] = words.count(word)  # count occurrences using list.count()
#     return freq  # return dictionary

# # Usage example
# print("\n=== Version 3 ===")
# print(word_freq_v3(text))  # print result


# # Version 4: Using nested loops

# def word_freq_v4(text):  # define function
#     freq = {}  # empty dictionary
#     words = text.split()  # split text
#     for word in words:  # outer loop
#         count = 0  # initialize counter
#         for w in words:  # inner loop
#             if w == word:  # if word matches
#                 count += 1  # increment counter
#         freq[word] = count  # assign count to dictionary
#     return freq  # return dictionary

# # Usage example
# print("\n=== Version 4 ===")
# print(word_freq_v4(text))  # print result


# # Version 5: Using try-except

# def word_freq_v5(text):  # define function
#     freq = {}  # empty dictionary
#     for word in text.split():  # loop through words
#         try:  # try block
#             freq[word] += 1  # increment count if exists
#         except KeyError:  # if word not in dictionary
#             freq[word] = 1  # initialize count
#     return freq  # return dictionary

# # Usage example
# print("\n=== Version 5 ===")
# print(word_freq_v5(text))  # print result




print("*************************************************************")
# Q:104. Implement pagination (show 5 records per age).

# =========================================================
# Pagination by Age
# Author: Waqar Ali
# Purpose: Demonstrate multiple ways to paginate records (5 per age)
# =========================================================

# Sample data: list of dictionaries with name and age
records = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 25},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
    {"name": "Frank", "age": 30},
    {"name": "Grace", "age": 25},
    {"name": "Hannah", "age": 30},
    {"name": "Ivy", "age": 25},
    {"name": "Jack", "age": 30},
    {"name": "Karen", "age": 25},
]


# Version 1: Using dictionary grouping and slices

def paginate_v1(records):  # define function
    pages = {}  # initialize empty dictionary to hold pages by age
    for record in records:  # loop through each record
        age = record["age"]  # extract age
        if age not in pages:  # if age not in dictionary
            pages[age] = []  # initialize empty list for that age
        pages[age].append(record)  # append record to age group

    # now paginate 5 records per age
    for age, recs in pages.items():  # loop through age groups
        print(f"\nAge: {age}")  # print age
        for i in range(0, len(recs), 5):  # loop with step 5
            print("Page:", (i // 5) + 1)  # print page number
            for r in recs[i:i + 5]:  # slice 5 records
                print(r)  # print record

# Usage example
print("=== Version 1 ===")
paginate_v1(records)


# # Version 2: Using while loop for pagination

# def paginate_v2(records, per_page=5):  # define function with per_page parameter
#     pages = {}  # initialize dictionary
#     for record in records:  # loop records
#         age = record["age"]  # extract age
#         if age not in pages:  # check age
#             pages[age] = []  # initialize list
#         pages[age].append(record)  # add record

#     for age, recs in pages.items():  # loop through age groups
#         print(f"\nAge: {age}")  # print age
#         start = 0  # starting index
#         page_num = 1  # page counter
#         while start < len(recs):  # loop while start index less than total records
#             print(f"Page: {page_num}")  # print page number
#             print(recs[start:start + per_page])  # print slice of records
#             start += per_page  # increment start index
#             page_num += 1  # increment page number

# # Usage example
# print("\n=== Version 2 ===")
# paginate_v2(records)


# # Version 3: Using generator function

# def paginate_v3(records, per_page=5):  # define generator function
#     pages = {}  # dictionary for age grouping
#     for record in records:  # loop through records
#         age = record["age"]  # get age
#         if age not in pages:  # check age in dictionary
#             pages[age] = []  # initialize list
#         pages[age].append(record)  # append record

#     for age, recs in pages.items():  # loop through age groups
#         for i in range(0, len(recs), per_page):  # loop with step per_page
#             yield age, (i // per_page) + 1, recs[i:i + per_page]  # yield age, page number, and slice

# # Usage example
# print("\n=== Version 3 ===")
# for age, page_num, page_records in paginate_v3(records):
#     print(f"\nAge: {age} | Page: {page_num}")
#     for r in page_records:
#         print(r)


# # Version 4: Using dictionary comprehension for grouping

# def paginate_v4(records, per_page=5):  # define function
#     # group records by age using dictionary comprehension
#     pages = {age: [r for r in records if r["age"] == age] for age in set(r["age"] for r in records)}
#     for age, recs in pages.items():  # loop age groups
#         print(f"\nAge: {age}")  # print age
#         for i in range(0, len(recs), per_page):  # loop with step per_page
#             print(f"Page: {(i // per_page) + 1}")  # print page number
#             for r in recs[i:i + per_page]:  # print records slice
#                 print(r)  # print each record

# # Usage example
# print("\n=== Version 4 ===")
# paginate_v4(records)






print("****************************************************")
# Q:105. Simulte restaurant order system with while + dict
# =========================================================
# Restaurant Order System
# Author: Waqar Ali
# Purpose: Demonstrate multiple ways to simulate a restaurant order system using while + dictionary
# =========================================================

# Sample menu dictionary with items and prices
menu = {
    "Burger": 5.99,   # item: price
    "Pizza": 8.99,    # item: price
    "Pasta": 7.49,    # item: price
    "Salad": 4.99     # item: price
}


# Version 1: Simple while loop and dict for orders

def order_system_v1(menu):  # define function with menu parameter
    orders = {}  # initialize empty dictionary for orders
    while True:  # infinite loop for taking orders
        print("\nMenu:")  # print menu header
        for item, price in menu.items():  # loop through menu items
            print(f"{item}: ${price}")  # print item and price
        choice = input("Enter item to order (or 'exit' to finish): ")  # take user input
        if choice.lower() == 'exit':  # check if user wants to exit
            break  # exit loop
        elif choice in menu:  # check if choice is valid
            quantity = int(input(f"Enter quantity for {choice}: "))  # input quantity
            if choice in orders:  # check if item already in orders
                orders[choice] += quantity  # increment quantity
            else:  # first time ordering this item
                orders[choice] = quantity  # add to orders
        else:  # invalid item
            print("Invalid item. Please choose from menu.")  # print error message
    # print final bill
    print("\nYour Order Summary:")
    total = 0  # initialize total cost
    for item, quantity in orders.items():  # loop through orders
        cost = menu[item] * quantity  # calculate cost
        total += cost  # add to total
        print(f"{item} x {quantity} = ${cost:.2f}")  # print item summary
    print(f"Total: ${total:.2f}")  # print total

# Usage example
order_system_v1(menu)


# # Version 2: Using get() method for safer addition

# def order_system_v2(menu):  # define function
#     orders = {}  # initialize empty dictionary
#     while True:  # infinite loop
#         print("\nMenu:")
#         for item, price in menu.items():  # loop menu
#             print(f"{item}: ${price}")  # print items
#         choice = input("Enter item to order (or 'exit' to finish): ")  # input
#         if choice.lower() == 'exit':  # exit condition
#             break  # exit
#         elif choice in menu:  # valid choice
#             quantity = int(input(f"Enter quantity for {choice}: "))  # input quantity
#             orders[choice] = orders.get(choice, 0) + quantity  # add quantity using get
#         else:  # invalid choice
#             print("Invalid item. Please choose from menu.")  # error message
#     # print final bill
#     print("\nYour Order Summary:")
#     total = 0  # total cost
#     for item, quantity in orders.items():  # loop orders
#         cost = menu[item] * quantity  # calculate cost
#         total += cost  # add to total
#         print(f"{item} x {quantity} = ${cost:.2f}")  # print summary
#     print(f"Total: ${total:.2f}")  # print total

# # Usage example
# # order_system_v2(menu)


# # Version 3: Using try-except to handle invalid quantity input

# def order_system_v3(menu):  # define function
#     orders = {}  # empty dictionary
#     while True:  # loop indefinitely
#         print("\nMenu:")
#         for item, price in menu.items():  # loop menu
#             print(f"{item}: ${price}")  # print items
#         choice = input("Enter item to order (or 'exit' to finish): ")  # input choice
#         if choice.lower() == 'exit':  # exit check
#             break  # break loop
#         elif choice in menu:  # valid item
#             try:  # try block for quantity input
#                 quantity = int(input(f"Enter quantity for {choice}: "))  # input quantity
#                 orders[choice] = orders.get(choice, 0) + quantity  # add to orders
#             except ValueError:  # if input not integer
#                 print("Invalid quantity. Please enter a number.")  # print error
#         else:  # invalid menu item
#             print("Invalid item. Please choose from menu.")  # error message
#     # print final bill
#     print("\nYour Order Summary:")
#     total = 0  # initialize total
#     for item, quantity in orders.items():  # loop orders
#         cost = menu[item] * quantity  # calculate cost
#         total += cost  # add to total
#         print(f"{item} x {quantity} = ${cost:.2f}")  # print summary
#     print(f"Total: ${total:.2f}")  # print total

# # Usage example
# # order_system_v3(menu)


# # Version 4: Using while loop with confirmation for each order

# def order_system_v4(menu):  # define function
#     orders = {}  # initialize dictionary
#     while True:  # infinite loop
#         print("\nMenu:")
#         for item, price in menu.items():  # loop menu
#             print(f"{item}: ${price}")  # print items
#         choice = input("Enter item to order (or 'exit' to finish): ")  # input choice
#         if choice.lower() == 'exit':  # exit check
#             break  # exit loop
#         elif choice in menu:  # valid item
#             quantity = int(input(f"Enter quantity for {choice}: "))  # input quantity
#             confirm = input(f"Confirm order {quantity} x {choice}? (y/n): ")  # confirm order
#             if confirm.lower() == 'y':  # if yes
#                 orders[choice] = orders.get(choice, 0) + quantity  # add to orders
#                 print(f"Added {quantity} x {choice}")  # print confirmation
#             else:  # if no
#                 print("Order cancelled")  # print cancellation
#         else:  # invalid item
#             print("Invalid item. Please choose from menu.")  # error message
#     # print final bill
#     print("\nYour Order Summary:")
#     total = 0  # total cost
#     for item, quantity in orders.items():  # loop orders
#         cost = menu[item] * quantity  # calculate cost
#         total += cost  # add to total
#         print(f"{item} x {quantity} = ${cost:.2f}")  # print summary
#     print(f"Total: ${total:.2f}")  # print total

# # Usage example
# # order_system_v4(menu)
