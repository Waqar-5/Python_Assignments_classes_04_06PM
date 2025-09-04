
# Dynamic Smart Data Processor Dashboard (Enhanced UX)

## Overview
The **Dynamic Smart Data Processor Dashboard** is a Python terminal application designed to provide **interactive, intuitive, and error-handled data processing**.  
It combines **Lambda functions, `map()`, `filter()`, `reduce()`**, and modern Python techniques to handle various data tasks.  
This version includes **well-commented code**, **color-coded output**, and **robust input validation**.

---

## Features
- **Interactive Terminal Dashboard:** Clean CLI menu for selecting operations.
- **Color-coded Output:** Uses ANSI terminal colors for headers, prompts, warnings, errors, and success messages.
- **Lambda Operations for Data Processing:**
  - Check Even/Odd numbers
  - Double numbers
  - Filter `.edu` emails
  - Compute product of numbers
  - Extract first characters of words
  - Sort employees by salary
  - Filter premium users
  - Sort names by last name
  - Format phone numbers `(xxx) xxx-xxxx`
  - Filter `.jpg` files
- **Dynamic Data Input:** Accepts user input or uses default datasets.
- **Robust Error Handling:** Prevents crashes from invalid inputs and provides user-friendly prompts.
- **Interactive Pauses:** Uses `wait_for_input()` to allow users to view results before continuing.

---

## How It Works
1. **Launch the program** using Python 3.6+.
2. **Select an operation** from the main menu by entering the corresponding number.
3. **Provide input**:
   - Enter data manually or press Enter to use default values.
   - Lists of numbers, words, emails, names, phone numbers, files, employees, or users.
4. **View color-coded results** for each operation.
5. **Return to the menu** and repeat or exit the program.

---

## Default Example Data
| Type          | Default Values |
|---------------|----------------|
| Numbers       | `[1, 2, 3, 4, 5, 6]` |
| Words         | `["Python", "Lambda", "Map", "Function"]` |
| Emails        | `["alice@edu.com", "bob@gmail.com", "carol@university.edu"]` |
| Names         | `["Alice Smith", "Bob Johnson", "Charlie Brown"]` |
| Phone Numbers | `["1234567890", "9876543210"]` |
| Files         | `["image1.jpg", "document.pdf", "photo.jpg"]` |
| Employees     | `[{"name":"Alice","salary":5000},{"name":"Bob","salary":7000}]` |
| Users         | `[{"name":"Alice","premium":True},{"name":"Bob","premium":False}]` |

---

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/dynamic-data-dashboard.git
Navigate into the project directory:

bash
Copy code
cd dynamic-data-dashboard
Run the dashboard:

bash
Copy code
python dashboard.py
Example Operations
1. Check Even/Odd
Input: [1,2,3,4,5]
Output:

makefile
Copy code
1: Odd
2: Even
3: Odd
4: Even
5: Odd
2. Double Numbers
Input: [1,2,3]
Output:

Copy code
1 → 2
2 → 4
3 → 6
3. Filter .edu Emails
Input: ["alice@edu.com","bob@gmail.com"]
Output:

css
Copy code
alice@edu.com
4. Product of Numbers
Input: [2,3,4]
Output:

makefile
Copy code
Product: 24
5. First Characters of Words
Input: ["Python","Lambda"]
Output:

css
Copy code
Python → P
Lambda → L
6. Sort Employees by Salary
Input: [{"name":"Alice","salary":5000},{"name":"Bob","salary":7000}]
Output:

nginx
Copy code
Alice → $5000
Bob → $7000
7. Filter Premium Users
Input: [{"name":"Alice","premium":True},{"name":"Bob","premium":False}]
Output:

scss
Copy code
Alice (Premium)
8. Sort Names by Last Name
Input: ["Alice Smith","Bob Johnson"]
Output:

nginx
Copy code
Bob Johnson
Alice Smith
9. Format Phone Numbers
Input: ["1234567890"]
Output:

scss
Copy code
1234567890 → (123) 456-7890
10. Filter .jpg Files
Input: ["photo.jpg","doc.pdf"]
Output:

Copy code
photo.jpg
Technologies Used
Python 3

functools.reduce()

Lambda functions, map(), filter()

ANSI terminal colors

Author
Waqar Ali – Developer and Python Enthusiast

