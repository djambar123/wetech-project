from Setup import *
import unittest
import pyautogui


PROFILE = '//body/div[@id="root"]/div[1]/div[2]/div[1]/div[3]/a[1]/img[1]'

class Post(Setup ,unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        self.driver = Setup.init(self)
        return self.driver


    def test_profile_picture(self):

        self.driver.find_element(By.XPATH, PROFILE).click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]").click()
        sleep(3)
        picture_post = self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]").get_attribute("innerText")
        assert picture_post == ""


    def test_namePost(self):
        self.driver.find_element(By.XPATH, PROFILE).click()
        sleep(2)
        name= self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").get_attribute("innerText")
        assert name == "betty melaku"


    def test_edit_post(self):
        EDIT_BUTTON = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/*[1]"
        INPUT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]'
        SAVE = '//button[contains(text(),"Edit")]'

        self.driver.find_element(By.XPATH, PROFILE).click()
        sleep(2)
        """click on the edit button"""
        self.driver.find_element(By.XPATH, EDIT_BUTTON).click()
        sleep(3)
        """edit"""
        self.driver.find_element(By.XPATH, INPUT).send_keys("hello you")
        sleep(3)
        """save changes"""
        self.driver.find_element(By.XPATH, SAVE).click()
        sleep(3)

    def test_delete_post(self):
        self.driver.find_element(By.XPATH, PROFILE).click()
        sleep(2)
        # self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/*[2]").click()
        # sleep(5)
        # pyautogui.press('enter')

    def test_like_post(self):
        self.driver.find_element(By.XPATH, PROFILE).click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/*[1]").click()
        sleep(5)

    def test_nolikepost(self):

        self.driver.find_element(By.XPATH, PROFILE).click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[2]/*[1]").click()
        sleep(5)

    def test_count_likes(self):
        self.driver.find_element(By.XPATH, PROFILE).click()
        sleep(2)
        count= self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]").get_attribute("innarText")
        assert count == "0 people like it"
