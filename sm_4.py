import time

# Создаем класс декоратора
class CallInfoDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Запоминаем текущее время
        start_time = time.time()

        # Вызываем функцию и сохраняем ее результат
        result = self.func(*args, **kwargs)

        # Вычисляем время выполнения функции
        execution_time = time.time() - start_time

        # Выводим информацию о вызове функции
        print(f"Функция {self.func.__name__} была вызвана с аргументами {args} и ключевыми аргументами {kwargs}")
        print(f"Время выполнения функции: {execution_time} секунд\n")

        # Возвращаем результат функции
        return result

# Определяем две функции, к которым будем применять декоратор
@CallInfoDecorator
def multiply(x, y):
    return x * y

@CallInfoDecorator
def greet(name):
    return f"Привет, {name}!"

# Тестируем работу декоратора
result = multiply(5, 7)
print(result)  # Выведет: 35

result = greet("Вася")
print(result)  # Выведет: Привет, Вася!