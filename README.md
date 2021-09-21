# The-Pitcher
## Author
Laurette Mong'ina @2021

# Description
This  is a flask application that allows users to post one minute pitch and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows an individual to signup and to be authenticated to use the app.

## Live Link
[View Site](https://pitch-paree.herokuapp.com/)


## User Stories

* As a user, I would like to see the pitches other people have posted.
* As a user, I would like to vote on the pitch they liked and give it a downvote or upvote.
* As a user, I would like to be signed in for me to leave a comment
* As a user, I would like to receive a welcoming email once I sign up.
* As a user, I would like to view the pitches I have created in my profile page.
* As a user, I would like to comment on the different pitches and leave feedback.
* As a user, I would like to submit a pitch in any category.
* As a user, I would like to view the different categories.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | *On page load* | Get all posts, Select between signup and login|
| Select SignUp| *Email,Username,Password* | Redirect to login|
| Select Login | *Username* and *password* | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | *Comment* | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|





## Development Installation
To get the code..

1. Cloning the repository:
  bash
  https://github.com/LauretteMongina/The_pitcher.git
  
2. Move to the folder and install requirements
  bash
  cd The-Pitcher
  pip install -r requirements.txt
  
3. Exporting Configurations
  bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  
4. Running the application
  bash
  python3.8 manage.py server
  
  
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)
* bootstrap
* css


## Known Bugs
* No known bugs.

## Contact Information 

If you have any question or contributions, please email me at [monginalaurette@gmail.com]

## License
* MIT License:
* Copyright (c) 2021 Laurette