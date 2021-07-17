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
    typewriter("########################################################################\n")
    print("#           _________            Welcome to                                 #\n")
    print("#          |         |      The Scarecrows Wedding                          #\n")
    print("#          |         |        At Diddly Squat                               #\n")
    print("#  ________|_________|_________     Farm      | *\_/* |________             #\n")
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
    typewriter("######################################################################\n\n")
    print("")

intro = "Hello!"




# typewriter style animation code adpted from https://www.youtube.com/watch?v=2h8e0tXHfk0
def typewriter(intro): 
    """
    This function allows the text to be displayed letter by letter using sys import rater than a
    whole block of text - A time delay added will apply at the end of each 
    sentance for 1 second unless "\n" is used.
    """

    for character in intro:
        sys.stdout.write(character) #print each character - print it
        sys.stdout.flush() # display it

        if character == "#\n":
            time.sleep(0.005) # wait until until the next character
        else:
            time.sleep(0.03) # 0.5 sec delay for the end of each sentance

typewriter(intro)    
welcome_msg()


def intro():
    """
    Intro function begins the game and welcomes the user
    by requesting their name in order to play
    """
    while True:
        # while loop to ensure user adds their name
        name = str(input("Please Tell me your name: \n")) 
        if name == "":
            print("We need to check your name off the guestlist to continue ....\n")
            continue
        else:
            break
    typewriter(f"Welcome to Diddly Squat Farm {name}, \n") 
    typewriter("Thank you for joining us\n")
    typewriter("for the Scarecrows Wedding.\n")
    
    startGame = input("Would you like to start the game? \n (yes/no): \n")
    if startGame == 'no' or startGame == 'No':
        game_over("Maybe next time. Goodbye")
        
    elif startGame == 'yes' or startGame == 'Yes':
        print()
        chapter_one()
                  

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
    first_response = input("Can you help Harry find some Pink flowers for the list \n"
                            "and get back for his wedding?\n(yes/no) : \n")
    if first_response == 'yes' or first_response == 'Yes':
        print("")
        chapter_two()

    elif first_response == 'no' or first_response == 'No':
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
    second_response = input("Choose option (1, 2 or 3): \n ")
    if second_response == '1':
        print()
        # if user picks option 1 there move to the next 
        chapter_three()
    elif second_response == '2':
        print()
        typewriter(" oh no the Farm Shop is sold out\n")
        typewriter(" Betty is not pleased\n")
        typewriter(" The Wedding is off ! - Game Over")
    elif second_response == '3':
        print()
        typewriter("You are a Scarecrrow !!! \n")
        typewriter("You have no phone to make the call and no money to pay for flowers.\n ")
        typewriter("Game Over")   

    
        

   # else:
    #     typewriter(" I dont understand that. Please type yes or no.")
     #    print("")
      #   second_response = input(" \n Can you help Harry find some Pink flowers for the list \n"
       # "and get back for his wedding?\n(yes/no) : \n")

       



def chapter_three():    
    typewriter("So the bee led the way, and they travelled for hours\n")
    typewriter("Till they come to a field full of pretty pink flowers.\n")
    typewriter('Harry is now thinking "I wont pick them yet.\n')
    typewriter('I will need to find water, to keep their stalks wet.” \n')
    print()
    third_response = input("Do you think Harry needs to find water?: \n (yes/no)\n")
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
    typewriter('"Just follow me",\n')
    typewriter("croaked a lumpy old toad.\n")
    typewriter('There is a lovely wet pool at the top of this road."\n')
    print()
    typewriter("They climbed up the road.\n")
    typewriter("It was terribly steep.\n")
    print()
    typewriter('"Im tired,” said the toad,\n')
    typewriter('"Will we stop for a sleep?"\n')
    print()
    forth_response = input("Do you think Harry should stop for a sleep?: \n (yes/no)\n")
    if forth_response == 'no' or forth_response == 'No':
        print("")
        chapter_five()

    elif forth_response == 'yes' or forth_response == 'Yes':        
        typewriter(
            "Oh dear, Harry overslept .....\n"
            "he missed the wedding!\n"
            "Game Over")





def chapter_five():
    typewriter("Wise choice ! \n")
    print()
    typewriter("Just over the hill they came to a pool.\n")
    typewriter('"This water," said Harry, "is beautifully cool,\n')
    typewriter("But now I need something to carry it in –\n")
    typewriter('A jug or a vase or a cup or a tin."\n')
    print()
    typewriter('"I think I can help," said a small squirly snail.\n')
    typewriter('"I can show you the way to a very fine pail."\n')
    fifth_response = input("Should Harry follow the snail ? \n (yes/no)\n")
    if fifth_response == 'no' or fifth_response == 'No':
        print("")
        chapter_six()

    elif fifth_response == 'yes' or fifth_response == 'Yes':        
        typewriter("So the snail and the scarecrow \n")
        typewriter("Set off on their way,\n")
        print()
        typewriter("But the snail was so slow …\n")
        typewriter("… it took more than a day.\n")
        print()
        typewriter("Harry has missed the wedding\n")
        typewriter("Game Over")



def chapter_six():
    print()
    typewriter("Good Advice\n")
    typewriter("Harry fills up his hat\n")
    typewriter("And runs back for the pink flowers to put in his hat\n")
    print()
    typewriter("Suddenly\n")
    print()
    typewriter("Who should appear on the farm\n")
    typewriter("But Harry O’Hay,\n")
    typewriter("With a hat of pink flowers in his arm.\n")
    print()
    typewriter("So Betty O’Barley and Harry O’Hay\n")
    typewriter("Wed one another the very next day\n")
    print()
    typewriter(f"Thanks for your help {name}, \n")
    typewriter("You helped make the best wedding ever, the best wedding yet,\n")
    typewriter("The wedding that no one will ever forget.\n")





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
  
