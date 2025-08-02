#  Factorial of Numbers and Count Even/Odd Factorials
# Factorial of Numbers and Count Even/Odd Factorials

# Step 1: Take input from user
count = int(input("How many numbers? : "))

# Step 2: Create lists
factorials = []       # to store all factorials
even_fact = []      # to store even factorials
odd_fact = []       # to store odd factorials


# Step 3: Loop through each number
for i in range(count):
    num = int(input(f"Enter number {i + 1}: "))
    fact = 1

 # Step 4: Calculate factorial
    for j in range(1, num + 1):
        fact *= j
    
      # Step 5: Store in the total factorials list
    factorials.append(fact)

      # Step 6: Separate even and odd factorials
    if fact % 2 == 0:
        even_fact.append(fact)
    else:
        odd_fact.append(fact)

# Step 7: Print results
print("\nAll Factorials:", factorials)
print("Even Factorials:", even_fact)
print("Odd Factorials:", odd_fact)






# # other way


# user_input = int(input("How many values you want to enter: "))

# factorials = []
# odd = []
# even = []

# for var in range(user_input):
#     num = int(input(f"Enter value {var+1}: "))
#     fact = 1

#     # Calculate factorial
#     for i in range(1, num + 1):
#         fact *= i

#     factorials.append(fact)

#     # Check even or odd based on original number
#     if num % 2 == 0:
#         even.append(fact)
#     else:
#         odd.append(fact)

# # Show results
# print("\nAll Factorials:", factorials)
# print("Even Number Factorials:", even)
# print("Odd Number Factorials:", odd)
