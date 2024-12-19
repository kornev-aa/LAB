import csv

# Функция для чтения CSV-файла и вывода содержимого
def read_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            print("Содержимое файла (Ключ → Значение):")
            for row in reader:
                print(", ".join(f"{key} → {value}" for key, value in row.items()))
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

# Функция для вычисления минимального/максимального значения
def get_min_max(file_path, column):
    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            values = [float(row[column].strip().replace('"', '')) for row in reader if row[column].strip()]
        return min(values), max(values)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при вычислении минимального/максимального значения: {e}")

# Функция для подсчета количества подходящих значений
def count_values(file_path, column, target_value):
    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            return sum(1 for row in reader if row[column].strip() == str(target_value))
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при подсчете значений: {e}")

# Функция для вычисления среднего значения
def get_avg(file_path, column):
    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            values = [float(row[column].strip().replace('"', '')) for row in reader if row[column].strip()]
        return sum(values) / len(values) if values else None
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при вычислении среднего значения: {e}")

# Путь к файлу
csv_file_path = '4.csv'

# Вывод содержимого файла
read_csv(csv_file_path)

# Вычисления
column_mileage = '"Mileage (thousands)"'
column_year = 'Year'
column_price = '"Price"'

min_mileage, max_mileage = get_min_max(csv_file_path, column_mileage)
print(f"Минимальный пробег: {min_mileage}, Максимальный пробег: {max_mileage}")

year_to_count = 1997
count_year = count_values(csv_file_path, column_year, year_to_count)
print(f"Количество записей с годом {year_to_count}: {count_year}")

avg_price = get_avg(csv_file_path, column_price)
print(f"Средняя цена: {avg_price}")

input("Press Enter to contine...")