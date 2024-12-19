import os
import glob
import shutil
import subprocess

def open_file(file_path):
    try:
        if os.path.exists(file_path):
            subprocess.run(['notepad', file_path], check=True)  # Замените "notepad" на нужный текстовый редактор
            print(f"Файл {file_path} успешно открыт.")
        else:
            print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")

def show_file_content(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                print(file.read())
        else:
            print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

def find_files(search_name):
    try:
        files = glob.glob(f"**/*{search_name}*", recursive=True)
        if files:
            print("Найденные файлы:")
            for file in files:
                print(file)
        else:
            print(f"Файлы с именем '{search_name}' не найдены.")
    except Exception as e:
        print(f"Ошибка при поиске файлов: {e}")

def list_directory(dir_path):
    try:
        if os.path.exists(dir_path):
            print("Содержимое директории:")
            for item in os.listdir(dir_path):
                print(item)
        else:
            print(f"Директория {dir_path} не найдена.")
    except Exception as e:
        print(f"Ошибка при раскрытии директории: {e}")

def create_file_or_folder(path):
    try:
        if path.endswith(("/", "\\")):
            os.makedirs(path, exist_ok=True)
            print(f"Папка {path} успешно создана.")
        else:
            with open(path, 'w') as file:
                file.write('')
            print(f"Файл {path} успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании: {e}")

def delete_file_or_folder(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Папка {path} успешно удалена.")
        elif os.path.isfile(path):
            os.remove(path)
            print(f"Файл {path} успешно удалён.")
        else:
            print(f"{path} не найден.")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")

def rename_file_or_folder(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        print(f"{old_path} переименован в {new_path}.")
    except Exception as e:
        print(f"Ошибка при переименовании: {e}")

def copy_file_or_folder(source, destination):
    try:
        if os.path.isdir(source):
            shutil.copytree(source, destination)
            print(f"Папка {source} успешно скопирована в {destination}.")
        elif os.path.isfile(source):
            shutil.copy2(source, destination)
            print(f"Файл {source} успешно скопирован в {destination}.")
        else:
            print(f"{source} не найден.")
    except Exception as e:
        print(f"Ошибка при копировании: {e}")

def move_file_or_folder(source, destination):
    try:
        shutil.move(source, destination)
        print(f"{source} успешно перемещён в {destination}.")
    except Exception as e:
        print(f"Ошибка при перемещении: {e}")

def main():
    while True:
        print("\nФайловый менеджер:")
        print("1 - Открыть файл")
        print("2 - Показать содержимое файла")
        print("3 - Найти файл/файлы")
        print("4 - Раскрыть директорию")
        print("5 - Создать файл/папку")
        print("6 - Удалить файл/папку")
        print("7 - Переименовать файл/папку")
        print("8 - Копировать файл/папку")
        print("9 - Переместить файл/папку")
        print("0 - Выход")

        choice = input("Введите номер операции: ").strip()

        if choice == '1':
            path = input("Введите путь к файлу: ").strip()
            open_file(path)
        elif choice == '2':
            path = input("Введите путь к файлу: ").strip()
            show_file_content(path)
        elif choice == '3':
            name = input("Введите имя файла или его часть: ").strip()find_files(name)
        elif choice == '4':
            path = input("Введите путь к директории: ").strip()
            list_directory(path)
        elif choice == '5':
            path = input("Введите путь и имя для создания: ").strip()
            create_file_or_folder(path)
        elif choice == '6':
            path = input("Введите путь к файлу/папке для удаления: ").strip()
            delete_file_or_folder(path)
        elif choice == '7':
            old_path = input("Введите текущий путь к файлу/папке: ").strip()
            new_path = input("Введите новый путь: ").strip()
            rename_file_or_folder(old_path, new_path)
        elif choice == '8':
            source = input("Введите путь к файлу/папке для копирования: ").strip()
            destination = input("Введите новый путь для копирования: ").strip()
            copy_file_or_folder(source, destination)
        elif choice == '9':
            source = input("Введите путь к файлу/папке для перемещения: ").strip()
            destination = input("Введите новый путь для перемещения: ").strip()
            move_file_or_folder(source, destination)
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

    input("Press Enter to exit...")

if name == "__main__":
    main()