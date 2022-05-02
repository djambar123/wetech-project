from Source import *
from selenium.webdriver.common.by import By
from Utils import *

#valid login
Emil = "dj@mac.com"
password = "123456"
driver = Cheak()
driver.test_log(Emil,password)
driver.find_element(By.XPATH, "//form[@class='loginBox']/child::*").get_attribute("validationMessage")


# #invalid login email null
# Emil = ""
# password = "123456"
# driver = Cheak()
# driver.test_log(Emil,password)
#
# #invalid login password null
# Emil = "dj@mac.com"
# password = ""
# driver = Cheak()
# driver.test_log(Emil,password)
#
# #invalid login password null
# Emil = "dj@mac.com"
# password = ""
# driver = Cheak()
# driver.test_log(Emil,password)
#
#
# #invalid login all null
# Emil = ""
# password = ""
# driver = Cheak()
# driver.test_log(Emil,password)
