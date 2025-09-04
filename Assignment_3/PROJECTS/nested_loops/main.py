"""
Nested Loops Showcase Project
=============================
Author: Waqar Ali
Purpose: Demonstrate real-world and interview-style nested loop problems in Python.
"""

# ---------------------------
# Section C: Nested Loops
# ---------------------------

def cinema_seats():
    print("\n🎬 Cinema Seats:")
    for row in ["A", "B", "C"]:
        for seat in range(1, 6):
            print(f"{row}{seat}", end=" ")
    print("\n")  # new line


def outfit_combinations():
    shirts = ["Red", "Blue"]
    pants = ["Black", "White"]
    print("\n👕 Outfit Combinations:")
    for shirt in shirts:
        for pant in pants:
            print(f"{shirt} Shirt + {pant} Pant")


def clock_minutes():
    print("\n⏰ Clock Minutes from 12:00 to 12:10:")
    for minute in range(0, 11):
        print(f"12:{minute:02d}")


def timetable():
    slots = ["Morning", "Evening"]
    print("\n📅 Timetable:")
    for day in range(1, 4):
        for slot in slots:
            print(f"Day {day} - {slot}")


def bus_seats():
    print("\n🚌 Bus Seating Chart:")
    for row in range(1, 4):
        for seat in ["A", "B", "C", "D"]:
            print(f"{row}{seat}", end=" ")
        print()


def tic_tac_toe():
    print("\n❌⭕ Tic-Tac-Toe Board:")
    for i in range(3):
        for j in range(3):
            print("[ ]", end=" ")
        print()


def star_pyramid():
    print("\n⭐ Star Pyramid:")
    rows = 5
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))


def team_pairs():
    players = ["Ali", "Sara", "John"]
    print("\n👥 Team Pairs:")
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            print(f"{players[i]} & {players[j]}")


def multiplication_tables():
    print("\n✖ Multiplication Tables (2–5):")
    for num in range(2, 6):
        print(f"\nTable of {num}:")
        for i in range(1, 11):
            print(f"{num} × {i} = {num * i}")


def shopping_categories():
    shop = {
        "Fruits": ["Apple", "Banana"],
        "Electronics": ["Mobile", "Laptop"]
    }
    print("\n🛒 Shopping Categories:")
    for category, products in shop.items():
        print(f"{category}:")
        for item in products:
            print(f"  - {item}")


def interview_qs():
    print("\n💡 Interview Insights:")
    print("33. Time complexity of nested loops?")
    print("   → Usually O(n²), but depends on loop sizes.\n")
    print("34. When replace nested loops with list comprehensions?")
    print("   → When readability improves or when concise data transformation is needed.")


# ---------------------------
# Main Menu Runner (Dynamic)
# ---------------------------

def main():
    options = {
        "23": ("Cinema Seats", cinema_seats),
        "24": ("Outfit Combinations", outfit_combinations),
        "25": ("Clock Minutes", clock_minutes),
        "26": ("Timetable", timetable),
        "27": ("Bus Seats", bus_seats),
        "28": ("Tic-Tac-Toe Board", tic_tac_toe),
        "29": ("Star Pyramid", star_pyramid),
        "30": ("Team Pairs", team_pairs),
        "31": ("Multiplication Tables", multiplication_tables),
        "32": ("Shopping Categories", shopping_categories),
        "33-34": ("Interview Questions", interview_qs),
        "all": ("Run All Examples", None),
    }

    while True:
        print("\n🚀 Nested Loops Showcase Project 🚀")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        print("0. Exit")

        choice = input("\n👉 Choose an option (e.g., 23, 29, all): ").strip()

        if choice == "0":
            print("👋 Exiting project. Goodbye!")
            break
        elif choice == "all":
            for _, func in options.values():
                if func:
                    func()
        elif choice in options:
            func = options[choice][1]
            if func:
                func()
        else:
            print("❌ Invalid choice, please try again.")


if __name__ == "__main__":
    main()












# """
# Nested Loops Showcase Project
# =============================
# Author: Waqar Ali
# Purpose: Demonstrate real-world and interview-style nested loop problems in Python.
# """

# # ---------------------------
# # Section C: Nested Loops (Dynamic)
# # ---------------------------

# def cinema_seats():
#     print("\n🎬 Cinema Seats:")
#     rows = input("👉 Enter row labels (comma separated, e.g., A,B,C): ").split(",")
#     seats = int(input("👉 Enter number of seats per row: "))
#     for row in rows:
#         for seat in range(1, seats + 1):
#             print(f"{row.strip()}{seat}", end=" ")
#     print("\n")


# def outfit_combinations():
#     shirts = input("👉 Enter shirt colors (comma separated): ").split(",")
#     pants = input("👉 Enter pant colors (comma separated): ").split(",")
#     print("\n👕 Outfit Combinations:")
#     for shirt in shirts:
#         for pant in pants:
#             print(f"{shirt.strip()} Shirt + {pant.strip()} Pant")


# def clock_minutes():
#     print("\n⏰ Clock Minutes:")
#     start = int(input("👉 Enter start minute (e.g., 0): "))
#     end = int(input("👉 Enter end minute (e.g., 10): "))
#     for minute in range(start, end + 1):
#         print(f"12:{minute:02d}")


# def timetable():
#     days = int(input("👉 Enter number of days: "))
#     slots = input("👉 Enter slots (comma separated, e.g., Morning,Evening): ").split(",")
#     print("\n📅 Timetable:")
#     for day in range(1, days + 1):
#         for slot in slots:
#             print(f"Day {day} - {slot.strip()}")


# def bus_seats():
#     rows = int(input("👉 Enter number of bus rows: "))
#     seats = input("👉 Enter seat labels (comma separated, e.g., A,B,C,D): ").split(",")
#     print("\n🚌 Bus Seating Chart:")
#     for row in range(1, rows + 1):
#         for seat in seats:
#             print(f"{row}{seat.strip()}", end=" ")
#         print()


# def tic_tac_toe():
#     size = int(input("👉 Enter Tic-Tac-Toe board size (default 3): ") or 3)
#     print(f"\n❌⭕ Tic-Tac-Toe {size}×{size} Board:")
#     for i in range(size):
#         for j in range(size):
#             print("[ ]", end=" ")
#         print()


# def star_pyramid():
#     rows = int(input("👉 Enter number of rows for pyramid: "))
#     print("\n⭐ Star Pyramid:")
#     for i in range(1, rows + 1):
#         print(" " * (rows - i) + "*" * (2 * i - 1))


# def team_pairs():
#     players = input("👉 Enter player names (comma separated): ").split(",")
#     print("\n👥 Team Pairs:")
#     for i in range(len(players)):
#         for j in range(i + 1, len(players)):
#             print(f"{players[i].strip()} & {players[j].strip()}")


# def multiplication_tables():
#     start = int(input("👉 Enter start table number (e.g., 2): "))
#     end = int(input("👉 Enter end table number (e.g., 5): "))
#     print(f"\n✖ Multiplication Tables ({start}–{end}):")
#     for num in range(start, end + 1):
#         print(f"\nTable of {num}:")
#         for i in range(1, 11):
#             print(f"{num} × {i} = {num * i}")


# def shopping_categories():
#     categories = int(input("👉 Enter number of categories: "))
#     shop = {}
#     for i in range(categories):
#         category = input(f"Enter name for category {i+1}: ")
#         items = input(f"Enter products for {category} (comma separated): ").split(",")
#         shop[category] = [item.strip() for item in items]

#     print("\n🛒 Shopping Categories:")
#     for category, products in shop.items():
#         print(f"{category}:")
#         for item in products:
#             print(f"  - {item}")


# def interview_qs():
#     print("\n💡 Interview Insights:")
#     print("33. Time complexity of nested loops?")
#     print("   → Usually O(n²), but depends on loop sizes.\n")
#     print("34. When replace nested loops with list comprehensions?")
#     print("   → When readability improves or when concise data transformation is needed.")


# # ---------------------------
# # Main Menu Runner (Dynamic)
# # ---------------------------

# def main():
#     options = {
#         "23": ("Cinema Seats", cinema_seats),
#         "24": ("Outfit Combinations", outfit_combinations),
#         "25": ("Clock Minutes", clock_minutes),
#         "26": ("Timetable", timetable),
#         "27": ("Bus Seats", bus_seats),
#         "28": ("Tic-Tac-Toe Board", tic_tac_toe),
#         "29": ("Star Pyramid", star_pyramid),
#         "30": ("Team Pairs", team_pairs),
#         "31": ("Multiplication Tables", multiplication_tables),
#         "32": ("Shopping Categories", shopping_categories),
#         "33-34": ("Interview Questions", interview_qs),
#         "all": ("Run All Examples", None),
#     }

#     while True:
#         print("\n🚀 Nested Loops Showcase Project 🚀")
#         for key, (desc, _) in options.items():
#             print(f"{key}. {desc}")
#         print("0. Exit")

#         choice = input("\n👉 Choose an option (e.g., 23, 29, all): ").strip()

#         if choice == "0":
#             print("👋 Exiting project. Goodbye!")
#             break
#         elif choice == "all":
#             for _, func in options.values():
#                 if func:
#                     func()
#         elif choice in options:
#             func = options[choice][1]
#             if func:
#                 func()
#         else:
#             print("❌ Invalid choice, please try again.")


# if __name__ == "__main__":
#     main()
