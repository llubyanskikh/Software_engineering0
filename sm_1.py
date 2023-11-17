from collections import Counter
import re


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words)


def find_most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)
    return most_common_word[0][0] if most_common_word else None


def main():
    file_path = 'input.txt' 
    article_content = read_file(file_path)

    word_count = count_words(article_content)
    most_common_word = find_most_common_word(article_content)

    print(f"Количество слов в статье: {word_count}")
    print(f"Самое часто встречающееся слово: {most_common_word}")


if __name__ == "__main__":
    main()
