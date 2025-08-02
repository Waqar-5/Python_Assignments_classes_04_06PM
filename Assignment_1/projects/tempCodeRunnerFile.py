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
