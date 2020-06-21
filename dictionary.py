#Given a dictionary
#3 functions:
# cars_dict()-> takes given parameters and creates new dictionary with a value as a key and dictionary as the value
#cars_sorted()-> sorts the value from cars_dict() in ascending order
#cars_updated() uses the value returned from cars_dict() to return keys with a specific value in the dict

import pprint

#Create dictionary for each vehicle with the keys and values
cars = [{'Name': 'Ka', 'Year Introduced': 1996,'Production of current model': 2014, 'Generation': '3rd Generation','Vehicle Information': ' Developed by Ford Brazil as a super mini car'},
{'Name': 'Fiesta', 'Year Introduced': 1976,'Production of current model': 2017, 'Generation': '7th Generation(Mark VIII)','Vehicle Information': ' Ford\'s long running subcompact line based on global B-car Platform'},
{'Name': 'Focus', 'Year Introduced': 1998,'Production of current model': 2018, 'Generation': '3rd Generation (Mark III)','Vehicle Information': ' Ford\'s Compact car based on global C-car platform'},
{'Name': 'Mondeo', 'Year Introduced': 1992,'Production of current model': 2012, 'Generation': '2nd Generation (Fusion)','Vehicle Information': ' Mid sized passenger sedan with \"One-Ford\" design based on CD4 platform.'},
{'Name': 'Fusion', 'Year Introduced': 2005,'Production of current model': 2014, 'Generation': '5th Generation (Mondeo)','Vehicle Information': ' Similar to Mondero.'},
{'Name': 'Taurius', 'Year Introduced': 1986,'Production of current model': 2009, 'Generation': '6th Generation','Vehicle Information': 'Full sized car based on D3 platform'},
{'Name': 'Fiesta ST', 'Year Introduced': 2013,'Production of current model': 2013, 'Generation': '1st Generation (6th Generation)','Vehicle Information': ' Fiesta\'s high performance factory tune'},
{'Name': 'Focus RS', 'Year Introduced': 2015,'Production of current model': 2015, 'Generation': '1st Generation (3rd Generation)','Vehicle Information': 'Special high performance Focus developed by SVT'},
{'Name': 'Mustang', 'Year Introduced': 1964,'Production of current model': 2014, 'Generation': '6th Generation','Vehicle Information': 'Ford\'s long running pony/muscle car'},
{'Name': 'GT', 'Year Introduced': 2004,'Production of current model': 2016, 'Generation': '2nd Generation','Vehicle Information': ' Ford\'s limited production super car inspired by the legendary race car GT40'}]

#funcion to take list of dictionary and return new dictionary
#with the name as the key 
#create new dict
#loop through the given car list and return the new dict
def cars_dict(cars_list):    
    new_Dict={}    
    for i in cars_list:
        new_Dict[i['Name']] = i
    return new_Dict


#function to go through the new_Dict and return list of all car names
#sorted alphabetically
#store the keys in var sorted_cars
def cars_sorted(new_value):         
    sorted_cars = new_value.keys()
    return sorted(sorted_cars)


     
#function to return a dictionary of car names and year introduced
# function would take value of new dict
#create a new dict called updated_dict
# get the value 'year introduced' from new_dict
# loop through using k,v to access the dict key and value   
# The year_value dict-> value also contains keys 
# #make each value['Year Introduced] to be updated with the car names(k) 
#in the updated_dict
def cars_updated(year_value):
     updated_dict = {} 
     for k,v in year_value.items():
       updated_dict[k]=v['Year Introduced']  
     return updated_dict   
       
            
    
   
#pprint.pprint(cars_dict(cars)
#print statement to show the results of sorted dictionary
#pprint.pprint(cars_sorted(cars_dict(cars)))

#pprint.pprint(cars_updated(cars_dict(cars)))

#printing out the result of the updated_dict sorted by year
a = sorted(cars_updated(cars_dict(cars)).items(),key=lambda x:x[1])
for k,v in a:
    print(k,v,sep=' :')
#pprint.pprint(a)
#pprint.pprint(cars)