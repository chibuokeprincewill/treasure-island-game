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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to brave the odds and find the Ultimate Treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
path1 = input ("I will be your guide, Indiana Ghost. For I myself died trying to find the Ultimate Treasure. My memory is a bit wonky so I won't be of much help but will you fulfill my dream? Type 'Y' or 'N': \n").lower()

if path1 == "y":
  path2 = input ("'Very well.' You reach a crossroad. The left path, dark, narrow and moist, smells of the undead threatening to choke the life out of you. The right path leads to an underground canal where creatures of the deep lurk. Which path do you take? Type 'left' or 'right':\n").lower()
  if path2 == "right":
    path3 = input ("You reach the canal safely and Indiana Ghost informs you that his ghoul sister, Lara Croftdead, will be taking you across the canal with her rickety boat. Do you swim across or wait for Lady Croftdead? Type 'swim' or 'wait':\n").lower()
    if path3 == "swim":
      path4 = input ("You make it across the canal but not without losing a foot and 4 fingers from fighting off sea-wraiths. You approach three doors: a red, black, and white door. You hold the key that opens them all. Which door do you enter? Type 'red', 'black', or 'white':\n").lower()
      if path4 == "red":
        print ("You find the treasure chest and it grants you the power of a million suns. You are now the greatest being in the universe! YOU WON!")
      elif path4 == "black":
        print ("Hurray! You've found a treasure chest. You reach to open it and you get transported to the planet Alabaster where the atmosphere is made of sulphur and you die in seconds. Game Over!")
      elif path4 == "white":
         print("You're in heaven. This doesn't need much of an explanation, does it? Game Over!")
      else:
        print ("That door does not exist. By trying to trick the laws of the cosmos, you are banished from existence. Game Over!")
    else:
      print("You hop in and moments later, a ravenous sea-wraith attacks the boat, seizes you and drains every ounce of your fluids. You died of dehydration before you even had a chance to react. Game Over!")  
  else:
    print("You saunter in and the minions of Azhora, the Goddess of Death, tear you apart limb by limb and enjoy the feast of their lives. If it's any consolation, you were quite tasty. Game Over!")
else:
  print ("Indiana Ghost pulls out a shotgun made of ghost aether and blasts your chest open. You now join him as a co-guide for others to find the treasure. Game Over!")