#Assingment 6
#Sam Schuller
import urllib2
import requests
from urllib2 import urlopen
from bs4 import BeautifulSoup
import os,csv

page = urlopen("https://www.dell.com/community/Laptops/ct-p/Laptops")
soup = BeautifulSoup(page,"html.parser")

InspironPage = urlopen("https://www.dell.com/community/Inspiron/bd-p/Inspiron")
InspironPage1 = BeautifulSoup(InspironPage,'html.parser')
print(type(InspironPage1))
print(InspironPage1.prettify())


# In[5]:


# Testing to Return the First Post on Inspiron sub-community

posts = InspironPage1.find('td',attrs={'class':'cThreadInfoColumn lia-data-cell-primary lia-data-cell-text'})
name = posts.text.strip()
print(name)
print(name.split('\n')[0])


# In[6]:


# Loading All of the Posts from 5 Pages of Inspiron Sub-Community

# Page 1
posts1 = InspironPage1.findAll('td',attrs={'class':'cThreadInfoColumn lia-data-cell-primary lia-data-cell-text'})

# Page 2
IP2 = urlopen("https://www.dell.com/community/Inspiron/bd-p/Inspiron/page/2")
InspironPage2 = BeautifulSoup(IP2,'html.parser')
posts2 = InspironPage2.findAll('td',attrs={'class':'cThreadInfoColumn lia-data-cell-primary lia-data-cell-text'})

# Page 3
IP3 = urlopen("https://www.dell.com/community/Inspiron/bd-p/Inspiron/page/3")
InspironPage3 = BeautifulSoup(IP3,'html.parser')
posts3 = InspironPage3.findAll('td',attrs={'class':'cThreadInfoColumn lia-data-cell-primary lia-data-cell-text'})

# Page 4
IP4 = urlopen("https://www.dell.com/community/Inspiron/bd-p/Inspiron/page/3")
InspironPage4 = BeautifulSoup(IP4,'html.parser')
posts4 = InspironPage4.findAll('td',attrs={'class':'cThreadInfoColumn lia-data-cell-primary lia-data-cell-text'})

# Page 5
IP5 = urlopen("https://www.dell.com/community/Inspiron/bd-p/Inspiron/page/3")
InspironPage5 = BeautifulSoup(IP5,'html.parser')
posts5 = InspironPage5.findAll('td',attrs={'class':'cThreadInfoColumn lia-data-cell-primary lia-data-cell-text'})
