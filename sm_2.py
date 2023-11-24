def read_file(sm2):
    try:
        with open(sm2, 'r') as file:
            read_file = file.read()
            if not read_file:
                raise Exception("Файл пустой")
            else:
                print("Содержимое файла:")
                print(read_file)
    except FileNotFoundError:
        print(f"Файл {sm2} не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

read_file('sm2.txt')

