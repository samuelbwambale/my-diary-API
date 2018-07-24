[![Coverage Status](https://coveralls.io/repos/github/samuelbwambale/my_diary/badge.svg?branch=master)](https://coveralls.io/github/samuelbwambale/my_diary?branch=master)

# My Diary

MyDiary is an online journal where users can pen down their thoughts and feelings. 

### Features
1. Users can create an account and log in. 
2. Users can view all entries to their diary. 
3. Users can view the contents of a diary entry. 
4. Users can add or modify an entry. 

  
| EndPoint                                      	| Functionality                                    |
| ----------------------------------------------	| ------------------------------------------------ |
| [GET /entries ](#)                            	| Fetch all entries                                |
| [GET /entries/<entryId>](#)                   	| Fetch single entry			           |
| [POST /entries](#)                     		| Create an entry	                           |
| [PUT  /entries/<entryId>](#)                  	| Modify an entry 		                   |


### Prerequisites
  1.	HTML/CSS
  2.	Javascript/ES6
  3.	Python/Flask


## Technologies

* Python 2.7 and above
* Flask Restful
* Flask Restful plus

## Requirements

* Install [Python](https://www.python.org/downloads/)
* Run `pip install virtualenv` on command prompt
* Run `pip install virtualenvwrapper-win` on command prompt
* Run `set WORKON_HOME=%USERPROFILES%\Envs` on command prompt

## Setup

* Run `git clone` this repository and `cd` into the project root.
* Run `mkvirtualenv venv` on command prompt
* Run `workon venv` on command prompt
* Run `pip freeze > requirements.txt` on command prompt
* Run `export FLASK_APP=app.py` on command prompt
* Run `python app.py runserver` on command prompt
* View the app on `http://127.0.0.1:5000/`


### GitHub pages

View the userinterface at (https://samuelbwambale.github.io/my_diary/UI/home.html)
