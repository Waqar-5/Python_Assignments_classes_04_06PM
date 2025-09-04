# Entry point of the project
from functions import *

while True:
    print("\n--- For Loop Playground ---")
    print("1. Print all file names")
    print("2. Print student names")
    print("3. Print Gmail emails")
    print("4. Display product prices")
    print("5. Mask phone numbers")
    print("6. Transactions above 50,000")
    print("7. Words in sentence reversed")
    print("8. Out of stock items")
    print("9. Pending tasks")
    print("10. First 5 notifications")
    print("11. Explain for vs range")
    print("12. Explain iterators")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print_files()
    elif choice == "2":
        print_students()
    elif choice == "3":
        print_gmail_emails()
    elif choice == "4":
        display_prices()
    elif choice == "5":
        mask_phones()
    elif choice == "6":
        high_transactions()
    elif choice == "7":
        reverse_words()
    elif choice == "8":
        out_of_stock()
    elif choice == "9":
        pending_tasks()
    elif choice == "10":
        first_notifications()
    elif choice == "11":
        explain_for_vs_range()
    elif choice == "12":
        explain_iterators()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Try again!")
