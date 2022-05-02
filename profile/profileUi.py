from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from profileimage import *

class profilepage(ProfileImage):
    def testUi(self):
        driver = ProfileImage.init(self)
        feed = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[1]").get_attribute("innerText")
        event = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[2]").get_attribute("innerText")
        video =driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[2]").get_attribute("innerText")
        people=driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[4]").get_attribute("innerText")
        following=driver.find_element(By.XPATH,"//h6[contains(text(),'My Followings')]").get_attribute("innerText")
        not_found = driver.find_element(By.XPATH,"//ul[contains(text(),'not found')]").get_attribute("innerText")
        profile_picture = driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/img[2]").get_attribute("innerText")
        text_profile=driver.find_element(By.XPATH,"//h4[contains(text(),'')]").get_attribute("innerText")
        user_information=driver.find_element(By.XPATH,"//h4[contains(text(),'User information')]").get_attribute("innerText")
        country=driver.find_element(By.XPATH,"//span[contains(text(),'Country:')]").get_attribute("innerText")
        city=driver.find_element(By.XPATH,"//span[contains(text(),'City:')]").get_attribute("innerText")
        Relationship= driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]").get_attribute("innerText")
        user= driver.find_element(By.XPATH,"//h4[contains(text(),"'User Friend''s'")]").get_attribute("innerText")

        assert feed == "Feed"
        assert event == "Event"
        assert video == "Video"
        assert people== "People"
        assert following == 'My Followings'
        assert not_found == 'not found'
        assert profile_picture == ""
        assert text_profile =="undefined undefined"
        assert user_information == 'User information'
        assert country == 'Country:'
        assert city == 'City:'
        assert Relationship == "Relationship: It's private ☺"
        assert user == "User Friend's"