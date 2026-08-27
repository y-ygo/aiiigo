class Hero:
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp
    def take_damage(self, amount):
        self.hp -= amount
Arthur = Hero("Arthur")
Morgana = Hero("Morgana")

Arthur.take_damage(10)

print(f"{Arthur.name} HP: {Arthur.hp}.")
print(f"{Morgana.name} HP: {Morgana.hp}.")
