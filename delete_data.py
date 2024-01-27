from return_data_file import data_file

def delete_row():
    data, nf = data_file()
    count_rows = len(data)

    if count_rows == 0:
        print("Файл пуст!")
    else:
        number_row = int(input(f"Введите номер строки от 1 до {count_rows}: "))

        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка! Введите номер строки от 1 до {count_rows}: "))

        # Проверяем, что введенный номер строки не выходит за границы списка
        if 0 <= number_row - 1 < len(data):
            del data[number_row - 1]

            # Пересоздаем файл с обновленными строками
            with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
                file.writelines(data)

            print("Строка успешно удалена!")
        else:
            print("Некорректный номер строки!")
