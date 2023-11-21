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

class ElectroViolin(Violin):
    def __init__(self, size, model, color, country, battery):
        super().__init__(size, model, color, country)
        self.battery = battery

    def sell(self):
        print(f"Sell an electric violin {self.size} {self.model} {self.color} color from {self.country} with a {self.battery} W")
my_electro_violin = ElectroViolin("3/4", "Yamaha360", "white", "Japan", "1.5")
my_electro_violin.buy()
my_electro_violin.sell()