
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from profileimage import *


class Second(ProfileImage):
    def testProfileSearch(self):
        driver = ProfileImage.init(self)
        sleep(2)
        PROFILE= "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[3]/a[1]/img[1]"
        driver.find_element(By.XPATH,PROFILE).click()
        SERCH="//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]"
        BUTTON_SERCH="//button[contains(text(),'Search')]"
        sleep(1)
        driver.find_element(By.XPATH,SERCH).send_keys("simha")
        sleep(2)
        driver.find_element(By.XPATH,BUTTON_SERCH).click()
        sleep(1)
        driver.find_element(By.XPATH,PROFILE).click()
        driver.find_element(By.XPATH,SERCH).send_keys('daniel')
        sleep(3)
        driver.find_element(By.XPATH,BUTTON_SERCH).click()
        sleep(5)

    def testButtonlogout(self):
        driver= ProfileImage.init(self)
        sleep(2)
        PROFILE = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[3]/a[1]/img[1]"
        driver.find_element(By.XPATH, PROFILE).click()
        sleep(4)
        LOGOUT= "//span[contains(text(),'logout')]"
        driver.find_element(By.XPATH,LOGOUT).click()
        sleep(3)

    def testButton_logo(self):
        driver=ProfileImage.init(self)
        sleep(2)
        PROFILE="/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[3]/a[1]/img[1]"
        LOGO="//span[contains(text(),'WeTech')]"
        driver.find_element(By.XPATH,PROFILE).click()
        driver.find_element(By.XPATH,LOGO).click()
        sleep(3)

    def testBotton_Toggle_theme(self):
        driver=ProfileImage.init(self)
        sleep(2)
        PROFILE = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[3]/a[1]"
        ToggleTheme ="//button[contains(text(),'Toggle theme')]"
        driver.find_element(By.XPATH,PROFILE).click()
        driver.find_element(By.XPATH,ToggleTheme).click()
        sleep(2)


    def testA_square(self):
        driver=ProfileImage.init(self)
        sleep(2)
        PROFILE = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[3]/a[1]"
        driver.find_element(By.XPATH,PROFILE).click()
        driver.find_element(By.CSS_SELECTOR,"#button").click()
        sleep(2)

    def testSelecting_friends(self):
        driver = ProfileImage.init(self)
        PROFILE= "//body/div[@id='root']/div[1]/div[2]/div[1]/div[3]/a[1]"
        SELECT = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/a[1]/div[1]"
        driver.find_element(By.XPATH,PROFILE).click()
        sleep(1)
        driver.find_element(By.XPATH,SELECT).click()
        sleep(2)