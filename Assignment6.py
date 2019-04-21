#Assignment 6
#Sam Schuller

import urllib2
import requests
from urllib2 import urlopen
from bs4 import BeautifulSoup
import os,csv

page=urllib2.urlopen("https://www.dell.com/community/Laptops/ct-p/Laptops")

soup=BeautifulSoup(page,'html.parser')
testing=soup.find_all('div',attrs={'class':'cat-card'})

#1
for i in range(len(testing)):
    x=testing[i].find('div',attrs={'class':'cat-card-title'}).text.strip()
    y=testing[i].find('span',attrs={'class':'cat-card-posts'}).text.strip()
    if x in ['Inspiron','Latitude','XPS']:
        print'{} has {}'.format(x,y)
    
#2
def csvwriter(blah, blah2):
    with open(blah, 'a') as toWrite:
        csv_writer=csv.writer(toWrite,delimiter=',')
        soup=BeautifulSoup(blah2,'html.parser')
        finds=soup.find('table',attrs={'class': 'lia-list-wide'}).find('tbody').find_all('tr')
        for i in finds:
            title=i.find('a',attrs={'class':'page-link lia-link-navigation lia-custom-event'}).text.strip()
            title=title.encode('utf-8')
            author=i.find_all('a',attrs={'class':'lia-link-navigation lia-page-link lia-user-name-link'})
            author2=author[0].find('span').text.strip()
            author2=author2.encode('utf-8')
            if len(author2)==2:
                author3=author2[1].find('span').text.strip()
                author3= author3.encode('utf-8')
            else:
                author3=' '

            localdate=i.find_all('span',attrs={'class':'local-date'})
            localtime=i.find_all('span',attrs={'class':'local-time'})
            date=localdate[0].text.strip()[-10:]+localtime[0].text.strip()
            date=date.encode('utf-8')
            if len(localtime) ==2:
                date2=localdate[1].text.strip()[-10:]+ ''+ localtime[1].text.strip()
                date2.encode('utf-8')
            else:
                date2= ' '
            
            kudos=i.find('div',attrs={'class':'lia-component-messages-column-message-kudos-count'}).find('span').text.strip()
            kudos=kudos.encode('utf-8')
            replies=i.find('div',attrs={'class':'lia-component-messages-column-message-replies-count'}).find('span').text.strip()
            replies=replies.encode('utf-8')
            views=i.find('div',attrs={'class':'lia-component-messages-column-topic-views-count'}).find('span').text.strip()
            views=views.encode('utf-8')
            var='No'
            if i.find('td',attrs={'class':'triangletop lia-data-cell-secondary lia-data-cell-icon'}).has_attr('aria-label'):
                if i.find('td',attrs={'class':'triangletop lia-data-cell-secondary lia-data-cell-icon'}).get('aria-label')=='This thread is solved':
                    var='Yes'
            csv_writer.writerow([title,author3, date, author3, date2, kudos,replies,views,var])
file1 = 'Assignment6.csv'
for i in ('A','B','C','D','E'):
    here='https://www.dell.com/community/Inspiron/bd-p/Inspiron'
    site= '{}/x/{}'.format(here,i)
    site2=urllib2.urlopen(site)
    csvwriter(file1, site2)
                                          
