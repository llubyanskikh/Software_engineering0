class MusicalInstrument:
    def cost(self):
        pass

class Violin(MusicalInstrument):
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def cost(self):
        return self.quantity * self.price

class Piano(MusicalInstrument):
    def __init__(self, quantity, price, delivery):
        self.quantity = quantity
        self.price = price
        self.delivery = delivery

    def cost(self):
        return self.quantity * self.price + self.delivery
instruments = [Violin(4, 25600), Piano(1, 48900, 3300)]# создаём массив, помещаем туда круг и прямоугольник
for instrument in instruments:# с помощью цикла for выводим их площади по очереди
    print(instrument.cost())