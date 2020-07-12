import sys
"""
def reversDigits(num): 
    reverse=0
    while (num > 0): 
        remainder = num%10 
        reverse= reverse*10 +remainder
        num=num//10

    return reverse  
           

def addNumbers(string):

    while string < 646376895:
        rev_num= reversDigits(string)
        string = rev_num+ string
        if palindrome(string):
            print (string)
            break
        else:
            if(string >646376895):
                return 'no palindrome'   


    

def palindrome(result):
    return (reversDigits(result)==result)    


value =53232
print(value+1)
print(addNumbers(reversDigits(value)))
"""
"""
string = 'My anime is sentence'
split= string.split()
reverse = ','.join(reversed(split))

print(reverse)
print(split[-2])
"""

for line in sys.stdin:
    print(line,end='')