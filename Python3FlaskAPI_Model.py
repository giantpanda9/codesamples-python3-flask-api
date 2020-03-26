#Data Model
from json import loads

class APIClass():
	def __init__(self):
		pass
	def getFile(self):
		allData = open("data/output.json", "rt")
		allDataJson = allData.read()
		allData.close()
		return allDataJson
	def getData(self):
		allDataJson = self.getFile()
		returned = loads(allDataJson)
		return returned
