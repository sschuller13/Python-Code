import urllib2
import requests
from bs4 import BeautifulSoup
import os,csv

page=urllib2.urlopen("https://imdb.com/chart/top")
#requests to access/download webpage
soup=BeautifulSoup(page,'html.parser')
#will do the same thing as installing packages
#restructures webpage in DOM format

name_box=soup.find('td',attrs={'class':'titleColumn'})

name_box.text.strip()

films=soup.find_all('td',attrs={'class':'titleColumn'})
len(films)
films[0]
films[1]
films[100]
#able to find all the films names on webpage

rating_box=soup.find_all('td',attrs={'class':'ratingColumn imdbRating'})
rating=rating_box[0].text
#gives us ratings of films

films[1].text #will display The Godfather
rating_box[1].text #will display 9.2 score

sdata={}
for i in range(5):
    a=films[i].get_text().split('\n')[2].strip()
    sdata[a]=float(rating_box[i].text.strip())
    #saves both rating and film name in tuple together


with open('filmdata.csv','w')as toWrite:
    writer =csv.writer(toWrite,delimiter=',')
    writer.writerow(['film','rating'])
    for a in sdata.keys():
        writer.writerow([a.encode('utf-8'),sdata[a]])
#writing and saving it into a csv file

#will reconstruct entire  file into something like the HTML and DOM diagram
type(soup)
soup.prettify()[0:1000]



                
