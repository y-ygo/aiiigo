#Car Game
class Car:
    def __init__(self, brand, model, battery=33):
        self.brand = brand
        self.model = model
        self.battery = battery
    def go(self, distance):
        s = distance/25
        self.baterry -= s
        print("You have traveled", distance, "km.")
        print("You have", self.battery, "wH left".)
    def charge(self, wH):
        self.battery += wH
        print("You charged", self.battery, "wH l\left")

myCar = Car("BYD", "Seal 5")
myCar.go(100)
myCar.charge(1)
















