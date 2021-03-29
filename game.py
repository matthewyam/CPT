import winsound

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
print("=============")
print("|   Music   |")
print("=============")


print("")
actions = input("What would you like to do? ").lower()


if actions == "rules":
    print("")
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
    print("")
    print("")
    print("Enemy Info")
    print("")
    print("Hacka Nub: This hacker is a beginner and just started learning to DDOS")
    print("HP:2 Atk:2")
    print("")
    print("Hacka Nub+")
    print("HP:5 Atk:3")
    print("")
    gostart = input("Ready to start?(Yes or Yes) ").lower()

if actions == "music":
    print("None (Default)")
    print("Candyland")
    print("Meme")
    mosic = input("You choose: ").lower()

    if mosic == "none":
        mstart = input("Ready to start? (Yes or Yes): ").lower

    if mosic == "candyland":
        import winsound
        winsound.PlaySound("Candyland.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
        mstart = input("Ready to start? (Yes or Yes): ").lower

    if mosic == "meme":
        import winsound
        winsound.PlaySound("meme.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
        mstart = input("Ready to start? (Yes or Yes): ").lower



if actions or gostart or mstart =="play" or "yes":
    print("")
    cont = input("Press space and enter to continue")
    if cont == u"\u0020":
        print("")
        print("macOS")
        print("")
        print("Windows")
        print("")
        print("Linux")
        print("")
        system = input("Choose an Operating System: ").lower()
        
        if system == "windows":
            print("")
            print("You have chosen Windows")
            cont1 = input("Press space and enter to continue")
            if cont1 == u"\u0020":
                print("")
                print("In the deepest darkest part of the web, the most dangerous place, there lies hackers.  You have been hired by the FBI to take them out.  You will have to fight back against their viruses and counterattack with you own")
                cont1 = input("Press space and enter to continue")
                if cont1 == u"\u0020":
                    print("")
                    print("A wild Hacka Nub has appeared")
                    cont1 == ("Press space and enter to continue")
                    if cont1 == u"\u0020":
                        print("")
                        

                        uhp = 5
                        end1 = 0    
                        hp1 = 2
                        hhp1 = 0
                        hp2 = 5

                        while hp1 != hhp1:
                                
                            while uhp != end1:

                                print("Attack")
                                print("Defend")
                                action = input("Choose an action: ").lower()
                            
                                if action == "defend":
                                    print("VPN (Use a VPN to mask your IP and trick the hacker)")
                                    print("Anitvirus (Uses McAfee to block hacker attacks)")
                                    defence = input("You choose: ").lower()
                                 
                                    if defence == "vpn":
                                    
                                        print("You have successfully evaded the hacker's DDOS")
                                        print("")
                                        print("Attack")
                                        print("Defend")

                                    if defence == "antivirus":
                                        uhp = uhp - 1
                                        print("")
                                        print("McAfee is utterly useless, allowing the Hacker to DOS you. You have lost 1 hp")
                                        print("Your current HP: "+str(uhp))
                                        cont1 = input("Press space and enter to continue")
                                        print("")
                                    
                                if action == "attack":
                                    print("")
                                    print("Ransomeware (Encrypt all the hacker's files **Super effective against Hacka nub**)")
                                    print("Trojan (Sends a Trojan to the hacker)")
                                    attack = input("You choose: ").lower()
                                    
                                    
                                    if attack == "ransomeware":
                                        hp1 = hp1 - 5
                                        print("You have encrypted all the hacker's files and he refuses to pays")
                                        print("")
                                        
                                      
                                      
                                    if attack =="trojan":
                                        hp1 = hp1 - 5
                                        print("You have inflitrated the hacker's computer and deleted all his files")
                                        print("")
                                        
                                    print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKA NUB ***")
                                    print("The FBI have swatted him and is now arrested")
                                    print("")
                                    print("HP fully restored")


                                print("Game Over")


                            



        
        if system == "linux":
            print("")
            print("You have chosen Linux")
            cont2 = input("Press space and enter to continue")
            if cont2 == u"\u0020":
               print("A")


        if system == "macos":
            print("")
            print("You have chosen macOS")
            cont3 = input("Press space and enter to continue")
            if cont3 == u"\u0020":
                print("")
                print("In the deepest darkest part of the web, the most dangerous place, there lies hackers.  You have been hired by the FBI to take them out.  You will have to fight back against their viruses and counterattack with you own")
                cont3 = input("Press space and enter to continue")
                if cont3 == u"\u0020":
                    print("")
                    print("A wild Hacka Nub has appeared")
                    cont3 == ("Press space and enter to continue")
                    if cont3 == u"\u0020":
                        print("")
                        print("Attack")
                        print("Defend")
                        action = input("Choose an action: ").lower()

                        if action or fightmenu == "attack":
                            print("")
                            print("Ransomeware (Encrypt all the hacker's files **Super effective against Hacka nub**)")
                            print("Trojan (Sends a Trojan to the hacker)")
                            attack = input("You choose: ").lower()

                            if attack == "ransomeware":
                                print("You have encrypted all the hacker's files and he refuses to pays")
                                print("")
                                print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKA NUB ***")
                                print("")

                            if attack =="trojan":
                                print("You have inflitrated the hacker's computer and deleted all his files")
                                print("")
                                print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKA NUB ***")

                        if action or fightmenu == "defend":
                            print("Firewall (Apple Firewall has blocked the hacker")
                            print("Apple Care (Apple Care removes the virus at the genius bar.)")
                            defence = input("You choose: ").lower()
                            
                            if defence == "vpn":
                                print("You have successfully evaded the hacker's DDOS")
                                print("")
                                print("Attack")
                                print("Defend")
                                fightmenu = input("What would you like to do: ").lower

                            if defence == "antivirus":
                                print("McAfee is utterly useless, allowing the Hacker to DOS you. You have lost 3 hp")
                                cont1 = input("Press space and enter to continue")
                                fightmenu = input("What would you like to do: ").lower
                                
                                if cont1 == u"\u0020":
                                    print("")
                                    print("Attack")
                                    print("Defend")
                                    action = input("Choose an action: ").lower()
                
