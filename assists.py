from bs4 import BeautifulSoup as bs
import re
import pandas as pd

handle=open("isl_assists.txt")
data=bs(handle.read(),"html.parser")
names=['Alberto Noguera']
assist=['8']
game=['20']

for cell in data.find_all(class_="si-tCel si-stats-team si-stats-teamName"):
    for ele in cell.find_all(class_="si-fullName"):
        names.append(ele.text)
for cell in data.find_all(class_="si-tCel si-gamplyd si-plyStats-gamplyd"):
    assist.append(cell.text)
for cell in data.find_all(class_="si-tCel si-gamplyd"):
    game.append(cell.text)

games=pd.DataFrame(game,columns=["Matches"])
assists=pd.DataFrame(assist,columns=["Assists"])
players=pd.DataFrame(names,columns=["Player"])
players=pd.concat([players,assists,games],axis=1)
print(players)
players.to_csv('isl_assist_data.csv')