class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        return 'Air start now!'        


    def fly(self):
        self.odometer += 100
        return f"{self.make}{self.model} is flying now {self.odometer}km during the flying {self.max_speed}km/h"
        # не хочет работать через vscode, выдает на 17 строке синтаксическую ошибку, через терминал все работает нормально

       
    def land(self):
        self.is_flying = False
        return 'Air is over!'


air = Airplane('Boieng', '707', '2003', '2000')
print(air.take_off())
print(air.fly())
print(air.fly())
print(air.land())


