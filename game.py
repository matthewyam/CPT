print("")
print("")


print("Welcome to Virus Defender")

print("")
print("")

print("=============")
print("|   PLAY    |")
print("=============")
print("")
print("=============")
print("|   Rules   |")
print("=============")

print("")
action = input("What would you like to do? ").lower()


if action == "rules":
    print("This game is a text based RPG")
    print("You will have to pick a Operating System and answer questions in order to beat the enemy")
    print("")
    print("OS info:")
    print("")
    print("macOS: This class is for all those users who puts all their skill points into defence. It has high defence but low attack")
    print("HP:10 Atk:2")
    print("")
    print("Windows: This class is for your average PC enjoyer. It has balance stats")
    print("HP:5 Atk:5")
    print("")
    print("Linux: This class is for all those people that end friendships with defence. It has high attack and low defence")
    print("HP: 1 Atk: 10")


if action =="play":
    print("")
    print("Welcome to ***")
    cont = input("Press space and enter to continue")
    if cont == u"\u0020":
        print("")
        print("Choose an Operating System")
        print("")
        print("macOS")
        print("")
        print("Windows")
        print("")
        print("Linux")