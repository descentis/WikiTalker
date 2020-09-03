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

	def putInDatabase(self, collection_name, file_name):
		collection = self.mongoClientDB[collection_name]
		json_file = open(file_name)
		data = json_file.read().strip("[]").split("\"},")
		for i in range(len(data)):
			if i != len(data)-1:
				data[i] += "\"}"
			ins = json.loads(data[i])
			collection.insert(ins)


	def deleteCollection(self, collection_name):
		collection = self.mongoClientDB[collection_name]
		collection.drop()



	def downloadAndLoad(self, collection_name, filename):
		self.download_file(filename)
		self.putInDatabase(collection_name, filename)


	def setCollectionName(self, dataCollectionName):
		self.dataCollectionName = dataCollectionName



	def getAlldata(self):
		mycol = self.mongoClientDB[self.dataCollectionName]
		arr = []
		for x in mycol.find():
		 	arr.append(x)
		return arr

	def totalNumberOfComments(self):
		mycol = self.mongoClientDB[self.dataCollectionName]
		return mycol.count()



	def getAllAuthors(self):
		mycol = self.mongoClientDB[self.dataCollectionName]
		return mycol.distinct('user')
    
	def allAuthorsContribution(self):
		mycol = self.mongoClientDB[self.dataCollectionName]
		pipeline = {"$group":{"_id":"$user", "count":{"$sum":1}}}
		dictionary = mycol.aggregate([pipeline])
		answer = {}
		for item in dictionary:
			answer[item["_id"]] = item["count"]
		return answer

	def getTopNContributors(self, n):
		authors = self.allAuthorsContribution()
		sorted_d = dict(sorted(authors.items(), key=operator.itemgetter(1),reverse=True))
		new_dict = {}
		num = 0
		for key, val in sorted_d.items():
			if num == n:
				break
			num += 1
			new_dict[key] = val
		return new_dict