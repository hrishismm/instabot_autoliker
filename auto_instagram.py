"""
Created By Hrishikesh Gawas
"""

from selenium import webdriver
import time
import requests
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import ElementClickInterceptedException


#Creating the Webprofile
fp=webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf") #mime Value
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "/Desktop/image")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("geo.prompt.testing", True)
fp.set_preference("geo.prompt.testing.allow", True)

#opening json file
with open('login.json','r') as c:
    params=json.load(c)["login"]

#Defination
def autoliker():
    #Creating object of webdriver by specifying the gecko driver link in your machine
    driver=webdriver.Firefox(executable_path="/home/hrishi/Desktop/geckodriver-v0.27.0-linux64/geckodriver",firefox_profile=fp)
    driver.get("https://www.instagram.com/")    
    driver.maximize_window()
    time.sleep(10)
    #getting username password from json file and inputing values
    driver.find_element_by_name("username").send_keys(params['username'])
    driver.find_element_by_name("password").send_keys(params['password'])
    #Click login button
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
    time.sleep(10)
    #Click notification button
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
    time.sleep(10)
    #Click notification button
    driver.find_element_by_class_name("aOOlW").click()
    time.sleep(10)
    for i in range(1,n):
        j=str(i)
        driver.implicitly_wait(4)
        time.sleep(2)
        if(i>=8):
            driver.execute_script("window.scrollBy(0,1500)")
            time.sleep(2)
            try:
                if(driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[4]/div[3]/section[1]/span[1]").is_enabled()):
                    input1 = wait(driver,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[4]/div[3]/section[1]/span[1]')))
                    input1.click()
                    time.sleep(2)
                    print(i,"Hekk")    
                else:
                    driver.execute_script("window.scrollBy(0,1200)")
                    time.sleep(2)
                    driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[4]/div[3]/section[1]/span[1]").click()
                    time.sleep(2)
            except ElementClickInterceptedException:
                driver.execute_script("window.scrollBy(0,200)")
                input1 = wait(driver,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[4]/div[3]/section[1]/span[1]')))
                input1.click()
                time.sleep(2)
                print(i,"xception")    
                
        else:    
            time.sleep(2)
            driver.execute_script("window.scrollBy(0,100)")
            driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[2]/div/article["+j+"]/div[3]/section[1]/span[1]/button").click()
            time.sleep(2)
            print(i)   
            
#Taking user inputs            
n=int(input("Enter the number of posts to like:"))                     
autoliker()


    

