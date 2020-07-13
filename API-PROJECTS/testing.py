#pip install requests
#import tkinter and requests
import tkinter as tk
import requests

#Prompt to check path of image
#The path where the image resides on the computer
#Preferably at the directory where the project resides 
#use r before the path for raw string as most IDE require
PATH_OF_IMAGE= input(r'type/paste the path to the image here. E.g C:\Users\PathOfImage.png: ')
try:
    f = open(PATH_OF_IMAGE, 'rb')

    #PATH_OF_IMAGE= r'C:\Users\micod\Documents\GitHub\Python-Projects\API-PROJECTS\my_image.png'
    #PATH_OF_IMAGE= input(r'type/paste the path to the image here. E.g C:\Users\PathOfImage.png: ')
    #raise PATH_OF_IMAGE
except FileNotFoundError:
    print('Please check the path again')    
#function to show items retreived in readable variables
#When the city name or zip code is provided then function should show:
#name of the city-> city_name
#current cloud view->cloud_view
#temperature of the city->temperature
#The wind speed-> wind_speed
def weather_content(current_weather):
    try:
        city_name= current_weather['name']+','+current_weather['sys']['country']
        cloud_view= current_weather['weather'][0]['description']
        temperature= str(current_weather['main']['temp'])+'F' 
        wind_speed= str(current_weather['wind']['speed'])+' Wind Speed'
        feels_like = 'Feels like '+str(current_weather['main']['feels_like'])+'F'
        humidity ='The humidity is '+str(current_weather['main']['humidity'])+'%'
        result = city_name +'\n ' + cloud_view +'\n '+ temperature  + '\n '+ wind_speed +' \n'+ feels_like +'\n'+ humidity
    except:
        result = 'There were issues with the retrieval\n Make sure you have the right Zip Code or City name'

    return result

#



#function to get the result of the city or zip code
#contains the provided api
#dictionary containing items to be requested from OpenWeather.org
#create object, response that is used to get the requests
#current weather stores the json parameters
def show_weather(city):
    api_key= ''
    url = 'https://api.openweathermap.org/data/2.5/weather'
    param_dict = {'APPID': api_key,'q': city,'units': 'imperial'}
    response = requests.get(url, params=param_dict)
    current_weather= response.json()
    myLabel['text']= weather_content(current_weather)

    
#root window to place content in 
root = tk.Tk()
root.title('Michaels Weather App..........Enter City Name or zip Code')

#canvas area residing in the root window
canvas = tk.Canvas(root,height=500, width= 600,bg='#e8e8fc')
canvas.pack()
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}


#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

#To add the image into the app add path
#Image should preferably be in the same directory
try:
    myImage = tk.PhotoImage(file=PATH_OF_IMAGE)
    imageLabel =tk.Label(root,image= myImage)
    imageLabel.place(relwidth=1,relheight=1)
except:
    print('Path was not correct, App would work without image.Sadly it might Look Ugly')
#create frame object and place in the app 
#Place the frame on the root window
frame = tk.Frame(root,bg='#bcf6bc',bd=10)
frame.place(relx=0.5,rely=0.1,relwidth= 0.75, relheight=0.1,anchor='n')

#entry to take input
inputText = tk.Entry(frame,font=40,bd=6)
inputText.place(relwidth=0.65,relheight=1)

#delete text function to continue trying different cities or zip codes
#still working on this function
#

#create myButton object and place in app
# define lambda function to receive the input 
# #using the .get() method to get the input 
#connecting button to the entry
myButton = tk.Button(frame,text='Submit',font=40,command=lambda:show_weather(inputText.get()))
myButton.place(relx=0.7,rely=0,relwidth=0.3,relheight=1)

#Bottom frame
#Holds the content to display the result of the weather
#Create object and place it on the root window
#Anchor frame to the North of the window
bottomFrame= tk.Frame(root,bg='#159d15',bd=10)
bottomFrame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

#Create label object
#Would cover the whole bottomframe
myLabel= tk.Label(bottomFrame)
myLabel.place(relwidth=1,relheight=1)
#run application 
root.mainloop()