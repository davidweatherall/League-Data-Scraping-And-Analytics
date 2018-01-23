import urllib.request
import os
import json
import math


y = 0
z = 0

path = 'game/'
games = os.listdir(path)

for game in games:
	y += 1
	file = 'game/' + game

	f = open(file, 'r')
	text = f.read()
	encjson = json.loads(text)

	if(encjson['teams'][0]['firstBlood'] is True):
		z += 1

os.system('clear')
print('Blue side FB is {}%. Sample size: {}'.format(str(round((z/y)*100)), str(y)))
print('Red side FB is {}%. Sample size: {}'.format(str(100 - round((z/y)*100)), str(y)))
