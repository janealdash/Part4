# 3)Car
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”

length = int(input('enter distance: '))
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0
        self.fuel = 70


    def desc(self):
        return ('{} {} {}'.format(self.make,self.model,self.year))

# принимает расстояние в км
    def drive(self):
        return self.odometer 
           
#  добавляет километры к значению одометра          
    def __substract_fuel(self):
        km = self.odometer + length
        print('Distance: {}km'. format(km))


    def __add_distance(self):
        benz = length / 10
        benz1 = self.fuel - benz
        if benz1 < 0:
            print ('Need more fuel, please, fill more')
        else:
            print('you have: ', benz1)
      
        
auto = Car('Lexus', 'rx360', 2015)
print(auto.desc())
auto.drive()
auto._Car__subtract_fuel()
auto._Car__add_distance()

