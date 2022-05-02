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
    # Load the system
    driver.get(baseURL)
    driver.maximize_window()
    sleep(3)
    # Login the system with mail and password
    driver.find_element(By.XPATH, LoginButton).click()
    driver.find_element(By.XPATH, MAILInput).send_keys(Mail)
    driver.find_element(By.XPATH, PasswordInput).send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[contains(text(),'Log In')]").click()
    return driver


def test_toggle_theme():
    # check if the page turn dark
    driver = init()
    driver.find_element(By.CLASS_NAME,"ToggleButton").click()


def test_upper_bur():

    driver = init()
    sleep(3)
    UpperBur = driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[1]").get_attribute("innerText")
    sleep(3)
    assert UpperBur == "WeTech\nSearch\nLOGOUT"


def test_search_page():
    SEARCH_BUTTON = "//button[contains(text(),'Search')]"
    PEOPLE_TEXT = "//body[1]/div[2]/div[1]/div[2]/div[2]/h1[1]"

    driver = init()
    sleep(3)
    driver.find_element(By.XPATH, SEARCH_BUTTON).click()
    sleep(2)
    value = driver.find_element(By.XPATH,PEOPLE_TEXT).get_attribute("innerText")
    sleep(3)
    assert value == "People"


def test_sideBurWrapper():


    # side bur UI
    driver = init()
    sleep(3)
    sideBur = driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[2]/div[1]").get_attribute("innerText")
    sleep(3)
    assert sideBur == "Feed\nEvent\nVideo\nPeople\nMy Followings"


def test_share():
    SHARE_POST = "//body[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]"

    # share post UI
    driver = init()
    sleep(3)
    share = driver.find_element(By.XPATH,SHARE_POST).get_attribute("innerText")
    assert share == "Photo or Video\nTag\nLocation\nFeeling\nShare"


def test_right_feed():
    driver = init()
    sleep(3)
    value = driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[2]/div[3]").get_attribute("innerText")
    assert value == "Syllabus\nHTML\nCSS\nJAVASCRIPT"




