def get_file_paths():
    source_choice = input("Выберите файл, с которым вы хотите работать (Введите цифру 1 или 2): ")

    # Проверяем введенную цифру
    while source_choice not in {'1', '2'}:
        print("Ошибка! Введите цифру 1 или 2.")
        source_choice = input("Выберите файл, с которым вы хотите работать (Введите цифру 1 или 2): ")

    destination_choice = input("Выберите файл назначения (Введите цифру 1 или 2): ")

    # Проверяем введенную цифру
    while destination_choice not in {'1', '2'}:
        print("Ошибка! Введите цифру 1 или 2.")
        destination_choice = input("Выберите файл назначения (Введите цифру 1 или 2): ")

    # Присваиваем соответствующие файлы в зависимости от выбора пользователя
    source_file = f"db/data_{source_choice}.TXT"
    destination_file = f"db/data_{destination_choice}.TXT"

    return source_file, destination_file

from delete_data import delete_row
from change_data import change_row
from add_data import add_row
from print_data import print_file
from copy_data import copy_data

def check_number(n):
    while n < 1 or n > 6:
        n = int(input("Ошибка, такого номера команды не "
                      "существует! Введите цифру от 1 до 6\n"
                      "Выберите функцию:\n"
                      "1. Добавить\n"
                      "2. Удалить\n"
                      "3. Изменить\n"
                      "4. Вывод\n"
                      "5. Копировать\n"
                      "6. Выход\n"
                      "Введите номер команды: "))
    return n

def start_menu():
    command = None
    while command != 6:
        command = int(input("Доброго времени суток!\n"
                            "Выберите функцию:\n"
                            "1. Добавить\n"
                            "2. Удалить\n"
                            "3. Изменить\n"
                            "4. Вывод\n"
                            "5. Копировать\n"
                            "6. Выход\n"
                            "Введите номер команды: "))
        command = check_number(command)
        if command == 1:
            add_row()
        elif command == 2:
            delete_row()
        elif command == 3:
            change_row()
        elif command == 4:
            print_file()
        elif command == 5:
            # Получите пути к файлам от пользователя
            source_file, destination_file = get_file_paths()

            # Спросите у пользователя номер строки для копирования
            row_number = int(input("Введите номер строки для копирования: "))
            copy_data(source_file, destination_file, row_number)
                
                      
            # copy_data()
    print("Спасибо, что воспользовались нашими услугами!\n"
          "Всего доброго! Приходите к нам ещё :)")
