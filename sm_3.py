def add_two_numbers():
    try:
        user_input = input("Ââåäèòå ÷èñëî: ")
        number = float(user_input)
        result = 2 + number
        print(f"Ðåçóëüòàò ñëîæåíèÿ 2 è {number}: {result}")
    except ValueError:
        print("Îøèáêà: Íåïîäõîäÿùèé òèï äàííûõ. Îæèäàëîñü ÷èñëî.")

# Òåñò 1: ââîä êîððåêòíîãî ÷èñëà
add_two_numbers()

# Òåñò 2: ââîä ñòðîêè
add_two_numbers()

# Òåñò 3: ââîä äðóãîãî íåïîäõîäÿùåãî òèïà äàííûõ
add_two_numbers()
