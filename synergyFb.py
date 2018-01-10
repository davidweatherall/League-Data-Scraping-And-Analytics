
import urllib.request
import os
import json
import math


def champidtoname(id):	
	champdict = {'77': 'Udyr', '427': 'Ivern', '85': 'Kennen', '18': 'Tristana', '78': 'Poppy', '9': 'Fiddlesticks', '267': 'Nami', '15': 'Sivir', '19': 'Warwick', '54': 'Malphite', '164': 'Camille', '14': 'Sion', '6': 'Urgot', '61': 'Orianna', '45': 'Veigar', '44': 'Taric', '60': 'Elise', '20': 'Nunu', '106': 'Volibear', '110': 'Varus', '62': 'MonkeyKing', '161': 'Velkoz', '429': 'Kalista', '27': 'Singed', '498': 'Xayah', '83': 'Yorick', '53': 'Blitzcrank', '133': 'Quinn', '245': 'Ekko', '74': 'Heimerdinger', '57': 'Maokai', '25': 'Morgana', '163': 'Taliyah', '63': 'Brand', '107': 'Rengar', '10': 'Kayle', '41': 'Gangplank', '203': 'Kindred', '223': 'TahmKench', '127': 'Lissandra', '13': 'Ryze', '105': 'Fizz', '17': 'Teemo', '117': 'Lulu', '254': 'Vi', '34': 'Anivia', '102': 'Shyvana', '7': 'Leblanc', '92': 'Riven', '31': 'Chogath', '43': 'Karma', '222': 'Jinx', '236': 'Lucian', '39': 'Irelia', '141': 'Kayn', '86': 'Garen', '26': 'Zilean', '99': 'Lux', '4': 'TwistedFate', '58': 'Renekton', '68': 'Rumble', '134': 'Syndra', '51': 'Caitlyn', '29': 'Twitch', '421': 'RekSai', '497': 'Rakan', '240': 'Kled', '266': 'Aatrox', '111': 'Nautilus', '36': 'DrMundo', '32': 'Amumu', '113': 'Sejuani', '121': 'Khazix', '50': 'Swain', '72': 'Skarner', '126': 'Jayce', '120': 'Hecarim', '104': 'Graves', '48': 'Trundle', '143': 'Zyra', '33': 'Rammus', '268': 'Azir', '201': 'Braum', '23': 'Tryndamere', '69': 'Cassiopeia', '112': 'Viktor', '38': 'Kassadin', '89': 'Leona', '24': 'Jax', '516': 'Ornn', '131': 'Diana', '432': 'Bard', '76': 'Nidalee', '42': 'Corki', '90': 'Malzahar', '142': 'Zoe', '1': 'Annie', '119': 'Draven', '64': 'LeeSin', '8': 'Vladimir', '37': 'Sona', '114': 'Fiora', '40': 'Janna', '59': 'JarvanIV', '420': 'Illaoi', '5': 'XinZhao', '35': 'Shaco', '103': 'Ahri', '67': 'Vayne', '84': 'Akali', '202': 'Jhin', '150': 'Gnar', '91': 'Talon', '55': 'Katarina', '30': 'Karthus', '238': 'Zed', '2': 'Olaf', '28': 'Evelynn', '98': 'Shen', '16': 'Soraka', '56': 'Nocturne', '11': 'MasterYi', '122': 'Darius', '157': 'Yasuo', '96': 'KogMaw', '12': 'Alistar', '412': 'Thresh', '82': 'Mordekaiser', '115': 'Ziggs', '81': 'Ezreal', '101': 'Xerath', '79': 'Gragas', '75': 'Nasus', '21': 'MissFortune', '136': 'AurelionSol', '22': 'Ashe', '80': 'Pantheon', '3': 'Galio', '154': 'Zac'}
	return champdict[str(id)]



ChampTeamNoFB = {}
ChampTeamFB = {}
ChampFirstDeath = {}
ChampTotalPlayed = {}



gamesArray = []

for filename in os.listdir('jsons'):
	if filename != 'timeline':
		gamesArray.append(filename)

i = 0

lenArray = len(gamesArray)

while i < lenArray:

	print("Progress: {} of total games {}".format(str(i), str(lenArray)))
	gameId = gamesArray[i]


	file = 'jsons/' + gameId
	print(file)
	f = open(file, 'rb')
	text = f.read()
	encjson = json.loads(text.decode())


	if encjson['teams'][0]['firstBlood']:

		champIds = []

		ii = 0
		while ii < 5:
			participant = encjson['participants'][ii]
			champIds.append(participant['championId'])

			ii += 1



		champIds = sorted(champIds)


		ii = 5
		while ii < 10:
			participant = encjson['participants'][ii]
			champIds.append(participant['championId'])

			ii += 1



		ii = 0
		while ii < 5:

			iii = ii

			while iii < 4:
				
				dictEntry = "{},{}".format(champIds[ii], champIds[iii+1])

				if(dictEntry not in ChampTeamFB):
					ChampTeamFB[dictEntry] = 0

				if(dictEntry not in ChampTotalPlayed):
					ChampTotalPlayed[dictEntry] = 0

				ChampTeamFB[dictEntry] += 1
				ChampTotalPlayed[dictEntry] += 1

				iii += 1

			ii += 1


		# Now we add the losers

		champIds = []

		ii = 5
		while ii < 10:
			participant = encjson['participants'][ii]
			champIds.append(participant['championId'])

			ii += 1



		champIds = sorted(champIds)


		ii = 5
		while ii < 10:
			participant = encjson['participants'][ii]
			champIds.append(participant['championId'])

			ii += 1



		ii = 0
		while ii < 5:

			iii = ii

			while iii < 4:
				
				dictEntry = "{},{}".format(champIds[ii], champIds[iii+1])

				if(dictEntry not in ChampTeamFB):
					ChampTeamFB[dictEntry] = 0

				if(dictEntry not in ChampTotalPlayed):
					ChampTotalPlayed[dictEntry] = 0

				ChampTotalPlayed[dictEntry] += 1

				iii += 1

			ii += 1



	else:

		champIds = []

		ii = 5
		while ii < 10:
			participant = encjson['participants'][ii]
			champIds.append(participant['championId'])

			ii += 1



		champIds = sorted(champIds)


		ii = 5
		while ii < 10:
			participant = encjson['participants'][ii]
			champIds.append(participant['championId'])

			ii += 1



		ii = 0
		while ii < 5:

			iii = ii

			while iii < 4:
				
				dictEntry = "{},{}".format(champIds[ii], champIds[iii+1])

				if(dictEntry not in ChampTeamFB):
					ChampTeamFB[dictEntry] = 0

				if(dictEntry not in ChampTotalPlayed):
					ChampTotalPlayed[dictEntry] = 0

				ChampTeamFB[dictEntry] += 1
				ChampTotalPlayed[dictEntry] += 1

				iii += 1

			ii += 1


		# Now we add the losers

		champIds = []


		ii = 0
		while ii < 5:
			participant = encjson['participants'][ii]
			champIds.append(participant['championId'])

			ii += 1



		champIds = sorted(champIds)


		ii = 5
		while ii < 10:
			participant = encjson['participants'][ii]
			champIds.append(participant['championId'])

			ii += 1



		ii = 0
		while ii < 5:

			iii = ii

			while iii < 4:
				
				dictEntry = "{},{}".format(champIds[ii], champIds[iii+1])

				if(dictEntry not in ChampTeamFB):
					ChampTeamFB[dictEntry] = 0

				if(dictEntry not in ChampTotalPlayed):
					ChampTotalPlayed[dictEntry] = 0

				ChampTotalPlayed[dictEntry] += 1

				iii += 1

			ii += 1









	f.close()

	i += 1



z = {}
for champ in ChampTotalPlayed:
	z[champ] = round((ChampTeamFB[champ] / ChampTotalPlayed[champ])*100)
q = sorted(z, key=z.get, reverse=True)

export = ''

for champ in q:
	if(ChampTotalPlayed[champ] > 30):
		champs = champ.split(',')
		export += "{} and {} get first blood in {}% of games. Sample size: {}".format(champidtoname(champs[0]), champidtoname(champs[1]), str(z[champ]), str(ChampTotalPlayed[champ]))
		export += "\n"

f = open('export.txt', 'w')
f.write(export)
f.close()
