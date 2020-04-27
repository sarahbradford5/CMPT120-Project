# Sarah Bradford
# Project 4 - Interactive Dictionary 
# 2020-04-27
# collaborated with Jadyn Kennedy


def main():
    copyright1="created by Sarah Bradford 4/26/2020"
    print(copyright1)
    myFile = input("enter the file name").strip()
    myFile = myFile.lower()

    with open(myFile, "r") as myFile:
        dictionary = myFile.readlines()
        term1 = dictionary[0].strip()
        definition1 = dictionary[1].strip()
        term2 = dictionary[2].strip()
        definition2 = dictionary[3].strip()

        words = {
            term1 : definition1,
            term2 : definition2
        }

        x = 0
        while x==0:
            enter = "enter a word to find its definition:"
            List = input(enter).strip()
            List = List.lower()
            if List == term1:
                print(words[term1])
            elif List == term2:
                print(words[term2])

            elif List == "":
                x=1
            else:
                invalid = "sorry, this word is not in this dictionary"
                print(invalid)
                x=0

main()
            
            
    
