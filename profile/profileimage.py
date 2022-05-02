from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class ProfileImage:
    def init(self):
        driver = webdriver.Chrome('C:/Users/User/wetech/Driver/chromedriver.exe')
        driver.get('https://wetechsocial.herokuapp.com/')
        driver.maximize_window()
        LOGIN = "//button[contains(text(),'Log into Account')]"
        EMAIL = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/input[1]"
        POSSWORD = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/input[2]"
        CLICK_LOGIN = "//button[contains(text(),'Log In')]"
        driver.find_element(By.XPATH, LOGIN).click()
        driver.find_element(By.XPATH, EMAIL).send_keys('simhaamara2020@gmail.com')
        sleep(1)
        driver.find_element(By.XPATH, POSSWORD).send_keys('202020888')
        sleep(1)
        driver.find_element(By.XPATH, CLICK_LOGIN).click()
        return driver
