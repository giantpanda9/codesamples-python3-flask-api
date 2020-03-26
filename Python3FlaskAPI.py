# Data Controller

import flask
from flask import request, jsonify
from Python3FlaskAPI_Model import APIClass

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def entry():
	return "<p>Small example Python 3 Flask API to share the data obtained by Python 2.7 Scrapy</p><p>Created with the single purpose to demonstrate ability to create APIs using Flask</p><p>Have fun! :)</p>"

@app.route('/pythonapi/getdata/all', methods=['GET'])
def getData():
	APIClassInstance = APIClass()
	# In this case we do not actually need an object to match
	APIResponse = APIClassInstance.getFile() # so loading just JSON data directly from file and using the function to load JSON file
	return APIResponse

@app.route('/pythonapi/getdata/byname', methods=['GET'])
def getDataByName():
	name = ""
	if "name" in request.args:
		name = str(request.args['name'])
	else:
		return "<p style='color:red'> Sorry, error! Please provide a name you wish to get the information for. </p>"
	APIClassInstance = APIClass()
	# In this case we need List of Dictionaries to match against
	allData = APIClassInstance.getData() # so we call for the method that returns it instead of text JSON
	returned = ""
	for item in allData:
		if name == item["name"]:
			returned = jsonify(item)
			break
	return returned
	
@app.route('/pythonapi/getdata/bydate', methods=['GET'])
def getDataByDate():
	date = ""
	if "date" in request.args:
		date = str(request.args['date'])
	else:
		return "<p style='color:red'> Sorry, error! Please provide a date you wish to get the Go version released at. </p>"
	APIClassInstance = APIClass()
	# In this case we need List of Dictionaries to match against
	allData = APIClassInstance.getData() # so we call for the method that returns it instead of text JSON
	returned = ""
	for item in allData:
		if date == item["date"]:
			returned = jsonify(item)
			break
	return returned

if __name__ == "__main__":
	app.run()
