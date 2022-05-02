import time

from Setup import *
import unittest
import pyautogui

LIKE_BUTTON ='//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]//*[name()="svg"]'
DELETE_BUTTON = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/*[name()="svg"][2]'
PROFILE = '//body/div[@id="root"]/div[1]/div[2]/div[1]/div[3]/a[1]/img[1]'

class Post(Setup ,unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        self.driver = Setup.init(self)
        return self.driver


    def test_profile_picture(self):

        self.driver.find_element(By.XPATH, PROFILE).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]").click()
        time.sleep(3)
        picture_post = self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]").get_attribute("innerText")
        assert picture_post == ""


    def test_namePost(self):
        self.driver.find_element(By.XPATH, PROFILE).click()
        time.sleep(2)
        name= self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").get_attribute("innerText")
        assert name == "betty melaku"


    def test_edit_post(self):
        EDIT_BUTTON = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/*[1]"
        INPUT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]'
        SAVE = '//button[contains(text(),"Edit")]'

        self.driver.find_element(By.XPATH, PROFILE).click()
        time.sleep(2)
        """click on the edit button"""
        self.driver.find_element(By.XPATH, EDIT_BUTTON).click()
        time.sleep(3)
        """edit"""
        self.driver.find_element(By.XPATH, INPUT).send_keys("hello you")
        time.sleep(3)
        """save changes"""
        self.driver.find_element(By.XPATH, SAVE).click()
        time.sleep(3)

    def test_delete_post(self):
        self.driver.find_element(By.XPATH, PROFILE).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, DELETE_BUTTON).click()
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)


    def test_likepost(self):

        self.driver.find_element(By.XPATH, PROFILE).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/*[1]").click()
        time.sleep(5)


    def test_comment_profile(self):
        INPUT_COMMENT1 = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/input[1]'
        SEND_BUTTON1 = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]'

        time.sleep(5)
        self.driver.find_element(By.XPATH, INPUT_COMMENT1).send_keys("hello")
        time.sleep(10)
        self.driver.find_element(By.XPATH, SEND_BUTTON1).click()
        time.sleep(10)

    def test_see_comment_profile(self):
        EXIT_COMMENT1 = '//span[contains(text(),"x")]'
        CLICK_ON_COMMENT1 = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]'

        time.sleep(5)
        self.driver.find_element(By.XPATH, CLICK_ON_COMMENT1).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, EXIT_COMMENT1).click()
        time.sleep(5)
