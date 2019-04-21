#Lab 9 Pandas
#Sam Schuller

import pandas as pd



#1 (made the chipotle.txt file into a readable chipotle.csv file

chipo = pd.read_csv('C:\Python27\chipotle.txt', sep='\t' )

chipo
#2
print chipo.head(10)
print chipo.info()
print chipo.shape
chipo.columns
print chipo.index
#3

orderid = chipo.sort_values(['order_id'], ascending = False)
print chipo['quantity'].max()
print orderid.head()
print chipo['quantity'].max()

#5
ordereditems = chipo.groupby('quantity')
print ordereditems.sum()
#6 unsure of how to convert dataframe variable type
revenue = chipo.sort_values(['item_price'], ascending = True)
print revenue.sum()

#7
print '# Orders: ', chipo['order_id'].max()

#8
