from bs4 import BeautifulSoup as bs
import re
import pandas as pd

handle=open("isl_goals.txt")
data=bs(handle.read(),"html.parser")
names=['Igor Angulo']
goal=['14']
game=['23']

for cell in data.find_all(class_="si-tCel si-stats-team si-stats-teamName"):
    for ele in cell.find_all(class_="si-fullName"):
        names.append(ele.text)
for cell in data.find_all(class_="si-tCel si-gamplyd si-plyStats-gamplyd"):
    goal.append(cell.text)
for cell in data.find_all(class_="si-tCel si-gamplyd"):
    game.append(cell.text)

games=pd.DataFrame(game,columns=["Matches"])
goals=pd.DataFrame(goal,columns=["Goals"])
players=pd.DataFrame(names,columns=["Player"])
players=pd.concat([players,goals,games],axis=1)
print(players)
players.to_csv('..\\data\\testing.csv')
