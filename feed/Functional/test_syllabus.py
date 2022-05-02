from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *


def init():
    driverPath = '../../Driver/chromedriver/chromedriver.exe'
    baseURL = "https://wetechsocial.herokuapp.com/"
    LoginButton = "//button[contains(text(),'Log into Account')]"
    MAILInput = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/input[1]"
    PasswordInput = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/input[2]"
    Mail = "melakubetty@gmail.com"
    PASSWORD = "123456"

    driver = webdriver.Chrome(driverPath)
    # Load the feed page
    driver.get(baseURL)
    driver.maximize_window()
    sleep(3)
    # Login the system with mail and password
    driver.find_element(By.XPATH, LoginButton).click()
    driver.find_element(By.XPATH, MAILInput).send_keys(Mail)
    driver.find_element(By.XPATH, PasswordInput).send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[contains(text(),'Log In')]").click()
    return driver


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
