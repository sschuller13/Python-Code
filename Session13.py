import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

white =pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine- quality/winequality-white.csv", sep=';')

red=pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine- quality/winequality-red.csv", sep=';')


red['type']=1
white['type']=0
wines = red.append(white,ignore_index=True)

read.head()

X=wines.ix[:,0:11]
y=np.ravel(wines.type)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42)

# Define the scaler
scaler = StandardScaler().fit(X_train)
# Scale the train set
X_train = scaler.transform(X_train)
# Scale the test set
X_test = scaler.transform(X_test)


#Neural Network

model=Sequential()
model.add(Dense(12,activation='relu',input_shape=(11,)))
model.add(Dense(8,activation='relu',))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fix(X_train,y_train,epochs=20,batch_size=1,verbose=2)


model.output_shape
model.summary()
