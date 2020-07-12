#Given user input for names, scores with provided number of students
#Program finds the name/names with the least scores and prints out
#Using for loop to iterate through the given number of students
#2 lists are created 
#my_list holds the list of names and score e.g [(harry,88.3),(john,90.2)]
#score_list holds the list of scored provided
#both list are sorted to get the lowest score associated with the name/names
import requests

if __name__ == '__main__':        
    score_list=[]
    my_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append([name,score])
        score_list.append(score)
    b = sorted(list(set(score_list)))[1] #use set to rule out duplicates and then sort
    for a,c in sorted(my_list):#find the lowest number 
        if c == b:
            print(a)  #print name/names 






print(show_weather('boston'))