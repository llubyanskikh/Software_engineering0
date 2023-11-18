# Чтение списка запрещенных слов из файла
with open('input.txt', 'r') as file:
    forbidden_words = file.read().split()

# Функция для замены запрещенных слов в предложении
def replace_forbidden_words(sentence, forbidden_words):
    modified_sentence = sentence
    for word in forbidden_words:
        # Замена слова в любом регистре
        modified_sentence = modified_sentence.replace(word, '*' * len(word), -1)
    return modified_sentence

# Предложение для проверки
input_sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"

# Замена запрещенных слов в предложении
result = replace_forbidden_words(input_sentence.lower(), forbidden_words)

# Вывод результата
print(result)