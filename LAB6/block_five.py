# block_five.py (10)

# 1.
def count_numbers_with_digits(a, b, c, n):

    # Подсчитывает количество чисел на отрезке [100, n], которые состоят только из цифр a, b и c.
    
    # :param a: первая допустимая цифра
    # :param b: вторая допустимая цифра
    # :param c: третья допустимая цифра
    # :param n: верхняя граница диапазона (210 < n < 231)
    # :return: количество чисел, состоящих только из цифр a, b и c

    # Проверка на корректность ввода
    if not (210 < n < 231):
        raise ValueError("N must be in [211; 230] range.")
    
    valid_digits = {str(a), str(b), str(c)}  # Множество допустимых цифр
    count = 0  # Счетчик подходящих чисел

    for number in range(100, n + 1):
        str_number = str(number)  # Преобразуем число в строку
        if all(digit in valid_digits for digit in str_number):  # Проверяем все цифры числа
            count += 1  # Если все цифры подходят, увеличиваем счетчик
    
    return count

# Пример:
n = 220
a, b, c = 1, 2, 3
result = count_numbers_with_digits(a, b, c, n)
print(f"Amount of numbers with {a}, {b}, {c} digits in [100, {n}] range: {result}")

# 2.
def geometric_sum(a1, q, n):

    # Рекурсивная функция для нахождения суммы n первых членов геометрической прогрессии.
    
    # :param a1: первый член прогрессии
    # :param q: знаменатель прогрессии
    # :param n: количество членов прогрессии
    # :return: сумма n первых членов прогрессии

    # Базовый случай
    if n == 1:
        return a1
    # Рекурсивный случай
    return geometric_sum(a1, q, n - 1) + a1 * q**(n - 1)

# Пример:
a1 = 2  # первый член прогрессии
q = 3   # знаменатель прогрессии
n = 4   # количество членов

result = geometric_sum(a1, q, n)
print(f"sum of the {n} first terms of a geometric progression: {result}")

input("Press Enter to close the window...")