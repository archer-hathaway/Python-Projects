#install selenium with 'pip install selenium' on your terminal/cmd
#Using chrome, install/download chromedriver for windows
#Mac and Linux Users can download with this https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver
#Some IDE might have issues opening chrome
#Depending on the IDE used , you might have to run the .py file from the terminal or cmd
# Run 'python filename.py' on the terminal/cmd if your prefered IDE dosent work  
#When adding the PATH, most IDE would require 'r' -> raw string so as not to get any unicode error
#The path should be the absolute path where chromedriver.exe resides on your computer
from selenium import webdriver
#from selenium.webdriver.chrome.options import options
#import time
import time
#Welcome page screen
#username and password function
#Function would return username and password

#Please add the path where the chromedriver resides
#PATH = r"C:\Users\fullPathonMyPC\chromedriver.exe"
PATH = r"C:\Users\micod\Documents\GitHub\Python-Projects\Automation_Tools\selenium\chromedriver.exe"

#create driver object
driver = webdriver.Chrome(PATH)

#access jobsearch webpage specified
driver.get('https://www.glassdoor.com/index.htm')
#click on the sign-in NAV to input username and password
driver.find_element_by_xpath('//*[@id="TopNav"]/nav/div/div/div[4]/div[1]/a').click()
#delay of 2secs
time.sleep(2)
#log-in details 
driver.find_element_by_name('username').send_keys('username@gmail.com')
driver.find_element_by_name('password').send_keys('password')
time.sleep(2)
driver.find_element_by_name('submit').click()
time.sleep(2)
#search through with required input
driver.find_element_by_xpath('//*[@id="sc.keyword"]').send_keys('Software Engineer')
driver.find_element_by_xpath('//*[@id="scBar"]/div/button/span').click()
time.sleep(2)

#driver.find_element_by_xpath('//*[@id="JAModal"]/div/div[2]/span/svg').click()
#driver.switchTo().alert().dismiss()
jobs_List = driver.find_elements_by_xpath("//ul[@class='jlGrid hover']/li")


#create text file 
jobs_outfile = open('./jobs.txt','w')
#loop through the list of jobs and write to file
for job in jobs_List:
    jobs_outfile.write(job.text)

#close file
jobs_outfile.close()

#To create an account
#driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys('username@gmail.com')
#driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys('*password')
#driver.find_element_by_xpath('//*[@id="what"]').send_keys('software Engineer')



