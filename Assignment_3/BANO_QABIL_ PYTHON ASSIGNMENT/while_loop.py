# Section B: While Loop (Real-Life + Interview Qs)

# 13. Keep asking user for password until it matches `"secure123"`.
while True:
    password = input("Enter the password: ")
    if password == "secure123":
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")


print("***********************************************************")

# Using while loop
# Commit: Start of While Loop Approach
# password = ""  # Commit: Initialize password variable

# # Commit: Keep asking until correct password is entered
# while password != "secure123":  # Commit: Loop until password matches
#     password = input("Enter your password: ")  # Commit: Ask user for input
#     if password == "secure123":  # Commit: Check if input matches correct password
#         print("Access granted!")  # Commit: Notify user of success
#     else:
#         print("Wrong password, try again.")  # Commit: Notify user of wrong attempt
# # Commit: End of While Loop Approach



# Commit: Start of Do-While Loop Equivalent
# while True:  # Commit: Infinite loop to simulate do-while
#     pwd = input("Enter password: ")  # Commit: Ask user input
#     if pwd == "secure123":  # Commit: Check if password is correct
#         print("Welcome! Password is correct.")  # Commit: Success message
#         break  # Commit: Exit loop
#     else:
#         print("Incorrect password, try again.")  # Commit: Failure message
# # Commit: End of Do-While Loop Equivalent




# Using recursion (manual approach)
# Commit: Start of Recursive Approach
# def ask_password():  # Commit: Define a function
#     user_input = input("Enter password: ")  # Commit: Ask user for input
#     if user_input == "secure123":  # Commit: Check if password is correct
#         print("Access granted!")  # Commit: Notify success
#     else:
#         print("Wrong password, try again.")  # Commit: Notify failure
#         ask_password()  # Commit: Call function again recursively

# # Commit: Call recursive function first time
# ask_password()
# # Commit: End of Recursive Approach


# # Manual checking step by step (no loops)
# # Commit: Start of Manual Checking Approach
# p1 = input("Enter password: ")  # Commit: First attempt
# if p1 == "secure123":  # Commit: Check first attempt
#     print("Access granted!")  # Commit: Success
# else:
#     p2 = input("Try again: ")  # Commit: Second attempt
#     if p2 == "secure123":  # Commit: Check second attempt
#         print("Access granted!")  # Commit: Success
#     else:
#         p3 = input("Last attempt: ")  # Commit: Third attempt
#         if p3 == "secure123":  # Commit: Check third attempt
#             print("Access granted!")  # Commit: Success
#         else:
#             print("Access denied!")  # Commit: Failure after 3 attempts
# # Commit: End of Manual Checking Approach



print("***********************************************************")
# Q#14. ATM PIN check with max 3 attempts.

# Using while loop
# Start of ATM PIN Check with While Loop
attempts = 0  #  Initialize attempt counter
max_attempts = 3  #  Set maximum attempts
correct_pin = "1234"  #  Define correct PIN
while attempts < max_attempts:  #  Loop until max attempts reached
    pin = input("Enter your ATM PIN: ")  #  Ask user for PIN
    if pin == correct_pin:  #  Check if PIN is correct
        print("PIN accepted. Access granted.")  #  Success message
        break  #  Exit loop
    else:
        attempts += 1  #  Increment attempt counter
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")  #  Notify user
else:
    print("Too many incorrect attempts. Your account is locked.")  #  Lock account after max attempts
#  End of ATM PIN Check with While Loop



# # Commit: Start of ATM PIN Check Program
# correct_pin = "4321"  # Commit: Store the correct ATM PIN
# attempts = 0  # Commit: Initialize attempts counter
# max_attempts = 3  # Commit: Set maximum allowed attempts

# # Commit: Start loop to allow user to enter PIN up to max_attempts
# while attempts < max_attempts:  # Commit: Loop while attempts are less than max
#     pin = input("Enter your ATM PIN: ")  # Commit: Ask user to input PIN
#     attempts += 1  # Commit: Increase attempts counter by 1
#     if pin == correct_pin:  # Commit: Check if entered PIN is correct
#         print("Access granted! Welcome!")  # Commit: Notify user of success
#         break  # Commit: Exit loop if correct PIN
#     else:
#         print("Incorrect PIN.")  # Commit: Notify user of wrong PIN
#         if attempts < max_attempts:  # Commit: Check if attempts left
#             print(f"Try again. Attempts left: {max_attempts - attempts}")  # Commit: Show remaining attempts
#         else:
#             print("Your account is blocked. Contact bank!")  # Commit: Max attempts reached
# # Commit: End of ATM PIN Check Program



# Commit: Start of ATM PIN Check using For Loop
# correct_pin = "4321"  # Commit: Correct PIN
# max_attempts = 3  # Commit: Maximum attempts

# # Commit: Loop exactly max_attempts times
# for attempt in range(1, max_attempts + 1):  # Commit: Start loop from 1 to 3
#     pin = input("Enter your ATM PIN: ")  # Commit: Ask for PIN
#     if pin == correct_pin:  # Commit: Check if PIN is correct
#         print("Access granted! Welcome!")  # Commit: Success message
#         break  # Commit: Exit loop
#     else:
#         print("Incorrect PIN.")  # Commit: Notify wrong attempt
#         if attempt < max_attempts:  # Commit: Check if attempts remaining
#             print(f"Attempts left: {max_attempts - attempt}")  # Commit: Show remaining attempts
#         else:
#             print("Your account is blocked. Contact bank!")  # Commit: Max attempts reached
# # Commit: End of ATM PIN Check using For Loop







print("***********************************************************")
#Q:15. Simulate downloading progress `[###      ] 30%`. 

# 1. Using while loop
import time #Import time for delay

progress = 0  # Initialize progress at 0
while progress <= 100:   #Continue until progress reaches 100
    bar = "#" * (progress // 10)  # Fill part of bar
    space = " " * (10 - (progress // 10))  # Remaining space
    print(f"[{bar}{space}] {progress}%", end="")  # Print progress bar
    time.sleep(0.5)  # Simulate download delay
    progress += 1  # Increase progress by 1




# Other ways 
# Using for loop + print

# # Commit: Start of Progress Bar using For Loop
# import time  # Commit: Import time module for delays

# # Commit: Loop from 1 to 31 (to show 100%)
# for i in range(1, 31):  # Commit: i represents progress percentage
#     bar = "#" * (i // 10)  # Commit: Create filled part of bar (# per 10%)
#     space = " " * (10 - (i // 10))  # Commit: Remaining empty spaces
#     print(f"\r[{bar}{space}] {i}%", end="")  # Commit: Print bar with carriage return \r
#     time.sleep(0.05)  # Commit: Delay to simulate downloading speed
# # Commit: End of For Loop Progress Bar

# 2. Using recursion

# Commit: Start of Recursive Progress Bar
# import time  # Commit: Import time module

# def download(p):  # Commit: Define function with parameter p (progress)
#     if p > 100:  # Commit: Stop condition when progress exceeds 100
#         return  # Commit: Exit function
#     bar = "#" * (p // 10)  # Commit: Create filled part
#     space = " " * (10 - (p // 10))  # Commit: Empty spaces
#     print(f"\r[{bar}{space}] {p}%", end="")  # Commit: Print progress bar
#     time.sleep(0.05)  # Commit: Delay
#     download(p + 1)  # Commit: Recursive call with incremented progress

# download(0)  # Commit: Start recursive download from 0%
# # Commit: End of Recursive Progress Bar


# 43. Using tqdm (third-party library)
# Commit: Start of TQDM Progress Bar
# from tqdm import tqdm  # Commit: Import tqdm for progress bar
# import time  # Commit: Import time for delay

# # Commit: Loop with tqdm to show progress bar
# for _ in tqdm(range(100), desc="Downloading", unit="%", ncols=70):  
#     time.sleep(0.05)  # Commit: Simulate download delay
# # Commit: End of TQDM Progress Bar

#3. Fancy animation (rotating progress)

# Commit: Start of Animated Progress Loader
# import time  # Commit: Import time
# import itertools  # Commit: Import itertools for infinite cycle

# # Commit: Define animation characters
# for c in itertools.cycle(['|', '/', '-', '\\']):  # Commit: Loop through rotating symbols
#     print(f'\rDownloading {c}', end="")  # Commit: Print rotating animation
#     time.sleep(0.1)  # Commit: Delay for effect
#     # Commit: Simulate breaking after some time
#     if time.time() % 10 < 0.1:  # Commit: Break after ~10 sec (example)
#         break
# # Commit: End of Animated Progress Loader




print("***********************************************************")
# Q:16. While loop to collect student marks until “done” entered.

collect_student_marks = []  #  Start with empty list

while True:  #  Infinite loop to keep asking
    user_input = input("Enter your marks: ")  #  Take user input
    if user_input == "done":  #  Stop if user types "done"
        print("Ok")  #  Confirmation message
        break  #  Exit loop
    else:
        collect_student_marks.append(user_input)  #  Add input to list

print(collect_student_marks)  #  Print collected marks



# Other ways 
# 1. While loop (store as integers)

# Commit: Start of Integer Conversion Approach
# marks = []  # Commit: Empty list

# while True:  # Commit: Keep looping
#     user_input = input("Enter your marks: ")  # Commit: Take input
#     if user_input.lower() == "done":  # Commit: Allow 'done' in any case
#         print("Ok")  # Commit: Message
#         break  # Commit: Exit loop
#     else:
#         marks.append(int(user_input))  # Commit: Convert input to integer before appending

# print(marks)  # Commit: Print collected integer marks
# # Commit: End of Integer Conversion Approach


#2. While loop with limited attempts
# Commit: Start of Limited Attempts Approach
# marks = []  # Commit: Empty list
# attempts = 0  # Commit: Track number of inputs
# max_attempts = 5  # Commit: Maximum inputs allowed

# while attempts < max_attempts:  # Commit: Loop until attempts reach max
#     user_input = input("Enter your marks (or type 'done'): ")  # Commit: Ask user
#     if user_input == "done":  # Commit: Exit if done
#         break  # Commit: Exit loop
#     else:
#         marks.append(user_input)  # Commit: Add mark
#         attempts += 1  # Commit: Increase attempts

# print(marks)  # Commit: Print collected marks
# # Commit: End of Limited Attempts Approach


#2. While loop with error handling
# Commit: Start of Error Handling Approach
# marks = []  # Commit: Empty list

# while True:  # Commit: Infinite loop
#     user_input = input("Enter your marks (or 'done'): ")  # Commit: Ask input
#     if user_input == "done":  # Commit: Break condition
#         break  # Commit: Exit loop
#     try:
#         marks.append(int(user_input))  # Commit: Try to convert to integer
#     except ValueError:  # Commit: If conversion fails
#         print("Invalid input, enter a number or 'done'")  # Commit: Error message

# print(marks)  # Commit: Show results
# # Commit: End of Error Handling Approach

#3. While loop with sentinel value (None)
# Commit: Start of Sentinel Value Approach
# marks = []  # Commit: Empty list
# user_input = None  # Commit: Initialize sentinel

# while user_input != "done":  # Commit: Loop until sentinel matches "done"
#     user_input = input("Enter your marks: ")  # Commit: Ask for input
#     if user_input != "done":  # Commit: Only add if not done
#         marks.append(user_input)  # Commit: Add to list

# print(marks)  # Commit: Print collected marks
# # Commit: End of Sentinel Value Approach


#4. Recursive version (not while, but same logic)
# Commit: Start of Recursive Approach
# marks = []  # Commit: Empty list to store marks

# def collect_marks():  # Commit: Define function
#     user_input = input("Enter your marks (or 'done'): ")  # Commit: Ask input
#     if user_input == "done":  # Commit: Stop condition
#         return  # Commit: Exit function
#     else:
#         marks.append(user_input)  # Commit: Add mark
#         collect_marks()  # Commit: Recursive call for next input

# collect_marks()  # Commit: Start recursion
# print(marks)  # Commit: Print collected marks
# Commit: End of Recursive Approach

#5. While loop with average calculation at the end
# Commit: Start of Average Calculation Approach
# marks = []  # Commit: Empty list

# while True:  # Commit: Infinite loop
#     user_input = input("Enter your marks (or 'done'): ")  # Commit: Input
#     if user_input == "done":  # Commit: Break condition
#         break  # Commit: Exit loop
#     marks.append(int(user_input))  # Commit: Add as integer

# if marks:  # Commit: Check list is not empty
#     average = sum(marks) / len(marks)  # Commit: Calculate average
#     print("Collected marks:", marks)  # Commit: Print marks
#     print("Average:", average)  # Commit: Print average
# else:
#     print("No marks entered.")  # Commit: Handle empty list
# # Commit: End of Average Calculation Approach





print("***********************************************************")
#Q:17. Keep looping until internet connection = True. 
internet_connection = False  # Start with no internet connection

while not internet_connection: # Loop until internet_connection is True
    print("Checking Connection...")  # Simulate checking
    user_inp = input("Type 'on' to connect internet: ") 
    if user_inp.lower() == 'on': # if user types "on"
        internet_connection = True  # change status to True
        print("Internet Connected!") # Success message
    else:
        print("No connection. Try again.")


# 1.While True with break

# Commit: Start of While True + Break Approach
# internet_connection = False  # Commit: Start disconnected

# while True:  # Commit: Infinite loop
#     print("Waiting for connection...")  # Commit: Print status
#     user_inp = input("Turn internet 'on': ")  # Commit: Ask input
#     if user_inp.lower() == "on":  # Commit: If correct input
#         internet_connection = True  # Commit: Change state
#         print("Internet Connected!")  # Commit: Success
#         break  # Commit: Exit loop
#     else:
#         print("Still disconnected!")  # Commit: Retry
# # Commit: End of While True + Break Approach



#2. While with sentinel variable (status)
# Commit: Start of Sentinel Approach
# status = "off"  # Commit: Initial sentinel value

# while status != "on":  # Commit: Loop until status equals "on"
#     status = input("Enter 'on' to connect internet: ")  # Commit: Ask user
#     if status == "on":  # Commit: If input is correct
#         print("Internet Connected!")  # Commit: Success
#     else:
#         print("No connection yet.")  # Commit: Retry
# # Commit: End of Sentinel Approach


#3. While loop with counter (max attempts)
# Commit: Start of Counter Approach
# internet_connection = False  # Commit: Start disconnected
# attempts = 0  # Commit: Count attempts
# max_attempts = 3  # Commit: Allow 3 tries only

# while not internet_connection and attempts < max_attempts:  # Commit: Loop until connected or attempts over
#     user_inp = input("Turn internet 'on': ")  # Commit: Ask input
#     if user_inp.lower() == "on":  # Commit: If connected
#         internet_connection = True  # Commit: Set flag
#         print("Internet Connected!")  # Commit: Success
#     else:
#         attempts += 1  # Commit: Increase attempt counter
#         print(f"Still disconnected! Attempts left: {max_attempts - attempts}")  # Commit: Show attempts left

# if not internet_connection:  # Commit: If user failed
#     print("Max attempts reached. Connection failed.")  # Commit: Final message
# # Commit: End of Counter Approach


#4. While loop with toggle (on/off simulation)
# Commit: Start of Toggle Approach
# internet_connection = False  # Commit: Start disconnected

# while not internet_connection:  # Commit: Loop until connected
#     action = input("Type 'on' to connect, 'off' to stay disconnected: ")  # Commit: Ask user
#     if action.lower() == "on":  # Commit: If 'on'
#         internet_connection = True  # Commit: Set to connected
#         print("Internet Connected!")  # Commit: Success
#     elif action.lower() == "off":  # Commit: If 'off'
#         print("Internet still off.")  # Commit: Retry message
#     else:
#         print("Invalid command.")  # Commit: Handle wrong input
# # Commit: End of Toggle Approach



# Q:18. While loop for chatbot (keep asking until user types “bye”).

# while True: #Start an infinite loop for chatbot interaction
#     user_asking = input("Enter anything: (if leaving write bye:)")
#     if user_asking.lower() == "bye": #Check if user typed "bye" to end conversation
#         print("Chatbot") #Print a final message before exiting
#         break  # Exit the while loop if condition is met
#     else:  #Otherwise, respond with a default chatbot reply
#         print("Chatbot: I am a bot, I can't understand you.")  #Display chatbot response

     

print("***********************************************************")

# Other ways
# Q:18. While loop for chatbot (keep asking until user types “bye”)

while True:  
    user_message = input("You: ")   # take user input
    if user_message.lower() == "bye":   # check if user says "bye"
        print("Chatbot: Goodbye! 👋")   # final message
        break   # stop the loop
    else:
        print("Chatbot: I am just a simple bot, I can’t understand much.")


# 2: Condition in while loop

# user_asking = ""  # commit: initialize variable
# while user_asking != "bye":  # commit: loop continues until 'bye' is entered
#     user_asking = input("Enter anything: (if leaving write bye:) ")  # commit: take user input
#     if user_asking != "bye":  # commit: check if not exit word
#         print("Chatbot: I am a bot, I can't understand you.")  # commit: chatbot reply
# print("Chatbot: Goodbye!")  # commit: final exit message after loop ends


# 2. Using while True + continue

# while True:  # commit: start infinite loop
#     user_asking = input("Enter anything: (if leaving write bye:) ")  # commit: take user input
#     if user_asking == "bye":  # commit: check for exit condition
#         print("Chatbot: Goodbye!")  # commit: say goodbye
#         break  # commit: exit loop
#     print("Chatbot: I am a bot, I can't understand you.")  # commit: chatbot response
#     continue  # commit: explicitly continue loop (not required, but possible way)


#3. While with flag variable

# running = True  # commit: create flag to control loop
# while running:  # commit: loop runs while flag is True
#     user_asking = input("Enter anything: (if leaving write bye:) ")  # commit: take user input
#     if user_asking == "bye":  # commit: check exit condition
#         print("Chatbot: Goodbye!")  # commit: exit response
#         running = False  # commit: change flag to stop loop
#     else:
#         print("Chatbot: I am a bot, I can't understand you.")  # commit: normal chatbot reply








print("***********************************************************")
#Q:19. While loop for traffic light simulation.
# it is infinite loop be careful

lights = ["Green", "Yellow", "Red"]
i = 0

while True:
    print("Light:", lights[i])
    i += 1
    if i == len(lights):  # Reset to first light
        i = 0


# Other ways
# Controlled Loop with Counter

# lights = ["Green", "Yellow", "Red"]
# i = 0
# cycles = 0

# while cycles < 2:  # Run for 2 full cycles only
#     print("Light:", lights[i])
#     i += 1
#     if i == len(lights):
#         i = 0
#         cycles += 1


# User-Controlled Simulation

# lights = ["Green", "Yellow", "Red"]
# i = 0

# while True:
#     print("Light:", lights[i])
#     i += 1
#     if i == len(lights):
#         i = 0
    
#     user = input("Continue? (yes/stop): ").lower()
#     if user == "stop":
#         print("Traffic light simulation stopped.")
#         break


# While with Condition Instead of Break
# lights = ["Green", "Yellow", "Red"]
# i = 0
# running = True

# while running:
#     print("Light:", lights[i])
#     i += 1
#     if i == len(lights):
#         i = 0

#     # Exit condition
#     if input("Type 'exit' to stop: ").lower() == "exit":
#         running = False

# Endless Simulation (like real traffic light)

# it is infinite loop be careful
# lights = ["Green", "Yellow", "Red"]
# i = 0

# while True:
#     print("Light:", lights[i])
#     i = (i + 1) % len(lights)  # Circular cycling





# while True:
#     light = input("Enter traffic light color (Green/Yellow/Red) or 'exit' to quit: ").lower()

#     if light == "green":
#         print("🚦 Green: You can GO.")
#     elif light == "yellow":
#         print("🚦 Yellow: Get READY to stop.")
#     elif light == "red":
#         print("🚦 Red: STOP immediately!")
#     elif light == "exit":
#         print("Simulation Ended 🚦")
#         break
#     else:
#         print("❌ Invalid light! Please enter Green, Yellow, or Red.")




# running = True
# while running:
#     light = input("Enter traffic light color (Green/Yellow/Red) or 'exit' to quit: ").lower()

#     if light == "green":
#         print("🚦 Green: You can GO.")
#     elif light == "yellow":
#         print("🚦 Yellow: Get READY to stop.")
#     elif light == "red":
#         print("🚦 Red: STOP immediately!")
#     elif light == "exit":
#         print("Simulation Ended 🚦")
#         running = False   # stops the loop
#     else:
#         print("❌ Invalid light! Please enter Green, Yellow, or Red.")




# light = ""
# while light != "exit":
#     light = input("Enter traffic light color (Green/Yellow/Red) or 'exit' to quit: ").lower()

#     if light == "green":
#         print("🚦 Green: You can GO.")
#     elif light == "yellow":
#         print("🚦 Yellow: Get READY to stop.")
#     elif light == "red":
#         print("🚦 Red: STOP immediately!")
#     elif light != "exit":
#         print("❌ Invalid light! Please enter Green, Yellow, or Red.")

# print("Simulation Ended 🚦")









print("***********************************************************")
#Q: 20. Simulate a taxi meter counting distance.
# Ask user continuously for distance (until "stop")
#  Start taxi meter simulation with while loop
total_distance = 0  

#  Keep asking user for distance until they type 'stop'
while True:
    distance = input("Enter distance traveled (or 'stop'): ")

    # Check if user wnats to stop
    if distance.lower() == "stop":
        break

#     # Convert input to integer and add to total
    total_distance += int(distance)

# # diplay total distance traveled
print("Total distance traveled:", total_distance, "km")



# Other ways
# Fixed increments (like a real meter running automatically)
# commit: Initialize starting distance
# distance = 0  

# # commit: Run infinite loop to simulate meter ticking
# while distance < 100:  # stop after 100 km  
#     # commit: Increase distance by 1 km at each tick
#     distance += 1  
#     print("Taxi meter:", distance, "km")  

# print("Trip completed!")



# Using a condition with user confirmation
# commit: Start taxi distance at 0
# distance = 0  

# # commit: Ask user if they want to continue after each km
# while True:  
#     distance += 1  # commit: add 1 km per loop  
#     print("Taxi meter:", distance, "km")  
    
#     # commit: confirm with user
#     cont = input("Continue? (yes/no): ")  
#     if cont.lower() == "no":  
#         break  

# # commit: Show total distance at end
# print("Final distance traveled:", distance, "km")  


# While loop with fare calculation (extra realistic 🚖💰)
# commit: Base fare setup
# fare_per_km = 50  
# distance = 0  

# commit: keep asking until user ends trip
# while True:  
#     km = input("Enter km traveled (or 'stop'): ")  
    
#     if km.lower() == "stop":  
#         break  
    
#     # commit: Add distance and calculate fare
#     distance += int(km)  

# fare = distance * fare_per_km  

# # commit: Display total fare
# print("Total distance:", distance, "km")  
# print("Total fare:", fare, "PKR")  




# Interview Qs:
# 21. Difference between while loop and do-while loop (Python alternative)

"""
)

👉 In most languages (C, C++, Java), we have do-while loop, but Python does NOT have a direct do-while.
Instead, we simulate it using while True with a break.

✨ Key Difference:

while loop → condition is checked before execution.

do-while loop (Python alternative) → condition is checked after execution (runs at least once).

Python Example
# Example: Asking user for a positive number

# -------- Normal while loop --------
number = int(input("Enter a positive number: "))
while number <= 0:
    print("❌ Invalid. Try again.")
    number = int(input("Enter a positive number: "))
print(f"✅ You entered {number}")

# -------- Do-While alternative --------
while True:
    number = int(input("Enter a positive number: "))
    if number > 0:
        print(f"✅ You entered {number}")
        break
    print("❌ Invalid. Try again.")
Difference shown:

while loop may not run if condition fails from the start.

do-while loop alternative always runs at least once.

🎯 Real-life Analogy

While loop:
"Check your wallet before entering the shop. If empty, you can’t go."

Do-while loop:
"Enter the shop first, then check wallet. You’ll at least walk in once!"

"""


# 22. What happens if while loop condition is always True?


"""
👉 If a while loop condition is always True, it creates an infinite loop.
This means the loop never stops unless we use break or external interruption (Ctrl + C).


Python Example 1: Infinite Loop (Bad ❌)


while True:
    print("I will run forever 🚀")
This keeps printing endlessly — not good without exit logic.


# Python Example 2: Controlled Infinite Loop (Good ✅)
count = 0
while True:  # always True
    print(f"Looping... Count = {count}")
    count += 1
    
    if count == 5:  # exit condition
        print("✅ Breaking loop after 5 counts.")
        break
Output stops at count 5, because we used break.

🎯 Real-life Analogy

Infinite loop without break:
"Like a fan running forever unless you switch it off."

Infinite loop with break:
"Like a fan that automatically turns off after 5 minutes."

"""