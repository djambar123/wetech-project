from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class Setup:
    def init(self):
        driver = webdriver.Chrome("../driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(("https://wetechsocial.herokuapp.com"))
        driver.find_element(By.XPATH, '//button[contains(text(),"Log into Account")]').click()
        driver.find_element(By.XPATH, '//form[1]/input[1]').send_keys("melakubetty@gmail.com")
        driver.find_element(By.XPATH, '//form[1]/input[2]').send_keys("123456")
        driver.find_element(By.XPATH, '//button[contains(text(),"Log In")]').click()
        sleep(3)
        driver.refresh()
        return driver
