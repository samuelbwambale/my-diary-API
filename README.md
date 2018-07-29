[![Build Status](https://travis-ci.org/samuelbwambale/my_diary.svg?branch=CHALLENGE-THREE)](https://travis-ci.org/samuelbwambale/my_diary)[![Coverage Status](https://coveralls.io/repos/github/samuelbwambale/my_diary/badge.svg?branch=CHALLENGE-THREE)](https://coveralls.io/github/samuelbwambale/my_diary?branch=CHALLENGE-THREE)[![Maintainability](https://api.codeclimate.com/v1/badges/664c55f5d7a35cfc08e4/maintainability)](https://codeclimate.com/github/samuelbwambale/my_diary/maintainability)

# My Diary

MyDiary is an online journal where users can pen down their thoughts and feelings. 

### Features
1. Users can create an account and log in. 
2. Users can view all entries to their diary. 
3. Users can view the contents of a diary entry. 
4. Users can add or modify an entry. 

### Supported endpoints
  
| EndPoint                                      		| Functionality                                   |
| --------------------------------------------------------------|------------------------------------------------ |
| [GET /entries ](#)                            		| Fetch all entries                               |
| [GET /entries/<entryId>](#)                   		| Fetch single entry			          |
| [POST /entries](#)                     			| Create an entry	                          |
| [PUT  /entries/<entryId>](#)                  		| Modify an entry 		                  |


### Prerequisites
  1.	HTML/CSS
  2.	Javascript/ES6
  3.	Python/Flask

## Technologies

* Python 3.6 and above
* Flask Restful


## Requirements

* Install [Python](https://www.python.org/downloads/)
* Run `pip install virtualenv` on command prompt
* Run `pip install virtualenvwrapper` on command prompt
* Run `export WORKON_HOME=~/Envs` on command prompt
* Run `source /usr/local/bin/virtualenvwrapper.sh` on command prompt

## Setup

* Run `virtualenv -p python3 env-name` on command prompt
* Run `workon env-name` on command prompt
* Run `git clone` this repository and `cd` into the project root.
* Run `pip install -r requirements.txt` on command prompt

## Run the app

* Run `python app.py runserver` on command prompt
* View the app on `http://127.0.0.1:5000/`

## Tests

* Run `pytest tests` on command prompt

### GitHub pages

View the userinterface at (https://samuelbwambale.github.io/my_diary/UI/home.html)

### Heroku

The app is accessible on Heroku at (https://sb-my-diary.herokuapp.com/)

