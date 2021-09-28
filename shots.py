from bs4 import BeautifulSoup as bs
import re
import pandas as pd


handle1=open('isl_shots.txt')
data1=bs(handle1.read(),'html.parser')
s_name=['Jorge Mendoza']
shot=['71']
s_game=['21']
for cell in data1.find_all(class_="si-tCel si-stats-team si-stats-teamName"):
    for ele in cell.find_all(class_="si-fullName"):
        s_name.append(ele.text)
for cell in data1.find_all(class_="si-tCel si-gamplyd si-plyStats-gamplyd"):
    shot.append(cell.text)
for cell in data1.find_all(class_="si-tCel si-gamplyd"):
    s_game.append(cell.text)
names_=pd.DataFrame(s_name,columns=['Player'])
shots=pd.DataFrame(shot,columns=['Shots'])
s_games=pd.DataFrame(s_game,columns=['Matches'])
shots_data=pd.concat([names_,shots,s_games],axis=1)
shots_data.to_csv('isl_shots_data.csv')
#print(data.prettify())