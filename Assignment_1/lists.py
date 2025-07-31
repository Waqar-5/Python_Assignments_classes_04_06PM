# Lists (Q21–Q27)
# Q:21. Create a list of 5 favorite fruits. Print the 3rd fruit.
# list created
fruits = ["Apple", "Orange", "Mango", "Kiwi", "Banana"]
print(fruits[2]) # Index 2 = 3rd item is Mango

print("***********************************************")

# Q:22.Add a new fruit to the end. Print updated list.
print("Original fruits list: ", fruits)
fruits.append("Grapes")
print("After adding an element at the end of list : ", fruits)


print("***********************************************")
# Q:23. Remove the 2nd item. Print the list.
print("Original fruits list: ", fruits)
# Remove the 2nd item (index 1)
fruits.pop(1)
print("After removing 2nd item from a list : ", fruits)


print("***********************************************")
# Q:24. Sort the list alphabetically and print it.
print("Original fruits list: ", fruits)

# Sort alphabetically
fruits.sort()
print("After sorting list: ",fruits)

print("***********************************************")

# Q:25. Replace all even numbers in a list of 5 numbers with "Even" using a loop.

# Starting list of 5 numbers
num = [1, 2, 3, 4, 5]
# Loop through the list by index
for i in range(len(num)):
    if num[i] % 2 == 0:     # if number is even
        num[i] = "Even"      # replace it with the word "Even"
# Print the updated list
print(num)

print("***********************************************")
# Q:26. Write a function that returns a new list with only unique elements.
# Function to get only unique elements from a list
def get_unique_elements(lst):
    unique_list = []  # Create an empty list to store unique items
    
    # Loop through each item in the input list
    for item in lst:
        # Check if the item is not already in the unique_list
        if item not in unique_list:
            unique_list.append(item)  # If it's not there, add it to the unique_list

    return unique_list  # Return the list of unique items


# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5]  # A sample list with some duplicate values
result = get_unique_elements(my_list)  # Call the function and store the result


# Print the original and the result lists
print("Original list:", my_list)         # Shows the original list with duplicates
print("Unique elements:", result)        # Shows only the unique values (no duplicates)



# def get_unique_fruits(fruits_list):
#     unique_fruits = []
#     for fruit in fruits_list:
#         if fruit not in unique_fruits:
#             unique_fruits.append(fruit)
#     return unique_fruits

# # Try it
# my_fruits = ["apple", "banana", "apple", "orange", "banana", "grape"]
# print("original list: ", my_fruits)
# result = get_unique_fruits(my_fruits)
# print("Unique fruits:", result)



print("***********************************************")
# Q:27. Sort a list of words by word length (not alphabetically).
# print("Original list: ", fruits)
# fruits.sort(key=len)  # ✅ Sort by length of each word
# print("Sorted by length:", fruits)


print("Original list: ", fruits)  
# Step 2: Print the list before sorting

fruits.sort(key=len)  
# Step 3: Sort by word length using len() function as a 'key'

print("Sorted by length:", fruits)  
# Step 4: Show sorted list



print("***********************************************")

"""
Python Lists – Key Points (Short & Powerful)
✅ Mutable – You can change values.

📦 Use square brackets: []

🧮 Indexing starts at 0 – mylist[0]

🔄 Slicing supported – mylist[1:3]

➕ Add items – append(), insert(), extend()

❌ Remove items – remove(), pop(), clear()

🔍 Find item index – index()

🔁 Loop through list – for item in mylist:

✅ Can store any data type – even mixed types.

🧠 Nested lists allowed – [1, [2, 3]]

📏 Get length – len(mylist)

🧹 Sort and reverse – sort(), reverse()

🆕 List comprehension – [x*2 for x in mylist]

🧪 Check membership – 'a' in mylist

🧊 Copy list safely – mylist.copy() (not just =)

⚠️ Negative indexing – mylist[-1] gives last item.

🔗 Join list to string – ' '.join(list_of_strings)

🧾 Count items – mylist.count(x)

⚙️ Can hold objects, functions, or lists

⚡ Flexible and most used data type in Python!

"""