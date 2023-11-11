def is_palindrome(word):
    word = word.lower()

    characters = list(word)

    characters = [char for char in characters if char != ' ']

    return characters == characters[::-1]

user_word = input("Введите слово: ")

if is_palindrome(user_word):
    print(f"{user_word} - это палиндром!")
else:
    print(f"{user_word} - это не палиндром.")