# Python Text Based Game - The Scarecrows Wedding
# Story taken and adapted from a book of the same name By Julia Donaldson
# By Moira Hartigan


# Import time for speed of text on story and sys to print individual characters.
import sys
import time

intro = "Hello! \n\
Welcome to Diddly Squat Farm. \n\
There is a big event happening today. \n "


def typewriter(intro):

    for char in intro:
        sys.stdout.write(char) #print each character - print it
        sys.stdout.flush() # display it

        if char != "\n":
            time.sleep(0.1) # wait until until the next character
        else:
            time.sleep(1)
        

typewriter(intro)
#function to start game


def intro():
    """ 
    The Story begins and the player is given their first option
    """
    print(" Welcome to Diddly Spuat Farm," + name)
    print("Betty O’Barley and Harry O’Hay are scarecrows.")
    print("Harry loved Betty and Betty loved Harry,")
    print('So Harry said, “Betty, my beauty, lets marry!')
    print("Lets have a wedding, the best wedding yet,")
    print('A wedding no one will ever forget.”')
    print("")
    print("Betty agreed, so they hugged")
    print("and they kissed.")
    print('Then Betty said, “Harry, dear,')
    print('Lets make a list.”')
    print("")
    print('Harry gave Betty his arm')
    print("And set off on a hunt round the farm.")
    print("")
    
   
def chooseOption():
    decision = ""
    while decision != "yes" and decision != "no" : # input validation
        decision = input("Can you help Harry find some Pink flowers for the list and get back for his wedding? (yes/no) : \n")

    return decision


def checkDecision(chooseOption):
    print("Pink Flowers were the only thing left on the list")
    print('Harry said “Betty, dear, I can find those.')
    print('Why don’t I pick some while you have a doze?” ')




#intro()
chooseOption()
    


    #print("Too bad …  It would have been a good wedding ! ")
    
    #print("")
    
    #if yes
    #print("")
    #print("Pink Flowers were the only thing left on the list")
    #print('Harry said “Betty, dear, I can find those.')
   # print('Why don’t I pick some while you have a doze?” ')
    #print()



#intro()
