import requests
import csv 

#http://stats.nba.com/stats/draftcombineplayeranthro?LeagueID=00&SeasonYear=2015-16
#http://stats.nba.com/stats/draftcombinedrillresults?LeagueID=00&SeasonYear=2015-16 200 GET stats.nba.com   /stats/draftcombinedrillresults?LeagueID=00&SeasonYear=2015-16

for i in range(10, 11):
    start = str(i)
    end = str(i + 1)

    if i < 10:
        start = "0" + start

    if i + 1 < 10:
        end = "0" + end

    url = 'http://stats.nba.com/stats/draftcombineplayeranthro?LeagueID=00&SeasonYear=20{0}-{1}'.format(start, end)
    print(url)
    r = requests.get(url)
    # print(r.json()['resultSets'][0]['rowSet'][0])

    with open('data/combines/anthro_20{0}.csv'.format(end), 'wb') as csvfile:
        w = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        w.writerow(r.json()['resultSets'][0]['headers'])
        for row in r.json()['resultSets'][0]['rowSet']:
            w.writerow(row)
