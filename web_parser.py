# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:55:40 2020

@author: Shravan_V02
"""
import requests
from bs4 import BeautifulSoup
import csv


page = requests.get("https://libgen.is/search.php?req=machine+learning&open=0&res=25&view=simple&phrase=1&column=def")

print(page.text)
soup = BeautifulSoup(page.text,"html.parser")

table = soup.find( "table", {"class":"c"} )
links = []
title = []
final=[]
for row in table.find_all("tr")[1:]:

    col = row.find_all("td")
    title.append(col[2].text)
    
    
    for line in row.find_all("a",title="Gen.lib.rus.ec"):
        links.append(line.get("href"))
        print(line.get("href"))
    #print(links[3])
    
    print("---")

for a,b in zip(title,links):
    fin = a+"|"+b
    final.append(fin)
final

with open('MLtitle.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(final)
    