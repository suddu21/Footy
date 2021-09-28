from bs4 import BeautifulSoup as bs
import re
import pandas as pd

handle=open("isl_touches.txt")
data=bs(handle.read(),"html.parser")
names=['Ahmed Jahouh']
touch=['1827']
game=['20']

for cell in data.find_all(class_="si-tCel si-stats-team si-stats-teamName"):
    for ele in cell.find_all(class_="si-fullName"):
        names.append(ele.text)
for cell in data.find_all(class_="si-tCel si-gamplyd si-plyStats-gamplyd"):
    touch.append(cell.text)
for cell in data.find_all(class_="si-tCel si-gamplyd"):
    game.append(cell.text)

games=pd.DataFrame(game,columns=["Matches"])
touches=pd.DataFrame(touch,columns=["Touches"])
players=pd.DataFrame(names,columns=["Player"])
players=pd.concat([players,touches,games],axis=1)
print(players)
players.to_csv('isl_touch_data.csv')