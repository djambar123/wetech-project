from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def init():
    driver = webdriver.Chrome('../wetech/Driver/chromedriver.exe')
    driver.get('https://wetechsocial.herokuapp.com/')
    driver.maximize_window()
    LOGIN="//button[contains(text(),'Log into Account')]"
    EMAIL="//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/input[1]"
    POSSWORD="//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/input[2]"
    CLICK_LOGIN="//button[contains(text(),'Log In')]"
    driver.find_element(By.XPATH,LOGIN).click()
    driver.find_element(By.XPATH,EMAIL).send_keys('simhaamara2020@gmail.com')
    sleep(1)
    driver.find_element(By.XPATH,POSSWORD).send_keys('202020888')
    sleep(1)
    driver.find_element(By.XPATH,CLICK_LOGIN).click()
    return driver

def testUi():
    driver=init()
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