import json

# Функция для чтения JSON-файла
def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            print("Содержимое файла:")
            print(json.dumps(data, indent=4, ensure_ascii=False))
            return data
    except Exception as e:
        print(f"Ошибка при чтении JSON: {e}")

# Функция для фильтрации данных по версии
def filter_by_version(data, version):
    return [entry for entry in data if entry.get('version') == version]

# Функция для записи отфильтрованных данных в файл
def write_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
            print(f"Данные записаны в файл: {file_path}")
    except Exception as e:
        print(f"Ошибка при записи JSON: {e}")

# Пример использования
json_file_path = 'lab.json'
output_json_file = 'out.json'

# Чтение и обработка данных
data = read_json(json_file_path)
version_to_filter = 1.88  # Нужную версию
filtered_data = filter_by_version(data, version_to_filter)

# Запись результата
write_json(filtered_data, output_json_file)

input("Press Enter to contine...")