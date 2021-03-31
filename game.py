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


actions = input("What would you like to do?: ").lower()

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
    print("Hacker Nub: This hacker is a beginner and just started learning to DDOS")
    print("HP:2 Atk:1")
    print("")
    print("Hacker Man")
    print("HP:5 Atk:3")
    print("")
    gostart = input("Ready to start?(Yes or Yes) ").lower()
        
    
if actions == "music":
    print("None (Default)")
    print("Candyland")
    print("Meme")
    print("SASAGEYO")
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
        
    if mosic == "sasageyo":
        import winsound
        winsound.PlaySound("sasageyo.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
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
                    print("A wild Hacker Nub has appeared")
                    cont1 == ("Press space and enter to continue")
                    if cont1 == u"\u0020":
                        print("")
                        
                        #Universal
                        win = 0
                        uhp = 5
                        
                        #boss 1
                        end1 = 0    
                        hp1 = 2
                        hhp1 = 0

                        #Boss 2 
                        hp2 = 5
                        hhp2 = 0
                        end2 = 0

                        #Boss 3
                        hp3 = 10
                        hhp3 = 0
                        end3 = 0

                        #finish
                        done = 0


                        while hp1 != hhp1 and win < 1:
                                
                            while win < 1:

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


                                    if defence == "antivirus":
                                        uhp = uhp - 1
                                        win = win + 0.2
                                        hp1 = hp1 - 0.4

                                        print("")
                                        print("McAfee is utterly useless, allowing the Hacker to DOS you. You have lost 1 hp")
                                        print("Your current HP: "+str(uhp))
                                        cont1 = input("Press space and enter to continue")
                                        print("")
                                    
                                if action == "attack":
                                    print("")
                                    print("Ransomeware (Encrypt all the hacker's files)")
                                    print("Trojan (Sends a Trojan to the hacker)")
                                    attack = input("You choose: ").lower()
                                    
                                    
                                    if attack == "ransomeware":
                                        hp1 = hp1 - 2 
                                        print("You have encrypted all the hacker's files and he refuses to pays")
                                        print("")
                                        
                                        
                                        
                                    if attack =="trojan":
                                        hp1 = hp1 - 2
                                        print("You have inflitrated the hacker's computer and deleted all his files")
                                        print("")
                                        
                                    print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKA NUB ***")
                                    print("The FBI have swatted him and is now arrested")
                                    print("")
                                    print("HP fully restored")
                                    win = win - win + 1
                                    uhp = uhp - uhp + 5



                        if uhp == end1:
                            print("Game Over")
                            exit


                        cont1 = input("Press space and enter to continue")

                        print("")
                        print("You are finally done dealing with the hacker and you are very tired.")
                        print("")
                        cont1 = input("Press space and enter to continue")

                        print("")
                        print("Suddenly you get a phone call saying that there is a hacker trying to break into the FBI system.")
                        print("")
                        cont1 = input("Press space and enter to continue")

                        print("")
                        print("You get out of bed and hop on your computer to take this person out")
                        print("")
                        cont1 = input("Press space and enter to continue")

                        print("** You have learned 4 new skills **")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")

                        print("A wild Hacker Man has appeared")
                        cont1 = input("Press space and enter to continue")
                        print("")

                        while hp2 != hhp2 and win < 2 and hp1 == 0:
                            
                            while win < 2:

                                print("Attack")
                                print("Defend")
                                action1 = input("Choose an action: ").lower()
                            
                                if action1 == "defend":
                                    print("Safe Mode (Use safe mode to stop the hacker from accessing your files)")
                                    print("Factory Reset (Reset you device and lose the hacker)")
                                    defence1 = input("You choose: ").lower()
                                    
                                    if defence1 == "safe mode":
                                    
                                        print("You have successfully bocked the hacker from seeing your files")
                                        print("")

                                    if defence1 == "factory reset":
                                        uhp = uhp - 5
                                        win = win + 1
                                        hp2 = hp2 - 5

                                        print("")
                                        print("You reset your computer to prevent the hacker from stealing any information, but you forgot to back up your data so its now all lost. You lost 5 HP")
                                        print("Your current HP: "+str(uhp))
                                        cont1 = input("Press space and enter to continue")
                                        print("")
                                    
                                if action1 == "attack":
                                    print("")
                                    print("Adware (Spams Ads on the hacker's screen annoying them)")
                                    print("Spyware (Spys on the hacker and steals information)")
                                    attack1 = input("You choose: ").lower()
                                    
                                    
                                    if attack1 == "adware":
                                        hp2 = hp2 - 5
                                        print("You have overloaded the hacker's computer with ads and it is now bricked")
                                        print(hp2)
                                        print("")
                                        
                                        
                                        
                                    if attack1 =="spyware":
                                        hp2 = hp2 - 5
                                        print("You have stolen enough information about him and the FBI have his location ready to be swatted")
                                        print(hp2)
                                        print("")
                                        
                                    print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKER MAN ***")
                                    print("The FBI have swatted him and is now arrested")
                                    print("")
                                    print("HP fully restored")
                                    win = win + 1
                                    uhp = uhp - uhp + 5

                        if uhp == end2:
                            print("Game Over")
                            exit
        
                        print("A wild Hacker Boss has appeared")
                        cont1 == input("Press space and enter to continue")



                        while hp3 != hhp3 and win < 4 and hp2 == 0:
                            
                            while win <4:

                                print("Attack")
                                print("Defend")
                                action = input("Choose an action: ").lower()
                            
                                if action == "defend":
                                    print("Encryption (Encrypt your files)")
                                    print("Cloud (Upload your data to a generic cloud storage)")
                                    defence = input("You choose: ").lower()
                                    
                                    if defence == "encryption":
                                    
                                        print("You have successfully encrypted all your files")
                                        print("")


                                    if defence == "cloud":
                                        uhp = uhp - 1
                                        win = win + 0.2
                                        hp3 = hp3 - 2

                                        print("")
                                        print("Using generic cloud storage allowed the server hosting company to see, leak and sell your information.  You have lost 1 HP")
                                        print("Your current HP: "+str(uhp))
                                        cont1 = input("Press space and enter to continue")
                                        print("")
                                    
                                if action == "attack":
                                    print("")
                                    print("Virus (Use generic virus to attack the hackers's computer")
                                    print("Keylogger (Log the hacker's activity)")
                                    attack = input("You choose: ").lower()
                                    
                                    
                                    if attack == "virus":
                                        hp3 = hp3 - 5 
                                        print("You have sent a virus to the hacker and it is attacking his PC")
                                        print("Hacker HP: "hp3)
                                        print("")
                                        
                                        
                                        
                                    if attack =="keylogger":
                                        hp3 = hp3 - 5
                                        print("You have logged part the hacker's information.")
                                        print("Hacker HP: "hp3)
                                        print("")

                                    win = win + 1
                                    uhp = uhp - uhp + 5


                    if uhp == end3:
                        print("Game Over")
                        exit

                        while done == 1 and win == 3 and hp3 == 0:
                            print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKER ***")
                            print("The FBI have swatted him and is now arrested")
                            print("")
                            print("")
                            print(" _____                             _         _       _   _")                 
                            print("/  __ \                           | |       | |     | | (_)")                
                            print("| /  \/ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___") 
                            print("| |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|")
                            print("| \__/\ (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ ")
                            print("\____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/")
                            print("                   __/ |")                                                  
                            print("                  |___/ ")                                                  

                            print("")









                            

"""

        
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
"""