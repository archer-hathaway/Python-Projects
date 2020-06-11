#pip install requests
# Using open notify API
#
#import requests module
import requests
import json

#create request object to get() which holds the url 
#request = requests.get('http://api.open-notify.org')
#Get html as a content
#print(request.text)
#print(request.status_code)
#using the endpoint 
#get location of iss
#iss_location = requests.get('http://api.open-notify.org/iss-now.json').text
#print(iss_location)
#get number of people in space
iss_people = requests.get('http://api.open-notify.org/astros.json')
data = iss_people.json()
print(data)
print(data['number'])
#
"""
parameter = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json",params=parameter)
data =response.json()
print(data)
"""
