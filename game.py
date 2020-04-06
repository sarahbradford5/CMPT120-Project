# name: Sarah Bradford
# date: 3/2/2020
# citation: got template from iLearn, collaborated with Jadyn Kennedy and Michael Conger



locales = ["you caught the ball from your favorite player", "you spilt your drink all over your jacket", "your friend bought you a tshirt of your favorite player", "you made it on the jumbotron", 
"you went to the bathroom and missed a great play", "you found a seat right behind the dugout"]

position=locales[0]


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
    global position
    position=locales[0]
    print(position)
    print("score = +100")
    input(enter)

def drink():
    global position
    position=locales[1]
    print(position)
    print("Score = -50")
    input(enter)
    print()


def friend():
    global position
    position=locales[2]
    print(position)
    print("Score = + 100")
    input(enter)
    print()


def jumbo():
    global position
    position=locales[3]
    print(position)
    print("Score = + 100")
    input(enter)
    print()

def bathroom():
    global position
    position=locales[4]
    print(position)
    print("Score = -50")
    input(enter)
    print()

def dugout():
    global position
    position=locales[5]
    print(position)
    print("Score = +100")
    input(enter)
    print()

    
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
