from bs4 import BeautifulSoup as bs
import re
import pandas as pd

handle=open("isl_intercepts.txt")
data=bs(handle.read(),"html.parser")
names=['Stephen Eze']
intercept=['60']
game=['20']

for cell in data.find_all(class_="si-tCel si-stats-team si-stats-teamName"):
    for ele in cell.find_all(class_="si-fullName"):
        names.append(ele.text)
for cell in data.find_all(class_="si-tCel si-gamplyd si-plyStats-gamplyd"):
    intercept.append(cell.text)
for cell in data.find_all(class_="si-tCel si-gamplyd"):
    game.append(cell.text)

games=pd.DataFrame(game,columns=["Matches"])
intercepts=pd.DataFrame(intercept,columns=["Interceptions"])
players=pd.DataFrame(names,columns=["Player"])
players=pd.concat([players,intercepts,games],axis=1)
print(players)
players.to_csv('isl_interceptions_data.csv')