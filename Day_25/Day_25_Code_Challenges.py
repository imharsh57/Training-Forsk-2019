'''
Q1. Human Activity Recognition

Human Activity Recognition with Smartphones

(Recordings of 30 study participants performing activities of daily living)

(Click Here To Download Dataset): https://github.com/K-Vaid/Python-Codes/blob/master/Human_activity_recog.zip

In an experiment with a group of 30 volunteers within an age bracket of 19 to 48 years, 
each person performed six activities (WALKING, WALKING UPSTAIRS, WALKING DOWNSTAIRS, 
SITTING, STANDING, LAYING) wearing a smartphone (Samsung Galaxy S II) on the waist. 
The experiments have been video-recorded to label the data manually.

The obtained dataset has been randomly partitioned into two sets, where 70% of 
the volunteers was selected for generating the training data and 30% the test data.

Attribute information 

For each record in the dataset the following is provided:

        Triaxial acceleration from the accelerometer (total acceleration) and the estimated body acceleration. 
        Triaxial Angular velocity from the gyroscope.
        A 561-feature vector with time and frequency domain variables.
        Its activity labels.
        An identifier of the subject who carried out the experiment.

Train a tree classifier to predict the labels from the test data set using the following approaches:

  (a) a decision tree approach,

  (b) a random forest approach and

  (c) a logistic regression.

  (d) KNN approach

Examine the result by reporting the accuracy rates of all approach on both the testing and training data set.
 Compare the results. Which approach would you recommend and why?

        Perform feature selection and repeat the previous step. Does your accuracy improve?
        Plot two graph showing accuracy bar score of all the approaches taken with and without feature selection.
'''
import pandas as pd
dataset_test = pd.read_csv("test.csv")
dataset_train = pd.read_csv("train.csv")

features_test = dataset_test.drop(['Activity','subject'],axis=1)
features_train = dataset_train.drop(['Activity','subject'],axis=1)

labels_test = dataset_test['Activity']
labels_train = dataset_train['Activity']
#********************* label encoding *****************************
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels_train = labelencoder.fit_transform(labels_train)
labels_test = labelencoder.fit_transform(labels_test) #optional


#***************** Decision tree classifier ****************************
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 
labels_pred_inverse = labelencoder.inverse_transform(labels_pred)
labels_test_inverse = labelencoder.inverse_transform(labels_test)

data_random=pd.DataFrame({'Actual':labels_test_inverse, 'Predicted':labels_pred_inverse}) 

print("Score for Decision tree on testing :",classifier.score(features_test,labels_test))
print("Score for Decision tree on training :",classifier.score(features_train,labels_train))

#**************** Random forest ******************************************
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  

print("Score for Random Forest on testing :",classifier.score(features_test,labels_test))
print("Score for Random Forest on training :",classifier.score(features_train,labels_train))

#***************** kNN ***************************************************
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

print("Score for knn on testing :",classifier.score(features_test,labels_test))
print("Score for knn on training :",classifier.score(features_train,labels_train))

#***************** logistic regression *************************************
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

print("Score for knn on testing :",classifier.score(features_test,labels_test))
print("Score for knn on training :",classifier.score(features_train,labels_train))

#************  Perform feature selection and repeat the previous step. Does your accuracy improve?
import statsmodels.api as sm

regressor_OLS = sm.OLS(endog = labels_train, exog = features_train).fit()

p_values = list(regressor_OLS.pvalues)

index=[] #store the index which has pvalues less than 5%
for item in p_values:
    if item <0.05:
        index.append(p_values.index(item))

#taking features        
features_train = features_train.iloc[:,index].values
features_test = features_test.iloc[:,index].values

#***************** Decision tree classifier ****************************
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 
labels_pred_inverse = labelencoder.inverse_transform(labels_pred)
labels_test_inverse = labelencoder.inverse_transform(labels_test)

data_random=pd.DataFrame({'Actual':labels_test_inverse, 'Predicted':labels_pred_inverse}) 

print("Score for Decision tree on testing :",classifier.score(features_test,labels_test))
print("Score for Decision tree on training :",classifier.score(features_train,labels_train))

#**************** Random forest ******************************************
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  

print("Score for Random Forest on testing :",classifier.score(features_test,labels_test))
print("Score for Random Forest on training :",classifier.score(features_train,labels_train))

#***************** kNN ***************************************************
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

print("Score for knn on testing :",classifier.score(features_test,labels_test))
print("Score for knn on training :",classifier.score(features_train,labels_train))

#***************** logistic regression *************************************
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

print("Score for knn on testing :",classifier.score(features_test,labels_test))
print("Score for knn on training :",classifier.score(features_train,labels_train))



     
'''        
Q2. Code Challenge

#Online Marketing

(Click Here To Download Resource File) : http://openedx.forsk.in/c4x/Manipal_University/FL007/asset/online_marketing.sql

Objective of this case study is to explore Online Lead Conversion for a Life Insurance 
company. Some people are interested in buying insurance products from this company hence
 they visit the site of this Life Insurance Company and fill out a survey asking about 
 attributes like income, age etc. These people are then followed and some of them become
 customers from leads. Company have all the past data of who became customers from lead.
 Idea is to learn something from this data and when

some new lead comes, assign a propensity of him/her converting to a customer based on
 attributes asked in the survey. This sort of problem is called as Predictive Modelling

Concept:

Predictive modelling is being used by companies and individuals all over the world 
to extract value from historical data. These are the mathematical algorithms, which
 are used to "learn" the patterns hidden on all this data. The term supervised learning
 or classification is also used which means you have past cases tagged or classified
 (Converted to Customer or Not) and you want to use this learning on new data. (machine learning)

Here are the attributes of the survey:

Attribute

age (Age of the Lead)

Job (Job Category e.g. Management)

marital (Marital Status)

education (Education of Lead)

smoker (Is Lead smoker or not (Binary – Yes / No))

monthlyincome (Monthly Income)

houseowner (Is home owner or not (Binary – Yes / No))

loan (Is having loan or not (Binary – Yes / No))

contact (Contact type e.g. Cellphone)

mod (Days elapsed since survey was filled)

monthlyhouseholdincome (Monthly Income of all family member)

target_buy (altogether Is converted to customer or not (Binary –Yes /No). This is known as Target or Responseand this is what we are modelling.)



Activities you need to perform:


a. Handle the missing data and perform necessary data pre-processing.
b. Summarise the data.
c. Perform feature selection and train using prediction model.
d. For a new lead, predict if it will convert to a successful lead or not.
e. Use different classification techniques and compare accuracy score and also plot them in a bar graph.
'''
import sqlite3 as sql
conn = sql.connect('mydb.db')
cursor = conn.cursor()

file = open('online_marketing.sql','r')
file_read = file.read()
file.close()
cursor.executescript(file_read)
conn.commit()

import pandas as pd
data = pd.read_sql('select * from online_marketing',conn)

#*************************************************************************************************
#xampp -->open file & replace mod with mod_ and then crete database and import sql file
import pandas as pd
import mysql.connector as sql

query = "select * from online_marketing"
conn = sql.connect(host="localhost",
                   user="root",
                   password="",
                   db = "online_market"
                   )

data = pd.read_sql(query,conn)

