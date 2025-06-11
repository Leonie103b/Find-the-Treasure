print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.")

equip = "nothing"

action = input("Which direction would like to go? left or right? ")

if action == "left":
    action =input("You enter in a fire room, what will you pick near you, the knife, the cat? ")
    if action == "knife":
        print("You break the window and escape.")
        equip = "knife"
        action = input("Now you walk to the river and want to cross it, what will you do? swim or wait")
        if action == "swim" and equip == "knife":
                print(f"You kill the crocodiles with {equip} and survival. \nA boat comes and drives you to the other side of the river.")
                action = input("A treasure box occurs in front of you.Do you hold the key? y or n")
                if action == "y" and equip == "key":
                        print("you open the box and get the treasure.")
                else:
                        print("you don't open the box and back home without anything.")
        else:
                print("You are die of hungry.")

    else:
        print("You and the cat died in the fired room.")



elif action =="right":
        action =input("You meet a fox who takes you home and share you some food, which would like to eat? \n currywurst, cake?")
        if action == "cake":
            
            print("the fox rewards you a key.")
            equip = "key"
            action = input("A treasure box occurs in front of you.Do you hold the key? y or n")
            if action == "y" and equip == "key":
                print("you open the box and get the treasure.")

            elif action == "y" and equip != "key":
                print("You a liar and killed by the fox.")

            else:
                print("you don't open the box and back home without anything.")

        else:
            print("You are died of salty food.")

else:
    print("You type the wrong word and died.")

number_pick = int(input("The fox would like to play the game <high card> with you. \nChoose a number from 0 to 9: ")
fox_number = 0
for fox_number in range(0,10)
    if fox_number > number_pick:
         print("You lose the game.")
    elif fox_number = number_pick:
         equip = "flower"
         print("You reward a flower.")
    else:
         equip = "key"
         print("The fox reward you a key)
