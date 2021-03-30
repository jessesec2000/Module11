#ASSIGNMENT 1
import requests
from bs4 import BeautifulSoup as bs
r=requests.get('https://worldhappiness.report/ed/2021/happiness-trust-and-deaths-under-covid-19/')
soup = bs(r.content, 'html.parser')

soup.find_all('h2')
h2s = soup.find_all('h2')
for h2 in h2s:
    print(h2)

#ASSIGNMENT 2
print(soup.prettify())

import csv
f = open(r'C:\Users\jesse\OneDrive\Documents\PythonCourse\Module11\COVID19ByCounty.csv','rt')
myReader = csv.DictReader(f)
for row in myReader:
    print(row ['COUNTYNAME'])
f.close()



