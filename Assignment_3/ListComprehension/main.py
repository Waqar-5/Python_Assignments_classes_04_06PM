# ========================================================
# Python List Comprehension Hub - Section H (Dynamic)
# Author: Waqar Ali
# Purpose: Interactive hub demonstrating real-life + interview Qs using list comprehension
# ========================================================

# Import modules
import re  # Regular expressions for hashtags and domains

# ========================================================
# Color helpers for terminal
# ========================================================
class Colors:
    HEADER = '\033[95m'   # Purple
    OKBLUE = '\033[94m'   # Blue
    OKCYAN = '\033[96m'   # Cyan
    OKGREEN = '\033[92m'  # Green
    WARNING = '\033[93m'  # Yellow
    FAIL = '\033[91m'     # Red
    ENDC = '\033[0m'      # Reset color
    BOLD = '\033[1m'      # Bold text

def print_header(title):
    # Print section header with color
    print(f"\n{Colors.HEADER}{'='*10} {title} {'='*10}{Colors.ENDC}\n")

# ========================================================
# Q83: Generate Roll Numbers dynamically
# ========================================================
def generate_roll_numbers():
    n = int(input("Enter the number of students: "))  # Get number of students dynamically
    return [f"BSE-{i}" for i in range(1, n+1)]  # List comprehension for roll numbers

# ========================================================
# Q84: Extract Vowels from String dynamically
# ========================================================
def extract_vowels():
    text = input("Enter a string: ")  # Dynamic string input
    vowels = "aeiouAEIOU"  # Vowels list
    return [ch for ch in text if ch in vowels]  # Extract vowels using list comprehension

# ========================================================
# Q85: Words starting with 'S' dynamically
# ========================================================
def words_starting_with_s():
    words = input("Enter words separated by space: ").split()  # Split input into list
    return [word for word in words if word.lower().startswith("s")]  # Filter words starting with S

# ========================================================
# Q86: Flatten Nested List dynamically
# ========================================================
def flatten_nested_list():
    n = int(input("Enter number of sublists: "))  # Number of nested lists
    nested_list = []
    for i in range(n):
        sublist = input(f"Enter elements of sublist {i+1} separated by space: ").split()
        nested_list.append(sublist)  # Append sublist
    return [item for sublist in nested_list for item in sublist]  # Flatten using list comprehension

# ========================================================
# Q87: Word-Length Dictionary dynamically
# ========================================================
def word_length_dict():
    words = input("Enter words separated by space: ").split()  # Dynamic word list
    return {word: len(word) for word in words}  # Dictionary comprehension

# ========================================================
# Q88: Extract Domains from Emails dynamically
# ========================================================
def extract_domains():
    emails = input("Enter emails separated by space: ").split()  # Dynamic email input
    return [email.split("@")[1] for email in emails]  # Extract domain using list comprehension

# ========================================================
# Q89: Even Numbers dynamically
# ========================================================
def even_numbers():
    start = int(input("Enter start number: "))  # Dynamic start
    end = int(input("Enter end number: "))      # Dynamic end
    return [i for i in range(start, end+1) if i % 2 == 0]  # Even numbers list

# ========================================================
# Q90: Filter Transactions dynamically
# ========================================================
def filter_transactions():
    transactions = input("Enter transactions separated by space: ").split()
    transactions = [float(t) for t in transactions]  # Convert to float
    threshold = float(input("Enter threshold amount: "))  # Threshold dynamically
    return [t for t in transactions if t > threshold]  # Filter transactions above threshold

# ========================================================
# Q91: Extract Hashtags dynamically
# ========================================================
def extract_hashtags():
    n = int(input("Enter number of tweets: "))  # Dynamic tweet count
    tweets = [input(f"Enter tweet {i+1}: ") for i in range(n)]  # Get all tweets
    return [tag for tweet in tweets for tag in re.findall(r"#\w+", tweet)]  # Extract hashtags

# ========================================================
# Q92: Seat Numbers dynamically
# ========================================================
def seat_numbers():
    rows = input("Enter row letters (e.g., ABC): ")  # Dynamic rows
    cols = int(input("Enter number of columns: "))  # Dynamic columns
    return [f"{row}{col}" for row in rows for col in range(1, cols+1)]  # Generate seat numbers

# ========================================================
# Interview Qs 93-94
# ========================================================
def interview_qs():
    # Return dictionary of questions and answers
    return {
        "When to prefer list comprehension over loops?":
        "Use list comprehension for concise, readable list creation. Avoid for complex logic or side effects.",

        "Can list comprehensions replace map/filter?":
        "Yes, list comprehension can replace map and filter in most cases, often making code more readable."
    }

# ========================================================
# Main Menu System (Dynamic + Interactive)
# ========================================================
def main_menu():
    while True:
        print_header("Python List Comprehension Hub (Dynamic)")
        print(f"{Colors.OKBLUE}Select a utility:{Colors.ENDC}")
        print("1. Generate Roll Numbers")
        print("2. Extract Vowels from String")
        print("3. Words Starting with 'S'")
        print("4. Flatten Nested List")
        print("5. Word-Length Dictionary")
        print("6. Extract Domains from Emails")
        print("7. Even Numbers")
        print("8. Filter Transactions")
        print("9. Extract Hashtags")
        print("10. Seat Numbers")
        print("11. Interview Questions")
        print("0. Exit")

        choice = input(f"{Colors.BOLD}Enter your choice: {Colors.ENDC}")  # User input

        # -------------------------------
        # Handle menu selections dynamically
        # -------------------------------
        if choice == '1':
            print(generate_roll_numbers())
        elif choice == '2':
            print(extract_vowels())
        elif choice == '3':
            print(words_starting_with_s())
        elif choice == '4':
            print(flatten_nested_list())
        elif choice == '5':
            print(word_length_dict())
        elif choice == '6':
            print(extract_domains())
        elif choice == '7':
            print(even_numbers())
        elif choice == '8':
            print(filter_transactions())
        elif choice == '9':
            print(extract_hashtags())
        elif choice == '10':
            print(seat_numbers())
        elif choice == '11':
            for q, a in interview_qs().items():
                print(f"Q: {q}\nA: {a}\n")
        elif choice == '0':
            print(f"{Colors.OKGREEN}Exiting... Goodbye!{Colors.ENDC}")
            break
        else:
            print(f"{Colors.WARNING}Invalid choice. Try again.{Colors.ENDC}")

        input(f"{Colors.OKBLUE}\nPress Enter to continue...{Colors.ENDC}")  # Pause for user

# ========================================================
# Run the project
# ========================================================
if __name__ == "__main__":
    main_menu()
