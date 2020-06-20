"""
try:
    strings = input()
    string_count = []
    for i in strings:        
        if i == i.upper():
             string_count.append(i)
    print(len(string_count))
except ValueError:    
    print('confused')
"""


"""
def upperCase_count(string):
    string_count=[]
    for i in string:        
        if i == i.upper():
             string_count.append(i)

    return len(string_count)        
                     
"""  
string= input()                   
print(bool(re.match('^[0-9]+$', string)))
