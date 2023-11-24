class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def example_function(number):
    if number < 0:
        raise CustomException("Неверный ввод. Число должно быть положительным.")
    else:
        return number ** 2


try:
    input_number = int(input("Введите положительное число: "))
    result = example_function(input_number)
    print("Результат:", result)
except CustomException as e:
    print("Ошибка:", e.message)