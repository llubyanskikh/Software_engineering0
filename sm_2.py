def read_file(sm2):
    try:
        with open(sm2, 'r') as file:
            read_file = file.read()
            if not read_file:
                raise Exception("Ôàéë ïóñòîé")
            else:
                print("Ñîäåðæèìîå ôàéëà:")
                print(read_file)
    except FileNotFoundError:
        print(f"Ôàéë {sm2} íå íàéäåí")
    except Exception as e:
        print(f"Îøèáêà: {e}")

read_file('sm2.txt')

