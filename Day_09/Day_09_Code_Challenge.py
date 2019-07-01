
"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""
import mysql.connector 
from pandas import DataFrame
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='harsh_mysql', password='monu1234',
                              host='db4free.net', database = 'mysqldb_harsh')

c = conn.cursor()


# STEP 2
#c.execute("DROP Table students;")

# STEP 3
c.execute ("""CREATE TABLE students(
          name TEXT,
          age  INTEGER,
          roll INTEGER,
          branch TEXT
          )""")


# STEP 4
c.execute("INSERT INTO students VALUES ('Harsh',21,33,'cse')")
c.execute("INSERT INTO students VALUES ('Harshit',20,34,'cse')")
c.execute("INSERT INTO students VALUES ('Akash',19,20,'ece')")
c.execute("INSERT INTO students VALUES ('Suresh',22,45,'ee')")
c.execute("INSERT INTO students VALUES ('Alok',21,11,'cv')")
c.execute("INSERT INTO students VALUES ('Harsha',20,31,'cse')")
c.execute("INSERT INTO students VALUES ('Harshita',21,30,'cse')")
c.execute("INSERT INTO students VALUES ('Akasha',17,24,'ece')")
c.execute("INSERT INTO students VALUES ('Suresha',24,35,'ee')")
c.execute("INSERT INTO students VALUES ('Aloka',20,13,'cv')")

# c.execute("INSERT INTO employee VALUES ({},'{}', '{}', {})".format(idd, first,last,pay))


c.execute("SELECT * FROM students")

print ( c.fetchall() )


c.execute("SELECT * FROM students")

df_students = DataFrame(c.fetchall())  # putting the result into Dataframe
df_students.columns = ["Name","Age","Roll","Branch"]



"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.
"""

import pymongo

client = pymongo.MongoClient("mongodb://harsh_19:monu1234@cluster0-shard-00-00-aymha.mongodb.net:27017,cluster0-shard-00-01-aymha.mongodb.net:27017,cluster0-shard-00-02-aymha.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

# --> drop the collection
#mydb.collection_harsh.drop() 


mydb = client.db_harsh

def add_students(Name,Age,Roll,Branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.collection_harsh.insert_one(
            {
            "st_name" : Name,
            "st_age" : Age,
            "st_roll" : Roll,
            "st_branch" : Branch
            })
    return "Students added successfully"


def fetch_all_students():
    user = mydb.collection_harsh.find()
    for i in user:
        print (i)




add_students('Harsh',21,33,'cse')
add_students('Harshit',20,34,'cse')
add_students('Akash',19,20,'ece')
add_students('Suresh',22,45,'ee')
add_students('Alok',21,11,'cv')
add_students('Harsha',20,36,'cse')
add_students('Harshita',19,39,'cse')
add_students('Akasha',22,23,'ece')
add_students('Suresha',21,41,'ee')
add_students('Aloka',22,14,'cv')

fetch_all_students()



"""
Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database
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
        
import mysql.connector 
conn = mysql.connector.connect(user='harsh_mysql', password='monu1234',
                              host='db4free.net', database = 'mysqldb_harsh')

c = conn.cursor()

#c.execute("DROP Table bid;")

c.execute ("""CREATE TABLE bid(
          bid_no VARCHAR(200),
          item  VARCHAR(200),
          quantity VARCHAR(200),
          address VARCHAR(2000),
          start VARCHAR(200),
          end VARCHAR(200)
          )""")
li_bid=list(zip(A,C,D,F,G,H))

for item in li_bid:
    #print(item[5])
    c.execute("INSERT INTO bid VALUES ('{}','{}','{}','{}','{}','{}')".format(item[0],item[1],item[2],item[3],item[4],item[5]))

c.execute("SELECT * FROM bid")  
print ( c.fetchall() )
c.execute("SELECT * FROM bid")


# STEP 6
df_bid_mysql = DataFrame(c.fetchall()) 
df_bid_mysql.columns = ["bid","item","quantity","address","start","end"]      


"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


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

import sqlite3
from pandas import DataFrame
conn = sqlite3.connect ( 'cricket.db' )
c = conn.cursor()

#c.execute("DROP TABLE cricket;")
c.execute ("""CREATE TABLE cricket(
          ranking INTEGER,
          Team  TEXT,
          Match INTEGER,
          Points INTEGER,
          Rating INTEGER
          )""")
      
li_cric=list(zip(A,B,C,D,E))
for item in li_cric:
    #print(item[4])
    # or c.execute("INSERT INTO cricket VALUES ('{}','{}','{}','{}','{}')".format(item[0],item[1],item[2],item[3],item[4]))  
    c.execute("INSERT INTO cricket VALUES (?,?,?,?,?)",(item))
c.execute("SELECT * FROM cricket")
print ( c.fetchall() )
c.execute("SELECT * FROM cricket")

df_cricket = DataFrame(c.fetchall()) 
df_cricket.columns = ["Rank","Team","Match","Points","Rating"]

conn.commit()
conn.close()
    