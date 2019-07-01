# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:39:24 2019

@author: Harsh Anand
"""


'''
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

'''
import pandas as pd

dataset = pd.read_csv('Female_Stats.csv')
features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, 0].values

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(features, labels)

reg.predict([[60,60]])


#Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not

import statsmodels.api as sm
#features = sm.add_constant(features)

features_opt = features[:, [0, 1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

p_value = regressor_OLS.pvalues
Count = True
for item in p_value:
    if item > 0.05:
        Count = False
print(Count)


print("When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height. :",reg.coef_[0])

print("When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.",reg.coef_[1])


'''
#average of student in dataset
average_student = (dataset['Height'].sum())/(len(dataset['Height']))
        

#When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
dataset_father = pd.read_csv('Female_Stats.csv')
#dataset_father['dadheight'] = dataset['dadheight'][0]
dataset_father['momheight'] = dataset_father['momheight'] + 1


average_student = (dataset_father['Height'].sum())/(len(dataset_father['Height']))
'''

#******************************************************************************************************************

'''
Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish-->label

Potential Predictor (Independent Variable): age (in years) of the fish--> feature

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.
'''

import pandas as pd

dataset = pd.read_csv('bluegills.csv')
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

linear_score = regressor.score(features,labels)


from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)

polynomial_score = lin_reg_2.score(features_poly,labels)

if polynomial_score > linear_score:
    print("Poluynomial is better",polynomial_score)
else:
    print("Linear is better",linear_score)

# What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

print (lin_reg_2.predict(poly_object.transform([[5]])))




'''
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
'''
import pandas as pd

dataset = pd.read_csv('iq_size.csv')

features = dataset.iloc[:, 1:].values  
labels = dataset.iloc[:, 0].values 

from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)
from sklearn.linear_model import LinearRegression
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)

polynomial_score = lin_reg_2.predict(poly_object.transform([[90,70,150]]))
print("IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds :",polynomial_score)

# Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
import statsmodels.api as sm
features = sm.add_constant(features) 
features_opt = features[:, [0, 1, 2, 3]]  #create duplicate of features for further progress
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [0, 1, 2]] 
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [1, 2]]  #create duplicate of features for further progress
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [1]]  #create duplicate of features for further progress
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
print ("\n")
print ("Output : Brain Size is the only factor which is more useful in predicting intelligence.")