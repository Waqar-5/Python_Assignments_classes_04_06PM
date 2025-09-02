"""
Loop Mastery Project
Author: Waqar Ali
Description:
    This project is a collection of mini-programs that teach
    different uses of while loops in Python.
    Each task is wrapped in its own function, and you can
    run them from a central menu.

Tasks:
13. Keep asking user for password until it matches "secure123".
14. ATM PIN check with max 3 attempts.
15. Simulate downloading progress "[### ] 30%".
16. While loop to collect student marks until “done” entered.
17. Keep looping until internet connection = True.
18. While loop for chatbot (keep asking until user types “bye”).
19. While loop for traffic light simulation.
20. Simulate a taxi meter counting distance.
"""

import time
import random


# 13. Password check
def password_check():
    while True:
        pwd = input("Enter password: ")
        if pwd == "secure123":
            print("✅ Access Granted!\n")
            break
        else:
            print("❌ Wrong password, try again.")


# 14. ATM PIN check (max 3 attempts)
def atm_pin_check():
    pin = "4321"
    attempts = 0
    while attempts < 3:
        entered = input("Enter ATM PIN: ")
        if entered == pin:
            print("✅ PIN correct! Access granted.\n")
            return
        else:
            attempts += 1
            print(f"❌ Wrong PIN. Attempts left: {3 - attempts}")
    print("🚨 Card blocked! Too many attempts.\n")


# 15. Download simulation
def download_progress():
    for i in range(0, 101, 10):
        bar = "#" * (i // 10)
        print(f"[{bar:<10}] {i}%", end="\r")
        time.sleep(0.3)
    print("\n✅ Download Complete!\n")


# 16. Collect student marks
def collect_marks():
    marks = []
    while True:
        entry = input("Enter student mark (or 'done' to finish): ")
        if entry.lower() == "done":
            break
        if entry.isdigit():
            marks.append(int(entry))
        else:
            print("❌ Please enter a number or 'done'.")
    print(f"📊 Marks collected: {marks}\n")


# 17. Internet connection loop
def internet_check():
    connected = False
    while not connected:
        print("🔄 Checking internet connection...")
        time.sleep(1)
        connected = random.choice([False, False, True])  # Random success
    print("✅ Internet Connected!\n")


# 18. Chatbot loop
def chatbot():
    print("🤖 Chatbot ready! (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: 👋 Bye!")
            break
        else:
            print(f"Chatbot: You said '{user_input}'. Cool!\n")


# 19. Traffic light simulation
def traffic_light():
    lights = ["🟥 Red - Stop", "🟡 Yellow - Wait", "🟢 Green - Go"]
    i = 0
    while True:
        print(lights[i % 3])
        time.sleep(2)
        i += 1
        if i == 6:  # limit cycles
            print("🚦 Simulation Ended.\n")
            break


# 20. Taxi meter simulation
def taxi_meter():
    distance = 0
    rate = 5  # cost per km
    while distance < 20:  # simulate 20 km max
        time.sleep(1)
        distance += 1
        fare = distance * rate
        print(f"🚕 Distance: {distance} km | Fare: ${fare}")
    print("🏁 Ride Complete!\n")


# --- Menu System ---
def main():
    tasks = {
        "13": password_check,
        "14": atm_pin_check,
        "15": download_progress,
        "16": collect_marks,
        "17": internet_check,
        "18": chatbot,
        "19": traffic_light,
        "20": taxi_meter,
    }

    while True:
        print("\n=== Loop Mastery Project ===")
        print("13. Password Check")
        print("14. ATM PIN Check")
        print("15. Download Simulation")
        print("16. Collect Student Marks")
        print("17. Internet Connection Check")
        print("18. Chatbot")
        print("19. Traffic Light Simulation")
        print("20. Taxi Meter")
        print("0. Exit")

        choice = input("Choose a task: ")
        if choice == "0":
            print("👋 Exiting Loop Mastery Project. Goodbye!")
            break
        elif choice in tasks:
            tasks[choice]()
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
