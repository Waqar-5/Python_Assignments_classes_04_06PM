numbers = [12, 1, "a", 10, 2]
# numbers = ["b","c", "a",]

sumOfAllValues = 0
count = 0  # To count how many numeric values we add

for i in numbers:
    try:
        sumOfAllValues += i
        count += 1
    except TypeError:
        # Skip non-numeric values
        continue
    # or
    # except TypeError as e:
        # print(f"Error adding value '{i}': {e}")


# Safely calculate the average
try:
    avg = sumOfAllValues / count
    print("Average of numeric values:", avg)
except ZeroDivisionError:
    print("No numeric values found to calculate average.")