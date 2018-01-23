# League Data Scraping and Analytics
Scripts analyse data from league of legends json files and scripts to scrape match data files and match timeline files from RIOT api 

# Data
Contains 11,000 match data files(/jsons) and their respective timeline file(/jsons/timeline) along with the code to generate your own more up to date data set.

# Scripts

publicScape.py - scrapes match data files from the riot games API and at the same time does an analysis on the best champions for First Blood.

scrapeTimelines.py - scrapes the matching timeline files from the match files (from publicScape)

synergyFb.py - Calculates First blood rates of synergy between champions from your data set (e.g. When Lee Sin and Shen are on the same team they have a 50% first blood rate). 

proScrape.py - Takes a match link as input and gets the relevant match and timeline data and storing them in .json's.

# Pro

This is where the data and scripts for pro games (LCK, LMS, EULCS, NALCS) is. 

firstBlood.py and firstDragon.py - Champion analysis of chance of each champion's team getting first blood / first dragon.

blueFB.py and blueDragon.py - Analysis of change of getting first blood / dragon on blue vs red side.



by David Weatherall
