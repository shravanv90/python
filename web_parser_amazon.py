# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:00:43 2020

@author: Shravan_V02
"""

import requests 
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
page = requests.get("https://www.amazon.in/s?k=lenovo+laptop&ref=nb_sb_noss_1",headers = headers)

soup = BeautifulSoup(page.content,"lxml")

print(soup)

itemname = []
itemprice = []
for item in soup.find_all("span",class_="a-size-medium a-color-base a-text-normal"):
    itemname.append(item.text)

for item2 in soup.find_all("span",class_="a-price-whole"):
    itemprice.append(item2.text)
        
    

#print(itemname)
#print(itemprice)

finalitem = []
for a,b in zip(itemname,itemprice):
    final = a + ";" + b
    finalitem.append(final)
    
print(finalitem)  


data = pd.DataFrame(data = finalitem)

data.to_csv("D:\ML\pricedetails.csv",index = False) 
