class Glassware:
  def __init__(self, name="Beaker Name"):
    self.name = name

class Beaker(Glassware):
  pass

class Tray:
  def __init__(self):
    self.beakers = []
    for i in range(5):
      self.beakers.append(Beaker())

my_tray = Tray()
print(f"You currently have {len(my_tray.beakers)} beakers.")
