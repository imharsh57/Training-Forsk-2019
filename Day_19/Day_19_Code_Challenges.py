"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    
    Find out the MPG value of a 80's model car of origin 3,
    weighing 2630 kgs with 6 cylinders, having acceleration
    around 22.2 m/s due to it's 100 horsepower engine giving
    it a displacement of about 215. (Give the prediction from both the models)
"""

import pandas as pd

df = pd.read_csv('Auto_mpg.txt', delim_whitespace=True, names=("mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"))
#read_table , read_fwf instead of read_csv
print("Car Name with highest miles per gallon value :",df[df['mpg']==df['mpg'].max()]['car name'].values)

# or df= df['horsepower'].replace({'?' : 0.0})
df= df.replace({'?' : 0})

features = df.drop(['mpg','car name'], axis=1)  #car name drop bz it creates problem for converting string to float

labels = df['mpg']

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  

#Training and making predictions
#********************************************************************************decision tree

from sklearn.tree import DecisionTreeRegressor 
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)

labels_pred = regressor.predict(features_test) 
data=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  

print("Accuracy with Decision tree:",regressor.score(features_test,labels_test))
#********************************************************************************random forest

from sklearn.ensemble import RandomForestRegressor
regressor_random = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor_random.fit(features_train, labels_train)  

labels_pred = regressor_random.predict(features_test) 
data_random=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred}) 
print("Accuracy with Random forest tree:",regressor_random.score(features_test,labels_test))
#*****************************************3rd solution]
input_data = [6,215,100,2630,22.2,80,3]
import numpy as np
input_data = np.array(input_data)
input_data = input_data.reshape(1,7)

input_data_sc = sc.transform(input_data)

print("Prediction by random forest :", regressor_random.predict(input_data_sc))
print("Prediction by decision tree :", regressor.predict(input_data_sc))


"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.
"""
import pandas as pd
dataset = pd.read_csv("PastHires.csv")

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
dataset['Employed?'] = labelencoder.fit_transform(dataset['Employed?'])
dataset['Level of Education'] = labelencoder.fit_transform(dataset['Level of Education'])
dataset['Top-tier school'] = labelencoder.fit_transform(dataset['Top-tier school'])
dataset['Interned'] = labelencoder.fit_transform(dataset['Interned'])
dataset['Hired'] = labelencoder.fit_transform(dataset['Hired'])

features = dataset.drop('Hired',axis = 1)
labels = dataset['Hired']


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 

from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})

labels_pred_inverse = pd.Series(labelencoder.inverse_transform(labels_pred.astype("int")))
#convert float to int by astype and pd.series is used to convert to series or pd.dataframe used to convert to dataframe from object
labels_test_inverse = pd.Series(labelencoder.inverse_transform(labels_test.astype("int")))
df_inverse=pd.DataFrame({'Actual':labels_test_inverse, 'Predicted':labels_pred_inverse})
print(df_inverse)

#********************************************************************
''' Predict employment of a currently employed 10-year veteran, previous employers 4,
 went to top-tire school, having Bachelor's Degree without Internship.'''
from sklearn.ensemble import RandomForestRegressor
random = RandomForestRegressor(n_estimators=10, random_state=0)  
random.fit(features_train, labels_train)  
labels_pred_random = random.predict(features_test) 

input_data = [10,'Y',4,'BS','Y','N']
import numpy as np
input_data = np.array(input_data)
input_data = input_data.reshape(1,6)

input_data[:,1] = labelencoder.fit_transform(input_data[:,1])
input_data[:,3] = labelencoder.fit_transform(input_data[:,3])
input_data[:,4] = labelencoder.fit_transform(input_data[:,4])
input_data[:,5] = labelencoder.fit_transform(input_data[:,5])

input_pred_random = random.predict(input_data) 
input_pred_inverse = pd.Series(labelencoder.inverse_transform(input_pred_random.astype("int")))
print("Employment :",input_pred_inverse.values)

#***************************************************************************
'''    Predict employment of an unemployed 10-year veteran, ,previous employers
 4, didn't went to any top-tire school, having Master's Degree with Internship.'''
input_data1 = [10,'N',4,'MS','Y','Y']
import numpy as np
input_data1 = np.array(input_data1)
input_data1 = input_data1.reshape(1,6)

input_data1[:,1] = labelencoder.fit_transform(input_data1[:,1])
input_data1[:,3] = labelencoder.fit_transform(input_data1[:,3])
input_data1[:,4] = labelencoder.fit_transform(input_data1[:,4])
input_data1[:,5] = labelencoder.fit_transform(input_data1[:,5])

input_pred_random1 = random.predict(input_data1) 
input_pred_inverse1 = pd.Series(labelencoder.inverse_transform(input_pred_random1.astype("int")))
print("Employment :",input_pred_inverse1.values)


