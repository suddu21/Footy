from bs4 import BeautifulSoup as bs
import re
import pandas as pd

handle=open("player_ratings.txt")
data=bs(handle.read(),"html.parser")
names=['Hugo Boumous']
rating=['7.86']

for cell in data.find_all(class_="si-tCel si-stats-team si-stats-teamName"):
    for ele in cell.find_all(class_="si-fullName"):
        names.append(ele.text)
for cell in data.find_all(class_="si-tCel si-gamplyd si-plyStats-gamplyd"):
    rating.append(cell.text)

ratings=pd.DataFrame(rating,columns=["Rating"])
players=pd.DataFrame(names,columns=["Player"])
players=pd.concat([players,ratings],axis=1)
print(players)
players.to_csv('isl_player_ratings.csv')