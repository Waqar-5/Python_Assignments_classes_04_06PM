# Python List Comprehension Hub - Section H (Dynamic)

**Author:** Waqar Ali  
**Purpose:** Interactive hub demonstrating **real-life and interview questions** using Python list comprehension.  

---

## 🌟 Project Overview

The **Python List Comprehension Hub** is an interactive command-line utility that helps you:

- Practice **Python list comprehension** in real-life scenarios.
- Solve common **programming interview questions**.
- Work with dynamic user input.
- Explore practical tasks like string, list, email, transactions, hashtags, and seating arrangements.

All functions are designed to be **dynamic**, **interactive**, and **Pythonic**, while the terminal output is **color-coded** for clarity.

---

## 💡 Features

- ✅ Dynamic user input for all functions
- ✅ Interactive menu with numbered selection
- ✅ Color-coded terminal output using ANSI codes
- ✅ Modular, reusable functions
- ✅ Covers real-life scenarios and interview questions

---

## 📝 Utilities / Questions Covered

| Q No | Functionality | Description |
|------|---------------|-------------|
| 83 | Generate Roll Numbers | `[BSE-1, BSE-2, ..., BSE-n]` dynamically |
| 84 | Extract Vowels | Extract vowels from a given string |
| 85 | Words Starting with 'S' | Filter words starting with "S" |
| 86 | Flatten Nested List | Flatten a list of lists into a single list |
| 87 | Word-Length Dictionary | Create `{word: length}` dictionary from a list of words |
| 88 | Extract Domains | Extract domain names from a list of emails |
| 89 | Even Numbers | Generate even numbers between a dynamic range |
| 90 | Filter Transactions | Filter transactions above a dynamic threshold |
| 91 | Extract Hashtags | Extract hashtags from user-entered tweets |
| 92 | Seat Numbers | Generate seat numbers dynamically like `A1–C5` |
| 93 | Interview Q | When to prefer list comprehension over loops? |
| 94 | Interview Q | Can list comprehensions replace `map`/`filter`? |

---

## 🚀 Installation

1. Make sure **Python 3.x** is installed.
2. Clone this repository or download the Python file:

```bash
git clone <repository-url>
cd python-list-comprehension-hub





No external dependencies are required.

🏃 How to Run

Open terminal or command prompt.

Navigate to the project folder.

Run the main Python file:

python list_comprehension_hub.py


The interactive menu will appear. Choose a utility by entering its number.

Enter dynamic inputs as prompted.

Results will display immediately. You can continue exploring other utilities.

✨ Example Usage
1️⃣ Generate Roll Numbers
Enter the number of students: 5
['BSE-1', 'BSE-2', 'BSE-3', 'BSE-4', 'BSE-5']

2️⃣ Extract Vowels from String
Enter a string: Hello World
['e', 'o', 'o']

3️⃣ Flatten Nested List
Enter number of sublists: 2
Enter elements of sublist 1 separated by space: 1 2
Enter elements of sublist 2 separated by space: 3 4
['1', '2', '3', '4']

4️⃣ Extract Hashtags
Enter number of tweets: 2
Enter tweet 1: Loving Python! #Python #Coding
Enter tweet 2: Good Morning! #Sunshine
['#Python', '#Coding', '#Sunshine']

🧐 Interview Questions

When to prefer list comprehension over loops?
Use list comprehension for concise, readable list creation. Avoid using it for complex logic or operations with side effects.

Can list comprehensions replace map/filter?
Yes, list comprehension can replace map and filter in most cases, making code more readable and Pythonic.

🎨 Color-Coded CLI

Purple – Section Headers

Blue – Menu prompts

Cyan – Informational messages

Green – Success messages / Exit

Yellow – Warnings

Red – Errors