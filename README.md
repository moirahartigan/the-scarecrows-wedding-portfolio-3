


## Portfolio Project 3: _Python Essentials_
A text based story game built with Python


## Demo

[View the Live Website Here](https://the-scarecrows-wedding.herokuapp.com/)
<p align ="center"> 
<img src="https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3/blob/main/assets/images/the-scarecrows-wedding.png">
</p>


# Table of Contents
+ [Design](#design)
+ [Features](#features)
  + [Existing Features](#existing-features)
  + [Future Features](#future-features)
+ [Technologies Used](#technologies-used)
+ [Testing](#testing)
  + [Bugs & Fixes](#bugs-&-fixes)
+ [Deployment](#deployment)
  + [Creating the App](#creating-the-app)
  + [Setting up the Heroku App](#setting-up-the-heroku-app)
  + [Deployment through Heroku](#deployment-through-Heroku)
  + [How to Fork the respository](#how-to-fork-the-respository)
  + [How to clone the repository](#how-to-clone-the-repository)
+ [Credits](#credits)
  + [Code](#code)
  + [Acknowledgements](#acknowledgements)
  
***
***
# Design
This is a text-based game that the user will operate in the command line. The story is taken from the Book "The Scarecrows Wedding" by Julia Donaldson and has been adapted into a text-based story game. The aim of the game is to assist Harry in finding flowers for his wedding by helping him make some decisions along the way. If the user decides not to help Harry they are asked to help Betty instead and the story takes a different path. Here a mad lib has been incorporated and the user is asked to input some data to help Betty write her wedding vows. Once complete the vows are printed out and the story continues. This game is completely written in Python.

  [Logic Flow Chart](https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3/blob/main/assets/images/flowchart%20-the-scarecrows-wedding.png)

# Features

## Current Features
+ Upon launching the app a welcome graphic is displayed. This identifies the theme of the game and illustrates the game/story title "The scarecrows Wedding.

<p align="center">  
 <img src="https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3/blob/main/assets/images/welcome_msg.png"> 
 </p>

The run program button has been updated to a "play again" button to allow the user to restart the game at any time by clicking this.

<p align="center">  
 <img src="https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3/blob/main/assets/images/play-again-button.png"> 
 </p>
 
 In addtition to this, the user has been given the option the replay the game from the terminal by typing "yes". This option appears if the user has chosen the wrong path, and the game ends or if they have completed the game and wish to play again.
 
 <p align="center">  
 <img src="https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3/blob/main/assets/images/game-over.png"> 
 </p>

The game requests a yes/no answer for the majority of the questions however a number choice has been added to keep it interesting. At chapter 3 the user is asked to choose an option from 1 to 3 to help Harry make his decision on what to do.

<p align="center">  
 <img src="https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3/blob/main/assets/images/number-selection.png"> 
 </p>

A second route has also been added to this story and the game incorporates a mad lib form which allows the user to input words in order to generate Bettys wedding vows. Once the vows have been printed the story continues. 

<p align="center">  
 <img src="https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3/blob/main/assets/images/wedding-vows.png"> 
 </p>
 
 Finally all of the questions has been validated to ensure the user inputs information where requested before the game continues and should any incorect data be used, the user is provided with feedback on what has gone wrong and the question is asked again.  
 
 <p align="center">  
 <img src="https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3/blob/main/assets/images/name-entry-validation.png"> 
 </p>
 
 <p align="center">  
 <img src="https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3/blob/main/assets/images/yes-no-validation.png"> 
 </p>
 
 <p align="center">  
 <img src="https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3/blob/main/assets/images/wedding-vows-input-validation.png"> 
 </p>

## Future Features
+ I would like to add a choice of story so that when the player opens the app they can choose from a list of stories each with different themes.
+ I would like to add sound animation to the game to allow for sound effects to play when the user makes it to the end of the game or makes the wrong decision. 
+ I would like to add some additional options to the wedding vows path, in the form of a list within the mad lib. This would give the user a choice of words in addition to the ones they have already inputted themselves - this would generate another paragraph of vows from a dictionary.
+ I would like to refactor the yes/no question responses to reduce the code and make it cleaner.

***
***

# Technologies Used

## Languages Used
1. [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - To create a basic site.

## Frameworks Libraries and Programmes Used
* [GitHub](https://github.com/) - used to host repository.
* [GitPod](https://gitpod.io/workspaces) - used to develop project and organise version control.
* [GitHub Pages](https://github.com/moirahartigan/Ms1-Schools-Out-Childcare/settings/pages) - used to deploy the site.
* [Heroku](https://www.heroku.com/home) - App used to run the game
* [Diagram Software & Flow Chart Maker](https://www.diagrams.net/) - Used to create a flowchart
***
***
# Testing
## Manual Testing
As each function was created print statements were used to check the outcome. Once the game was complete manual texting of each path/ choice and option was carried out to ensure the game run as designed and also to ensure each response was dealt with correctly. Family members also played the game and tested its functionality. Once all bugs and issues had been resolved the game ran smoothly.

The game was again manually tested through the heroku app to ensure it ran smoothly and without errors.

## Validator Testing
At the completion or heavy editing of sections, I used the following to check my code for errors:


### <em>PEP8 Linter</em>

  <p align="center">  
 <img src="https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3/blob/main/assets/images/pep-8-validation.png"> 
 </p>
  
 
 
    
* Following corrections no errors were found.
 

## Bugs & Fixes
* A number of errors were found when the code was passed through the [PEP8 validator](http://pep8online.com). The main issues were line length - where lines were over 79 characters. Other issues was the presence of white space. These errors were fixed and the code error fee on the final check.
  * FIXED
* A bug was found when the game was complete and the play again function had been called - the user had the option to either click the "play again" button or type yes in the terminal to restart the game, however if the user hit enter and didn't add "yes" a question would appear from an earlier part of the game. This was corrected by adding a while loop to the function and controlling the iteration with a continue and break statement. This resolved the bug.
   * FIXED
* Finally, the output animation for the text works perfectly in the terminal, however when pushed to the heroku app the output is not displaying the text as desired. While the text does not appear in blocks which was the case before the animation was added, the flow and speed of the text is no the same as in the terminal.
   * No fix found.
***
***
# Deployment
## Creating the App
This application will be deployed via [Heroku](https://dashboard.heroku.com/apps)

* Ensure all code is correct and ready for deployment.
* Enter the following code to import the required dependencies to the requirements.txt file:
    * pip3 freeze > requirements.txt

* Heroku will use this file to import the dependencies that are required.
* Log into Heroku or sign up for a free account.
* If signing up, you will need to wait and accept an authentication email.
* Navigate to Dashboard.
* Click "New" and select "create new app" from the drop-down menu. This is found in the top right corner of the window.
* Provide a unique name for your application and select your region.
* Click "Create App".

## Setting up the Heroku App 
* Navigate to "Settings" and scroll down to "build packs".
* Click "build packs" and then click both "python" and "node.js"(node.js is needed for the mock terminal.)
* Take note of the order and ensure that the python build pack is above the node.js build pack, You can click and drag the packs to re-arrange them.

This site was deployed through GitHub Pages using the following steps:
## Deployment through Heroku
* Navigate to the "Deploy" section.
* Scroll down to "Deployment Method" and select "GitHub".
* Authorize the connection of Heroku to GitHub.
* Search for your GitHub repository name, and select the correct repository.
* For Deployment there are two options, Automatic Deployments or Manual.
* Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
* Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so.
* Ensure the correct branch is selected "master/Main", and select a deployment method. For this project I chose Automatic Deployment.

## How to Fork the respository
* Log into GitHub.
* In Github go to (https://github.com/moirahartigan/the-scarecrows-wedding-portfolio-3).
* In the top right hand corner click "Fork".
* A copy of the repository will then be added to your repositories page.

## How to clone the repository
* Go to the GitHub repository.
* Locate the Code button which is to the left of the green gitpod button and click it.
* Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard.
* Open Git Bash.
* Change the current working directory to the one where you want the cloned directory.
* Type git clone and paste the URL from the clipboard.
* Press Enter to create your local clone.

***
***
# Credits
## Code
* [youtube](https://www.youtube.com/watch?v=2h8e0tXHfk0) typewriter style animation code adpted from this tutorial.
* [w3schools](https://www.w3schools.com/) was used as a general source of knowledge 
* [MND Web Docs](https://developer.mozilla.org) was used as a general source of knowledge.
* [Stack Overflow](https://stackoverflow.com/) was used to assist during debugging.

## Content
* The story for this game has been taken and adapted from the book "The Scarecrows wedding" by Julia Donaldson

  
## Acknowledgements
* I would like to thank the Slack Community for their endless support.
* I would like to thank Kasia Bogucka our class cohort facilitator for her constant assistance and encouragement.
* I would like to thank my Husband for giving me the childfree time to work on this project and to my whole family for playing and testing the game.
* Finally, I would like to thank my mentor Oluwafemi Medale for his guidence and feedback throughout this portfolio project.
 
