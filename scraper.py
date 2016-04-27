import requests

#http://stats.nba.com/stats/draftcombineplayeranthro?LeagueID=00&SeasonYear=2015-16
#http://stats.nba.com/stats/draftcombinedrillresults?LeagueID=00&SeasonYear=2015-16	200	GET	stats.nba.com	/stats/draftcombinedrillresults?LeagueID=00&SeasonYear=2015-16

r = requests.get('http://stats.nba.com/stats/draftcombineplayeranthro?LeagueID=00&SeasonYear=2015-16')
print(r.json()['resultSets'][0]['headers'])