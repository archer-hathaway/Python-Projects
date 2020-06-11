#pip install requests
# Using open notify API
#
#import requests module
import requests as requests

#create request object to get() which holds the url 
request = requests.get('http://api.open-notify.org')
#Get html as a content
#print(request.text)
#print(request.status_code)
#using the endpoint 
iss_location = requests.get('http://api.open-notify.org/iss-now.json').text
print(iss_location)