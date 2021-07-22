# Python Text Based Game - The Scarecrows Wedding
# Story taken and adapted from a book of the same name By Julia Donaldson
# By Moira Hartigan

# This is a story about The scarecrows wedding - You have been invited but
# Harry and Betty need your help so the wedding can go ahead.

# Import time and sys to print typewriter effect.
import sys
import time

# player name
name = ""


def welcome_msg():
    """
    Function to print welcome graphics
    """
    print()
    print("##################################################################")
    print("#          ________          Welcome to                          #")
    print("#         |        |     The Scarecrows Wedding                  #")
    print("#         |        |                                             #")
    print("#  _______|________|_________           | *\-/* |_______         #")
    print("#     |   ___________   |             | |__/-\__|____   |        #")
    print("#     |  |           |  |             |  |           |  |        #")
    print("#     |  |   0   0   |  |             |  |   0   0   |  |        #")
    print("#     |  |     -     |  |             |  |     -     |  |        #")
    print("#     |  |   \___/   |  |             |  |   \___/   |  |        #")
    print("#     |  |           |  |             |  |           |  |        #")
    print("#     |  |___|\_/|___|  |             |  |___________|  |        #")
    print("#     |______|/ \|______|             |_______****______|        #")
    print("# _\_______|_______|______/_      _\_______|________|______/_    #")
    print("#  /                      \        /                       \     #")
    print("#                                                                #")
    print("#        Harry & Betty need your help for their wedding          #")
    print("##################################################################")
    print()


# typewriter style animation code adpted from
# https://www.youtube.com/watch?v=2h8e0tXHfk0

def print_text(text):
    """
    This function allows the text to be displayed letter by letter using sys
    import rather than a whole block of text - A time delay
    added will apply at the end of each sentance for 1 second
    unless "\n" is used.
    """
    for character in text:
        sys.stdout.write(character)  # print each character - print it
        sys.stdout.flush()  # display it

        if character == "\n":
            time.sleep(0.005)  # wait until until the next character
        else:
            time.sleep(0.03)  # 0.5 sec delay for the end of each sentance


welcome_msg()


def intro():
    """
    Intro function begins the game and welcomes the user
    by requesting their name in order to play
    """
    # while loop to ensure user adds their name
    while True:
        name = str(input("Please Tell me your name: \n"))
        if name == "":
            print("We need to check your name off the guestlist"
                  "to continue ....\n")
            continue
        else:
            break
    print_text(f"Welcome to Diddly Squat Farm {name}, \n")
    print_text("Thank you for joining us\n")
    print_text("for the Scarecrows Wedding.\n")
    print()
    start_game()


def start_game():
    while True:
        print()
        response = input("Would you like to start the game? \n(yes/no): \n")
        if response.lower().strip() == 'no':
            print_text("Maybe next time. Goodbye")
            print()
            game_over()
            play_again()
            break
        elif response.lower().strip() == 'yes':
            print()
            chapter_one()
            continue
        else:
            print_text("Hmmmm .... I dont understand that.\n")
            print_text("Please type yes or no.\n")
            print()
            continue


def chapter_one():
    """
    Function to move the player into the first chapter of the gaem once they
    have agreed to play
    """
    print_text("Ok Great ! \n")
    print_text("Here is the story so far ...... \n")
    print_text("Betty O'Barley and Harry O'Hay are scarecrows, \n")
    print_text("Harry loved Betty and Betty loved Harry, \n")
    print_text('So Harry said, “Betty, my beauty, lets marry!\n')
    print_text("Lets have a wedding, the best wedding yet,\n")
    print_text('A wedding no one will ever forget.”\n')
    print()
    print_text("Betty agreed, so they hugged \n")
    print_text("and they kissed. \n")
    print_text('Then Betty said, “Harry, dear, \n')
    print_text('Lets make a list.” \n')
    print()
    print_text('Harry gave Betty his arm \n')
    print_text("And set off on a hunt round the farm. \n")
    print()
    print()
    while True:
        response = input("Can you help Harry find some Pink flowers \n"
                         "for the list and get back for his wedding?\n"
                         "(yes/no) : \n")
        if response.lower().strip() == 'yes':
            print()
            chapter_two()
        elif response.lower().strip() == 'no':
            print_text("Ok then, stay here, until Harry gets back.\n")
            print_text("Betty needs your help anyway to write\n")
            print_text("her wedding vows while Harry is off \n"
                       "finding flowers.....\n")
            print()
            wedding_vows()
        else:
            print_text("Hmmmm .... I dont understand that.\n")
            print_text("Please type yes or no.\n")
            print()
            


def wedding_vows():
    """
    user takes a different route if they choose not to help Harry find flowers
    instead the user helps betty write her wedding vows
    """
    while True:
        emotion = str(input("Enter an emotion : \n"))
        if emotion == "":
            print("oops you need to enter an emotion to continue ....")
            continue
        noun = str(input("Enter a noun (A person, place or thing) : \n"))
        if noun == "":
            print("oops you need to enter a noun to continue ....")
            continue
        adjective = str(input("Enter an adjective (A word that describes a noun) : \n"))
        if adjective == "":
            print("oops you need to enter an adjective to continue ....")
            continue
        second_adjective = str(input("Enter another adjective : \n"))
        if second_adjective == "":
            print("oops you need to enter an adjective to continue ....")
            break
        print()
        print_text("Nice work .... you make a good team \n")
        print_text("Lets see what you came up with! \n")
        print()
        print_text("Betty's wedding vows \n")
        print_text("####################\n")
        print()
        print_text(f"I am so {emotion} to have you all here today ")
        print_text(f"at our {adjective} wedding.\n")
        print_text("I promise to love you Harry, as long as we both shall live.\n")
        print_text(f"I offer my {second_adjective} vow to be your \n")
        print_text(f"forever {noun} in sickness and in health.\n")
        print()
        print_text("I'll love you all the days of my life \n")
        print_text("and I hope to live happily ever after.\n")
        print()
        chapter_seven()


def chapter_two():
    """
    function allow player onto the next chapter of the game
    after they agree to help Harry find the pink Flowers
    otherwise the game ends. This level allows the player a choice in
    response.
    """
    print_text("Flowers were the only thing left on the list \n")
    print_text('Harry said “Betty, dear, I can find those. \n')
    print_text('Why don’t I pick some while you have a doze?” \n')
    print()
    print_text("I can find you a field of pink flowerzzzzz! \n")
    print_text("Follow me! ..... \n")
    print_text("Buzzed a big stripy bee. \n")
    print()
    print_text("What should Harry do? \n ")
    print_text("1.) Follow the bee \n")
    print_text(" 2.) Go to the farm shop to buy some flowers instead \n")
    print_text(" 3.) Call the florist and have them deliver the flowers \n")
    print()
    while True:
        response = input("Choose option (1, 2 or 3): \n ")
        if response == '1':
            print()
            chapter_three()
            continue
        elif response == '2':
            print()
            print_text("oh no the Farm Shop is sold out\n")
            print_text("Betty is not pleased\n")
            print_text("The Wedding is off !")
            print()
            game_over()
            break
        elif response == '3':
            print()
            print_text("You are a Scarecrrow !!! \n")
            print_text("You have no phone to make the call and no money \n"
                       "to pay for the flowers.\n")
            print()
            game_over()
            break
        else:
            print_text("Hmmmm .... I dont understand that.\n")
            print_text("Please type yes or no.\n")
            print()


def chapter_three():
    """
    Function to allow player to move to chapter three
    and looks for the player to give a yes/ no response
    """
    print_text("So the bee led the way, and they travelled for hours\n")
    print_text("Till they come to a field full of pretty pink flowers.\n")
    print_text('Harry is now thinking "I wont pick them yet.\n')
    print_text('I will need to find water, to keep their stalks wet.” \n')
    print()
    while True:
        response = input("Do you think Harry needs to find water?: \n"
                         "(yes/no)\n")
        if response.lower().strip() == 'yes':
            print("")
            chapter_four()
            continue
        elif response.lower().strip() == 'no':
            print_text("Harry returns with the flowers..... \n")
            print_text("but they have died without water!\n")
            print_text("oh dear Betty is not pleased and the wedding\n"
                       "is off.\n")
            print()
            game_over()
            play_again()
            break
        else:
            print_text("Hmmmm .... I dont understand that.\n")
            print_text("Please type yes or no.\n")
            print()
            continue


def chapter_four():
    """
    Function to move player into chapter four,
    here the player uses yes/no again to choose an option
    """
    print_text('"Just follow me",\n')
    print_text("croaked a lumpy old toad.\n")
    print_text('There is a lovely wet pool at the top of this road."\n')
    print()
    print_text("They climbed up the road.\n")
    print_text("It was terribly steep.\n")
    print()
    print_text('"Im tired,” said the toad,\n')
    print_text('"Will we stop for a sleep?"\n')
    print()
    while True:
        response = input("Do you think Harry should stop for a sleep?: \n"
                         "(yes/no)\n")
        if response.lower().strip() == 'no':
            print("")
            chapter_five()
            continue
        elif response.lower().strip() == 'yes':
            print_text("Oh dear, Harry overslept .....\n")
            print_text("he missed the wedding!\n")
            print()
            game_over()
            break
        else:
            print_text("Hmmmm .... I dont understand that.\n")
            print_text("Please type yes or no.\n")
            print()
            continue


def chapter_five():
    """
    The story continues to chapter 5 and a yes/ no response is requested
    here again
    """
    print_text("Wise choice ! \n")
    print()
    print_text("Just over the hill they came to a pool.\n")
    print_text('"This water," said Harry, "is beautifully cool,\n')
    print_text("But now I need something to carry it in –\n")
    print_text('A jug or a vase or a cup or a tin."\n')
    print()
    print_text('"I think I can help," said a small squirly snail.\n')
    print_text('"I can show you the way to a very fine pail."\n')
    while True:
        print()
        response = input("Should Harry follow the snail ? \n(yes/no)\n")
        if response.lower().strip() == 'no':
            print()
            chapter_six()
            
        elif response.lower().strip() == 'yes':
            print_text("So the snail and the scarecrow \n")
            print_text("Set off on their way,\n")
            print()
            print_text("But the snail was so slow …\n")
            print_text("… it took more than a day.\n")
            print()
            print_text("Harry has missed the wedding\n")
            print()
            game_over()
            break
        else:
            print_text("Hmmmm .... I dont understand that.\n")
            print_text("Please type yes or no.\n")
            print()
            


def chapter_six():
    """
    Final chapter function where the story comes to an end and
    the user can read the ending, they are thanked for their help
    """
    print()
    print_text("Good Advice\n")
    print_text("Harry fills up his hat\n")
    print_text("And runs back for the pink flowers to put in his hat\n")
    print()
    print_text("Suddenly\n")
    print()
    print_text("Who should appear on the farm\n")
    print_text("But Harry O’Hay,\n")
    print_text("With a hat of pink flowers in his arm.\n")
    print()
    chapter_seven()


def chapter_seven():
    print_text("So ............ \n")
    print_text("Betty O’Barley and Harry O’Hay\n")
    print_text("Wed one another the very next day\n")
    print()
    print_text("Thanks for your help,\n")
    print_text("You helped make the best wedding ever, \n"
               "the best wedding yet,\n")
    print_text("The wedding that no one will ever forget.\n")
    print()
    happy_ending()


def game_over():
    """
    Function for when the user chooses the wrong option/answer
    prints game over
    """
    print("")
    print("##############################")
    print("#                            #")
    print("#        |GAME OVER|         #")
    print("#                            #")
    print("##############################")
    print("")
    play_again()


def happy_ending():
    """
    function to display end of game message when user reaches the end of
    the story
    """
    print()
    print("################################")
    print("#                              #")
    print("#        ****     ****         #")
    print("#       ******   ******        #")
    print("#      ******** ********       #")
    print("#      *******THE*******       #")
    print("#       ******END******        #")
    print("#        *************         #")
    print("#         ***********          #")
    print("#          *********           #")
    print("#           *******            #")
    print("#             ***              #")
    print("#              *               #")
    print("#                              #")
    print("################################")
    print()
    play_again()


def play_again():
    """
    Function to allow the user to restart
    the game from the terminal
    """
    print_text("To play again click the 'Play again' button\n")
    print()
    print_text("or\n")
    while True:
        response = input("type 'yes': \n")
        if response.lower().strip() == "yes":
            start_game()
            continue
        elif response.lower().strip() != "yes":
            print("I dont understand that....")
            continue
        else:
            print_text("Thanks for playing!")
            break

intro()
