# -*- coding: windows-1251 -*-
def add_two_numbers():
    try:
        user_input = input("������� �����: ")
        number = float(user_input)
        result = 2 + number
        print(f"��������� �������� 2 � {number}: {result}")
    except ValueError:
        print("������: ������������ ��� ������. ��������� �����.")

# ���� 1: ���� ����������� �����
add_two_numbers()

# ���� 2: ���� ������
add_two_numbers()

# ���� 3: ���� ������� ������������� ���� ������
add_two_numbers()