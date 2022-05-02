from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
import pyautogui
from Setup import Setup
from selenium.webdriver.common.action_chains import ActionChains




TEXT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
INPUT_COMMENT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/input[1]'
INPUT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]'
SAVE = '//button[contains(text(),"Edit")]'
SHARE = '//form[1]/button[1]'
PHOTO_OR_VIDEO ='//form[1]/div[1]/label[1]'
DELETE_BUTTON = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]//*[name()="svg"][2]'
LIKE_BUTTON ='//div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]//*[name()="svg"]'
SEND_BUTTON = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/button[1]'
SEE_COMMENT_BUTTON = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/span[1]'
EDIT_BUTTON = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/*[1]'



class Post(Setup,unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        self.driver = Setup.init(self)
        return self.driver


    def test_share_text_correctly(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,TEXT).send_keys("Hello, my name is Aviva")
        time.sleep(3)
        self.driver.find_element(By.XPATH,SHARE).click()
        time.sleep(3)




    def test_share_text_incorrectly(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,TEXT).send_keys("")
        time.sleep(3)
        self.driver.find_element(By.XPATH,SHARE).click()
        time.sleep(3)



    def test_share_image_correctly(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,PHOTO_OR_VIDEO).click()
        path = r'\\Users\aviva\OneDrive\Pictures\Saved Pictures\log.jpg'
        pyautogui.write(path,interval=0.25)
        pyautogui.press('enter')
        self.driver.find_element(By.XPATH, SHARE).click()
        time.sleep(10)



    def test_share_text_with_image(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,TEXT).send_keys("Hello, aviva")
        time.sleep(3)
        self.driver.find_element(By.XPATH,PHOTO_OR_VIDEO).click()
        path = r'\\Users\aviva\OneDrive\Pictures\Saved Pictures\pog.jpg'
        pyautogui.write(path,interval=0.25)
        pyautogui.press('enter')
        self.driver.find_element(By.XPATH, SHARE).click()
        time.sleep(3)


    def test_tag_in_post(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,TEXT).send_keys("tag")
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//span[contains(text(),"Tag")]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,SHARE).click()
        time.sleep(3)



    def test_location_in_post(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,TEXT).send_keys("location")
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//span[contains(text(),"Location")]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,SHARE).click()
        time.sleep(3)



    def test_feelings_in_post(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,TEXT).send_keys("feelings")
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//span[contains(text(),"Feeling")]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,SHARE).click()
        time.sleep(3)


    def test_comment_on_post(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,INPUT_COMMENT).send_keys("Nice picture")
        time.sleep(3)
        self.driver.find_element(By.XPATH,SEND_BUTTON).click()
        time.sleep(3)



    def test_see_comment(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,SEE_COMMENT_BUTTON).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//span[contains(text(),"x")]').click()
        time.sleep(3)



    def test_like_post(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,LIKE_BUTTON).click()
        time.sleep(3)



    def test_delete_post(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,DELETE_BUTTON).click()
        time.sleep(3)
        pyautogui.press('enter')
        self.driver.refresh()
        time.sleep(5)




    def test_edit_post(self):
        time.sleep(3)
        """click on the edit button"""
        self.driver.find_element(By.XPATH,EDIT_BUTTON).click()
        time.sleep(3)
        """edit"""
        self.driver.find_element(By.XPATH,INPUT).send_keys("hello you")
        time.sleep(3)
        """save changes"""
        self.driver.find_element(By.XPATH,SAVE).click()
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()





