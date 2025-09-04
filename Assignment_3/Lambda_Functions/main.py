# =========================================================
# Dynamic Smart Data Processor Dashboard (Enhanced UX)
# Author: Waqar Ali
# Purpose: Fully interactive, intuitive, and error-handled Lambda dashboard
# =========================================================

from functools import reduce  # Import reduce function for cumulative operations like product, sum, etc.
import sys                     # Import sys module to allow exit from program

# -----------------------------
# Terminal Colors
# -----------------------------
class Colors:
    # This class defines ANSI escape codes to colorize terminal output
    HEADER = '\033[95m'  # Purple, for headers
    OKBLUE = '\033[94m'  # Blue, for menu items
    OKCYAN = '\033[96m'  # Cyan, for prompts, highlights
    OKGREEN = '\033[92m' # Green, for success messages
    WARNING = '\033[93m' # Yellow, for warnings
    FAIL = '\033[91m'    # Red, for errors
    ENDC = '\033[0m'     # Reset to default terminal color
    BOLD = '\033[1m'     # Bold text

# -----------------------------
# Utility Functions
# -----------------------------
def print_header(title):
    """
    Prints a colored section header in the terminal
    """
    print(f"\n{Colors.HEADER}{'='*10} {title} {'='*10}{Colors.ENDC}\n")
    # '==='*10: creates visual separators
    # Colors.HEADER and Colors.ENDC: adds purple color for title

def wait_for_input():
    """
    Pauses execution until user presses Enter
    """
    input(f"{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

def get_list_input(prompt, convert_type=str, default=None):
    """
    Get a list of values from the user, convert each to specified type
    - prompt: text to show user
    - convert_type: type to convert each item to (int, str, etc.)
    - default: list to return if user presses Enter
    """
    while True:
        inp = input(prompt)
        if inp.strip() == "" and default is not None:
            return default  # return default if user presses Enter
        try:
            return [convert_type(x) for x in inp.strip().split()]
            # split string by spaces, convert each to required type
        except ValueError:
            print(f"{Colors.FAIL}Invalid input! Try again.{Colors.ENDC}")

# -----------------------------
# Lambda Operations
# -----------------------------
def check_even_odd(numbers):
    """Check if each number is even or odd"""
    print_header("Even/Odd Check")
    # Using lambda inside map to check even or odd
    result = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", numbers))
    for n, r in zip(numbers, result):
        # Print each number with its status
        print(f"{n}: {Colors.OKGREEN if r=='Even' else Colors.FAIL}{r}")
    wait_for_input()

def double_numbers(numbers):
    """Double each number in the list"""
    print_header("Double Numbers")
    result = list(map(lambda x: x*2, numbers))
    for n, r in zip(numbers, result):
        print(f"{n} → {Colors.OKGREEN}{r}")
    wait_for_input()

def filter_edu_emails(emails):
    """Show only emails ending with '.edu'"""
    print_header("Emails Ending with .edu")
    result = list(filter(lambda x: x.endswith(".edu"), emails))
    if not result:
        print(f"{Colors.WARNING}No .edu emails found.{Colors.ENDC}")
    for email in result:
        print(f"{Colors.OKCYAN}{email}")
    wait_for_input()

def product_of_numbers(numbers):
    """Compute product of all numbers"""
    print_header("Product of Numbers")
    if numbers:
        product = reduce(lambda x, y: x*y, numbers)
        print(f"Numbers: {numbers}")
        print(f"Product: {Colors.OKGREEN}{product}")
    else:
        print(f"{Colors.FAIL}No numbers provided!{Colors.ENDC}")
    wait_for_input()

def first_characters(words):
    """Extract first character of each word"""
    print_header("First Character of Each Word")
    result = list(map(lambda x: x[0], words))
    for w, r in zip(words, result):
        print(f"{w} → {Colors.OKCYAN}{r}")
    wait_for_input()

def sort_employees_salary(employees):
    """Sort employee list by salary ascending"""
    print_header("Sort Employees by Salary")
    if not employees:
        print(f"{Colors.WARNING}No employees data!{Colors.ENDC}")
    sorted_emp = sorted(employees, key=lambda x: x["salary"])
    for emp in sorted_emp:
        print(f"{emp['name']} → {Colors.OKGREEN}${emp['salary']}")
    wait_for_input()

def filter_premium_users(users):
    """Show only premium users"""
    print_header("Premium Users")
    result = list(filter(lambda x: x["premium"], users))
    if not result:
        print(f"{Colors.WARNING}No premium users found.{Colors.ENDC}")
    for u in result:
        print(f"{Colors.OKGREEN}{u['name']} (Premium)")
    wait_for_input()

def sort_names_lastname(names):
    """Sort list of names by last word (last name)"""
    print_header("Sort Names by Last Name")
    result = sorted(names, key=lambda x: x.split()[-1])
    for n in result:
        print(f"{Colors.OKCYAN}{n}")
    wait_for_input()

def format_phone_numbers(phone_numbers):
    """Format phone numbers as (xxx) xxx-xxxx"""
    print_header("Format Phone Numbers")
    result = list(map(lambda x: f"({x[:3]}) {x[3:6]}-{x[6:]}", phone_numbers))
    for o, f in zip(phone_numbers, result):
        print(f"{o} → {Colors.OKGREEN}{f}")
    wait_for_input()

def filter_jpg_files(files):
    """Show only files ending with '.jpg'"""
    print_header("Filter .jpg Files")
    result = list(filter(lambda x: x.endswith(".jpg"), files))
    if not result:
        print(f"{Colors.WARNING}No .jpg files found.{Colors.ENDC}")
    for f in result:
        print(f"{Colors.OKCYAN}{f}")
    wait_for_input()

# -----------------------------
# Dynamic Data Input
# -----------------------------
def input_employees(default=None):
    """Interactive employee input with optional default"""
    employees = []
    while True:
        entry = input("Enter employee name and salary (name,salary) or press Enter for default/done: ")
        if entry.lower() in ["done", ""] and default:
            return default
        elif entry.lower() in ["done", ""]:
            break
        try:
            name, salary = entry.split(",")
            employees.append({"name": name.strip(), "salary": int(salary.strip())})
        except:
            print(f"{Colors.FAIL}Invalid format! Use name,salary{Colors.ENDC}")
    return employees

def input_users(default=None):
    """Interactive user input with premium status"""
    users = []
    while True:
        entry = input("Enter user name and premium status (name,True/False) or press Enter for default/done: ")
        if entry.lower() in ["done", ""] and default:
            return default
        elif entry.lower() in ["done", ""]:
            break
        try:
            name, premium = entry.split(",")
            users.append({"name": name.strip(), "premium": premium.strip().lower()=="true"})
        except:
            print(f"{Colors.FAIL}Invalid format! Use name,True/False{Colors.ENDC}")
    return users

# -----------------------------
# Main Menu
# -----------------------------
def main_menu():
    """
    Main interactive dashboard menu
    - Provides default example data for simplicity
    - Maps menu choice to lambda functions for each operation
    """
    default_numbers = [1,2,3,4,5,6]
    default_words = ["Python","Lambda","Map","Function"]
    default_emails = ["alice@edu.com","bob@gmail.com","carol@university.edu"]
    default_names = ["Alice Smith","Bob Johnson","Charlie Brown"]
    default_phones = ["1234567890","9876543210"]
    default_files = ["image1.jpg","document.pdf","photo.jpg"]
    default_employees = [{"name":"Alice","salary":5000},{"name":"Bob","salary":7000}]
    default_users = [{"name":"Alice","premium":True},{"name":"Bob","premium":False}]

    while True:
        print_header("Dynamic Smart Data Processor Dashboard")
        print(f"{Colors.OKBLUE}1. Check Even/Odd")
        print("2. Double Numbers")
        print("3. Filter Emails (.edu)")
        print("4. Product of Numbers")
        print("5. First Characters of Words")
        print("6. Sort Employees by Salary")
        print("7. Filter Premium Users")
        print("8. Sort Names by Last Name")
        print("9. Format Phone Numbers")
        print("10. Filter .jpg Files")
        print("0. Exit")

        choice = input(f"{Colors.BOLD}Enter your choice: {Colors.ENDC}").strip()

        if choice=="0":
            print(f"{Colors.OKGREEN}Exiting... Goodbye!{Colors.ENDC}")
            sys.exit()

        # -----------------------------
        # Gather data with defaults
        # -----------------------------
        numbers = get_list_input("Enter numbers (or press Enter for default): ", int, default_numbers)
        words = get_list_input("Enter words (or press Enter for default): ", str, default_words)
        emails = get_list_input("Enter emails (or press Enter for default): ", str, default_emails)
        names = get_list_input("Enter full names (or press Enter for default, comma-separated): ", str, default_names)
        phone_numbers = get_list_input("Enter phone numbers (or press Enter for default): ", str, default_phones)
        files = get_list_input("Enter file names (or press Enter for default): ", str, default_files)
        employees = input_employees(default_employees)
        users = input_users(default_users)

        # Map menu options to corresponding functions
        operations = {
            "1": lambda: check_even_odd(numbers),
            "2": lambda: double_numbers(numbers),
            "3": lambda: filter_edu_emails(emails),
            "4": lambda: product_of_numbers(numbers),
            "5": lambda: first_characters(words),
            "6": lambda: sort_employees_salary(employees),
            "7": lambda: filter_premium_users(users),
            "8": lambda: sort_names_lastname(names),
            "9": lambda: format_phone_numbers(phone_numbers),
            "10": lambda: filter_jpg_files(files)
        }

        if choice in operations:
            operations[choice]()
        else:
            print(f"{Colors.WARNING}Invalid choice. Try again.{Colors.ENDC}")
            wait_for_input()

# -----------------------------
# Run Dashboard
# -----------------------------
if __name__ == "__main__":
    main_menu()
