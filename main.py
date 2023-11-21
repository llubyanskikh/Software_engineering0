class Tomato:
    # Статическое свойство states, содержащее все стадии созревания помидора
    states = ["отсутствует", "цветение", "зеленый", "красный"]

    def __init__(self, index):
        # Динамическое свойство _index, переданное параметром
        self._index = index
        # Динамическое свойство _state, принимает первое значение из словаря states
        self._state = self.states[0]

    def grow(self):
        # Метод перевода томата на следующую стадию созревания
        if self._state != self.states[-1]:
            current_index = self.states.index(self._state)
            self._state = self.states[current_index + 1]

    def is_ripe(self):
        # Метод проверки зрелости томата
        return self._state == self.states[-1]


class TomatoBush:
    def __init__(self, num_tomatoes):
        # Динамическое свойство tomatoes, содержащее список объектов класса Tomato
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        # Метод перевода всех томатов на следующий этап созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Метод проверки, все ли томаты из списка стали спелыми
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Метод очистки списка томатов после сбора урожая
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        # Динамическое свойство name, переданное параметром, является публичным
        self.name = name
        # Динамическое свойство _plant, принимает объект класса TomatoBush
        self._plant = plant

    def work(self):
        # Метод, заставляющий садовника работать, что позволяет растению становиться более зрелым
        self._plant.grow_all()

    def harvest(self):
        # Метод проверки зрелости всех плодов и сбора урожая
        if self._plant.all_are_ripe():
            print(f"{self.name} собрал урожай!")
            self._plant.give_away_all()
        else:
            print("Плоды еще не все созрели. Подождите немного.")

    @staticmethod
    def knowledge_base():
        # Статический метод вывода справки по садоводству
        print("Садоводство - это искусство выращивания растений в саду.")

# Вызов справки по садоводству
Gardener.knowledge_base()

# Создание объектов классов TomatoBush и Gardener
tomato_bush = TomatoBush(num_tomatoes=5)
gardener = Gardener(name="John", plant=tomato_bush)

# Уход за кустом с помидорами
gardener.work()  # Растение становится более зрелым

# Попытка собрать урожай, когда томаты еще не дозрели
gardener.harvest()  # Плоды еще не все созрели. Подождите немного.

# Продолжение ухода за растением
gardener.work()  # Растение становится еще более зрелым
gardener.work()  # Растение становится еще более зрелым

# Попытка снова собрать урожай
gardener.harvest()  # John собрал урожай!