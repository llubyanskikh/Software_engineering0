# -*- coding: windows-1251 -*-
def add_two_numbers():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print(f"Результат сложения 2 и {number}: {result}")
    except ValueError:
        print("Ошибка: Неподходящий тип данных. Ожидалось число.")

# Тест 1: ввод корректного числа
add_two_numbers()

# Тест 2: ввод строки
add_two_numbers()

# Тест 3: ввод другого неподходящего типа данных
add_two_numbers()