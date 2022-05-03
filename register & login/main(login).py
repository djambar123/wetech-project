from Source import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utils import *

# valid login
Emil = "dj@mac.com"
password = "123456"
driver = Cheak()
driver.test_log(Emil,password)


#invalid login email null
Emil = ""
password = "123456"
driver = Cheak()
driver.test_log(Emil,password)

#invalid login password null
a = "dj@mac.com"
b = ""
driver = Cheak()
driver.test_log(a,b)

#invalid login password
Emil = "dj@mac.com"
password = "qw1"
driver = Cheak()
driver.test_log(Emil,password)


#invalid login username
Emil = "dj@mac"
password = "123456"
driver = Cheak()
driver.test_log(Emil,password)


#invalid login password
Emil = "dj@mac.com"
password = "123"
driver = Cheak()
driver.test_log(Emil,password)

#invalid login all
Emil = "sdc"
password = "sd2"
driver = Cheak()
driver.test_log(Emil,password)

driver.test_ui_signup()