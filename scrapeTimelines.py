
import urllib.request
import json
import time
import os



apiKey = ''

gamesArray = []

for filename in os.listdir('jsons'):
	gamesArray.append(filename)

i = 0

while i < len(gamesArray):

	print(str(i))

	gameId = gamesArray[i].replace('.json', '')
	urlString = 'https://euw1.api.riotgames.com/lol/match/v3/timelines/by-match/'+str(gameId)+'?api_key=' + apiKey
	
	try:
		with urllib.request.urlopen(urlString) as url:
			json_raw = url.read().decode()
			dataGame = json.loads(json_raw)

		json_file = open('jsons/timeline/{}.json'.format(str(gameId)), 'wb')
		json_file.write(json_raw.encode('utf-8'))
		json_file.close

	except urllib.error.HTTPError as err:

		print(str(err))

		if err.code == 429:
			print('sleeping 2')
			time.sleep(25)

			i-=1

	i += 1