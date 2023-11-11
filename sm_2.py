def del_from_tuple(tup, element):
    # Проверяем, есть ли элемент в кортеже
    if element in tup:
        # Находим индекс первого появления элемента
        index = tup.index(element)
        # Создаем новый кортеж до элемента и после элемента и склеиваем их
        new_tuple = tup[:index] + tup[index + 1:]
        return new_tuple
    else:
        # Если элемент не найден, возвращаем исходный кортеж
        return tup

# Пример использования
a = input().split()
original_tuple = tuple(a)
b = input()
element_to_remove = tuple(b)

result_tuple = del_from_tuple(a, b)

print(f"Исходный кортеж: {original_tuple}")
print(f"Новый кортеж после удаления {element_to_remove}: {result_tuple}")

