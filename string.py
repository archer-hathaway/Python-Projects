#
#
#
#

#function to return count of UpperCase letters in a given string
def upperCase_count(string):
    string_count=[]   #list to store the UpperCase letters in string
    returnValue=string.isalpha() #check to see if string contains all letters and no numbers
    if returnValue == True:
            for i in string:   #loop through the given string     
                if i == i.upper():
                     string_count.append(i)
                     return len(string_count)  #return the count of uppercase letters, None if no uppercase found 
    else: print('Input characters should be string only')  #message if string is not all letters               
                     
   


        
                     




print(upperCase_count('654'))                  
