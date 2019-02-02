# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:29:26 2019

@author: dell
"""

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs

url = "https://www.google.com/"
browser = webdriver.Chrome("E:\\Study\\Project_4_Web_Scrapping\\chromedriver.exe")
browser.get(url)

sleep(2)

search = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
search.click()
type_search = "wikipedia"
search.send_keys(type_search)

sleep(2)

search1 = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[2]/div[2]/div/center/input[1]')
search1.click()

sleep(5)

browser.quit()