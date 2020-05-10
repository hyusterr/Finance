#!bin/python
# -*- coding: big5 -*-

import selenium as se
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://mops.twse.com.tw/mops/web/t123sb06_q1')

doc = driver.find_element_by_xpath('//*[@id="table01"]/center/form/div[2]/b/button/font/u')
doc.click()
time.sleep(10)

