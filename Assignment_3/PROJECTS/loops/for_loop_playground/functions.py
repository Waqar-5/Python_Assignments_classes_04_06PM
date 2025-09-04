# Functions implementing all 10 tasks
from data import *

# 1. Print all file names
def print_files():
    for f in files:
        print(f)

# 2. Print student names
def print_students():
    for roll, name in students:
        print(f"Roll {roll}: {name}")

# 3. Print only Gmail emails
def print_gmail_emails():
    for email in emails:
        if email.lower().endswith("@gmail.com"):
            print(email)

# 4. Display product prices with PKR
def display_prices():
    for price in prices:
        print(f"PKR {price}")

# 5. Mask phone numbers except last 4 digits
def mask_phones():
    for c in contacts:
        masked = "*"*(len(c["phone"])-4) + c["phone"][-4:]
        print(f"{c['name']}: {masked}")

# 6. Transactions above 50,000
def high_transactions():
    for t in transactions:
        if t > 50000:
            print(t)

# 7. Words in sentence reversed
def reverse_words():
    words = sentence.split()
    for w in reversed(words):
        print(w)

# 8. Out of stock items
def out_of_stock():
    for p in shopping_cart:
        if p["quantity"] == 0:
            print(f"{p['item']} -> Out of stock")

# 9. Pending tasks
def pending_tasks():
    for t in tasks:
        if t["status"].lower() == "pending":
            print(t["title"])

# 10. First 5 notifications
def first_notifications():
    for n in notifications[:5]:
        print(n)

# 11. Explanation: for item vs range(len(list))
def explain_for_vs_range():
    print("for item in list: → directly gives value")
    print("for i in range(len(list)): → gives index, use list[i] to get value")

# 12. Explanation: for loop and iterators
def explain_iterators():
    print("Python internally uses iter() to create an iterator and calls next() until StopIteration occurs.")
