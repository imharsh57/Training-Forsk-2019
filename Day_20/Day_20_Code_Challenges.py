'''
Code Challenge 01: (Prostate Dataset)

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.
(a) Train the unregularized model (linear regressor) and calculate the mean squared error.
(b) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.
'''
import pandas as pd
import numpy as np
dataset = pd.read_csv("Prostate_Cancer.csv")

dataset = dataset.fillna(0)

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
dataset['diagnosis_result'] = labelencoder.fit_transform(dataset['diagnosis_result'])


features = dataset.drop('diagnosis_result',axis=1)
labels = dataset['diagnosis_result']

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.linear_model import LinearRegression 
lm = LinearRegression ()
lm.fit(features_train, labels_train)

labels_pred = lm.predict(features_test)
data=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred}) 

print ("RSquare Value for Simple Regresssion TEST data is-") 
print (np.round (lm .score(features_test,labels_test)*100,2))


from sklearn import metrics   
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
#**********************************************************************************************

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
lm_lasso = Lasso() 
lm_ridge =  Ridge() 

lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))

predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))

'''
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
'''
import pandas as pd
import numpy as np
dataset = pd.read_csv("kc_house_data.csv")
dataset = dataset.fillna(0)

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
dataset['date'] = labelencoder.fit_transform(dataset['date'])

features = dataset.drop('price',axis=1)
labels = dataset['price']

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.linear_model import LinearRegression 
lm = LinearRegression ()
lm.fit(features_train, labels_train)

labels_pred = lm.predict(features_test)
data=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred}) 

print ("RSquare Value for Simple Regresssion TEST data is-") 
print (np.round (lm .score(features_test,labels_test)*100,2))

#***************************************************************************************
from sklearn import metrics 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
lm_lasso = Lasso() 
lm_ridge =  Ridge() 

lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))

predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))



'''
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
'''
import pandas as pd
import numpy as np
dataset = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delim_whitespace=True)

dataset = dataset.fillna(0)

features = dataset.drop('lpsa',axis=1)
labels = dataset['lpsa']

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.linear_model import LinearRegression 
lm = LinearRegression ()
lm.fit(features_train, labels_train)

labels_pred = lm.predict(features_test)
data=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred}) 

print ("RSquare Value for Simple Regresssion TEST data is-") 
print (np.round (lm .score(features_test,labels_test)*100,2))


from sklearn import metrics   
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
#**********************************************************************************************

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
lm_lasso = Lasso() 
lm_ridge =  Ridge() 

lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))

predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))


#***********************************************************
#(b) Can we predict whether lpsa is high or low, from other variables?
#convert lpsa to T or F
def lpsaaa(value):
    if value < 0.5:
        value =  "T"
    else:
        value = "F"
    return value
dataset['lpsa'] = dataset["lpsa"].apply(lpsaaa)

dataset = dataset.fillna(0)
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
dataset['lpsa'] = labelencoder.fit_transform(dataset['lpsa'])

features = dataset.drop('lpsa',axis=1)
labels = dataset['lpsa']

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)
data=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred}) 
labels_pred_inverse = pd.Series(labelencoder.inverse_transform(labels_pred.astype("int")))
labels_test_inverse = pd.Series(labelencoder.inverse_transform(labels_test.astype("int")))
df_inverse=pd.DataFrame({'Actual':labels_test_inverse, 'Predicted':labels_pred_inverse})
print(df_inverse)