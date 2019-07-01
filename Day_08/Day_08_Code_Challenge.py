

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""
from bs4 import BeautifulSoup
import requests
odi= "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(odi).text
soup = BeautifulSoup(source,"lxml")
#print (soup.prettify())
all_tables=soup.find_all('table')
print (all_tables)

right_table=soup.find('table',class_='table')
print(right_table)

A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    #print(row)
    cells = row.findAll('td')
    if len(cells)==5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
import pandas as pd
from collections import OrderedDict

col_name = ["Position","Team","Weighted Match","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(col_data) 
df.to_csv("cricke_rating.csv")
       
"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
import pandas as pd
from selenium import webdriver
link="https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Chrome("E:\\Forsk\\chromedriver.exe")
driver.get(link)
right_table=driver.find_element_by_xpath('//*[@id="pagi_content"]')
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]

for i in range(1,11):
    for row in right_table.find_elements_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']'):
        #print(row)   
        states=row.find_elements_by_tag_name('p')
        i+=1
        
        A.append(states[0].text.strip())
        B.append(states[1].text.strip())
        C.append(states[2].text.strip())
        D.append(states[3].text.strip())
        E.append(states[4].text.strip())
        F.append(states[5].text.strip())
        G.append(states[6].text.strip())
        H.append(states[7].text.strip())
        
import pandas as pd
from collections import OrderedDict

col_name = ["BID_NO","Item","Quantity","Department address","Start Date","End Date"]
col_data = OrderedDict(zip(col_name,[A,C,D,F,G,H]))
df_bid = pd.DataFrame(col_data) 
     

"""
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image


"""
import pandas as pd
from selenium import webdriver
link="http://forsk.in/images/Forsk_logo_bw.png"
driver = webdriver.Chrome("E:\\Forsk\\chromedriver.exe")
driver.get(link)
