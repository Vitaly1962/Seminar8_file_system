
def print_file():
    file_number = int(input("Выберите файл (1 или 2): "))
    with open(f'db/data_{file_number}.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            data = line.split(';')
            print(';'.join(str(item) for item in data))
