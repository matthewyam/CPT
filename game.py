'''
Filename: game.py
Description: This program is a text based RPG 
Author:Yam.M
Created On:22/03/2021

'''
import winsound

print("")
print("")

print("Welcome to Hacker Defender")

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
    print("macOS: This class is for all those rich kids that use their parents credit card.  **$10.99 TO UNLOCK**")
    print("HP:999 Atk:999")
    print("")
    print("Windows: This class is for your average PC enjoyer. It has balance stats")
    print("HP:5 Atk:5")
    print("")
    print("Linux: This class is for all those big brian people that don't use an interface. It has high attack and is immune to most attacks")
    print("HP: 1 Atk: 10")
    print("")
    print("")
    print("Enemy Info")
    print("")
    print("Hacker Nub: This hacker is a beginner and just started learning to DDOS")
    print("HP:2")
    print("")
    print("Hacker Man: The more advance hacker and the manager of the hacker nub")
    print("HP:5")
    print("")
    print("Hacker Boss: The big boss of the hacker trio")
    print("HP: 10")
    print("")
    gostart = input("Ready to choose Music? (Yes or Yes) ").lower()
        
    
if actions or gostart == "music" or "yes":
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
        
    
    

if actions or gostart or mstart =="play" or "start":
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
    
        #Windows

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
                                        
                                    print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKER NUB ***")
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
                                    
                                        print("You have successfully blocked the hacker from seeing your files")
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
                                        print("")
                                        
                                        
                                        
                                    if attack1 =="spyware":
                                        hp2 = hp2 - 5
                                        print("You have stolen enough information about him and the FBI have his location ready to be swatted")
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
        

                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("You collaps the bed wasted after spending 8 hours taking out two hackers.")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("You roll around the bed for a few minutes fully prepared to sleep when suddenly an alarm goes off.")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("You roll across the bed and realize that it was 8 AM and you have worked throughout the night.  You have work in half an hour")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("You get a phone call from your boss and he informes you that there was a very experienced hacker and if you take him out, you can take ther day off. ")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("*** You have learned 4 new skills ***")
                        

                        print("A wild Hacker Boss has appeared")
                        cont1 == input("Press space and enter to continue")



                        while hp3 != hhp3 and win < 3 and hp2 == 0:
                            
                            while win <3:

                                print("")
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
                                        print("Hacker HP: ",hp3)
                                        print("")
                                        
                                        
                                        
                                    if attack =="keylogger":
                                        hp3 = hp3 - 5
                                        print("You have logged part the hacker's information.")
                                        print("Hacker HP: ",hp3)
                                        print("")

                                    win = win + 0.5
                                    uhp = uhp - uhp + 5
                                    done = done + 0.5


                        if uhp == end3:
                            print("Game Over")
                            exit

                        if done == 1 and win == 3 and hp3 == 0:
                            print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKER ***")
                            print("The FBI have swatted him and is now arrested")
                            print("")
                            print("You have take out all three hackers and now you have the day off.  You sit back and relax knowing the community is now a bit safer.")
                            print("")
                            print(" _____                             _         _       _   _")                 
                            print("/  __ \                           | |       | |     | | (_)")                
                            print("| /  \/ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___") 
                            print("| |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|")
                            print("| \__/\ (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ ")
                            print(" \____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/")
                            print("                   __/ |")                                                  
                            print("                  |___/ ")                                                  

                            print("")
                            exit



        #Linux

        if system == "linux":
            print("")
            print("You have chosen Linux")
            cont2 = input("Press space and enter to continue")
            if cont2 == u"\u0020":
                print("")
                print("In the deepest darkest part of the web, the most dangerous place, there lies hackers.  You are a freelance programmer and you have noticed that someone is taking your code and is passing it at your own.  After digging, you notice that it is a group of hackers that are making lots of money off your work.  The more you read into this the more angrier you get until you noticed that there is a backdoor in their system.  It is now time for your revenge")
                cont1 = input("Press space and enter to continue")
                if cont1 == u"\u0020":
                    print("")
                    print("A wild Hacker Nub has appeared")
                    cont1 == ("Press space and enter to continue")
                    if cont1 == u"\u0020":
                        print("")
                        
                        #Universal
                        win = 0
                        uhp = 10
                        
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
                                    print("Immunity (Use a VPN to mask your IP and trick the hacker)")
                                    defence = input("You choose: ").lower()
                                    
                                    if defence == "immunity":
                                    
                                        print("Immune to all attacks")
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
                                        
                                    print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKER NUB ***")
                                    print("The police have tracked him down and is now arrested")
                                    print("")
                                    print("HP fully restored")
                                    win = win - win + 1
                                    uhp = uhp - uhp + 5



                        if uhp == end1:
                            print("Game Over")
                            exit


                        cont1 = input("Press space and enter to continue")

                        print("")
                        print("You are finally done dealing with the first hacker.")
                        print("")
                        cont1 = input("Press space and enter to continue")

                        print("")
                        print("You feel a sense of relief as you take him out.")
                        print("")
                        cont1 = input("Press space and enter to continue")

                        print("")
                        print("As you finish him off by reporting him to the authorities you notice that he has information to two other hackers that he is working under.  Seeing that it fills you with rage and you proceed with the second attack.")
                        print("")
                        cont1 = input("Press space and enter to continue")

                        print("** You have learned 3 new skills **")
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
                                    print("Immunity (Use safe mode to stop the hacker from accessing your files)")
                                    print("Factory Reset (Reset you device and lose the hacker)")
                                    defence1 = input("You choose: ").lower()
                                    
                                    if defence1 == "immunity":
                                    
                                        print("Immune to all attack")
                                        print("")

                                    if defence1 == "factory reset":
                                        uhp = uhp - 10
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
                                        print("")
                                        
                                        
                                        
                                    if attack1 =="spyware":
                                        hp2 = hp2 - 5
                                        print("You have stolen enough information about him and can be reported to the proper authorities")
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
        

                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("You collaps the bed wasted after spending 8 hours taking out two hackers.  You plan to take out the third hacker the next day due to the fatigue taking over.")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("You roll around the bed for a few minutes fully prepared to sleep when suddenly an alarm goes off.")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("You roll across the bed and look up at your PC.  You see a bunch of error messages and realise that the hacker is attacking you!")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("You jump out of bed, into your chair and ready to take out the third hacker. ")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("*** You have learned 2 new skills ***")
                        

                        print("A wild Hacker Boss has appeared")
                        cont1 == input("Press space and enter to continue")



                        while hp3 != hhp3 and win < 3 and hp2 == 0:
                            
                            while win <3:

                                print("")
                                print("Attack")
                                print("Defend")
                                action = input("Choose an action: ").lower()
                            
                                if action == "defend":
                                    print("Immunity (Immune to all attack)")
                                    defence = input("You choose: ").lower()
                                    
                                    if defence == "immunity":
                                    
                                        print("Immune to all attacks")
                                        print("")
                                    
                                if action == "attack":
                                    print("")
                                    print("Virus (Use generic virus to attack the hackers's computer")
                                    print("Keylogger (Log the hacker's activity)")
                                    attack = input("You choose: ").lower()
                                    
                                    
                                    if attack == "virus":
                                        hp3 = hp3 - 10 
                                        print("You have sent a virus to the hacker and it is attacking his PC")
                                        print("Hacker HP: ",hp3)
                                        print("")
                                        
                                        
                                        
                                    if attack =="keylogger":
                                        hp3 = hp3 - 10
                                        print("You have logged part the hacker's information.")
                                        print("Hacker HP: ",hp3)
                                        print("")

                                    win = win + 1
                                    uhp = uhp - uhp + 5
                                    done = done + 1


                        if uhp == end3:
                            print("Game Over")
                            exit

                        if done == 1 and win == 3 and hp3 == 0:
                            print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKER ***")
                            print("The police have tracked him down and is now arrested")
                            print("")
                            print("You finally have taken justice for your work and is now satified.  You sit back and relax knowing your work is fully secure and have take it back.")
                            print("")
                            print(" _____                             _         _       _   _")                 
                            print("/  __ \                           | |       | |     | | (_)")                
                            print("| /  \/ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___") 
                            print("| |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|")
                            print("| \__/\ (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ ")
                            print(" \____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/")
                            print("                   __/ |")                                                  
                            print("                  |___/ ")                                                  

                            print("")
                            exit


        #MacOS
        if system == "macos":
            print("")
            print("You have chosen macOS")
            cont3 = input("Press space and enter to continue")
            if cont3 == u"\u0020":
                print("")
                print("In the deepest darkest part of the web, the most dangerous place, there lies hackers.  You are the song of CEO of Bapple and you have noticed that there is a hacker trying to steal your comapn's information.  You must take them out with your basic computer skills")
                cont3 = input("Press space and enter to continue")
                if cont3 == u"\u0020":
                    print("")
                    print("A wild Hacka Nub has appeared")
                    cont3 == ("Press space and enter to continue")
                    if cont3 == u"\u0020":
                        print("")
                        
                        #Universal
                        win = 0
                        uhp = 10
                        
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
                                    print("Bapple Care (Go to the Bapple store and get a technician to look at your computer)")
                                    defence = input("You choose: ").lower()
                                    
                                    if defence == "bapple care":
                                    
                                        print("The final total for blocking the attack would be $499 plus tax ")
                                        print("")
                                    
                                if action == "attack":
                                    print("")
                                    print("Bribe (Bribe the hacker with money that has a tracker in it)")
                                    print("Hitman (Hire a professional to take out the hacker for you)")
                                    attack = input("You choose: ").lower()
                                    
                                    
                                    if attack == "bribe":
                                        hp1 = hp1 - 2 
                                        print("You have bribed the hacker with money and he has left you alone.")
                                        print("")
                                        
                                        
                                        
                                    if attack =="hitman":
                                        hp1 = hp1 - 2
                                        print("The hitman tracked his IP and went to his house to smash his PC")
                                        print("")
                                        
                                    print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKER NUB ***")
                                    print("Your private army have gone to the hacker's house and have arrested him")
                                    print("")
                                    print("HP fully restored")
                                    win = win - win + 1
                                    uhp = uhp - uhp + 5



                        if uhp == end1:
                            print("Game Over")
                            exit


                        cont1 = input("Press space and enter to continue")

                        print("")
                        print("You are done dealing with the first hacker.")
                        print("")
                        cont1 = input("Press space and enter to continue")

                        print("")
                        print("You didn't even break a sweat taking him out.")
                        print("")
                        cont1 = input("Press space and enter to continue")

                        print("")
                        print("You go dive into your swimming pool filled with money and relax.  You swim for a bit, but then your butler Sebastian comes and notifies you that another hacker is trying to break into the system")
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
                                    print("Private Technician (Get you private technician to block the attack for you)")
                                    print("Factory Reset (Reset the server and lose the hacker)")
                                    defence1 = input("You choose: ").lower()
                                    
                                    if defence1 == "private technician":
                                    
                                        print("You private technician has blocked the attack for you")
                                        print("")

                                    if defence1 == "factory reset":
                                        uhp = uhp - 10
                                        win = win + 1
                                        hp2 = hp2 - 5

                                        print("")
                                        print("You reset the Bapple server to prevent the hacker from stealing any information, but you forgot to back up your data so its now all lost.  Your father is furious. You lost 5 HP")
                                        print("Your current HP: "+str(uhp))
                                        cont1 = input("Press space and enter to continue")
                                        print("")
                                    
                                if action1 == "attack":
                                    print("")
                                    print("Backroom deals (Do a backroom deal with the hacker)")
                                    print("Exchange (Trade him Bapple devices to make him stop attacking you)")
                                    attack1 = input("You choose: ").lower()
                                    
                                    
                                    if attack1 == "backroom deals":
                                        hp2 = hp2 - 5
                                        print("You do a backroom deal wiht the hacker and you find his location while making the deal")
                                        print("")
                                        
                                        
                                        
                                    if attack1 =="exchange":
                                        hp2 = hp2 - 5
                                        print("You trade him Bapple devices that you have put trackers in")
                                        print("")
                                        
                                    print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKER MAN ***")
                                    print("Your private army have raided his house arresting him.")
                                    print("")
                                    print("HP fully restored")
                                    win = win + 1
                                    uhp = uhp - uhp + 5

                        if uhp == end2:
                            print("Game Over")
                            exit
        

                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("Slightly irritated after two hackers attacking you, you go punch a punching bag full of money to release stress.")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("You beat up the bag really well but when your maid Tooru comes to tell that there is a hacker boss attacking, you get all pissed again.")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("You run to the control room in your house and prepare for a full on attack")
                        print("")
                        cont1 = input("Press space and enter to continue")
                        print("")
                        print("*** You have learned 2 new skills ***")
                        

                        print("A wild Hacker Boss has appeared")
                        cont1 == input("Press space and enter to continue")



                        while hp3 != hhp3 and win < 3 and hp2 == 0:
                            
                            while win <3:

                                print("")
                                print("Attack")
                                print("Defend")
                                action = input("Choose an action: ").lower()
                            
                                if action == "defend":
                                    print("Great Firewall of Bapple (Activate the Great Firewall of Bapple)")
                                    defence = input("You choose: ").lower()
                                    
                                    if defence == "great firewall of bapple":
                                    
                                        print("You filter out all the bad people connected to your server and finds the hacker")
                                        print("")
                                    
                                if action == "attack":
                                    print("")
                                    print("FBI (Get the FBI to take out the hacker for you")
                                    print("Private Army (Get your private army to raid the hacker)")
                                    attack = input("You choose: ").lower()
                                    
                                    
                                    if attack == "fbi":
                                        hp3 = hp3 - 10 
                                        print("You have sent the FBI to take out the hacker and they find his IP")
                                        print("Hacker HP: ",hp3)
                                        print("")
                                        
                                        
                                        
                                    if attack =="private army":
                                        hp3 = hp3 - 10
                                        print("You send you private awrmy to the hacker's house")
                                        print("Hacker HP: ",hp3)
                                        print("")

                                    win = win + 1
                                    uhp = uhp - uhp + 5
                                    done = done + 1


                        if uhp == end3:
                            print("Game Over")
                            exit

                        if done == 1 and win == 3 and hp3 == 0:
                            print("*** YOU HAVE SUCESSFULLY BEATEN THE HACKER ***")
                            print("Your private army have raided his house taking him out")
                            print("")
                            print("You finally have taken out the hackers that were attacking your company.  Money can buy you defence against hackers.")
                            print("")
                            print(" _____                             _         _       _   _")                 
                            print("/  __ \                           | |       | |     | | (_)")                
                            print("| /  \/ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___") 
                            print("| |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|")
                            print("| \__/\ (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ ")
                            print(" \____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/")
                            print("                   __/ |")                                                  
                            print("                  |___/ ")                                                  

                            print("")
                            exit