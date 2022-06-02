class Weapons:
  def __init__(self, type, color):
    self.type = type
    self.color = color

class Swords(Weapons):
  def __init__(self, type, attack, price):
    self.type = type
    self.attack = attack
    self.price = price

swords = [Swords("Diamond", 6, 89), Swords("Gold", 4, 102), Swords("Netherite", 8, 250), Swords("Iron", 2, 56) ]

class Arrows(Weapons):
  def __init__(self, type, price):
    self.type = type
    self.price = price

arrows = [Arrows("Night Vision", 23), Arrows("Fire Resitance", 50), Arrows("Strength", 70), Arrows("Invisibility", 104)]

intro = input("Welcome dear customer would you like to see my wares ")
if intro == "yes":
  print("These are the items that we have:")
  print("1. Weapons")
  print("2. Armor")
  print("___________________________________")
user = input("What does your cavalrly require ")
if user == "1":
  print("1. Swords")
  print("2. Arrows")
  critic = input("What would you like to explore? ")
  print("___________________________________")
  
if critic == "1":
  print("1. Iron, 2, 56")
  print("2. Diamond, 6, 89")
  print("3. Gold, 4, 102")
  print("4. Netherite, 8, 250")
  user2 = input("What weapon would you like to buy ")
  print("___________________________________")

  if user2 == "1":
    print("My iron is the finest in the land")
    print("These are the items that we have:")
    print("1. Weapons")
    print("2. Armor")
    print("___________________________________")

  if user2 == "2":
    print("A valuable choice")
    print("These are the items that we have:")
    print("1. Weapons")
    print("2. Armor")
    print("___________________________________")
  
  if user2 == "3":
    print("Looking for glory are we")
    print("These are the items that we have:")
    print("1. Weapons")
    print("2. Armor")
    print("___________________________________")
  
  if user2 == "4":
    print("Go big or go home, I agree")
    print("These are the items that we have:")
    print("1. Weapons")
    print("2. Armor")
    print("___________________________________")


if critic == "2":
  print("My arrows can pierce through 5 feet of netherite")
  print("1. Night Vision , 23")
  print("2. Fire Resistance , 50")
  print("3. Strength , 70")
  print("4. Invisibility , 104")
  cho = input("Which arrow do you require")
  print("___________________________________")
  
if cho == "1":
  print("May your nightly foes be conqured")
  print("___________________________________")

if cho == "2":
  print("Dealing with fire, well this is going to save your life")
  print("___________________________________")


if cho == "3":
  print("Oooh, very interesting")
  print("___________________________________")

if cho == "4":
  print("Now that is some confidence")
  print("___________________________________")
  
  
  
  
  
  