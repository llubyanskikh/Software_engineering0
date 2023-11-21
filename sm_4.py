class Violin: # создаём класс Скрипка
    def __init__(self, size, model): #передаём объекты класса размер, модель, цвет, страна. Self - специальный параметр, который передается первым аргументом в метод класса и представляет собой ссылку на экземпляр класса. Метод init отвечает за инициализацию экземпляров класса,
        self.__size = size #защищённый атрибут
        self._model = model#приватный атрибут


    def buy(self):#определяем функцию buy
        print(f"Buy a {self.__size} {self._model} violin")

my_violin = Violin("4/4", "Yamaha V3-SKA")#передаём значения атрибутов
print(my_violin._model)
my_violin.buy()
