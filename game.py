# name: Sarah Bradford
# date: 4/6/2020
# citation: got template from iLearn, collaborated with Jadyn Kennedy and Michael Conger


#global list
locales = ["you caught the ball from your favorite player", "you spilt your drink all over your jacket", "your friend bought you a tshirt of your favorite player", "you made it on the jumbotron", 
"you went to the bathroom and missed a great play", "you found a seat right behind the dugout"]

#new global list
locnames = ["catch", "drink", "friend", "jumbo", "bathroom", "dugout"]

#tracking where player has been
moves = [False, False, False, False, False, False] 

score=0
playermoves=0
position=locales[0]
currentlocale=locnames[0]

playermoves=0

print("Fenway Trip!")
enter="press enter to continue"
def copyright(fenway):
    print(fenway)
def greeting():
    name=input("enter your name: ")
    favoriteplayer=input("enter your favorite Red Sox player: ")
    greeting1="hello",name,"how are you?"
    intro="Let's go watch a baseball game!"
    print(greeting1, intro)
    input(enter)

def catch():
    global currentlocale 
    global position #determine players position
    global score
    global moves
    global playermoves 
    if moves[0] == False:
        score = score + 100
    else:
        score = score 
    currentlocale = locnames[0]
    position = locales[0]
    print(currentlocale)
    print(position)
    print (score + 100)
    input(enter)
    moves[0] = True
    playermoves = playermoves + 1
    return moves[0], playermoves

def drink():
    global currentlocale 
    global position #determine players position
    global score
    global moves
    global playermoves
    if moves[1] == False:
        score = score - 50
    else:
        score = score 
    currentlocale = locnames[1]
    position = locales[1]
    print(currentlocale)
    print(position)
    print (score - 50)
    input(enter)
    moves[1] = True
    playermoves = playermoves + 1
    return moves[1], playermoves


def friend():
    global currentlocale 
    global position #determine players position
    global score
    global moves
    global playermoves
    if moves[2] == False:
        score = score + 100
    else:
        score = score 
    currentlocale = locnames[2]
    position = locales[2]
    print(currentlocale)
    print(position)
    print(score + 100)
    input(enter)
    moves[2] = True
    playermoves = playermoves + 1
    return moves[2], playermoves


def jumbo():
    global currentlocale 
    global position #determine players position
    global score
    global moves
    global playermoves
    if moves[3] == False:
        score = score + 100
    else:
        score = score 
    currentlocale = locnames[3]
    position = locales[3]
    print(currentlocale)
    print(position)
    print(score + 100)
    input(enter)
    moves[3] = True
    playermoves = playermoves + 1
    return moves[3], playermoves

def bathroom():
    global currentlocale 
    global position #determine players position
    global score
    global moves
    global playermoves
    if moves[4] == False:
        score = - 50 
    else:
        score = score 
    currentlocale = locnames[4]
    position = locales[4]
    print(currentlocale)
    print(position)
    print(score - 50)
    input(enter)
    moves[4] = True
    playermoves = playermoves + 1
    return moves [4], playermoves
    

def dugout():
    global currentlocale 
    global position #determine players position
    global score
    global moves
    global playermoves
    if moves[5] == False:
        score = score + 100
    else:
        score = score 
    currentlocale = locnames[5]
    position = locales[5]
    print(currentlocale)
    print(position)
    print(score + 100)
    input(enter)
    moves[5] = True
    playermoves = playermoves + 1
    return moves[5], playermoves

    
def End():
    thanks = "Thank you for playing!"
    print(thanks)


def loop():
    x=1
    while x==1:
        prompt = "which direction would you like to go?\n"
        choice = input (prompt)
        invalid="that command was invalid, please enter Help"
        Help = "please input north, south, east or west, or quit\n"
        north = "lets go north"
        south = "lets go south"
        east = "lets go east"
        west = "lets go west"
        if choice [0] == "h":
            x=1
            print (Help)
        elif choice [0] =="q":
            x=2
            Quit()
        elif choice [0] == "n" or choice [0] =="s" or choice [0] == "e" or choice [0] =="w":
            x=1
            if position == locales[0]:
                x=1
                if choice [0] == "n":
                    drink()
                elif choice [0] =="s":
                    print (invalid)
                elif choice [0] =="e":
                    friend()
                elif choice [0] =="w":
                    print(invalid)
                    
            elif position == locales[1]:
                x=1
                if choice [0] == "n":
                    print(invalid)
                elif choice [0] =="s":
                    catch()
                elif choice [0] =="e":
                    bathroom()
                elif choice [0] =="w":
                    print (invalid)
                                                        
            elif position == locales[2]:
                x=1
                if choice [0] == "n":
                    bathroom() 
                elif choice [0] =="s":
                    print (invalid)  
                elif choice [0] =="e":
                    jumbo() 
                elif choice [0] =="w":
                    catch() 

            elif position == locales[3]:
                x=1
                if choice [0] == "n":
                    dugout()
                elif choice [0] =="s":
                    print(invalid)
                elif choice [0] =="e":
                    print(invalid)
                elif choice [0] =="w":
                    friend()

            elif position == locales[4]:
                x=1
                if choice [0] == "n":
                    print(invalid)
                elif choice [0] =="s":
                    friend()
                elif choice [0] =="e":
                    dugout()
                elif choice [0] =="w":
                    drink()

            elif position == locales[5]:
                x=1
                if choice [0] == "n":
                    print(invalid)
                elif choice [0] =="s":
                    jumbo()
                elif choice [0] =="e":
                    print(invalid)
                elif choice [0] =="w":
                    bathroom()
        else:
            x=1
            print(invalid)

def main():
    greeting()
    loop()
    End()
    copyright1="created by Sarah Bradford 3/2/2020"
    copyright(copyright1)


def Quit():
    print("okay, bye")


main()
