'''
Q1. Code Challenge

 Time Series using RNN with Keras
 This is Multivariate Time Series data.
 
 In this project, we will need to do Google stock prediction using time series. We will
 use Keras and Recurrent Neural Network(RNN).
 
 Donwnload the Google stock prices for past 5 years from https://www.nasdaq.com/symbol/goog/historical to a csv file Google2014to2019.csv

and import the basic libraries and read the data from the CSV file.

Take the average of the low and high of the Google stock for the day and volume of the stocks traded
 for the day as input features to predict the stock prices.

We will be creating the data that will go back to 50 business days in past for the prediction.

Also, we will take 30% of the latest data as our test dataset.

For RNN LSTM to predict the data we need to convert the input data.

Input data is in the form: [Volume of stocks traded, Average stock price] and we need to create a time series data.

The time series data for today should contain the [Volume of stocks traded, Average stock price]
 for past 50 days and the target variable will be Google’s stock price today and so on.
'''
import pandas as pd
import numpy as np
dataset = pd.read_csv("Google2014to2019.csv")

#convert all column to float and replace , with space
dataset = dataset.apply(lambda x: x.str.replace(",",""))

for i in dataset:
    if i == "date":
        continue
    dataset[i] = dataset[i].astype(np.float64)

dataset.dtypes 
'''
or
#convert into numeric
dataset['high'] = pd.to_numeric(dataset['high'], errors='coerce')
dataset['low'] = pd.to_numeric(dataset['low'], errors='coerce')
'''

#take average og high & low
dataset['Average'] = dataset[["high", "low"]].mean(axis=1)


test_length = len(dataset)*.3   #take 30% of dataset
test  = dataset.loc[1:test_length,:]
train = dataset.loc[test_length:,:] #take 70% of dataset

test = test[['volume','Average','open']]
train = train[['volume','Average','open']]

from sklearn.preprocessing import MinMaxScaler  
scaler = MinMaxScaler(feature_range = (0, 1))

training_scaled = scaler.fit_transform(train)

features_set = []  
labels = []  
for i in range(50, 882):  
    features_set.append(training_scaled[i-50:i,0:2])
    labels.append(training_scaled[i, -1])
    
features_set, labels = np.array(features_set), np.array(labels)

features_set.shape

from keras.models import Sequential  
from keras.layers import Dense  
from keras.layers import LSTM  
from keras.layers import Dropout

model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape=(features_set.shape[1], 2)))
 #2--> 2 columns, features_set.shape[1]=50 --> no of entries
model.add(Dropout(0.2))

model.add(LSTM(units=50, return_sequences=True))  
model.add(Dropout(0.2))

model.add(LSTM(units=50, return_sequences=True))  
model.add(Dropout(0.2))

model.add(LSTM(units=50))  
model.add(Dropout(0.2))


model.summary()

model.add(Dense(units = 1))

model.compile(optimizer = 'adam', loss = 'mean_squared_error')

model.fit(features_set, labels, epochs = 100, batch_size = 32)
#********************************************************************************************************

"""# Testing the LSTM"""


test.shape

"""Converting test data into right format
"""

total_vol = pd.concat((train['volume'], test['volume']), axis=0)
total_average = pd.concat((train['Average'], test['Average']), axis=0)
total_open = pd.concat((train['open'], test['open']), axis=0)

total_vol.shape
total_average.shape

"""Now let's prepare our test inputs. The input for each day should contain the opening stock prices for the previous 60 days. That means we need opening stock prices for the 20 test days for the month of January 2018 and the 60 stock prices from the last 60 days for the training set."""

test_inputs_vol = total_vol[len(total_vol) - len(test) - 50:].values 
test_inputs_average = total_average[len(total_average) - len(test) - 50:].values 
test_inputs_open = total_open[len(total_open) - len(test) - 50:].values 
#we have to predict last 50 so we don't require top 50 for that
#total_vol[1260 - 378 - 50:] --> [782:]     1260-782=428

test_inputs_vol.shape
test_inputs_average.shape

"""Scale our test data as we did in train data"""
test_inputs_vol = test_inputs_vol.reshape(-1,1)
test_inputs_average = test_inputs_average.reshape(-1,1)
test_inputs_open = test_inputs_open.reshape(-1,1)

test_inputs_vol.shape
test_inputs_average.shape

test_inputs_vol = pd.DataFrame(test_inputs_vol)
test_inputs_average = pd.DataFrame(test_inputs_average)
test_inputs_open = pd.DataFrame(test_inputs_open)

test_inputs_vol['1'] = test_inputs_average
test_inputs_vol['2'] = test_inputs_open
test_input = test_inputs_vol

test_input = scaler.transform(test_input)


test_features = []  
for i in range(832,1260):  
    test_features.append(test_input[i-50:i, 3])

test_features = np.array(test_features)

test_features.shape

test_features = np.reshape(test_features, (test_features.shape[0], test_features.shape[1], 1))

test_features.shape

predictions = model.predict(test_features)

"""Since we scaled our data, the predictions made by the LSTM are also scaled. We need to reverse the scaled prediction back to their actual values. To do so, we can use the ìnverse_transform method of the scaler object we created during training."""



predictions = scaler.inverse_transform(predictions)

plt.figure(figsize=(10,6))  
plt.plot(apple_testing_processed, color='blue', label='Actual Apple Stock Price')  
plt.plot(predictions , color='red', label='Predicted Apple Stock Price')  
plt.title('Apple Stock Price Prediction')  
plt.xlabel('Date')  
plt.ylabel('Apple Stock Price')  
plt.legend()  
plt.show()




