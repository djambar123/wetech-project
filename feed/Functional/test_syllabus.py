from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *
from profile import *

def test_syllabus():
    driver = init()
    sleep(3)
    #
    driver.find_elements(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/ul[1]/ul[1]/li")
    p = 0
    # clicking buttons
    while p < 3:
        html_link = driver.find_elements(By.CLASS_NAME,"links")
        html_link[p].click()
        sleep(10)
        driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[2]").click()
        sleep(3)
        driver.back()
        sleep(3)
        p += 1
