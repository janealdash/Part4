# 2)Airplane
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекAта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.

class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometr = 0
        self.is_flying = False

    def description(self):
        air = self.make + ' ' + self.model + ' ' + str(self.year) + ' ' + str(self.max_speed) + ' ' + str(self.odometr) + ' ' + str(self.is_flying)
        return air.title()

    def flyed(self):
        if self.odometr > 0:
            print("This airplane fly " + str(self.odometr) + " km.")
        else:
            print('Airplane stayed')
    

    def fly(self):
        if self.odometr > 0:
            self.is_flying = True
            print('Airplane is flying')
        else:
            self.odometr = 0
            self.is_flying = False
            print('Airplane is not flying')

new_air = Airplane('Aeroflot', 'Airbus', 2018, 8000)
print(new_air.description())
new_air.odometr = 0
new_air.flyed()
new_air.fly()
    

