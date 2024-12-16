# block_two.py (4)

# 1.
# Input values
a = int(input("Enter the value of a (a <= 200): "))

# Ensure the input is valid
if a > 200:
    print("Invalid input. a must be less than or equal to 200.")
else:
    # Calculate the sum of integers from a to 200
    total_sum = 0
    count = 0

    for num in range(a, 201):
        total_sum += num
        count += 1

    # Calculate the arithmetic mean
    arithmetic_mean = total_sum / count
    print(f"The arithmetic mean of integers from {a} to 200 is {arithmetic_mean:.2f}.")

# 2.
# Input the sequence
sequence = list(map(float, input("Enter the sequence of numbers separated by spaces: ").split()))

# Ensure the sequence starts with a positive number
if sequence[0] <= 0:
    print("The sequence must start with a positive number.")
else:
    # Count positive numbers using while
    count = 0
    i = 0

    while i < len(sequence) and sequence[i] > 0:
        count += 1
        i += 1

    print(f"The number of positive numbers at the start of the sequence is {count}.")
    
    input("Press Enter to close the window...")