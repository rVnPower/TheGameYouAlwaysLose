import os
import random
defaultOS = 'Windows'
clear = lambda:os.system('cls')
minNum = 1
maxNum = 10
maxPoint = 100
# Settings function
def settings():
    global clear, defaultOS
    clear()
    while True:
        print(f"1) Change current operating system settings (Current: {defaultOS})")
        print("2) Return to menu")
        pInput = int(input(">> "))
        try:
            if pInput == 1:
                clear()
                if defaultOS == 'Windows':
                    clear = lambda: os.system('clear')
                    defaultOS = 'Linux'
                    print("Changed to Linux!")
                elif defaultOS == 'Linux':
                    clear = lambda : os.system('cls')
                    defaultOS = 'Windows'
                    print("Changed to Windows")
            elif pInput ==2:
                break
            else:
                break

        except ValueError:
                pass
# Help
def rules():
    clear()
    print("Rules: \nYou will play this game with a code written by me. Take a number between 1 and 10. The first person one to get to 100 wins.")
    print("_____________________________________________________________________")
    print("Developer: VnPower\nInspired by: Vsauce2\nSpecial thanks: Atro")
    print("_____________________________________________________________________")
    print("Found a bug? You can always open an issue on my GitHub repo:link  \nPlease don't open issues about visual bugs. This was build to work on a console.")
    input("Press any key to continue... And thx!")
# New game menu
def newGame():
    def Sandbox():
        def PlaySandbox():
            totalPoint = 0
            play1Point = 0
            play2Point = 0
            play1Scores = 0
            play2Scores = 0
            play1Turn  = True
            play2Turn = False
            clear()
            while True:
                clear()
                print("You can always break out the game using Ctrl+C.\n______________________________________________________")
                print(f"P1: {play1Scores} - P2: {play2Scores}")
                totalPoint = 0
                while totalPoint < maxPoint + 10:
                    if play1Turn:
                        try:
                            play1Point = int(input("Player 1 number: "))
                        except ValueError:
                            pass
                        if minNum <= play1Point <= maxNum:
                            totalPoint += play1Point
                            print(f"Total points now = {totalPoint}")
                            play1Turn  = False
                            play2Turn = True
                            if totalPoint >= maxPoint:
                                play1Scores += 1
                                print(f"Player 1 Win! Now you have {play1Scores} points!")
                                input("Press any key to continue...")
                                break
                            print("______________________________________________________")
                        else:
                            print(f"Please choose a number between {minNum} and {maxNum}.")
                            print("___________________________________________________")
                    if play2Turn:
                        try:
                            play2Point = int(input("Player 2 number: "))
                        except ValueError:
                            pass
                        if minNum <= play2Point <= maxNum:
                            totalPoint += play2Point
                            print(f"Total points now = {totalPoint}")
                            play1Turn  = True
                            play2Turn = False
                            if totalPoint >= maxPoint:
                                play2Scores += 1
                                print(f"Player 2 Win! Now you have {play2Scores} points!")
                                input("Press any key to continue...")
                                break
                            print("______________________________________________________")
                        else:
                            print(f"Please choose a number between {minNum} and {maxNum}.")
                            print("___________________________________________________")
        global minNum, maxNum, maxPoint
        while True:
            clear()
            print("You are free to edit any value in this mode!\n______________________________________________________")
            print(f"1) Min Number (Current: {minNum})\n2) Max Number: (Current: {maxNum})\n3) Max Point (Current: {maxPoint})\n4) Play!\n5) Return to menu")
            try:
                Input = int(input(">> "))
            except ValueError:
                pass
            if Input == 1:
                minNum = int(input("Enter value: "))
            elif Input == 2:
                maxNum = int(input("Enter value: "))
            elif Input == 3:
                maxPoint = int(input("Enter value: "))
            elif Input == 4:
                PlaySandbox()
            elif Input == 5:
                break
    def AI():
        clear()
        totalPoint = 1
        playPoint = 0
        aiPoint = 1
        print("You can always break out the game using Ctrl+C.\n______________________________________________________")
        print("AI chose 1. Total points now = 1")
        while totalPoint < 100:
            try:
                playPoint = int(input("Your number: "))
            except ValueError:
                pass
            if 0 < playPoint <= 10:
                totalPoint += playPoint
                print(f"Total points now = {totalPoint}")
                aiPoint = 11 - playPoint
                print(f"AI chose {aiPoint}.")
                totalPoint += aiPoint
                print(f"Total points now = {totalPoint}")
                print("______________________________________________________")
            else:
                print("Please choose a number between 1 and 10.")
                print("___________________________________________________")
        print("AI wins! That's the real fact lol!")
        input("Press any key to exit...")
    def You():
            clear()
            totalPoint = 0
            playPoint = 0
            aiPoint = 0
            print("You can always break out the game using Ctrl+C.\n______________________________________________________")
            while totalPoint < 110:
                try:
                    playPoint = int(input("Your number: "))
                except ValueError:
                    pass
                if 0 < playPoint <= 10:
                    totalPoint += playPoint
                    print(f"Total points now = {totalPoint}")
                    if totalPoint >= 100:
                        print("You Win!")
                        input("Press any key to continue...")
                        break
                    else:
                        pass
                    # AI algorithms
                    if 80 <= totalPoint < 90:
                        aiPoint = 89 - totalPoint
                    elif 60 <= totalPoint < 68:
                        aiPoint = 68 - totalPoint
                    elif 70 <= totalPoint < 78:
                        aiPoint = 78 - totalPoint
                    elif 90 <= totalPoint:
                        aiPoint = 11 - playPoint
                    elif totalPoint == 79:
                        aiPoint = 10
                    else:
                        aiPoint = round((playPoint+5)/2)
                    if aiPoint == 0:
                        aiPoint = 1
                    print(f"AI chose {aiPoint}.")
                    totalPoint += aiPoint
                    print(f"Total points now = {totalPoint}")
                    if totalPoint >= 100:
                        print("Ai Wins!")
                        input("Press any key to continue...")
                        break
                    print("______________________________________________________")
                else:
                    print("Please choose a number between 1 and 10.")
                    print("___________________________________________________")
    def Random():
        clear()
        totalPoint = 0
        playPoint = 0
        aiPoint = 0
        print("You can always break out the game using Ctrl+C.\n______________________________________________________")
        while totalPoint < 110:
            try:
                playPoint = int(input("Your number: "))
            except ValueError:
                pass
            if 0 < playPoint <= 10:
                totalPoint += playPoint
                print(f"Total points now = {totalPoint}")
                if totalPoint >= 100:
                    print("You Win!")
                    input("Press any key to continue...")
                    break
                else:
                    pass
                aiPoint = random.randint(1, 10)
                print(f"AI chose {aiPoint}.")
                totalPoint += aiPoint
                print(f"Total points now = {totalPoint}")
                if totalPoint >= 100:
                    print("Ai Wins!")
                    input("Press any key to continue...")
                    break
                print("______________________________________________________")
            else:
                print("Please choose a number between 1 and 10.")
                print("___________________________________________________")
    def Versus():
        clear()
        totalPoint = 0
        play1Point = 0
        play2Point = 0
        play1Scores = 0
        play2Scores = 0
        play1Turn  = True
        play2Turn = False
        while True:
            totalPoint = 0
            clear()
            print("You can always break out the game using Ctrl+C.\n______________________________________________________")
            print(f"P1: {play1Scores} - P2: {play2Scores}")
            while totalPoint < 110:
                if play1Turn:
                    try:
                        play1Point = int(input("Player 1 number: "))
                    except ValueError:
                        pass
                    if 0 < play1Point <= 10:
                        totalPoint += play1Point
                        print(f"Total points now = {totalPoint}")
                        play1Turn = False
                        play2Turn = True
                        if totalPoint >= 100:
                            play1Scores += 1
                            print(f"Player 1 Win! Now you have {play1Scores} points!")
                            input("Press any key to continue...")
                            break
                        print("______________________________________________________")
                    else:
                        print("Please choose a number between 1 and 10.")
                        print("___________________________________________________")
                elif play2Turn:
                    try:
                        play2Point = int(input("Player 2 number: "))
                    except ValueError:
                        pass
                    if 0 < play2Point <= 10:
                        totalPoint += play2Point
                        print(f"Total points now = {totalPoint}")
                        play1Turn = True
                        play2Turn = False
                        if totalPoint >= 100:
                            play2Scores += 1
                            print(f"Player 2 Win! Now you have {play2Scores} points!")
                            input("Press any key to continue...")
                            break
                        print("______________________________________________________")
                    else:
                        print("Please choose a number between 1 and 10.")
                        print("___________________________________________________")
    # Mode menu
    while True:
        clear()
        print("Choose a mode to play!\n1) AI go first(You always lose)\n2) You go first\n3) Random AI\n4) Versus mode\n5) Sandbox mode\n6) Return to main menu")
        pInput = int(input())
        try:
            if pInput == 1:
                AI()
            elif pInput == 2:
                You()
            elif pInput == 3:
                Random()
            elif pInput == 4:
                Versus()
            elif pInput == 5:
                Sandbox()
            elif pInput == 6:
                break
        except:
            pass
# Displaying menu
def display():
    global clear
    clear()
    while True:
        clear()
        print("Welcome to The Game You Can Always Lose!")
        print("__________________________________________________")
        print("1) New Game")
        print("2) Help")
        print("3) Settings")
        print("4) Exit")
        pInput = int(input(">> "))
        if pInput == 1:
            newGame()
        elif pInput == 2:
                rules()
        elif pInput == 3:
            settings()
        elif pInput == 4:
                exit()
# Call the main menu function
display()
