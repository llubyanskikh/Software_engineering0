def get_statistics(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    letter_count = sum(c.isalpha() and c.isascii() for c in content)
    word_count = len(content.split())
    line_count = content.count('\n') + 1

    return letter_count, word_count, line_count

def main():
    file_path = 'input.txt'

    try:
        letter_count, word_count, line_count = get_statistics(file_path)

        print(f"Input file contains:")
        print(f"{letter_count} letters")
        print(f"{word_count} words")
        print(f"{line_count} lines")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == "__main__":
    main()