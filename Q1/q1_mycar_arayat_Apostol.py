#Car Game
class Car:
    def __init__(self, brand, model, battery=33):
        self.brand = brand
        self.model = model
        self.battery = battery
    def go(self, distance):
        s = distance/25
        self.battery -= s
        print("You have traveled", distance, "km.")
        print("Your",self.brand, self.model, "has", self.battery, "wH left.")
    def charge(self, wH):
        self.battery += wH
        print("Your",self.brand, self.model, "has", self.battery, "wH left.")

brand = input("What is the brand of your car?: ")
model = input("What is the model of your car?: ")
total_distance = 0
myCar = Car(brand, model)
while myCar.battery > 0:
    command = input("What do you want to do? (go, charge): ")
    if command == "go":
        distance = int(input("How far (km)?: "))
        myCar.go(distance)
        total_distance += distance
    elif command == "charge":
        wH = int(input("How much (wH)?: "))
        myCar.charge(battery)
    else:
         print("Invalid command.")
print(f"Your car ran out of battery!\nYou traveled a total of {total_distance} km.")
















