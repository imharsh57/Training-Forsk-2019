'''
Q1. 

(Click Here To Download Training data File): 
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json

(Click Here To Download Test data File):
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json


This is the data for local classified advertisements. It has 9 prominent sections:
    jobs, resumes, gigs, personals, housing, community, services, for-sale and
    discussion forums. Each of these sections is divided into subsections called
    categories. For example, the services section has the following categories under it:
beauty, automotive, computer, household, etc.

For a set of sixteen different cities (such as newyork, Mumbai, etc.), we provide to you data from four sections

        for-sale
        housing
        community
        services

and we have selected a total of 16 categories from the above sections.

        activities
        appliances
        artists
        automotive
        cell-phones
        childcare
        general
        household-services
        housing
        photography
        real-estate
        shared
        temporary
        therapeutic
        video-games
        wanted-housing

Each category belongs to only 1 section.

About Data:

        city (string) : The city for which this Craigslist post was made.
        section (string) : for-sale/housing/etc.
        heading (string) : The heading of the post.

each of the fields have no more than 1000 characters. The input for the program has 
all the fields but category which you have to predict as the answer.

A total of approximately 20,000 records have been provided to you, proportionally 
represented across these sections, categories and cities. The format of training data is the same as input format but with an additional field "category", the category in which the post was made.

Task:

    Given the city, section and heading of an advertisement, can you predict the category under which it was posted?
    Also Show top 5 categories which has highest number of posts
'''

import pandas as pd

'''
with open("data.json") as f:
    data = f.read()
data = data[data.find('{'):]
data = pd.read_json(data,lines = True)

########################################
with open("data.json") as f:
    data = f.read()
data = data[data.find('['):]
data = pd.read_json(data)
'''

#copy the complete data from web and create a new file in spyder and paste it and save as json file
data_train = pd.read_json('Advertisement_train.json', lines=True)
features_test = pd.read_json('Advertisement_test.json', lines=True)

features_train = data_train.drop('category',axis=1)
labels_train = data_train['category']

######################## apply nlp on heading column for train dataset ##############################################
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer

corpus_train = []
for i in range(0, 20217):
    review = re.sub('[^a-zA-Z]', ' ', features_train['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]

    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus_train.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 150)
features= cv.fit_transform(corpus_train).toarray()
features = pd.DataFrame(features)

######################## aapply dummies on city and section #########################################
features_train = features_train.drop('heading',axis=1)
features_train = pd.get_dummies(features_train)

###### merge all the city,heading,section after encoding ##########################
features1=pd.concat([features, features_train], axis=1)

#############label encoding of labels i.e category #########################
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels_train = labelencoder.fit_transform(labels_train)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features1, labels_train)



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
######################## apply nlp on heading column for test dataset ##############################################

corpus_test = []
for i in range(0, 15370):
    review = re.sub('[^a-zA-Z]', ' ', features_test['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]

    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus_test.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 150)
test= cv.fit_transform(corpus_test).toarray()
test = pd.DataFrame(test)

######################## aapply dummies on city and section #########################################
features_test = features_test.drop('heading',axis=1)
features_test = pd.get_dummies(features_test)

###### merge all the city,heading,section after encoding ##########################
test1 = pd.concat([test, features_test], axis=1)
 


# Predicting the Test set results
labels_pred = classifier.predict(test1)
labels_pred = pd.DataFrame(labelencoder.inverse_transform(labels_pred))
print(labels_pred[0].value_counts().head())






'''
Q2. Facial Recognition + OpenCV Python

Facial recognition is a biometric software application capable of uniquely identifying
 or verifying a person by comparing and analyzing.

Things that you need in this project: OpenCV and face_recognition

The project is mainly a method for detecting faces in a given image by using OpenCV-Python
 and face_recognition module. The first phase uses camera to capture the picture of our faces
 which generates a feature set in a location of your PC.

• The face_recognition command lets you recognize faces in a photograph or folder full for photographs.

It has two simple commands

Face_ recognition- Recognise faces in a photograph or folder full for photographs.
face_detection - Find faces in a photograph or folder full for photographs.
For face recognition, first generate a feature set by taking few image of your face
 and create a directory with the name of person and save their face image.


Then train the data by using the Face_ recognition module.By Face_ recognition module
 the trained data is stored as pickle file (.pickle).

By using the trained pickle data, we can recognize face.

The main flow of face recognition is first to locate the face in the picture and the
 compare the picture with the trained data set.If the there is a match, it gives the recognized label.
(Ref: https://github.com/sriram251/-face_recognition)
'''
