#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
'''
from selenium.common.exceptions import
from selenium.webdriver.support.
'''
import time
print(time.perf_counter())
driver=webdriver.Chrome()

driver.get("https://www.gdms.cloud")
print(time.perf_counter())
driver.implicitly_wait(5)
username=driver.find_element_by_xpath('//input[@type=\'text\']')
username.send_keys('lshuai@grandstream.cn')
psw=driver.find_element_by_xpath('//input[@type=\'password\']')
psw.send_keys('123456gs')
psw.send_keys(Keys.ENTER)



#driver.close()
print(time.perf_counter())