x = input(" Enter your birth year: ")

while True:
  if x < 1900:
    print("\n Invalid Year, it should not be earlier than 1800")
  elif x % 12 == 0:
    print("\n Your Chinese Zodiac Sign is : Rat (鼠 / Shǔ)")
    break
  elif x % 12 == 1:
    print:("\n Your Chinese Zodiac Sign is : Ox (牛 / Niú)")
    break
  elif x % 12 == 2:
    print(" Your Chinese Zodiac Sign is : Tiger (虎 / Hǔ)")
    break
  elif x % 12 == 3:
    print(" Your Chinese Zodiac Sign is : Rabbit (兔 / Tù)")
    break
  #x%12==4
