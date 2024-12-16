# block_three.py (11)

string = ("89-3589-23580-6320-hhhhhHhhh2949Hhh!-!-1-1-1-1-!!-.......-!_-11_!1!!-!-!-1!1!1!!!!")
print(string)

# Find the longest sequence of consecutive 'н'
max_count = 0
current_count = 0

for char in string:
    if char == 'h':
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print(f"The longest sequence of consecutive 'h' is {max_count}.")

# Replace all exclamation marks with dots
transformed_string = string.replace('!', '.')

print(f"The transformed string is: {transformed_string}")

input("Press Enter to close the window...")