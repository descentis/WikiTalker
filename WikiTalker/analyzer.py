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