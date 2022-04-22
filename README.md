# Scurri Exercise #1
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”. 


* python3 -m pip install --upgrade pip
* python3 -m venv env(PS> virtualenv env)
* source env/bin/activate (PS> .\env\Scripts\activate.bat)
* pip3 install -r requirements.txt
* export FLASK_ENV=development
* export set FLASK_APP=app.webapp (PS> $env:FLASK_APP="webapp")
* python3 -m flask run --host=0.0.0.0 (PS> flask run)

# How to call the app locally

http://localhost:5000/print_numbers
# Tests

* coverage run -m pytest
* coverage report -m
# Heroku Deploy

* heroku login
* heroku create scurri-exercise-1-app
* git push heroku master / git push heroku HEAD:master
* heroku config:set SECRET_KEY=scurri_892840328239048
* heroku logs --tail