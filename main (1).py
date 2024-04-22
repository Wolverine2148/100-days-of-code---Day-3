print('''
  *******************************************************************************
            |                   |                  |                     |
   _________|________________.=""_;=.______________|_____________________|_______
  |                   |  ,-"_,=""     `"=.|                  |
  |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
   _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
  |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
  |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
   _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
  |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
  |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
  ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
  /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
  ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
  /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
  /______/______/______/______/______/______/______/______/______/______/[TomekK]
  *******************************************************************************
''')
print("Welcome to treasure island")
c1 = input("You are at a crossroad. Do you wish to go Left or Right? ")
c1_low = c1.lower()
if c1.lower() == "left":
  c2 = input("You have arrived unharmed at the docks. " +
  "You can either wait for the boat to arrive or you can swim to the island. " +
  "Do you want to wait or swim? ").lower()
  if c2.lower() == "wait":
    print("You have rowed the boat safely to the island. "
      "Now you see three doors in front of you, Red, Green, and Blue.")
    c3 = input("Which door do you wish to go through? ").lower()
    if c3.lower() == "blue":
      print("Congrats, you've found the treasure! "
        "Now it's just a matter of what to do with it...")
    elif c3.lower() == "green":
      print("Uh oh! You walked into the chamber of secrets! "
        "You have been instantly killed by the Basilisk!")
    else:
      print("Uh oh! You have been killed by an army of goblins!")
  else:
    print("You tried swimming to the island, but "
      "drowned after being hit by a huge wave.")
else:
  print("You go to the right, but the bridge you are walking on is very old and "
    "it falls apart as you walk, plunging you to your death.")
