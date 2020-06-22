#install selenium with pip install selenium
#Using chrome, install/download chromedriver for windows
#Mac and Linux Users can download with this https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver
#Depending on the IDE used , you might have to run the .py file from the terminal or cmd
# By -> python filename.py 
from selenium import webdriver
#from selenium.webdriver.chrome.options import options

driver = webdriver.Chrome()

driver.get('https://www.glassdoor.com/index.htm')
driver.find_element_by_xpath('//*[@id="TopNav"]/nav/div/div/div[4]/div[1]/a').click()

#If user has a log-in info
driver.find_element_by_xpath('//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[1]/div').send_keys('micodian83@gmail.com')
driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys('*Venturus09')
driver.find_element_by_xpath('//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/button').click()
#To create an account
#driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys('micodian83@gmail.com')
#driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys('*Venturus09')
#driver.find_element_by_xpath('//*[@id="what"]').send_keys('software Engineer')


#driver.find_element_by_xpath('//*[@id="LoginModal"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/button').click()

#job_list= driver.find_elements_by_xpath('//*[@class="jobsearch-SerpJobCard unified row result clickcard"]')
#driver.find_element_by_xpath('//*[@id="popover-x"]/a/svg/g/path').click()

"""
jobs_outfile = open('.jobs.txt','w')
for job in job_list:
    jobs_outfile.write(job.text)


//*[@id="InlineLoginModule"]/div/div/div/div/div/div[3]/form/div[3]/button
//*[@id="userEmail"]
jobs_outfile.close()
#//*[@id="popover-form-container"]
#//*[@class="jobsearch-SerpJobCard unified row result clickcard"]
"""