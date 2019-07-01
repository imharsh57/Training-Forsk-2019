'''
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
'''
import pandas as pd
dataset = pd.read_csv("BreadBasket_DMS.csv")
df =  (dataset[dataset['Item']=="NONE"]).index
dataset = dataset.drop(df)
dataset = dataset.reset_index(drop=True)

list1=[]

#groupby transction & item and we have to apply lambda on both, key as Transction and value as Item
#store in set then convert to list and append it to list1
dataset.groupby('Transaction')['Item'].apply(lambda x:list1.append(list(set(x))))


'''
for j in range(1,max(dataset['Transaction']+1)):
    transct = []
    for i in range(0,20507):
        if dataset['Transaction'][i]==j:
            transct.append(dataset['Item'][i])
            
    #print(j,transct)
    list1.append(transct)
'''
    
dataset['Item'].value_counts().head(15).plot.pie()
 


    
#************************************************************************************    
from apyori import apriori
rules = apriori(list1, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

# Visualising the results
results = list(rules)
for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

#**********************************************************************************

for item in list1:
    items= item[0]
    pair = item[1:] 
    print("Associated_item for {} are {}  ".format(items ,pair))


'''
Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.
'''
import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset1 = pd.read_csv('Market_Basket_Optimisation.csv', header = None)


#drop the nan values and store the row in list and then all list are store in another list
transactions1 = dataset1.apply(lambda x: x.dropna().tolist(), axis=1).tolist()

########### or ############################
transactions1 = []

for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    transactions1.append([str(dataset1.values[i,j]) for j in range(0, 20)])
    

#removing nan values
i=0
while(i<5):
    for item in transactions1:
        #print(item)
        
        for element in item:
            #print(element)
            if str(element)=='nan':
                #print(element)
                item.remove(element)
    i+=1

###################### or #####################################    
transactions1 = []

for i in range(0, 7501):
    transactions = []
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    for j in range(0, 20):
        if str(dataset1.values[i,j]) == 'nan':
            pass
        else:
            transactions.append(str(dataset1.values[i,j]))
    transactions1.append(transactions)
# Training Apriori on the dataset

rules = apriori(transactions1, min_support = 0.003, min_confidence = 0.25, min_lift = 4)
#min_support--> greater than 3 per day so,per week = 21 -->min_support=21/7501 =0.3
#min_confidence -->25% 
#min_lift --> for  strong association > 1

# Visualising the results
results = list(rules)




for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")




