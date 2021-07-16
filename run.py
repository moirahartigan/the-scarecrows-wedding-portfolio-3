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
    print("#############################################################################\n")
    print("#                                                                           #\n")
    print("#                          The Scarecrows Wedding                           #\n")
    print("#           _________      At Diddly Squat Farm                             #\n")
    print("#          |         |                                                      #\n")
    print("#          |         |                                                      #\n")
    print("#  ________|_________|_________               | *\_/* |________             #\n")
    print("#      |   ____________   |                 | |__/-\__|_____   |            #\n")                                
    print("#      |  |            |  |                 |  |            |  |            #\n")
    print("#      |  |   0    0   |  |                 |  |   0    0   |  |            #\n")
    print("#      |  |     -      |  |                 |  |      -     |  |            #\n")
    print("#      |  |   \____/   |  |                 |  |    \___/   |  |            #\n")
    print("#      |  |            |  |                 |  |            |  |            #\n")
    print("#      |  |____|\_/|___|  |                 |  |____________|  |            #\n")
    print("#      |_______|/ \|______|                 |_______*****______|            #\n")
    print("# _\_______|____________|________/_   _\_______|__________|__________/_     #\n")
    print("#  /                             \     /                             \      #\n")
    print("#############################################################################\n")
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
            time.sleep(0.02) # wait until until the next character
        else:
            time.sleep(0.5) # 0.5 sec delay for the end of each sentance

typewriter(intro)        


welcome_msg()


name = str(input("What is your name: \n")) 
print()
typewriter(f"Welcome to The Scarecrows Wedding {name}, Thank you for joining us. \n")



def intro():

    first_response = input("Would you like to start the game? \n (yes/no): \n")
    if first_response == 'yes' or first_response == 'Yes':
        print("")
        typewriter("Ok Great ! \n")
        typewriter("Here is the story so far ...... \n")
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
        print("")

    elif first_response == 'no' or first_response == 'No':
        print("Maybe next time. Goodbye")

intro()     

def start_game():
    second_response = input("Can you help Harry find some Pink flowers for the list \n"
                            "and get back for his wedding?\n(yes/no) : \n")
    second_response = ""
    if second_response == 'yes' or second_response == 'Yes':
        print("part_2")
        
    elif second_response == 'no' or second_response == 'No':
        typewriter("Too bad, it would have been the best wedding yet . Goodbye, " + name + ".")
        game_over()

    else:
         typewriter(" I dont understand that. Please type yes or no.")
         print("")
         second_response = input(" \n Can you help Harry find some Pink flowers for the list \n"
        "and get back for his wedding?\n(yes/no) : \n")



def game_over():
    """
    Function for when the user chooses the wrong option/ answer Prints game over and the reason why
    """
    print("")
    print("##############################")
    print("#                            #")
    print("#        |GAME OVER|         #")
    print("#                            #")
    print("##############################")
    print("")

game_over()


start_game()