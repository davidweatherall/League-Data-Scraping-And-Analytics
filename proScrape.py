import os
import json
import urllib.request

directory = ''

def find_between( s, first, last ):
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""



while True:

	print('Link to game:')
	url = input('')

	region = find_between(url, 'match-details/', '/')
	gameId = find_between(url, region + '/', '?gameHash')
	gameHash = url.split('gameHash=')[1]

	print(region)
	print(gameId)
	print(gameHash)


	urlString = 'https://acs.leagueoflegends.com/v1/stats/game/{}/{}?gameHash={}'.format(region, gameId, gameHash)

	with urllib.request.urlopen(urlString) as url:
		json_raw = url.read().decode()

	json_file = open('Pro/game/{}.json'.format(str(gameId)), 'wb')
	json_file.write(json_raw.encode('utf-8'))
	json_file.close

	urlString = 'https://acs.leagueoflegends.com/v1/stats/game/{}/{}/timeline?gameHash={}'.format(region, gameId, gameHash)

	with urllib.request.urlopen(urlString) as url:
		json_raw = url.read().decode()

	json_file = open('Pro/timeline/{}.json'.format(str(gameId)), 'wb')
	json_file.write(json_raw.encode('utf-8'))
	json_file.close








# https://matchhistory.na.leagueoflegends.com/en/#match-details/TRLH1/1002440062?gameHash=a3b08c115923f00d&tab=overview

# https://acs.leagueoflegends.com/v1/stats/game/TRLH1/1002440062/timeline?gameHash=a3b08c115923f00d

# https://acs.leagueoflegends.com/v1/stats/game/TRLH1/1002440062?gameHash=a3b08c115923f00d