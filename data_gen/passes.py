from bs4 import BeautifulSoup as bs
import re
import pandas as pd

handle=open("isl_passes.txt")
data=bs(handle.read(),"html.parser")
names=['Edu Bedia']
passe=['1496']
game=['20']

for cell in data.find_all(class_="si-tCel si-stats-team si-stats-teamName"):
    for ele in cell.find_all(class_="si-fullName"):
        names.append(ele.text)
for cell in data.find_all(class_="si-tCel si-gamplyd si-plyStats-gamplyd"):
    passe.append(cell.text)
for cell in data.find_all(class_="si-tCel si-gamplyd"):
    game.append(cell.text)

games=pd.DataFrame(game,columns=["Matches"])
passes=pd.DataFrame(passe,columns=["Passes"])
players=pd.DataFrame(names,columns=["Player"])
players=pd.concat([players,passes,games],axis=1)
print(players)
players.to_csv('..\\data\\isl_passes_data.csv')