# ========================================================
# Python Utility Hub - Section D: Functions + Loops
# Author: Waqar Ali
# Purpose: Interactive utility hub covering real-life + interview Qs
# ========================================================

# Import modules
import random  # For random number generation (dice roll)
import re      # For regular expressions (hashtag extraction)
from collections import Counter  # For word frequency counting

# ========================================================
# Color helpers for terminal
# ========================================================
class Colors:
    # ANSI escape codes for terminal colors
    HEADER = '\033[95m'   # Purple
    OKBLUE = '\033[94m'   # Blue
    OKCYAN = '\033[96m'   # Cyan
    OKGREEN = '\033[92m'  # Green
    WARNING = '\033[93m'  # Yellow
    FAIL = '\033[91m'     # Red
    ENDC = '\033[0m'      # Reset color
    BOLD = '\033[1m'      # Bold text

# Function to print a section header with color and separators
def print_header(title):
    print(f"\n{Colors.HEADER}{'='*10} {title} {'='*10}{Colors.ENDC}\n")

# ========================================================
# Q35: Count PDFs
# ========================================================
def count_pdfs(file_list):
    # Returns the number of files ending with '.pdf'
    return sum(1 for f in file_list if f.endswith('.pdf'))

# ========================================================
# Q36: Username availability
# ========================================================
def check_username(username, existing_users):
    # Case-insensitive check if username exists in existing_users list
    return username.lower() not in [u.lower() for u in existing_users]

# ========================================================
# Q37: Longest word
# ========================================================
def longest_word(sentence):
    # Splits sentence into words and returns the longest one
    return max(sentence.split(), key=len)

# ========================================================
# Q38: Palindrome check
# ========================================================
def is_palindrome(s):
    # Normalize string: lowercase and remove spaces
    s_clean = s.lower().replace(" ", "")
    # Check if string equals its reverse
    return s_clean == s_clean[::-1]

# ========================================================
# Q39: Multiplication table
# ========================================================
def multiplication_table(n):
    # Returns multiplication table of 'n' from 1 to 10 as a list of strings
    return [f"{n} x {i} = {n*i}" for i in range(1, 11)]

# ========================================================
# Q40: Dice roll until 6
# ========================================================
def roll_until_six():
    rolls = []  # List to store dice rolls
    while True:
        roll = random.randint(1,6)  # Roll a dice
        rolls.append(roll)           # Save roll
        if roll == 6:                # Stop if dice shows 6
            break
    return rolls                     # Return all rolls

# ========================================================
# Q41: Filter products under price
# ========================================================
def filter_products(products, max_price):
    # products is a dictionary {name: price}
    # Returns list of product names with price <= max_price
    return [p for p, price in products.items() if price <= max_price]

# ========================================================
# Q42: Mask passwords
# ========================================================
def mask_passwords(passwords):
    # Returns list of passwords replaced with asterisks (*)
    return ['*'*len(pw) for pw in passwords]

# ========================================================
# Q43: Word frequency
# ========================================================
def word_frequency(sentence):
    # Lowercase sentence, split into words, count frequency
    return Counter(sentence.lower().split())

# ========================================================
# Q44: Extract hashtags
# ========================================================
def extract_hashtags(post):
    # Returns all words starting with '#' using regex
    return re.findall(r'#\w+', post)

# ========================================================
# Q45: Return vs Print demo
# ========================================================
def demo_return_vs_print(a, b):
    # Demonstrates difference between print and return
    print(f"{Colors.OKCYAN}Using print: {Colors.ENDC}")
    print(a+b)  # Prints sum
    print(f"{Colors.OKGREEN}Using return: {Colors.ENDC}")
    return a+b  # Returns sum for further use

# ========================================================
# Q46: Functions returning multiple values
# ========================================================
def get_name_age():
    # Returns multiple values as tuple
    return "Waqar", 22

def sum_product(a,b):
    # Returns sum and product of two numbers as tuple
    return a+b, a*b

# ========================================================
# Menu System
# ========================================================
def main_menu():
    while True:  # Infinite loop until user chooses Exit
        print_header("Python Utility Hub")  # Section header
        print(f"{Colors.OKBLUE}Select a utility:{Colors.ENDC}")  # Menu header
        # Menu options
        print("1. Count PDF files")
        print("2. Check username availability")
        print("3. Find longest word")
        print("4. Check palindrome")
        print("5. Multiplication table")
        print("6. Dice roll simulator")
        print("7. Filter products under price")
        print("8. Mask passwords")
        print("9. Word frequency")
        print("10. Extract hashtags")
        print("11. Return vs Print demo")
        print("12. Multiple return demo")
        print("0. Exit")
        
        choice = input(f"{Colors.BOLD}Enter your choice: {Colors.ENDC}")  # User input
        
        # -------------------------------
        # Handle menu selections
        # -------------------------------
        if choice == '1':
            files = input("Enter filenames separated by comma: ").split(",")
            print(f"PDF count: {count_pdfs(files)}")
            
        elif choice == '2':
            users = input("Enter existing usernames separated by comma: ").split(",")
            username = input("Enter username to check: ")
            available = check_username(username, users)
            print(f"Username available? {'Yes' if available else 'No'}")
            
        elif choice == '3':
            sentence = input("Enter a sentence: ")
            print(f"Longest word: {longest_word(sentence)}")
            
        elif choice == '4':
            word = input("Enter a word/string: ")
            print(f"Is palindrome? {'Yes' if is_palindrome(word) else 'No'}")
            
        elif choice == '5':
            n = int(input("Enter a number: "))
            print("\n".join(multiplication_table(n)))
            
        elif choice == '6':
            rolls = roll_until_six()
            print(f"Dice rolls: {rolls}")
            print(f"Total rolls: {len(rolls)}")
            
        elif choice == '7':
            products_input = input("Enter products in format name:price separated by comma: ")
            products = {}
            for item in products_input.split(","):
                name, price = item.split(":")
                products[name.strip()] = float(price)
            max_price = float(input("Enter max price: "))
            print(f"Affordable products: {filter_products(products, max_price)}")
            
        elif choice == '8':
            passwords = input("Enter passwords separated by comma: ").split(",")
            print(f"Masked passwords: {mask_passwords(passwords)}")
            
        elif choice == '9':
            sentence = input("Enter a sentence: ")
            print("Word frequency:")
            for word, count in word_frequency(sentence).items():
                print(f"{word}: {count}")
                
        elif choice == '10':
            post = input("Enter social media post: ")
            print(f"Hashtags: {extract_hashtags(post)}")
            
        elif choice == '11':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            result = demo_return_vs_print(a,b)
            print(f"Returned value: {result}")
            
        elif choice == '12':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            s, p = sum_product(a,b)
            print(f"Sum: {s}, Product: {p}")
            
        elif choice == '0':
            print(f"{Colors.OKGREEN}Exiting... Goodbye!{Colors.ENDC}")
            break  # Exit loop
        
        else:
            print(f"{Colors.WARNING}Invalid choice. Try again.{Colors.ENDC}")
        
        input(f"{Colors.OKBLUE}\nPress Enter to continue...{Colors.ENDC}")

# ========================================================
# Run the project
# ========================================================
if __name__ == "__main__":
    main_menu()  # Start the interactive menu
