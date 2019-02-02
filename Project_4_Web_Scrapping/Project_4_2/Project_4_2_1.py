# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 18:25:28 2019

@author: dell
"""

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
browser = webdriver.Chrome("E:\\Study\\Project_4_Web_Scrapping\\chromedriver.exe")
browser.get(url)


sleep(2)

 
school_code = browser.find_element_by_name("treg")
code="2000"
school_code.send_keys(code)


sleep(2)


get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')
get_school_result.click()


sleep(5)
 
html_page = browser.page_source

soup = BS(html_page)


sleep(3)


browser.quit()