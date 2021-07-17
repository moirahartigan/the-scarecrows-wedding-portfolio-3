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
    print("###########################################################################\n\n")
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
            time.sleep(0.03) # wait until until the next character
        else:
            time.sleep(0.5) # 0.5 sec delay for the end of each sentance

typewriter(intro)    
welcome_msg()


def intro():
    name = str(input("What is your name: \n")) 
    print()
    typewriter(f"Welcome to The Scarecrows Wedding {name}, Thank you for joining us. \n")

    first_response = input("Would you like to start the game? \n (yes/no): \n")
    if first_response == 'yes' or first_response == 'Yes':
        print("")
        chapter_one()

    elif first_response == 'no' or first_response == 'No':
        game_over("Maybe next time. Goodbye")


def chapter_one():     
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
    second_response = input("Can you help Harry find some Pink flowers for the list \n"
                            "and get back for his wedding?\n(yes/no) : \n")
    if second_response == 'yes' or second_response == 'Yes':
        print("")
        chapter_two()

    elif second_response == 'no' or second_response == 'No':
        typewriter(
            "Too bad, it would have been the best wedding yet. Goodbye.")
        
       



def chapter_two():
    typewriter("Pink Flowers were the only thing left on the list \n")
    typewriter('Harry said “Betty, dear, I can find those. \n')
    typewriter('Why don’t I pick some while you have a doze?” \n')
    print("")
    typewriter("I can find you a field of pink flowerzzzzz! \n")
    typewriter("Follow me! ..... \n")
    typewriter("Buzzed a big stripy bee. \n")
    print("")
    typewriter("What should Harry do? \n ")
    typewriter("1.) Follow the bee \n")
    typewriter(" 2.) Go to the farm shop to buy some flowers instead \n")
    typewriter(" 3.) Call the florist and have them deliver the flowers \n")
    print("")
    choice = input("Choose option (1, 2 or 3): \n ")
    if choice == '1':
        print()
        # if user picks option 1 there move to the next 
        chapter_three()
    elif choice == '2':
        print()
        print(" oh no the Farm Shop is sold out \n")
        print(" Betty is not pleased \n")
        print(" The Wedding is off ! - Game Over")
    elif choice == '3':
        print()
        print("You are a Scarecrrow !!! \n")
        print("You have no phone to make the call and no money to pay for flowers.\n ")
        print("Game Over")   

    
        

   # else:
    #     typewriter(" I dont understand that. Please type yes or no.")
     #    print("")
      #   second_response = input(" \n Can you help Harry find some Pink flowers for the list \n"
       # "and get back for his wedding?\n(yes/no) : \n")

       



def chapter_three():    
    print("So the bee led the way, and they travelled for hours\n")
    print("Till they come to a field full of pretty pink flowers.\n")
    print('Harry is now thinking "I wont pick them yet.\n')
    print('I will need to find water, to keep their stalks wet.” \n')
    print()
    third_response = input("Do you think Harry needs to find water?: \n (yes/no) \n")
    if third_response == 'yes' or third_response == 'Yes':
        print("")
        chapter_four()

    elif third_response == 'no' or third_response == 'No':        
        typewriter(
            "Harry returns with the flowers....."
            "but they have died without water!"
            "oh dear Betty is not pleased and the wedding is off"
            "Game Over")





def chapter_four():
    print()
    
    




def chapter_five():
    print()



def chapter_six():
    print()



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

intro()  
