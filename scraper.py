#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import BeautifulSoup
import time
import re
import json
import sys


#----------------------------------------------------------
#This part of the program handles the username and password
#and takes us to the scrapping page
# Module : Selenium and PhantomJS
#----------------------------------------------------------

browser = webdriver.PhantomJS()
browser.set_window_size(1124, 850)#still headless

browser.get('http://etranssolutions.net/web/#')
browser.find_element_by_id('open').click()
browser.find_element_by_id('unm').send_keys(sys.argv[1])
browser.find_element_by_id('pwd').send_keys(sys.argv[2])
browser.find_element_by_class_name('bt_login').click()
time.sleep(3)
browser.get('http://etranssolutions.net:8180/web/vehPos.do')

#----------------------------------------------------------
#This part of the program handles the html source and gives
#us the javascrpt
# Module : BeautifulSoup
#----------------------------------------------------------
html_source = browser.page_source
browser.quit()
soup = BeautifulSoup.BeautifulSoup(html_source)
script = soup('script',{'type' : 'text/javascript'})

#----------------------------------------------------------
#This part of the program handles the javascript and create
#the neccessary json file
# Module : re , json 
#**Note**
# Due to poor formatting of input data and required format
# The large amount of lines.
#----------------------------------------------------------
data_list = re.findall('var desc="(.*?)"', str(script), re.M)
data = [each.split(',&lt;br&gt;') for each in data_list]
data.pop(0)	

raw_dict = {}
for each in data:
	updater = {}
 	raw_dict.update({each[0].split(" - ")[1].strip() : updater })
 	each[2] = each[2].replace("DATE &amp; TIME","TIME")
	each[-1] = each[-1].replace("Latitude,Longitude","location")
 	for count in range(len(each)):
 		temp = each[count].split(" - ")
 		updater.update({temp[0].strip().lower().replace(" ","_"): temp[1].strip()})

for key in raw_dict:
    raw_dict[key].update({"driver_attributes":(raw_dict[key]['driver_mobile_no.'],raw_dict[key]['driver_name'])})
    del raw_dict[key]['driver_mobile_no.']
    del raw_dict[key]['driver_name']

with open('data.json', 'w') as outfile:
    json.dump(raw_dict, outfile)