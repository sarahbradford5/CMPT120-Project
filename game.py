# name: Sarah Bradford
# date: 2/10/2020
# citation: got template from iLearn, collaborated with Jadyn Kennedy and Michael Conger

def game():
    print("Help Me Get to Fenway!")

    enter="press enter to continue"
    score=0
    name=input("enter your name")
    favoriteplayer=input("enter your favorite Red Sox player")
    greeting1="hello",name,"how are you?"
    intro="I am running late. Help me get to the Red Sox game tonight!"
    l="My dad just gave me his tickets to the baseball game tonight, but I am running late and I have to pick up my friend and then take the T into Boston."
    x="I can't wait to see",favoriteplayer
    m="Oh no",name,"! My car is almost out of gas. I have to stop and fill up my tank."
    n="I get to my friends house, but she isn't ready to go yet. 10 minutes later she finally gets into the car and we head on our way."
    y="I get to the T station but, it already left without us."
    z="We have to drive to another station to get to another T."
    v="We finally get on the T and head into Boston."
    t="We have arrived in Boston!"
    s="Now we Uber to Fenway, and everything seems to be going our way."
    a="We finally get to Fenway and can't find our tickets in my backpack."
    c="Yes!! I finally found them in my pocket."
    o="The game is about to start, we cut it close."
    q="My favorite player",favoriteplayer,"hit a homerun right near my seat!"
    h="I caught the ball!!"
    p="The Red Sox won the game! They are now doing post game interviews with some of our favorite players!"
    w="Congratulations",name,"you have won! Thank you for your help! Would you like to play again?"
    b="created by Sarah Bradford 2/10/2020"

    print(greeting1,)

    print(intro)
    input(enter)

    print() # Prints a blank line
    print(l)
    print(x)
    print("Score:", score)
    input(enter)
    print()

    print(m)
    print("Score:", score + 50)
    input(enter)
    print()

    print(n)
    print("Score:", score + 100)
    input(enter)
    print()

    print(y)
    print(z)
    print("Score:", score + 150)
    input(enter)
    print()

    print(v)
    print("Score:", score + 200)
    input(enter)
    print()

    print(t)
    print("Score:", score + 250)
    input(enter)
    print()

    print(s)
    print("Score:", score + 300)
    input(enter)
    print()

    print(a)
    print(c)
    print("Score:", score + 350)
    input(enter)
    print()

    print(o)
    print("Score:", score + 400)
    input(enter)
    print()

    print(q)
    print(h)
    print("Score:", score + 450)
    input(enter)
    print()
    
    print(p)
    print("Score:", score + 500)
    input(enter)
    print()

    print(w)
    input(enter)
    
    print(b)

def main(fenway):
    fenway() 


main(game)


