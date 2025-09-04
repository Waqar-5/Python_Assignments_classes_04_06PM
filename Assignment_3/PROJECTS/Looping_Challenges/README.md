# Dynamic Smart Office Dashboard Hub (Error-Handled Version)

## Author
**Waqar Ali**

## Overview
The **Dynamic Smart Office Dashboard Hub** is an interactive, terminal-based Python application designed to manage and analyze common office data. It includes features for employee salaries, student grades, contacts, inventory management, email validation, and more. The application emphasizes **error-handling**, **dynamic input**, and **user-friendly terminal output with colors** for an enhanced user experience.

---

## Features

1. **Employee Salary Analysis**
   - Input multiple employee names and salaries dynamically.
   - Automatically calculate the average salary.
   - Display employees earning **above-average salaries**.

2. **Student Grades Pass/Fail**
   - Input student names and grades dynamically.
   - Grades are validated to ensure they are integers between 0 and 100.
   - Display **Pass/Fail report** based on grade threshold (50).

3. **Unique Contact Management**
   - Input a list of contacts.
   - Automatically remove duplicates.
   - Filter **Pakistani contacts** starting with `+92`.

4. **Nested List Flattening**
   - Flatten nested lists of departments or groups into a single list.

5. **Email Validation**
   - Validate emails based on the presence of the `@` symbol.
   - Separate valid and invalid emails.

6. **Urgent Message Counter**
   - Count messages containing the keyword **URGENT** (case-insensitive).

7. **Inventory Management**
   - Track inventory items and quantities.
   - Update inventory based on incoming orders dynamically.

8. **Doctor Specialist Filter**
   - Display only doctors marked as **specialists**.

9. **Student Courses Display**
   - Show courses enrolled by each student in a structured format.

10. **Nested Loops Demo**
    - Demonstrates breaking out of nested loops using a real example.

---

## Technical Highlights

- **Error-Handling:** All user inputs are validated with helpful error messages.
- **Dynamic Input:** Users can enter any number of employees, students, contacts, or other data without modifying code.
- **Terminal UI Enhancements:** Uses colored text for headers, prompts, warnings, and errors for better clarity.
- **Utility Functions:** Includes reusable functions like `unique_list`, `flatten_nested_list`, and `validate_emails`.
- **Nested Loops Management:** Demonstrates breaking nested loops effectively.

---

## Installation & Requirements

1. **Python Version:** 3.x or higher
2. **No external libraries required** – only built-in modules `random` and `re`.
3. Clone the repository:
   ```bash
   git clone <repository-url>



Run the dashboard:

python dashboard.py

Usage

Run the program in a terminal.

Navigate through the main menu by entering the option number.

Input data as prompted.

View results immediately on the console.

Press Enter to return to the menu or continue.

Example
========== Dynamic Smart Office Dashboard ==========

1. Above Average Salaries
2. Grades Pass/Fail
3. Unique Contacts
...
Enter your choice: 1

Number of employees: 3
Employee Name: Ali
Salary for Ali: 50000
Employee Name: Sara
Salary for Sara: 60000
Employee Name: Usman
Salary for Usman: 40000

Average Salary: 50000.0
Above average salaries:
Sara: 60000

Contributing

Feel free to contribute by:

Adding new dashboard features

Enhancing error handling

Improving UI aesthetics

Adding more data validation checks

