"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
import json
json_string_s={
        
        
        "Student1" : {
                "First Name" : "Harsh",
                "Last Name" : "Anand",
                "Photo" : "https://cdn.pixabay.com/photo/2014/04/03/10/22/business-310217_960_720.png",
                "Department": "Computer",
                "Contact Details" : {
                        "contact_no" : 78441551,
                        "email_id" : "shhhjs@gsg.chs"
                        }
                }
        }
json_string_f={
        "faculty1" : {
                "First Name" : "Akash",
                "Last Name" : "Singh",
                "Photo" : "https://cdn.pixabay.com/photo/2014/04/03/10/22/business-310217_960_720.png",
                "Department": "Computer",
                "Research Areas" : ["CN","ML"],
                "Contact Details" : {
                        "contact_no" : 85452122,
                        "email_id" : "hdjjhhj@dgh.hh"
                        }
                },
        "faculty2" : {
                "First Name" : "Suresh",
                "Last Name" : "Kumar",
                "Photo" : "https://cdn.pixabay.com/photo/2014/04/03/10/22/business-310217_960_720.png",
                "Department": "Electrical",
                "Research Areas" : ["EDC","DL"],
                "Contact Details" : {
                        "contact_no" : 78441551,
                        "email_id" : "shhhjs@gsg.chs"
                        }
                }
            }
        

with open("faculty.json", "w") as write_file:
    json.dump(json_string_f, write_file)



"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
import requests
city=str(input("Enter city :"))
url1="http://api.openweathermap.org/data/2.5/weather"
url2="?q="
url3=city
url4="&appid=d5e06a3e231b4652d3a448cf7ae5c1da"
url=url1+url2+url3+url4
response=requests.get(url)
data = response.json()
#print(data)
print("Coordinate :",data['coord'])
print("Weather Condition :",data['main'])
print("Wind speed :",data['wind'])
print("Sunrise :",data['sys']['sunrise'])
print("Sunset :",data['sys']['sunset'])




"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import requests
inp1=str(input("what u want to convert :")).upper()
inp2=str(input("In which u want to convert :")).upper()
url="https://free.currconv.com/api/v7/convert?q="+inp1+"_"+inp2+"&compact=ultra&apiKey=c89bace1956dd1fc8884"
response=requests.get(url)
data=response.json()



# Create a new Code Challenge to POST data 

# Research the below wesbite and post some data on it

# https://requestbin.com
import json
import requests

Host = "http://13.127.155.43/api_v0.1/sending"

data = {"Phone_Number":"4572244215","Name":"harsh","College_Name":"Piet","Branch":"cse"}
j_data=json.dumps(data)
headers = {"Content-Type":"application/json"}

def post_method():
    response = requests.post(Host,data=j_data,headers=headers)
    return response

print ( post_method().text)


def get_method():
    response = requests.get("http://13.127.155.43/api_v0.1/receiving")
    return response

print (get_method().text)






