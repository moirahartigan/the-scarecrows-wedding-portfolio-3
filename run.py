# Python Text Based Game - The Scarecrows Wedding
# Story taken and adapted from a book of the same name By Julia Donaldson
# By Moira Hartigan


# Import time and sys to print typewriter effect.
import sys
import time

def welcome_msg():
    """
    Function to print welcome graphics
    """
    print()
    print("######################################################################################################")
    print("#                                                                                                    #")
    print("#                                     The Scarecrows Wedding                                         #")
    print("#                                      At Diddly Squat Farm                                          #")
    print("#                                                                                                    #")
    print("#                          ___________                                                               #")
    print("#                         |           |                                                              #")
    print("#                         |           |                                                              #")
    print("#                _________|___________|_________                  | *\_/* |___________               #")
    print("#                    |   _______________   |                    | |__/-\__|________   |              #")                                
    print("#                    |  |               |  |                    |  |               |  |              #")
    print("#                    |  |    0    0     |  |                    |  |    0    0     |  |              #")
    print("#                    |  |       -       |  |                    |  |       -       |  |              #")
    print("#                    |  |     \___/     |  |                    |  |     \___/     |  |              #")
    print("#                    |  |               |  |                    |  |               |  |              #")
    print("#                    |  |_____|\__/|____|  |                    |  |_______________|  |              #")
    print("#                    |________|/  \|_______|                    |________******_______|              #")
    print("#               _\_______|_____________|____________/_      _\_______|_____________|____________/_   #")
    print("#                /                                  \        /                                  \    #")
    print("######################################################################################################")
    print("")


intro = "Hello! \n\
Welcome to Diddly Squat Farm. \n\
There is a big event happening today. \n "

# typewriter style animation code adpted from https://www.youtube.com/watch?v=2h8e0tXHfk0
def typewriter(intro): 
    """
    Text will be displayed letter by letter using sys import rater than a
    whole block of text - A time delay added will apply at the end of each 
    sentance for 1 second unless "\n" is used.
    """

    for char in intro:
        sys.stdout.write(char) #print each character - print it
        sys.stdout.flush() # display it

        if char != "\n":
            time.sleep(0.1) # wait until until the next character
        else:
            time.sleep(1) # 1 sec delay for the end of each sentance

typewriter(intro)        

#function to start game
def start_game():
    """ 
    The Story begins and the player is given their first option
    """
   # print welcome message
welcome_msg()

name = str(input("Thank you for joining us. \n\
    What is your name: \n"))
print("")
typewriter("Welcome to The Scarecrows Wedding " + str(name) + ".")
print("")
startGame = input("Would you like to start the game? (yes/no): \n")
if startGame == 'no' or startGame == 'No':
    typewriter("Maybe next time")
elif startGame == 'yes' or startGame == 'Yes':
    print("")
    typewriter("Harry loved Betty and Betty loved Harry, \n")
    typewriter('So Harry said, “Betty, my beauty, lets marry!\n')
    typewriter("Lets have a wedding, the best wedding yet,\n")
    typewriter('A wedding no one will ever forget.”\n')
    print("")
    typewriter("Betty agreed, so they hugged \n")
    typewriter("and they kissed. \n")
    typewriter('Then Betty said, “Harry, dear, \n')
    typewriter('Lets make a list.” \n')
    print("")
    typewriter('Harry gave Betty his arm \n')
    typewriter("And set off on a hunt round the farm. \n")
    print("")


 

    start_game()