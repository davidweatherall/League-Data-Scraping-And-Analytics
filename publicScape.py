

# PLAN:

# Start off with challenger player ID:

# Get 20 recent games of player, for each game check if ranked and check if .

# Get data required

# at same time find a player id

# go to next game

# every 100 games, store data in a json and create a json file

# continue indefinitely

import urllib.request, json
import time



apiKey = 'RGAPI-5409d370-8281-4589-b8d0-983bb13e6166'

UserId = 0
UsersDone = []
AvailableIds = [28224933]
GamesDone = []


ChampGetFB = {}
ChampTeamFB = {}
ChampFirstDeath = {}
ChampTotalPlayed = {}
PositionGetFB = {}
PositionDieFB = {}
MatchesDone = []
PeopleChecked = []


i = 0

while i < 2000:

	if UserId == 0:
		i_len = 0
		while i_len < len(AvailableIds):
			if AvailableIds[i_len] not in UsersDone:
				UserId = AvailableIds[i_len]
				print('setting UserId as {}'.format(UserId))
				i_len = len(AvailableIds)
			i_len += 1



	if UserId == 0:
		print('UserId 0, breaking')
		break

	UsersDone.append(UserId)

	print('-----')
	print('stage 1')
	print(i)
	print('-----')
	urlMatchHistory = 'https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/' + str(UserId) + '/recent?api_key=' + apiKey
	try:
		with urllib.request.urlopen(urlMatchHistory) as url:
			data = json.loads(url.read().decode())

		for match in data['matches']:
			if match['queue'] == 420 and match['gameId'] not in GamesDone:

				gameId = match['gameId']
				GamesDone.append(gameId)
				urlString = 'https://euw1.api.riotgames.com/lol/match/v3/matches/' + str(gameId) + '?api_key=' + str(apiKey)
				
				try:
					with urllib.request.urlopen(urlString) as url:
						json_raw = url.read().decode()
						dataGame = json.loads(json_raw)

					json_file = open('jsons/{}.json'.format(str(gameId)), 'wb')
					json_file.write(json_raw.encode('utf-8'))
					json_file.close

					for participantid in dataGame['participantIdentities']:

						accId = participantid['player']['accountId']

						if accId not in AvailableIds:
							AvailableIds.append(accId)
					
					for person in dataGame['participants']:

						partic_i = 0

						if person['championId'] in ChampTotalPlayed:
							ChampTotalPlayed[person['championId']] += 1

						else:
							ChampTotalPlayed[person['championId']] = 1


					if dataGame['teams'][0]['firstBlood']:
						ii = 0
						while ii < 5:
							participant = dataGame['participants'][ii]
							ChampId = participant['championId']
							
							if ChampId  in ChampTeamFB:
								ChampTeamFB[ChampId] += 1
							else:
								ChampTeamFB[ChampId] = 1


							ii += 1


					else:
						ii = 5
						while ii < 10:
							participant = dataGame['participants'][ii]
							ChampId = participant['championId']
							
							if ChampId  in ChampTeamFB:
								ChampTeamFB[ChampId] += 1
							else:
								ChampTeamFB[ChampId] = 1


							ii += 1
						

				except urllib.error.HTTPError as err:
					print(str(err))
					if(str(err) == 'HTTP Error 429: Too Many Requests'):
						print('sleeping 1')
						time.sleep(25)

	except urllib.error.HTTPError as err:
		print(str(err))
		if(str(err) == 'HTTP Error 429: Too Many Requests'):
			print('sleeping 2')
			time.sleep(25)

			i-=1

		if(err.code == 404):
			UserId = 0

	UserId = 0
	i+=1

print(i)
print(ChampTeamFB)
print(ChampTotalPlayed)

ChampFBCalc = {}



with open('/home/david/Data/champions.json') as champJson:
	champArray = json.load(champJson)

for champ in ChampTotalPlayed:
	if champ not in ChampTeamFB:
		ChampTeamFB[champ] = 0

	ChampFBCalc[champ] = ChampTeamFB[champ] / ChampTotalPlayed[champ]

sChampFBCalc = sorted(ChampFBCalc, key=ChampFBCalc.get, reverse=True)

for champ in sChampFBCalc:
	print('{} fb rate is {}% Sample size: {}'.format(champArray['data'][str(champ)]['name'], round(100 * ChampFBCalc[champ] ), str(ChampTotalPlayed[champ])))
