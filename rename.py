import os
import re
from unidecode import unidecode

def correct_file_name(src: str) -> str:
    """Применяет правила переименования к имени файла."""
    # Преобразуем текст в нижний регистр и транслитерируем
    str_transliterated = unidecode(src.lower())
    # Заменяем все символы, кроме латинских букв, цифр, точки и дефиса, на "_"
    str_cleaned = re.sub(r"[^a-z0-9.\-]+", "_", str_transliterated)
    return str_cleaned

def rename_files_in_current_directory():
    """Переименовывает все файлы в текущей директории по правилам."""
    current_directory = os.getcwd()  # Получаем текущую директорию
    print(f"Working in directory: {current_directory}")

    for file_name in os.listdir(current_directory):
        if os.path.isfile(file_name):  # Проверяем, что это файл, а не папка
            new_file_name = correct_file_name(file_name)
            if new_file_name != file_name:
                # Временное имя для обработки ситуации с регистром
                temp_name = f"{new_file_name}.temp"
                old_path = os.path.join(current_directory, file_name)
                temp_path = os.path.join(current_directory, temp_name)
                new_path = os.path.join(current_directory, new_file_name)

                # Переименование в промежуточное имя, чтобы обойти чувствительность к регистру
                os.rename(old_path, temp_path)
                # Переименование в окончательное имя
                if not os.path.exists(new_path):
                    os.rename(temp_path, new_path)
                    print(f"Renamed: {file_name} -> {new_file_name}")
                else:
                    print(f"File {new_file_name} already exists. Skipping.")
    print("Renaming completed.")

if __name__ == "__main__":
    rename_files_in_current_directory()
