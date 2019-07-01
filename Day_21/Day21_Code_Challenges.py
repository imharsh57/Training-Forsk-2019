'''
Q1. (Create a program that fulfills the following specification.)

Program Specification:

Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                     ----> represented by column A.

Clump Thickness (1 – 10)                                     ----> represented by column B.
Uniformity of Cell Size(1 - 10)                             ----> represented by column C.
Uniformity of Cell Shape (1 - 10)                        ----> represented by column D.
Marginal Adhesion (1 - 10)                                  ----> represented by column E.
Single Epithelial Cell Size (1 - 10)                        ----> represented by column F.
Bare Nuclei (1 - 10)                                               ----> represented by column G.
Bland Chromatin (1 - 10)                                     ----> represented by column H.
Normal Nucleoli (1 - 10)                                      ----> represented by column I.
Mitoses (1 - 10)                                                     ----> represented by column J.
Class: (2 for Benign and 4 for Malignant)         ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor.

                    Impute the missing values with the most frequent values.
                    Perform Classification on the given data-set to predict if the tumor is cancerous or not.
                    Check the accuracy of the model.
                    
                    Predict whether a women has Benign tumor or Malignant tumor,
                    if her Clump thickness is around 6, uniformity of cell size is 2,
                    Uniformity of Cell Shape is 5, Marginal Adhesion is 3, 
                    Bland Chromatin is 9, Mitoses is 4, Bare Nuclei is 7,
                    Normal Nuclei is 2 and Single Epithelial Cell Size is 2
(you can neglect the id number column as it doesn't seem  a predictor column)
'''
import pandas as pd
dataset = pd.read_csv("breast_cancer.csv")

dataset = dataset.fillna(dataset.mode().iloc[0])

features = dataset.drop(['A','K'],axis = 1)
labels = dataset['K']

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

# Feature Scaling may be applied

# Fitting Kernel SVM to the Training set
# kernels: linear, poly and rbf
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

def cancer(value):
    if value == 4:
        value = 'cancer'
    elif value == 2:
        value = 'not cancer'
    return value
labels_test = labels_test.apply(cancer)
labels_pred = list(map(cancer,labels_pred))
data=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred}) 
print(data)
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)
#****************************************************************************************

import numpy as np
input_data = [6,2,5,3,2,7,9,2,4]
input_data = np.array(input_data)
input_data = input_data.reshape(1,9)

pred = classifier.predict(input_data)

def cancer1(value):
    if value == 4:
        value = 'Malignant tumor'
    elif value == 2:
        value = 'Benign tumor'
    return value
pred = list(map(cancer1,pred))
print(pred)



'''
Q2. This famous classification dataset first time used in Fisher’s 
classic 1936 paper, The Use of Multiple Measurements in Taxonomic
 Problems. Iris dataset is having 4 features of iris flower and one target class.

The 4 features are

SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
The target class

The flower species type is the target class and it having 3 types

Setosa
Versicolor
Virginica
The idea of implementing svm classifier in Python is to use the iris features
 to train an svm classifier and use the trained svm model to predict the Iris
 species type. To begin with let’s try to load the Iris dataset.
'''
import pandas as pd
from sklearn import datasets 
iris = datasets.load_iris ()

iris_df	= pd.DataFrame (iris.data, columns= iris.feature_names )
iris_df['Target']= iris.target

features = iris_df.drop('Target',axis = 1)
labels = iris_df['Target']

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

# Feature Scaling may be applied

# Fitting Kernel SVM to the Training set
# kernels: linear, poly and rbf
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)
target_names = iris.target_names

def target(value):
    if value==0:
        value = target_names[0]
    elif value==1:
        value = target_names[1]
    elif value==2:
        value = target_names[2]
    return value

labels_test1 =  labels_test.apply(target)
labels_pred1 = list(map(target,labels_pred))

data=pd.DataFrame({'Actual':labels_test1, 'Predicted':labels_pred1}) 
print(data)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)
