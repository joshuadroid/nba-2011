
#part 1
#read file
#print headers

import os
import csv
import numpy
from numpy.lib.arraysetops import unique
import time

file = "2010-11_pbp.csv"
data = []
uniquegames = []
startTime = time.time()

with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for x in csvreader:
        data.append(x)

# print(csvheader)

# search for unique game ids
# trying to get a list of all the games
def column(list, i):
    return [row[i] for row in list]


uniquegames = numpy.unique(column(data, 4))

# -------------------------------
# All Above Working As Planned
# -------------------------------

executionTime = (time.time() - startTime)
print(executionTime)
output_path = os.path.join("2010-11_ugid.csv")

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Game IDs"])
    for x in uniquegames:
        csvwriter.writerow(uniquegames)

print(executionTime)






#part 2
#figure out how to make a list of both teams in each game

# def findGamesAndTeams(dataset, j, k, l):
#     gat = []
#     for eachrow in dataset:
#         gameid = dataset[j]
#         team1 = dataset[k]
#         team2 = dataset[l]
#         gat.append([gameid, team1, team2])
#     return gat

# gamesandteams = numpy.unique(findGamesAndTeams(data, 4, 15, 21))

# print(gamesandteams)



#figure out how to write unique games and teams to a csv
        
# teamsid = []
# gameid = 0
# team1 = 0
# team2 = 0
# not working
# for row in data:
#     gameid = row[4]
#     team1 = row[14]
#     if row[14] != team1:
#         team2 = row[14]
#     teamsid.append(unique(gameid, team1, team2))


# print(teamsid)

        

#Search for each value in data, 
#  find unique values for each team for each row
#  add to a list

#part 3
#figure out how to get unique games of the mavericks
#figure out how to total up mavs game scoring data

#part 4
#figure out how to get dirk game stats per game
#write a function to summarize player data per game?
#write a function to search for team data?


