name = input('Type your name:')
print("Welcome ", name, "to this adventure")
answer = input("You are on the dirt road,it has come to an end you can go left or right.Which way you would like to "
               "go? ").lower()

if answer == 'left':
    answer = input("You come to a river ,you can walk around it or swim across?Type walk to walk around and swim to "
                   "swim across:").lower()
    if answer == 'swim':
        print("You swim across and eaten by a crocodile.")
    elif answer == 'walk':
        print("You walked for many miles,ran out of water and you lost the game. ")
    else:
        print("Not a valid option.You loose.")

elif answer == 'right':
    answer = input(
        "You landed in the middle of dense forest,you can wait someone to come and rescue you or you can climb tree "
        "to navigate near about area ").lower()
    if answer == "wait":
        print("You died without food and water in the middle of forest")
    elif answer == "climb":
        print("There is one village far ,may be some miles far...you walked and rescued from dense jungle")
    else:
        print("Not a valid option.You loose.")


else:
    print("Not a valid option.You loose.")

print("Thank you for trying", name)
