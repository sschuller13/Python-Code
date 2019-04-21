#Session 12

import pandas

from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

 
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('class').size())#number of instances for each type

dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
#histogram
dataset.hist()
plt.show()
#scatter plot
scatter_matrix(dataset)
plt.show()


array = dataset.values
type(array)
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
scoring = 'accuracy'
#how we are going to evaluate the performance of model

#estimate model using Logistic Regression
kfold = model_selection.KFold(n_splits=10, random_state=seed)
cv_results = model_selection.cross_val_score(LogisticRegression(), X_train, Y_train, cv=kfold, scoring=scoring)
print cv_results.mean(),cv_results.std()

#results are mean and std dev, .966666 and .04082 respectively

logistic = LogisticRegression(C=1e5)
logistic.fit(X_train, Y_train).score(X_validation,Y_validation)
print logistic.coef_
iris_y_pred=logistic.predict(X_validation)
print iris_y_pred
confusion_matrix(Y_validation,iris_y_pred)#performance on validation set

