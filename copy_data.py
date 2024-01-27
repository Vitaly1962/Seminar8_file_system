def copy_data(source_file, destination_file, row_number):
    # Открываем файлы для чтения и записи
    with open(source_file, 'r', encoding='utf-8') as source:
        with open(destination_file, 'a',encoding='utf-8') as destination:
            # Считываем все строки из исходного файла
            lines = source.readlines()
            # Проверяем, что введенный номер строки существует
            if row_number < 1 or row_number > len(lines):
                print("Некорректный номер строки")
                return
            # Копируем указанную строку в конец файла назначения
            destination.write(lines[row_number - 1])
    print("Строка успешно скопирована")
