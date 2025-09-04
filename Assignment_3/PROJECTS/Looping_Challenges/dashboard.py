# =========================================================
# Dynamic Smart Office Dashboard Hub (Error-Handled Version)
# Author: Waqar Ali
# Purpose: Fully interactive and error-handled dashboard
# =========================================================

import re      # Regular expressions (used for email validation if needed)
import random  # Random numbers (for dice rolls, simulations, etc.)

# -----------------------------
# Terminal Colors for Better UI
# -----------------------------
class Colors:
    HEADER = '\033[95m'   # Purple for headers
    OKBLUE = '\033[94m'   # Blue for menu items
    OKCYAN = '\033[96m'   # Cyan for prompts and highlights
    OKGREEN = '\033[92m'  # Green for success messages
    WARNING = '\033[93m'  # Yellow for warnings
    FAIL = '\033[91m'     # Red for errors
    ENDC = '\033[0m'      # Reset color to default
    BOLD = '\033[1m'      # Bold text

# -----------------------------
# Function to print colored section headers
# -----------------------------
def print_header(title):
    # Prints the dashboard section header with separators
    print(f"\n{Colors.HEADER}{'='*10} {title} {'='*10}{Colors.ENDC}\n")

# -----------------------------
# Input Functions with Error Handling
# -----------------------------
def input_employee_salaries():
    """Dynamically input employee names and salaries with error checking"""
    salaries = {}  # Dictionary to store employee:salary
    while True:
        try:
            n = int(input("Number of employees: "))  # Get number of employees
            if n <= 0:
                print(f"{Colors.WARNING}Please enter a positive number.{Colors.ENDC}")
                continue
            break  # Exit loop if input is valid
        except ValueError:
            # Handle non-integer input
            print(f"{Colors.FAIL}Invalid input! Enter an integer.{Colors.ENDC}")
    for _ in range(n):
        name = input("Employee Name: ").strip()  # Strip extra spaces
        while True:
            try:
                salary = int(input(f"Salary for {name}: "))  # Convert salary to int
                break
            except ValueError:
                print(f"{Colors.FAIL}Invalid salary! Enter a number.{Colors.ENDC}")
        salaries[name] = salary  # Add employee and salary to dictionary
    return salaries  # Return final dictionary

def input_student_grades():
    """Dynamically input student names and grades with validation"""
    grades = {}  # Dictionary to store student:grade
    while True:
        try:
            n = int(input("Number of students: "))
            if n <= 0:
                print(f"{Colors.WARNING}Please enter a positive number.{Colors.ENDC}")
                continue
            break
        except ValueError:
            print(f"{Colors.FAIL}Invalid input! Enter an integer.{Colors.ENDC}")
    for _ in range(n):
        name = input("Student Name: ").strip()
        while True:
            grade_input = input(f"Grade for {name}: ").strip()  # Get input as string
            try:
                grade = int(grade_input)  # Convert to integer
                if grade < 0 or grade > 100:
                    # Ensure grade is within valid range
                    print(f"{Colors.WARNING}Enter grade between 0 and 100.{Colors.ENDC}")
                    continue
                break
            except ValueError:
                print(f"{Colors.FAIL}Invalid grade! Enter a number between 0-100.{Colors.ENDC}")
        grades[name] = grade  # Add student and grade to dictionary
    return grades

# -----------------------------
# Utility Functions
# -----------------------------
def unique_list(lst):
    """Remove duplicates from a list manually"""
    uniq = []  # New list to store unique items
    for item in lst:
        if item not in uniq:
            uniq.append(item)
    return uniq

def flatten_nested_list(nested):
    """Flatten a nested list of lists into a single list"""
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    return flat

def validate_emails(email_list):
    """Check validity of emails containing '@'"""
    valid, invalid = [], []  # Two lists to separate valid and invalid
    for email in email_list:
        if "@" in email:
            valid.append(email)
        else:
            invalid.append(email)
    return valid, invalid

def filter_pakistani_contacts(contacts):
    """Filter contacts starting with +92"""
    return [c for c in contacts if c.startswith("+92")]

def inventory_update(inventory, orders):
    """Update inventory quantities based on orders"""
    for order in orders:
        item, qty = order["item"], order["qty"]
        if item in inventory:
            inventory[item] -= qty  # Reduce inventory
            print(f"{qty} {item} ordered, remaining: {inventory[item]}")

def display_specialists(doctors):
    """Display only specialist doctors"""
    for doc in doctors:
        if doc["specialist"]:
            print(f"{doc['name']} is a specialist")

def display_courses(student_courses):
    """Display courses per student"""
    for student, courses in student_courses.items():
        print(f"{student} is enrolled in: {courses}")

def break_nested_loops_example():
    """Demonstrate breaking out of nested loops"""
    found = False  # Flag to stop outer loop
    for i in range(1,5):
        for j in range(1,5):
            print(i, j)  # Print loop variables
            if i*j == 6:  # Condition to break
                found = True
                break
        if found:
            break
    print("Exited nested loops when i*j == 6")

# -----------------------------
# Main Menu Function
# -----------------------------
def main_menu():
    """Display interactive dashboard menu and handle user choices"""
    while True:
        print_header("Dynamic Smart Office Dashboard")
        # Menu options
        print(f"{Colors.OKBLUE}1. Above Average Salaries")
        print("2. Grades Pass/Fail")
        print("3. Unique Contacts")
        print("4. Flatten Department List")
        print("5. Validate Emails")
        print("6. Count Urgent Messages")
        print("7. Inventory Simulation")
        print("8. Doctor Specialists")
        print("9. Courses per Student")
        print("10. Break Nested Loops Example")
        print("0. Exit\n")
        
        choice = input(f"{Colors.BOLD}Enter your choice: {Colors.ENDC}").strip()

        # Exit condition
        if choice == "0":
            print(f"{Colors.OKGREEN}Exiting... Goodbye!{Colors.ENDC}")
            break

        # Section 1: Salaries
        elif choice == "1":
            salaries = input_employee_salaries()
            avg = sum(salaries.values()) / len(salaries)
            print(f"Average Salary: {avg}")
            print("Above average salaries:")
            for emp, sal in salaries.items():
                if sal > avg:
                    print(f"{emp}: {sal}")

        # Section 2: Grades
        elif choice == "2":
            grades = input_student_grades()
            print("Pass/Fail Report:")
            for student, grade in grades.items():
                print(f"{student}: {grade} - {'Pass' if grade >=50 else 'Fail'}")

        # Section 3: Contacts
        elif choice == "3":
            contacts = input("Enter contacts separated by commas: ").split(",")
            contacts = unique_list([c.strip() for c in contacts])
            print("Unique Contacts:", contacts)
            print("Pakistani Contacts (+92):", filter_pakistani_contacts(contacts))

        # Section 4: Flatten list
        elif choice == "4":
            departments = [["Ali","Sara"],["Usman","Hina"],["Zara"]]
            print("All Employees Flattened:", flatten_nested_list(departments))

        # Section 5: Emails
        elif choice == "5":
            emails = input("Enter emails separated by commas: ").split(",")
            valid, invalid = validate_emails([e.strip() for e in emails])
            print("Valid Emails:", valid)
            print("Invalid Emails:", invalid)

        # Section 6: Urgent messages
        elif choice == "6":
            messages = ["Meeting at 10", "URGENT: Submit report", "Lunch break", "URGENT: Server down"]
            count = sum(1 for msg in messages if "URGENT" in msg.upper())
            print("Number of urgent messages:", count)

        # Section 7: Inventory
        elif choice == "7":
            inventory = {"Pens": 100, "Notebooks": 50, "Staplers": 20}
            orders = [{"item":"Pens","qty":15},{"item":"Staplers","qty":5},{"item":"Notebooks","qty":10}]
            inventory_update(inventory, orders)

        # Section 8: Specialists
        elif choice == "8":
            doctors = [
                {"name":"Dr. Ahmed","specialist":True},
                {"name":"Dr. Sara","specialist":False},
                {"name":"Dr. Ali","specialist":True}
            ]
            display_specialists(doctors)

        # Section 9: Courses
        elif choice == "9":
            student_courses = {
                "Ali":["Math","Physics"],
                "Sara":["Biology","English"],
                "Usman":["Math","CS"]
            }
            display_courses(student_courses)

        # Section 10: Nested loops demo
        elif choice == "10":
            break_nested_loops_example()

        # Invalid choice
        else:
            print(f"{Colors.WARNING}Invalid choice. Try again.{Colors.ENDC}")

        input(f"{Colors.OKCYAN}\nPress Enter to continue...{Colors.ENDC}")

# -----------------------------
# Run the Dashboard
# -----------------------------
if __name__ == "__main__":
    main_menu()
