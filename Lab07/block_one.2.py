# Функция для обработки файла
def process_file(input_file, output_file):
    try:
        # Читаем строки из входного файла, переводим их в нижний регистр
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = [line.lower() for line in infile]

        # Записываем результат в выходной файл
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(lines)

        print(f"Файл '{output_file}' успешно создан.")
    
    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Укажите входной и выходной файлы
input_file = 'input.txt'
output_file = 'output.txt'

# Обрабатываем файл
process_file(input_file, output_file)

input("Press Enter to contine...")