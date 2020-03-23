# codesamples-python3-flask-api
Python 3 Flask API in virtualenv
# Description
Simple API on Go lang code example - made using Flask microframework and codesamples-python-scrapy-scrap-golang-site - https://github.com/giantpanda9/codesamples-python-scrapy-scrap-golang-site project results
# Purposes
To demonstrate ability to create APIs on Python 3 and Flask and to study how to virtualenv works
# Requirements
1) Python 3
2) Flask
3) virtualenv
4) codesamples-python-scrapy-scrap-golang-site - https://github.com/giantpanda9/codesamples-python-scrapy-scrap-golang-site results - output.json (included)
# Installation instructions (approximate, not the last ones to follow):
1) sudo pip3 install virtualenv
2) mkdir Python3FlaskAPI
3) cd Python3FlaskAPI
4) virtualenv Python3FlaskAPI
5) source Python3FlaskAPI/bin/activate
6) pip install gunicorn flask
7) copy the file to Python3FlaskAPI/ (just near the second folder Python3FlaskAPI in Python3FlaskAPI folder)
8) copy the file data/output.json (the whole folder) to the secondary Python3FlaskAPI folder inside the project or simply copy /Python3FlaskAPI fodler from the git to the Flask virtualenv'ed project folder
9) Overall you structure should be similar to the one in github except for the files created by Flask
9) sudo ufw allow 5000
10) python Python3FlaskAPI.py
11) [optional, done playing?] deactivate
 # How to run?
1) 127.0.0.1:5000/pythonapi/getdata/all - should return all the data available
2) http://127.0.0.1:5000/pythonapi/getdata/byname?name=rsa - should return data for Go lang rsa module
3) http://127.0.0.1:5000/pythonapi/getdata/bydate?date=February%202019 - should return information about Go release from February 2019
# Notes
1) Example input data conatined within Python3FlaskAPI/data/output.json file
2) ouput.json named like so because it actually an output file of the project - codesamples-python-scrapy-scrap-golang-site - https://github.com/giantpanda9/codesamples-python-scrapy-scrap-golang-site
3) The virtualenv project kept under development settings in virtualenv during the development 
4) project kept with simple structure to allow quick overview - I know MVC pattern, but shall demonstrate this abilty in dedicated project, if you do not mind - and this is solely to demonstrate the API creation abilities
5) Logic is similar to https://github.com/giantpanda9/codesamples-golang-gorilla-mux-api and https://github.com/giantpanda9/codesamples-golang-gorilla-mux-api-no-marshall-edition
