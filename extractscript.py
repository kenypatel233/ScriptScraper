from time import sleep
import csv
import random
import os.path
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By   #used to locate elements in the page
from selenium.webdriver.support.ui import WebDriverWait    #explicit wait(wait for a certain condition before getting ahead)
from selenium.webdriver.support import expected_conditions as EC    #a set of predefined conditions to use with WebDriverWait
from selenium.webdriver.chrome.options import Options   #manipulate capabilitites of webdriver

def logit(id,msg):
    logwriter.writerow({'id':id,'msg':msg})
    
def getscript(videoid):
    options = Options()
    options.add_argument("--headless")

	# navigate to video
    driver.get("https://www.youtube.com/watch?v="+videoid)
    try:
        moreActionsButton = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//button[@id="button"][@aria-label="More actions"]'))
    except:
        error = 'Option button not found'
        driver.quit()
        return error
    
    try:
        moreActionsButton.click()
    except:
        error = "1Couldn't click"
        driver.quit()
        return error

    try:
         element = WebDriverWait(driver, waittime).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#items > ytd-menu-service-item-renderer:nth-child(2) > paper-item")))
    except:
        error = 'Transcript not found in options'
        driver.quit()
        return error

    try:
        element.click()
    except:
        error = "2Couldn't click"
        driver.quit()
        return error
    try:
        ActionsButton = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="menu"]/ytd-menu-renderer'))
    except:
        error="transcipt toggle not found"
        driver.quit()
        return error
    try:
        ActionsButton.click()
    except:
        error = "3Couldn't click"
        driver.quit()
        return error
    try:
        toggle=WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_xpath('//*[@id="items"]/ytd-menu-service-item-renderer'))
    except:
        error="toggle option not found"
        driver.quit()
        return error                      
                                                        
                                                        
    try:
        element = WebDriverWait(driver, waittime).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-transcript-body-renderer.style-scope")))
    except:
        error = "Transcript text not found"
        driver.quit()
        return error
    file = open("results.txt","w")
    file.write(element.text)
    file.close() 

    driver.quit()
    
    _file = open("results.txt", "r")
    text = _file.readlines()[1::2]
    
    
       
    _file.close()
    file = videoid + "_" + ".txt"
    _file = open("file.txt", "w")
     
    for i in text:
        
        i = i.replace("\n"," ")
        _file.write(i)
            
        
    
    _file.close()

    return 'OkDone! '



driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
file_n = 'videodetails.csv'
col = 'VID'
delimiter = ','													
waittime = 15														# seconds browser waits before giving up
sleeptime = [5,15]													# random seconds range before loading next video id
headless = True														# select True if you want the browser window to be invisible






msg = getscript("Dox6Y9uefLk")
    

print("Dox6Y9uefLk" + " : " + msg)

