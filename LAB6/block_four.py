# block_four.py (10)

# 1.
# List with duplicates
list_with_duplicates = [1, 2, 3, 4, 2, 5]
# List without duplicates
list_without_duplicates = [1, 2, 3, 4, 5]

def check_duplicates(lst):
    duplicates = set([x for x in lst if lst.count(x) > 1])
    if duplicates:
        print(f"The list {lst} contains duplicates: {duplicates}")
    else:
        print(f"The list {lst} has no duplicates.")

# Check both lists
check_duplicates(list_with_duplicates)
check_duplicates(list_without_duplicates)


# 2. 
import random

# Generate a one-dimensional array with 15 random elements
array = [random.randint(0, 30) for _ in range(15)]
print("Original array:", array)

# Transform the array
transformed_array = [
    0 if x < 10 else 1 if x > 20 else x for x in array
]

print("Transformed array:", transformed_array)

input("Press Enter to close the window...")