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


driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")#write your path of webdriver
URL = "https://www.youtube.com/results?search_query=python&sp=EgIQAQ%253D%253D" #url for your required search results in youtube 
r = requests.get(URL) 

driver.get("https://www.youtube.com/results?search_query=python&sp=EgIQAQ%253D%253D")
content = driver.page_source
soup = BeautifulSoup(content)
all_links = soup.find_all('a',href=True, attrs={'id':"video-title"}) #finds all elements with the given id in hyperlinks
#lists to store video names and their respective ids
v_names=[]
v_id=[]
for link in all_links:
    title = link.get('title', 'No title attribute')
    v_names.append(title)
    x=link.get("href")
    vid=x.strip("/watch?v=")
    v_id.append(vid)
#You can check the length of both the lists to see if the code is working correctly    
df = pd.DataFrame({'VID':v_id,'Video_Title':v_names}) 
df.to_csv('videodetails.csv', index=True, encoding='utf-8')  
print("csv File successfully created!")

file_n = 'videodetails.csv'
col = 'VID'
delimiter = ','													
waittime = 10														# seconds browser waits before giving up
sleeptime = [5,15]													# random seconds range before loading next video id
headless = True														# select True if you want the browser window to be invisible



# prepare log file
logwrite = open('captions.log','w',newline='\n')
logwriter = csv.DictWriter(logwrite, fieldnames=['id','msg'])
logwriter.writeheader()

#Accesing csv file
csvread = open(file_n, newline='\n')
csvreader = csv.DictReader(csvread, delimiter=delimiter, quoting=csv.QUOTE_NONE)
count_rows = len(open(file_n).readlines())

#To Iterate through the ids and store the transcript,uncomment below

#for id in csvreader:
#	msg = gettranscript(id[col])
#	logit(id[col],msg)
#	count_rows -= 1
#	print(str(count_rows) + " :  " + id[col] + " : " + msg)

    
    
