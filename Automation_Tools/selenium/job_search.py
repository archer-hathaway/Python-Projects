#install selenium with pip install selenium
#Using chrome, install/download chromedriver for windows
#Mac and Linux Users can download with this https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver
#Depending on the IDE used , you might have to run the .py file from the terminal or cmd
# By -> python filename.py 
#When adding the PATH, most IDE would require 'r' -> raw string so as not to get unicode error
#The path should be the absolute path where chromedriver.exe resides
from selenium import webdriver
#from selenium.webdriver.chrome.options import options
#import time
import time


PATH = r"C:\Users\micod\Documents\GitHub\Python-Projects\Automation_Tools\selenium\chromedriver.exe"

driver = webdriver.Chrome(PATH)

#access the webpage specified
driver.get('https://www.glassdoor.com/index.htm')
#click on the sign-in NAV to input username and password
driver.find_element_by_xpath('//*[@id="TopNav"]/nav/div/div/div[4]/div[1]/a').click()
#delay of 2secs
time.sleep(2)
#log-in details 
driver.find_element_by_name('username').send_keys('micodian83@gmail.com')
driver.find_element_by_name('password').send_keys('*Venturus09')
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

jobs_outfile = open('./jobs.txt','w')

for job in jobs_List:
    jobs_outfile.write(job.text)


jobs_outfile.close()
#If user has a log-in info
#driver.find_element_by_xpath('//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[1]/div').send_keys('micodian83@gmail.com')
#driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys('*Venturus09')
#driver.find_element_by_xpath('//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/button').click()
#To create an account
#driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys('micodian83@gmail.com')
#driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys('*Venturus09')
#driver.find_element_by_xpath('//*[@id="what"]').send_keys('software Engineer')




"""
jobs_outfile = open('.jobs.txt','w')
for job in job_list:
    jobs_outfile.write(job.text)

//*[@id="JAModal"]/div/div[2]/span/svg

//*[@id="MainCol"]/div[1]/ul

//*[@id="InlineLoginModule"]/div/div/div/div/div/div[3]/form/div[3]/button
//*[@id="userEmail"]
jobs_outfile.close()
#//*[@id="popover-form-container"]
#//*[@class="jobsearch-SerpJobCard unified row result clickcard"]
"""