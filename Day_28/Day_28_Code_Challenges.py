'''.
Q1. (Create a program that fulfills the following specification.)

Program Specification

Use the prev. ANN model to predict if the customer with the following information will leave the bank: (Churn_Modelling.csv)

        Geography: France
        Credit Score: 600
        Gender: Male
        Age: 40 years old
        Tenure: 3 years
        Balance: $60000
        Number of Products: 2
        Does this customer have a credit card? Yes
        Is this customer an Active Member: Yes?
        Estimated Salary: $50000

So, should we say goodbye to that customer?
'''
import numpy as np
import pandas as pd
dataset = pd.read_csv("Churn_Modelling.csv")
features = dataset.iloc[:, 3:13].values

labels = dataset.iloc[:, 13].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_features_1 = LabelEncoder()
features[:,1] = labelencoder_features_1.fit_transform(features[:,1])

features = pd.DataFrame(features)

labelencoder_features_2 = LabelEncoder()
features[:,2] = labelencoder_features_2.fit_transform(features[:,2])

onehotencoder = OneHotEncoder(categorical_features = [1])
features = onehotencoder.fit_transform(features).toarray()

features = features[:, 1:] #dummy variable trap

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

labels_pred = classifier.predict(features_test)
labels_pred = (labels_pred > 0.5)


input_data = [ 600,'France','Male',40,3,60000, 2,1,1,50000]
input_data=np.array(input_data)
input_data = input_data.reshape(-1,10)


input_data[:,1] = labelencoder_features_1.fit_transform(input_data[:,1])
input_data[:,2] = labelencoder_features_2.fit_transform(input_data[:,2])

input_data = onehotencoder.fit_transform(input_data).toarray()


input_data = sc.fit_transform(input_data)







'''
Q2. (Create a program that fulfills the following specification.)

Program Specification

This dataset contains 50 instances for each class. What is interesting about it is that first class is linearly separable from the other two, but the latter two are not linearly separable from each other. Each instance has five attributes:

    Sepal length in cm
    Sepal width in cm
    Petal length in cm
    Petal width in cm
    Class (Iris setosa, Iris virginica, Iris versicolor)

There are two datasets "iris_training.csv" and "iris_test.csv". 
Using these perform ANN with Keras (Sequence Model) and print the accuracy of the model.
'''

