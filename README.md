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

![flow-chart](https://i.imgur.com/PuHlcAk.png)

When creating this game, I spoke with my mentor and the suggestion was made to liven up the game interface by added color to it. The game has a black background with a yellow border. When the user eats the food, the background of the game becomes green momentarily to give the user some visual feedback that they are progressing in the game. Here are example photos of the game interface with color:

#### Default game colors
![default](https://i.imgur.com/PNiwLLB.png)


#### User feedback - snake eats food
![food-eat](https://i.imgur.com/OGmgkQe.png)


## Technologies Used

### Primary Language
Python

Frameworks and Libraries Used
* Python Standard Library.
* I used GitHub which allowed me to store my repository.
* I used Heroku to deploy the live version.
* Colorama library was used to add color print to the terminal for some of the text areas.
* My primary IDE was Gitpod which I used for creating and programming as I had unlimited hours through the Code Institute.
* Diagrams.net was used to create a flow chart to illustrate the logic of the game.

## Deployment

The project has been deployed to Heroku and can be found [here](https://snakegamead.herokuapp.com/) 

The Github repo can be found at the following [link](https://github.com/anthonyfdunphy/project-python-pp3)

To deploy my site to Heroku - the following was done:

* Login to your Heroku account and selected "create new app"
* The 'settings' was seclected
* Select'Reveal Config Vars'and add config vars in the KEY/VALUE pair data section
* Select 'Add Buildpack' - add Python and NodeJS
* Select the 'Deploy' tab
* Github was selected as the deployment method
* Connection was made to the repo by inputting my repo name and clicking connect
* A message will confirm that your app was successfuly deployed
* When the site has been deployed, a 'view' button will become active which can be clicked to show the live site

## Validator Testing

### PEP8

To ensure that the code adhered to the Python style guidelines, I used the online tool - The PEP8 Online linter. I got the follow result when I submitted my code for validation.

![code-validation](https://i.imgur.com/hFBVVFA.png)

## Credits

Attaching any links to videos or books with code which helped me develop this project. I will be adding video to link below to demonstate this.

