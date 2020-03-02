# name: Sarah Bradford
# date: 3/2/2020
# citation: got template from iLearn, collaborated with Jadyn Kennedy and Michael Conger

def copyright(fenway):
    print(fenway)

locales["you caught the ball from your favorite player", "you spilt your drink all over your jacket", "your friend bought you a tshirt of your favorite player", "you made it on the jumbotron", 
"you went to the bathroom and missed a great play", "you found a seat right behind the dugout"]



print("Help Me Get to Fenway!")

enter="press enter to continue"
score=0


def greeting():
    name=input("enter your name")
    favoriteplayer=input("enter your favorite Red Sox player")
    greeting1="hello",name,"how are you?"
    intro="I am running late. Help me get to the Red Sox game tonight!"
    print(greeting1, intro)
    input(enter)

def catch():
    locales[0]
    print("Score:", score+100)
    input(enter)
    print()

def drink():
    locales[1]
    print("Score:", score-50)
    input(enter)
    print()

def friend():
    locales[2]
    print("Score:", score + 100)
    input(enter)
    print()

def jumbo():
    locales[3]
    print("Score:", score + 100)
    input(enter)
    print()

def dugout():
    locales[4]
    print("Score:", score + 100)
    input(enter)
    print()

def bathroom():
   locales[5]
   print("Score:", score-50)
   input(enter)
   print()




def congrats():
    print(w)
    input(enter)
    



def main():
    greeting()
    loop()
    Exit()
    copyright1="created by Sarah Bradford 3/2/2020"
    copyright(copyright1)


def loop():
    x=1
    while x==1:
        prompt = "which direction would you like to go?\n"
        choice = input (prompt)
        invalid="that command was invalid, please enter help"
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
            Quit ()
        elif choice [0] == "n" or choice [0] =="s" or choice [0] == "e" or choice [0] =="w":
            x=1
        else:
            print (invalid)
            if players current position = the first locale in the list:
                if they say north:
                    print some locale
                if they say east:
                    print some locale
                if they say west:
                    say invaid
                if they say south:
                    print(invalid)
                    
            if the players current positin = the second locale in the list:
                if they say north:
                    have them go to a different locale (it doesn't matter which one)
                if they say east:
                    say invalid
                if they say west:
                    print some locale
                if they say south:
                    print some locale 
            

def quit():
    print("okay, bye")


main()


