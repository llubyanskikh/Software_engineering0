# -*- coding: windows-1251 -*-
def read_file(sm2):
    try:
        with open(sm2, 'r') as file:
            read_file = file.read()
            if not read_file:
                raise Exception("���� ������")
            else:
                print("���������� �����:")
                print(read_file)
    except FileNotFoundError:
        print(f"���� {sm2} �� ������")
    except Exception as e:
        print(f"������: {e}")

read_file('sm2.txt')

