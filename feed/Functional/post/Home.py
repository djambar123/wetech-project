from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import pyautogui




def init():
    driver = webdriver.Chrome("../../../driver/chromedriver.exe")
    driver.maximize_window()
    driver.get(("https://wetechsocial.herokuapp.com"))
    driver.find_element(By.XPATH, '//button[contains(text(),"Log into Account")]').click()
    driver.find_element(By.XPATH,'//form[1]/input[1]').send_keys("melakubetty@gmail.com")
    driver.find_element(By.XPATH,'//form[1]/input[2]').send_keys("123456")
    driver.find_element(By.XPATH, '//button[contains(text(),"Log In")]').click()
    time.sleep(3)
    driver.refresh()
    return driver

def test_share_text_correctly():
    TEXT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
    SHARE = '//form[1]/button[1]'

    driver = init()
    driver.find_element(By.XPATH,TEXT).send_keys("my name is aviva")
    time.sleep(3)
    driver.find_element(By.XPATH,SHARE).click()
    time.sleep(3)

def test_share_text_incorrectly():
    TEXT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
    SHARE = '//form[1]/button[1]'

    driver = init()
    driver.find_element(By.XPATH,TEXT).send_keys("")
    time.sleep(3)
    driver.find_element(By.XPATH,SHARE).click()
    time.sleep(3)

def test_share_image_correctly():
    PHOTO_OR_VIDEO ='//form[1]/div[1]/label[1]'
    SHARE = '//form[1]/button[1]'

    driver = init()
    time.sleep(3)
    driver.find_element(By.XPATH,PHOTO_OR_VIDEO).click()
    path = r'\\Users\aviva\OneDrive\Pictures\Saved Pictures\log.jpg'
    pyautogui.write(path,interval=0.25)
    pyautogui.press('enter')
    driver.find_element(By.XPATH, SHARE).click()
    time.sleep(10)


def test_share_text_with_image():
    TEXT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
    PHOTO_OR_VIDEO ='//form[1]/div[1]/label[1]'
    SHARE = '//form[1]/button[1]'

    driver = init()
    driver.find_element(By.XPATH,TEXT).send_keys("Hello, aviva")
    time.sleep(3)
    driver.find_element(By.XPATH,PHOTO_OR_VIDEO).click()
    path = r'\\Users\aviva\OneDrive\Pictures\Saved Pictures\pog.jpg'
    pyautogui.write(path,interval=0.25)
    pyautogui.press('enter')
    driver.find_element(By.XPATH, SHARE).click()
    time.sleep(5)


def test_tag_in_post():
    TEXT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
    SHARE = '//form[1]/button[1]'

    driver = init()
    time.sleep(10)
    driver.find_element(By.XPATH,TEXT).send_keys("tag")
    time.sleep(3)
    driver.find_element(By.XPATH,'//span[contains(text(),"Tag")]').click()
    time.sleep(3)
    driver.find_element(By.XPATH,SHARE).click()
    time.sleep(3)

def test_location_in_post():
    TEXT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
    SHARE = '//form[1]/button[1]'

    driver = init()
    time.sleep(10)
    driver.find_element(By.XPATH,TEXT).send_keys("location")
    time.sleep(3)
    driver.find_element(By.XPATH,'//span[contains(text(),"Location")]').click()
    time.sleep(3)
    driver.find_element(By.XPATH,SHARE).click()
    time.sleep(3)


def test_feelings_in_post():
    TEXT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
    SHARE = '//form[1]/button[1]'

    driver = init()
    time.sleep(10)
    driver.find_element(By.XPATH,TEXT).send_keys("feelings")
    time.sleep(3)
    driver.find_element(By.XPATH,'//span[contains(text(),"Feeling")]').click()
    time.sleep(3)
    driver.find_element(By.XPATH,SHARE).click()
    time.sleep(3)


def test_comment_on_post():
    driver = init()
    time.sleep(10)
    driver.find_element(By.XPATH,'//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/input[1]').send_keys("Nice picture")
    time.sleep(3)
    driver.find_element(By.XPATH,'//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/button[1]').click()
    time.sleep(3)

def test_see_comment():
    driver = init()
    time.sleep(10)
    driver.find_element(By.XPATH,'//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/span[1]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//span[contains(text(),"x")]').click()
    time.sleep(5)



def test_like_post():
    driver = init()
    time.sleep(10)

    driver.find_element(By.XPATH,'//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div[1]').click()
    time.sleep(5)

def test_delete_post():
    driver = init()
    time.sleep(10)

    driver.find_element(By.XPATH,'//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/*[2]').click()
    time.sleep(5)
    pyautogui.press('enter')




def test_edit_post():
    EDIT_BUTTON = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/*[1]'
    INPUT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]'
    SAVE = '//button[contains(text(),"Edit")]'

    driver = init()
    time.sleep(3)
    """click on the edit button"""
    driver.find_element(By.XPATH,EDIT_BUTTON).click()
    time.sleep(3)
    """edit"""
    driver.find_element(By.XPATH,INPUT).send_keys("hello you")
    time.sleep(3)
    """save changes"""
    driver.find_element(By.XPATH,SAVE).click()
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)



