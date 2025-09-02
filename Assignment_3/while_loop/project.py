import time
import random

# ----------------------------
# Loop Learning Simulator
# ----------------------------
# This project demonstrates while loops in fun real-world scenarios.
# Each function is a "lesson" disguised as a small app.


# 1. Password Checker

def password_checker():
    print("🔐 PASSWORD CHECKER")
    correct_password = "python123"
    attempts = ""
    tries = 0

    while attempts != correct_password:
        attempts = input("Enter password: ")
        tries += 1
        if attempts != correct_password:
            print("Incorrect! Try again.")
        if tries >= 3:
            print("Too many attempts! Access denied.")
            return
        
    print("✅ Access granted! Welcome.")

# 2. ATM PIN
def atm_simulator():
    print("🏧 ATM SIMULATOR")
    correct_pin = "4321"
    balance = 1000
    entered_pin = input("Enter your 4-digit PIN: ")

    while entered_pin != correct_pin:
        print("❌ Incorrect PIN.")
        entered_pin = input("Re-enter your PIN: ")

    print("✅ PIN accepted.")
    while True: 
        choice = input("WithDraw (w), Balance (b), Exit (e): ")
        if choice.lower() == 'w':
            amount = int(input("Enter amount: "))
            if amount <= balance:
                balance -= amount
                print(f"💸 Withdrawn {amount}. Remaining balance {balance}.")
            else:
                print("❌ Insufficient funds.")
        elif choice.lower() == 'b':
            print(f"💰 Current balance: {balance}.")
        elif choice.lower() == 'e':
            print("👋 Thank you for using the ATM.")
            break

# 3. progressing bar
def progress_bar():
    print("📊 PROGRESS BAR SIMULATOR")
    progress = 0
    while progress <= 100:
        print(f"Loading... {progress}%", end="\r")
        time.sleep(0.2)
        progress += 10
    print("✅ Task Completed!")




# # 4. Chatbot (exit with 'bye')
# def simple_chatbot():
#     print("💬 SIMPLE CHATBOT")
#     print("Type 'bye' to exit.")
#     user_input = ""
#     while user_input.lower() != "bye":
#         user_input = input("You: ")
#         if user_input.lower() != "bye":
#             responses = [
#                 "Interesting!",
#                 "Tell me more.",
#                 "Why do you say that?",
#                 "I see.",
#                 "Can you elaborate?"
#             ]
#             print("Bot:", random.choice(responses))
#     print("Bot: Goodbye! Have a great day.")

# 4. Chatbot (exit with 'bye')
def simple_chatbot():
    print("🤖 SIMPLE CHATBOT (type 'bye' to exit)")
    user_input = ""
    while user_input.lower() != "bye":
        user_input = input("You: ")
        if user_input.lower() != "bye":
            print("Bot: I'm still learning, but nice!")
    print("Bot: Goodbye! 👋")


# 5. Traffic Light Simulation
def traffic_light():
    print("🚦 TRAFFIC LIGHT SIMULATOR")
    lights = ["Red", "Green", "Yellow"]
    i = 0
    while i < 6: # Cycle 6 times
        light = lights[i % 3]
        print(f"Light is {light}")
        time.sleep(1)
        i += 1
    print("Traffic light simulation ended.")


# 6. Taxi Meter (Distance simulation)

# def taxi_meter():
#     print("🚕 TAXI METER SIMULATOR")
#     distance = 0
#     rate_per_km = 5  # $5 per km
#     while distance < 20: # Simulate up to 20 km
#         print(f"Distance: {distance} km | Fare: ${distance * rate_per_km}")
#         time.sleep(1)
#         distance += 1
#     print(f"Total Distance: {distance} km | Total Fare: ${distance * rate_per_km}")
#     print("Taxi ride ended.")
def taxi_meter():
    print("🚕 TAXI METER SIMULATOR")
    distance = 0
    fare = 50 # base fare
    while distance < 10:
        time.sleep(0.5)
        distance += 1
        fare += 20
        print(f"Distance: {distance} km | Fare: Rs. {fare}")
    print("✅ Trip ended! Pay Rs.", fare)


# 7. While vs Do-While Simulation
def while_vs_do_while():
    print("🔄 WHILE vs DO-WHILE SIMULATION")
    print("Python does not have a do-while, but we can simulate it!")


# While loop example
    print("While loop: condition checked first")
    count = 0
    while count > 0:
        print("This will never run")


# Do-While simulation
    print("Do-While simulation: runs at least once")
    count = 0
    while True:
        print("This runs once before checking condition")
        if count > 0:
            break
        break


# 8. Infinite Loop Demo (with break)
def infinite_loop_demo():
    print("♾️ INFINITE LOOP DEMO")
    counter = 0
    while True:
        print("Loop running...")
        counter += 1
        if counter == 5:
            print("Breaking infinite loop!")
            break



# ----------------------------
# Main Menu
# ----------------------------

def main():
    while True:
        print("""
======== LOOP LEARNING SIMULATOR ========
1. Password Checker
2. ATM Simulator
3. Progress Bar
4. Simple Chatbot
5. Traffic Light
6. Taxi Meter
7. While vs Do-While
8. Infinite Loop Demo
9. Exit
=========================================
      """)
        
        choice = input("Choose an option: ")
        if choice == '1':
            password_checker()
        elif choice == '2':
            atm_simulator()
        elif choice == '3':
            progress_bar()
        elif choice == '4':
            simple_chatbot()
        elif choice == '5':
            traffic_light()
        elif choice == '6':
            taxi_meter()
        elif choice == '7':
            while_vs_do_while()
        elif choice == '8':
            infinite_loop_demo()
        elif choice == '9':
            print("👋 Goodbye! Keep learning.")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run project
if __name__ == "__main__":
    main()