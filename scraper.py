import requests
import csv 

#http://stats.nba.com/stats/draftcombineplayeranthro?LeagueID=00&SeasonYear=2015-16
#http://stats.nba.com/stats/draftcombinedrillresults?LeagueID=00&SeasonYear=2015-16 200 GET stats.nba.com   /stats/draftcombinedrillresults?LeagueID=00&SeasonYear=2015-16

def get_anthro_data():
    for i in range(0, 12):
        start = str(i)
        end = str(i + 1)

        if i < 10:
            start = "0" + start

        if i + 1 < 10:
            end = "0" + end

        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}
        url = 'http://stats.nba.com/stats/draftcombineplayeranthro?LeagueID=00&SeasonYear=20{0}-{1}'.format(start, end)
        print(url)
        r = requests.get(url, headers=headers)
        # print(r.json()['resultSets'][0]['rowSet'][0])

        with open('data/combines/anthro_20{0}.csv'.format(start), 'wb') as csvfile:
            w = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            w.writerow(r.json()['resultSets'][0]['headers'])
            for row in r.json()['resultSets'][0]['rowSet']:
                w.writerow(row)

def get_drills_data():
    for i in range(0, 12):
        start = str(i)
        end = str(i + 1)

        if i < 10:
            start = "0" + start

        if i + 1 < 10:
            end = "0" + end

        url = 'http://stats.nba.com/stats/draftcombinedrillresults?LeagueID=00&SeasonYear=20{0}-{1}'.format(start, end)
        print(url)
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}
        r = requests.get(url, headers=headers)
        print(r.status_code)
        # print(r.json()['resultSets'][0]['rowSet'][0])

        with open('data/combines/drills_20{0}.csv'.format(start), 'wb') as csvfile:
            w = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            w.writerow(r.json()['resultSets'][0]['headers'])
            for row in r.json()['resultSets'][0]['rowSet']:
                w.writerow(row)

get_drills_data()