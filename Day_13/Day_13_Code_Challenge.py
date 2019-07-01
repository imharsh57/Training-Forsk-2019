
"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""
from bs4 import BeautifulSoup   
import requests
import matplotlib.pyplot as plt

source = requests.get("https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area").text
print(source)

soup = BeautifulSoup(source,"lxml")
#print (soup.prettify())
table=soup.find('table',class_="wikitable")

B=[]
E=[]

count=0
for row in table.findAll('tr'):
    cells = row.findAll('td')
    #print(cells)
    if len(cells)==7 and count<6:

        B.append(cells[1].text.strip())
        E.append(cells[4].text.strip())
        count+=1

list1=list(zip(B,E))
print(list1)
explode=(0.1,0,0,0,0,0)
colors = ['gold', 'yellowgreen']
plt.pie(E, explode=explode, labels=B, colors=colors,autopct='%1.1f%%', shadow=True, startangle=0)

plt.show()

"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""
import pandas as pd
import matplotlib.pyplot as plt
df_auto = pd.read_csv("Automobile.csv")
make = df_auto['make'].value_counts()
top_10 = make[:10]
series_index = top_10.index
series_value = top_10.values
explode=(0.1,0,0,0,0,0,0,0,0,0)
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(series_value, explode=explode, labels=series_index, colors=colors,autopct='%1.1f%%', shadow=True, startangle=0)

plt.show()


"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""
'''
import pandas as pd
df=pd.DataFrame()
with open("E:\\Forsk\\Day_13\\baby_names\\yob1880.txt","r") as fp:
    fp_read=list(fp.readlines())
with open("E:\\Forsk\\Day_13\\baby_names\\yob1881.txt","r") as fp1:
    fp_read1=list(fp1.readlines())
df['1982']=pd.Series(fp_read1)
'''

import os
import pandas as pd
df=pd.DataFrame()
path = os.getcwd()
os.chdir(path + "\\baby_names")
files = os.listdir(path + "\\baby_names")
os.chdir(path)
index=1880
for item in files:
    if item.endswith("txt"):    
        with open('E:\\Forsk\\Day_13\\baby_names'+'\\'+item,'r') as fp:
            fp_read=list(fp.readlines())
            df[index] = pd.Series(fp_read)
            fp_read.clear()
            index+=1
df.isnull()
count_girl=0
count_boy=0
df=df.fillna('0')
df_top5 = df[1898].str.split(",")
for item in df_top5:
    if item[1]=='F' and count_girl<5:
        print("Girls name :",item[0])
        count_girl+=1
    elif item[1]=='M' and count_boy<5:
        print("Boys name :",item[0])
        count_boy+=1

'''Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  '''



"""
import os
import pandas as pd
df=pd.DataFrame(columns=["Name","Sex","No","Year"])
path = os.getcwd()
os.chdir(path + "\\baby_names")
files = os.listdir(path + "\\baby_names")
os.chdir(path)
index=1880
count=0
for item in files:
    if count<5:
        if item.endswith("txt"):    
            with open('E:\\Forsk\\Day_13\\baby_names'+'\\'+item,'r') as fp:
                fp_read=list(fp.readlines())
                for element in fp_read:
                    t=element.split(",")
                    df['Name']=t[0]
                    df['Sex']=t[1]
                    df['No']=t[2]
                    df['Year']=index
            index+=1
            count+=1
"""
            

        

"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/
    
"""
import pandas as pd
from collections import Counter
dfjson = pd.read_json("usagov_bitly_data.json", lines=True)
dfjson=dfjson.fillna('Missing')
dfjson = dfjson.replace('','Unknown')

df_time = dfjson['tz'].value_counts()
print(df_time.head(10))
print("*********************")
print(df_time)   #Count the number of occurrence for each time-zone

#without pandas
df_counter = Counter(dfjson['tz'])
df_counter = sorted(df_counter.items(), key=lambda x:x[1] ,reverse=True)
print(df_counter[:10])

df_time_10 = df_time.head(10).plot.bar()

df_browser = dfjson['a'].value_counts().head().plot.bar()






"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
    
  Hint:

import pandas as pd
import requests
import StringIO as StringIO
import numpy as np
        
url = "https://data.baltimorecity.gov/api/views/2j28-xzd7/rows.csv?accessType=DOWNLOAD"
r = requests.get(url)
data = StringIO.StringIO(r.content)

dataframe = pd.read_csv(data,header=0)

dataframe['AnnualSalary'] = dataframe['AnnualSalary'].str.lstrip('$')
dataframe['AnnualSalary'] = dataframe['AnnualSalary'].astype(float)

# group the data
grouped = dataframe.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])

# sort the data
pd.set_option('display.max_rows', 10000000)
output = aggregated.sort(['amax'],ascending=0)
output.head(15)


aggregated = grouped.agg([np.sum])
output = aggregated.sort(['sum'],ascending=0)
output = output.head(15)
output.rename(columns={'sum': 'Salary'}, inplace=True)


from matplotlib.ticker import FormatStrFormatter

myplot = output.plot(kind='bar',title='Baltimore Total Annual Salary by Job Title - 2014')
myplot.set_ylabel('$')
myplot.yaxis.set_major_formatter(FormatStrFormatter('%d'))

"""
import pandas as pd
import numpy as np
dfb = pd.read_csv("Baltimore_City_Employee_Salaries_FY2014.csv")
dfb['AnnualSalary'] = dfb['AnnualSalary'].str.replace('$','')
dfb['AnnualSalary'] = dfb['AnnualSalary'].astype(float)

group = dfb.groupby(['JobTitle'])['AnnualSalary']
aggregated = group.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])

sort = dfb.sort_values("AnnualSalary",  ascending = False) 
sort.head(1)
print (str(sort.iloc[0,0])+" get the highest salary")

group1 = dfb.groupby(['JobTitle'])
group1_s = sorted(group1)


print(dfb['JobTitle'].value_counts()[0:10].plot('bar'))

job_spends_most = aggregated.sort_values("sum", ascending = 0)
job_spends_most.head(1)
print(str(job_spends_most.index[0]) + " Spends most")

agency_name_id = dfb[['Agency','AgencyID']]

dfb['GrossPay'].isnull().sum()






"""
Code Challenge
  Name: 
    IGN Analysis
  Filename: 
    ign.py
  Problem Statement:
    Read the ign.csv file and perform the following task :
   
   Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
   
   
   
  Hint:

    The columns contain information about that game:

    score_phrase — how IGN described the game in one word. 
                   This is linked to the score it received.
    title — the name of the game.
    url — the URL where you can see the full review.
    platform — the platform the game was reviewed on (PC, PS4, etc).
    score — the score for the game, from 1.0 to 10.0.
    genre — the genre of the game.
    editors_choice — N if the game wasn't an editor's choice, Y if it was. This is tied to score.
    release_year — the year the game was released.
    release_month — the month the game was released.
    release_day — the day the game was released.



xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
filtered_reviews.head()
      
%matplotlib inline
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

filtered_reviews["score"].hist()
        
"""
import pandas as pd
import matplotlib.pyplot as plt
df_ign = pd.read_csv("ign.csv")
df_score_7 = df_ign[(df_ign['score'] > 7) & (df_ign['platform'] == "Xbox One")]
plt.hist(df_score_7["score"], normed=True, bins=30)
print("games released for the Xbox One that have a score of more than 7",df_score_7['title'].value_counts())

xbox_one = df_ign[df_ign['platform'] == "Xbox One"]['score']
playstation = df_ign[df_ign['platform'] == "PlayStation 4"]['score']
plt.hist(xbox_one, normed=True, bins=30)
plt.hist(playstation, normed=True, bins=30)

