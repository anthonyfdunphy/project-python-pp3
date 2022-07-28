# Snake Game

This is my creation of the famous snake game, popularised by the Nokia mobile phone version. This version runs in the terminal which has been deploed on Heroku. This game was created as a part of Portfolio Project 3 (PP3) for the Code Institute's Full Stack Web Development course. This project was created to share and showcase Python skills and to utilise the Heroku platform for deployment. Initally, the Code Institute template is used to create a base for a mock terminal app which I then modified with my own code.

![snake-game](https://i.imgur.com/D10H8Mw.png)

## User experiences

### User Stories

* As a user I want the instructions to be intuitive.
* As a user I want to be given cues on how I am doing.
* As a user I want to be able to restart the game if I am having a bad run.
* As a user I want text that is easy to see

### Fulfilment of user stories

Examples placed here with screenshots

![holding-image](https://miro.medium.com/max/1400/0*8aY8pX5CoNGImZU4.png)

----------------------
### Flowchat / Wireframes

This is a terminal operated game so there are not as many UX/UI options as previous projects. The terminal style favours this snake game design best I feel as it give the user a 'retro' feel to how the game is. Below is a basic flow chart of the logic of the snake game. The game begins on load of the page, the user then uses the cursor arrows to move the direction of the snake toward the food or away from the border. If the user hits the border or hits itself, the game ends and the users score is revealed to them. They are then prompted to see if they wish to play again, if they select yes then the game begins again.

![holding-image](https://i.imgur.com/PuHlcAk.png)

When creating this game, I spoke with my mentor and the suggestion was made to liven up the game interface by added color to it. The game has a black background with a yellow border. When the user eats the food, the background of the game becomes green momentarily to give the user some visual feedback that they are progressing in the game. Here are example photos of the game interface with color:


## Technologies Used

### Primary Language
Python

Frameworks and Libraries Used
* Python Standard Library.
* I used Heroku to deploy the live version.
* I used GitHub which allowed me to store my repository.
* My primary IDE was Gitpod which I used for creating and programming as I had unlimited hours through the Code Institute.

## Deployment

The project has been deployed to Heroku and can be found [here](https://snakegamead.herokuapp.com/) 

The Github repo can be found at the following [link](https://github.com/anthonyfdunphy/project-python-pp3)

Deployment of the site to Heroku was done as follows:

* Login to your Heroku account
* Create a New App
* Select the 'Settings' tab first
* Click on 'Reveal Config Vars'
* Add config vars in the KEY/VALUE pair data section
* Select 'Add Buildpack' - add Python and NodeJS
* Select the 'Deploy' tab
* For the Deplyoment Method select GitHub
* Connect to GitHub repo by entering YOUR-REPO-NAME, then Connect
* A message will confirm that your app was successfuly deployed
* Test that the site has successfully gone live by clicking on the 'View' button
* Your app can now be accessed via any browser at: https://YOUR-APP-NAME.heroku.com

## Validator Testing

### PEP8

Speak about using PEP8 for checking all my Python code

### Lighthouse

I will attached a screenshot here and show the final performance score of the website.

## Credits

Attaching any links to videos or books with code which helped me develop this project. I will be adding video to link below to demonstate this.

