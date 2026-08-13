x = input(" Enter your birth year: ")

while True:
  if x < 1900:
    print("\n Invalid Year, it should not be earlier than 1800")
  elif x % 12 == 0:
    print("\n Your Chinese Zodiac Sign is : 
