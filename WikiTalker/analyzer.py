import pymongo
import json
import operator
import math
import matplotlib.pyplot as plt
import requests

def download_file(filename):
	file = filename
	url = 'https://wikitalkpages.s3.ap-south-1.amazonaws.com/' + file +'.json'
	r = requests.get(url, allow_redirects=True)
	open(file + '.json', 'wb').write(r.content)


def putInDatabase(collection_name, file_name, myclient, mongoClientDB):
	collection = mongoClientDB[collection_name]
	json_file = open(file_name)
	data = json_file.read().strip("[]").split("\"},")
	for i in range(len(data)):
		if i != len(data)-1:
			data[i] += "\"}"
		ins = json.loads(data[i])
		collection.insert(ins)

class Analyzer:



	def __init__(self, myclient, mongoClientDB):
		self.myclient = myclient
		self.mongoClientDB = mongoClientDB
		self.dataCollectionName = None

	def download_file(self, filename):
		file = filename
		url = 'https://wikitalkpages.s3.ap-south-1.amazonaws.com/' + file +'.json'
		r = requests.get(url, allow_redirects=True)
		json_file = file + '.json'
		open(filename, 'wb').write(r.content)