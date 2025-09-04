# =========================================================
# Dynamic Smart Data Utility Dashboard Hub (Error-Handled)
# Author: Waqar Ali
# Purpose: Fully interactive and market-ready data utility dashboard
# =========================================================

import re      # For validation
import random  # For simulations and random tasks

# -----------------------------
# Terminal Colors for Better UI
# -----------------------------
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_header(title):
    print(f"\n{Colors.HEADER}{'='*10} {title} {'='*10}{Colors.ENDC}\n")

# -----------------------------
# Login System
# -----------------------------
users = {"admin": "admin123", "user1": "pass123"}

def login():
    print_header("Login System")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if users.get(username) == password:
        print(f"{Colors.OKGREEN}✅ Login successful! Welcome {username}{Colors.ENDC}")
        return True
    print(f"{Colors.FAIL}❌ Invalid credentials!{Colors.ENDC}")
    return False

# -----------------------------
# Custom Enumerate Generator
# -----------------------------
def my_enumerate(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

# -----------------------------
# Input Functions
# -----------------------------
def input_employee_salaries():
    salaries = {}
    while True:
        try:
            n = int(input("Number of employees: "))
            if n <= 0:
                print(f"{Colors.WARNING}Enter a positive number.{Colors.ENDC}")
                continue
            break
        except ValueError:
            print(f"{Colors.FAIL}Invalid input! Enter an integer.{Colors.ENDC}")
    for _ in range(n):
        name = input("Employee Name: ").strip()
        while True:
            try:
                salary = int(input(f"Salary for {name}: "))
                break
            except ValueError:
                print(f"{Colors.FAIL}Invalid salary! Enter a number.{Colors.ENDC}")
        salaries[name] = salary
    return salaries

def input_student_grades():
    grades = {}
    while True:
        try:
            n = int(input("Number of students: "))
            if n <= 0:
                print(f"{Colors.WARNING}Enter a positive number.{Colors.ENDC}")
                continue
            break
        except ValueError:
            print(f"{Colors.FAIL}Invalid input! Enter an integer.{Colors.ENDC}")
    for _ in range(n):
        name = input("Student Name: ").strip()
        while True:
            try:
                grade = int(input(f"Grade for {name}: "))
                if grade < 0 or grade > 100:
                    print(f"{Colors.WARNING}Grade must be 0-100.{Colors.ENDC}")
                    continue
                break
            except ValueError:
                print(f"{Colors.FAIL}Invalid grade! Enter a number.{Colors.ENDC}")
        grades[name] = grade
    return grades

# -----------------------------
# Utility Functions
# -----------------------------
def unique_list(lst):
    uniq = []
    for item in lst:
        if item not in uniq:
            uniq.append(item)
    return uniq

def flatten_nested_list(nested):
    return [item for sublist in nested for item in sublist]

def validate_emails(email_list):
    valid, invalid = [], []
    for email in email_list:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            valid.append(email)
        else:
            invalid.append(email)
    return valid, invalid

def filter_pakistani_contacts(contacts):
    return [c for c in contacts if c.startswith("+92")]

def inventory_update(inventory, orders):
    for order in orders:
        item, qty = order["item"], order["qty"]
        if item in inventory:
            inventory[item] -= qty
            print(f"{qty} {item} ordered, remaining: {inventory[item]}")

def display_specialists(doctors):
    for doc in doctors:
        if doc["specialist"]:
            print(f"{doc['name']} is a specialist")

def display_courses(student_courses):
    for student, courses in student_courses.items():
        print(f"{student} is enrolled in: {courses}")

def break_nested_loops_example():
    found = False
    for i in range(1,5):
        for j in range(1,5):
            print(i, j)
            if i*j == 6:
                found = True
                break
        if found:
            break
    print("Exited nested loops when i*j == 6")

def word_frequency():
    text = input("Enter text: ")
    freq = {}
    for word in text.split():
        freq[word] = freq.get(word, 0) + 1
    print("Word Frequencies:", freq)

def unique_pairs():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    target = int(input("Enter target sum: "))
    pairs = set()
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    print("Unique Pairs:", list(pairs))

def check_parentheses():
    s = input("Enter parentheses string: ")
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            print("❌ Not Balanced")
            return
    print("✅ Balanced" if count == 0 else "❌ Not Balanced")

# -----------------------------
# Main Menu
# -----------------------------
def main_menu():
    while True:
        print_header("Dynamic Smart Data Utility Dashboard")
        print(f"{Colors.OKBLUE}1. Employee Salaries Above Average")
        print("2. Student Pass/Fail Grades")
        print("3. Unique Contacts & Pakistani Contacts")
        print("4. Flatten Nested List")
        print("5. Validate Emails")
        print("6. Word Frequency Counter")
        print("7. Unique Sum Pairs")
        print("8. Check Balanced Parentheses")
        print("9. Inventory Simulation")
        print("10. Doctor Specialists")
        print("11. Courses per Student")
        print("12. Break Nested Loops Example")
        print("0. Exit\n")

        choice = input(f"{Colors.BOLD}Enter choice: {Colors.ENDC}").strip()

        if choice == "0":
            print(f"{Colors.OKGREEN}Exiting... Goodbye!{Colors.ENDC}")
            break
        elif choice == "1":
            salaries = input_employee_salaries()
            avg = sum(salaries.values()) / len(salaries)
            print(f"Average Salary: {avg}")
            for emp, sal in salaries.items():
                if sal > avg:
                    print(f"{emp}: {sal}")
        elif choice == "2":
            grades = input_student_grades()
            for student, grade in grades.items():
                print(f"{student}: {grade} - {'Pass' if grade>=50 else 'Fail'}")
        elif choice == "3":
            contacts = input("Enter contacts separated by commas: ").split(",")
            contacts = unique_list([c.strip() for c in contacts])
            print("Unique Contacts:", contacts)
            print("Pakistani Contacts (+92):", filter_pakistani_contacts(contacts))
        elif choice == "4":
            departments = [["Ali","Sara"],["Usman","Hina"],["Zara"]]
            print("All Employees Flattened:", flatten_nested_list(departments))
        elif choice == "5":
            emails = input("Enter emails separated by commas: ").split(",")
            valid, invalid = validate_emails([e.strip() for e in emails])
            print("Valid Emails:", valid)
            print("Invalid Emails:", invalid)
        elif choice == "6":
            word_frequency()
        elif choice == "7":
            unique_pairs()
        elif choice == "8":
            check_parentheses()
        elif choice == "9":
            inventory = {"Pens": 100, "Notebooks": 50, "Staplers": 20}
            orders = [{"item":"Pens","qty":15},{"item":"Staplers","qty":5},{"item":"Notebooks","qty":10}]
            inventory_update(inventory, orders)
        elif choice == "10":
            doctors = [
                {"name":"Dr. Ahmed","specialist":True},
                {"name":"Dr. Sara","specialist":False},
                {"name":"Dr. Ali","specialist":True}
            ]
            display_specialists(doctors)
        elif choice == "11":
            student_courses = {
                "Ali":["Math","Physics"],
                "Sara":["Biology","English"],
                "Usman":["Math","CS"]
            }
            display_courses(student_courses)
        elif choice == "12":
            break_nested_loops_example()
        else:
            print(f"{Colors.WARNING}Invalid choice. Try again.{Colors.ENDC}")

        input(f"{Colors.OKCYAN}\nPress Enter to continue...{Colors.ENDC}")

# -----------------------------
# Run Dashboard
# -----------------------------
if __name__ == "__main__":
    if login():
        main_menu()
