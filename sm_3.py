def count_most_common_numbers(input_string):
    # Проверяем, что длина строки не менее 15 символов
    if len(input_string) < 15:
        return "Строка должна содержать как минимум 15 символов."

    # Создаем словарь для подсчета частоты встречаемости каждой цифры
    count_dict = {}
    for digit in input_string:
        count_dict[digit] = count_dict.get(digit, 0) + 1

    # Сортируем словарь по убыванию значений
    sorted_counts = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    # Отбираем три самых часто встречаемых числа
    top_three = sorted_counts[:3]

    # Создаем словарь из топ-тройки
    result_dict = dict(top_three)

    return result_dict

# Пример использования
input_sequence = "876598745612345"
result = count_most_common_numbers(input_sequence)

print("Самые часто встречаемые числа в порядке возрастания ключа:")
for key in sorted(result.keys()):
    print(f"{key}: {result[key]} раз")