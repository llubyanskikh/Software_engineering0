import json

def add_expense(expenses, category, amount):
    if category in expenses:
        expenses[category].append(amount)
    else:
        expenses[category] = [amount]

def save_expenses(expenses, file_name):
    with open(file_name, 'w') as file:
        json.dump(expenses, file)

def load_expenses(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def display_expenses(expenses):
    if not expenses:
        print("Нет сохраненных расходов.")
        return

    print("Существующие данные о расходах:")
    for category, amounts in expenses.items():
        total_amount = sum(amounts)
        print(f"{category}: {total_amount}")

def main():
    file_name = 'expenses.json'
    expenses = load_expenses(file_name)

    while True:
        print("\n1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Выход")

        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            category = input("Введите категорию расхода: ")
            amount = float(input("Введите сумму расхода: "))
            add_expense(expenses, category, amount)
            save_expenses(expenses, file_name)
            print("Расход добавлен.")

        elif choice == '2':
            display_expenses(expenses)

        elif choice == '3':
            print("Программа завершена.")
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()