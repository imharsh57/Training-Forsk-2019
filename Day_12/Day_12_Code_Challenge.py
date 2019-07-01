"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""
import pandas as pd
df_code=pd.read_csv("training_titanic.csv")

data_survived = df_code['Survived'].value_counts()
print("people in the given training set survived the disaster :",data_survived[1])
print("people in the given training set died the disaster :",data_survived[0])

data_survived_percentage=df_code['Survived'].value_counts(normalize = True)  
print("people in the given training set survived the disaster :",data_survived_percentage[1])

#or
'''
df_survive=df_code[df_code['Survived'].map(lambda x:True if x==1 else False)]['Survived'].value_counts()
df_died=df_code[df_code['Survived'].map(lambda x:False if x==1 else True)]['Survived'].value_counts()
print("people in the given training set survived the disaster :",df_survive)
print("people in the given training set died the disaster :",df_died)
'''
df_survive_male=df_code['Survived'][df_code['Sex']=="male"].value_counts(normalize = True)[1]
df_survive_female=df_code['Survived'][df_code['Sex']=="female"].value_counts(normalize = True)[1]
df_died_male=df_code['Survived'][df_code['Sex']=="male"].value_counts(normalize = True)[0]
df_died_female=df_code['Survived'][df_code['Sex']=="female"].value_counts(normalize = True)[0]
print("Male survive :",df_survive_male)
print("FeMale survive :",df_survive_female)
print("Male died :",df_died_male)
print("feMale died :",df_died_female)

''' 
a1=df_code["Age"].mean()   #fill the NaN value with mean of age
df_code["Age"]=df_code["Age"].fillna(a1)
'''
df_code["Age"]=df_code["Age"].fillna(0)
df_code["child"] = df_code["Age"].map(lambda x: 0 if x >18 else 1 ) #creates new column of child

df_survive_child=df_code['Survived'][df_code['child']==1].value_counts(normalize=True)[1]
df_dead_child=df_code['Survived'][df_code['child']==1].value_counts(normalize=True)[0]
print("Child survive :",df_survive_child)
print("Child died :",df_dead_child)




"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import pandas as pd
import numpy as np
df_auto=pd.read_csv("Automobile.csv")
df_price_mean=df_auto['price'].mean()
df_auto['price']=df_auto['price'].fillna(df_price_mean) #Handle the missing values for Price column

list_price = df_auto['price'].tolist()
#print(list_price)
list_price_numpy=np.array(list_price) #Get the values from Price column into a numpy.ndarray
print("Minimum Price :",list_price_numpy.min())
print("Maximum Price :",list_price_numpy.max())
print("Aveerage Price :",list_price_numpy.mean())
print("Standard Deviation :",list_price_numpy.std())




"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
  Hint:

"""
import pandas as pd
import numpy as np
df=pd.read_csv("thanksgiving.csv",encoding="Windows 1252")
#df.columns = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13','a14','a15','a16','a17','a18','a19','a20','a21','a22','a23','a24','a25','a26','a27','a28','a29','a30','a31','a32','a33','a34','a35','a36','a37','a38','a39','a40','a41','a42','a43','a44','a45','a46','a47','a48','a49','a50','a51','a52','a53','a54','a55','a56','a57','a58','a59','a60','a61','a62','a63','a64','a65']

columns_name = list(df.columns)#storing the column name

li=[]
for i in range(1,len(df.columns)+1):
    #li.append('a'+str(i))
    li.append(i)
df.columns = list(li) #column name changed

#storing the column name
code_col= list(df.columns)

    # Storing the column name with their codes for further reference
columns_ref = dict(zip(code_col, columns_name))

#***************************************************************************
#Using the apply method to Gender column to convert Male & Female
def gender(gender_str):
    if gender_str=="Male":
        gender_str="M"
    elif gender_str=="Female":
        gender_str="F"
    else:
        pass
    return gender_str

df[63] = df[63].fillna('not specified') #fill the nan values
df[63] = df[63].apply(gender)
#*****************************************************************************
''' Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)'''
df[64] = df[64].replace(['Prefer not to answer',np.NaN],[0,0])




"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
      
File Name : Telecom_Churn.py
problem Statement:
To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght? Predict and print it
6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
7. In which area code the international plan is most availed?
"""
import pandas as pd
df_telecom=pd.read_csv("Telecom_churn.csv")   

df_voice_int=df_telecom[(df_telecom['international plan']=="yes") & (df_telecom['voice mail plan']=="yes") & (df_telecom['churn']==True)]
df_voice_int['voice mail plan'].value_counts()

df_int_churn=df_telecom[(df_telecom['total intl charge']>0) & (df_telecom['churn']==True)]
print("Total charges for international calls made by churned :",df_int_churn['total intl charge'].sum())
df_int_notchurn=df_telecom[(df_telecom['total intl charge']>0) & (df_telecom['churn']==False)]
print("Total charges for international calls made by non- churned :",df_int_notchurn['total intl charge'].sum())

df_churn=df_telecom[df_telecom['churn']==True]
night_call=df_churn.loc[df_churn['total night calls'].argmax()]
# argmax return index of maximum element from column & max return max element from column
print("{} state having highest night call minutes for churned customer".format(night_call['state']))


list1=[]
df_day_calls = df_churn['total day calls'].sum()
list1.append(df_day_calls)
df_eve_calls = df_churn['total eve calls'].sum()
list1.append(df_eve_calls)
df_night_calls = df_churn['total night calls'].sum()
list1.append(df_night_calls)
df_intl_calls = df_churn['total intl calls'].sum()
list1.append(df_intl_calls)
#print(list1)
most_popular = max(list1)
for i,j in enumerate(list1):
    if j==most_popular:
        if i==0:
            print("Day_calls are the most popular amoung churned user")
        elif i==1:
            print("Evening_calls are the most popular amoung churned user")
        elif i==2:
            print("Night_calls are the most popular amoung churned user")
        else:
            print("International_calls are the most popular amoung churned user")
list2=[]
df_day_charge = df_churn['total day charge'].sum()
list2.append(df_day_charge)
df_eve_charge = df_churn['total eve charge'].sum()
list2.append(df_eve_charge)
df_night_charge = df_churn['total night charge'].sum()
list2.append(df_night_charge)
df_intl_charge = df_churn['total intl charge'].sum()
list2.append(df_intl_charge)
#print(list2)
min_chargable = min(list2)
for i,j in enumerate(list2):
    if j==min_chargable:
        if i==0:
            print("Day_calls are the less chargable amoung churned user")
        elif i==1:
            print("Evening_calls are the less chargable amoung churned user")
        elif i==2:
            print("Night_calls are the less chargabler amoung churned user")
        else:
            print("International_calls are the less chargable amoung churned user")


max_account_length = df_telecom.loc[df_telecom['account length'].argmax()]
print(max_account_length )

avail_intl_plan = pd.DataFrame(df_telecom,columns=['area code','international plan'])
avail_intl=avail_intl_plan[(avail_intl_plan['international plan']=="yes")]
most_availed = avail_intl['area code'].value_counts().argmax()
print("{} area code the international plan is most availed".format(most_availed))
