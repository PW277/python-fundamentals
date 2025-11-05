# ====================================================
# File Handling and Unpacking Examples
# ====================================================

# --- 1. Writing to a file safely with 'with open' ---

# 'w' = write mode (overwrites existing file)
# 'a' = append mode (adds to the end)
# 'r' = read mode (default)

print("Example 1: Writing to a file...")

with open("example_output.txt", "w") as f:
    f.write("This file was created with python!\n")
    f.write("Each write adds text exactly as given.\n")

print("File written successfully.\n")

# --- 2. Appending to an existing file ---

print("Example 2: Appending more content")

with open("example_output.txt", "a") as f:
    f.write("Appending more lines...\n")
    f.write("No overwrite this time!\n")

print("More text appended.\n")

# --- 3. Reading from a file ---

print("Example 3: Reading the file back...")

with open("example_output.txt", "r") as f:
    content = f.read()

print("File contents:\n")
print(content)

# --- 4. Reading line by line ---

print("Example 4: reading line by line...")

with open("example_output.txt", "r") as f:
    for line in f:
        print("LINE:", line.strip())

print()

# --- 5. Simple unpacking ---

print("Example 5: Unpacking a list...")

letters = ["a", "b", "c"]
print("Normal print:", letters)
print("Unpacked print:", *letters)
print()


# --- 6. Unpacking in variable assignment ---

print("Example 6: Unpacking into variables...")

coords = (10, 20, 30)
x, y, z = coords
print(f"x={x}, y={y}, z={z}")
print()


# --- 7. Extended unpacking with * ---

print("Example 7: Extended unpacking...")

#nums = [1, 2, 3, 4, 5]
nums = [1, 2, 3, 4]
first, *middle, last = nums
print(f"First: {first}, Middle: {middle}, Last: {last}")
print()

# --- 8. Function argument unpacking (* and **) ---

print("Example 8: Function argument unpacking...")

def greet(name, age, country):
    print(f"Hello, I’m {name}, I’m {age} years old, from {country}.")

args = ["Paul", 46, "England"]
kwargs = {"name": "Paul", "age": 46, "country": "England"}

greet(*args)   # Unpack list into positional args
greet(**kwargs)  # Unpack dict into keyword args
print()

# --- 9. Combining both ideas (file + unpacking) ---

print("Example 9: Combining both...")

# We'll read the lines from the file and unpack them directly into print()
with open("example_output.txt", "r") as f:
    lines = f.readlines()  # list of lines

print("Unpacked lines:")
print(*lines, sep="")  # each line already ends with a newline

print("Done!")