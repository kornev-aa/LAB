# block_one.py (11)

def count_positive_numbers(a, b, c):
    numbers = [a, b, c]
    positive_count = sum(1 for num in numbers if num > 0)
    return positive_count

try:
    a, b, c = map(int, input("Введите три числа через пробел: ").split())
    positive_count = count_positive_numbers(a, b, c)
    print(f"Количество положительных чисел: {positive_count}")
except ValueError:
    print("Ошибка: введите ровно три числа, разделенные пробелами!")

input("Press Enter to close the window...")