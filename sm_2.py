class Violin: ## создаём класс Скрипка
    def __init__(self, size, model, color, country): ##передаём объекты класса размер, модель, цвет, страна. Self - специальный параметр, который передается первым аргументом в метод класса и представляет собой ссылку на экземпляр класса. Метод init отвечает за инициализацию экземпляров класса,
        self.size = size ##устанавливает атрибут размер текущего объекта класса Скрикпи в значение размер(size), переданное в __init__.
        self.model = model
        self.color = color
        self.country = country

    def buy(self):#определяем функцию buy
        print(f"Buy a {self.size} {self.model} {self.color} violin from {self.country}")

my_violin = Violin("4/4", "Yamaha V3-SKA", "mahogany", "Japan")#передаём значения атрибутов
my_violin.buy()


