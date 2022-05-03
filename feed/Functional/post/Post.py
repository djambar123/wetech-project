from selenium.webdriver.common.by import By
import unittest
import time
import pyautogui
from Setup import Setup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TEXT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
INPUT_COMMENT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/input[1]'
INPUT = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]'
SAVE = '//button[contains(text(),"Edit")]'
SHARE = '//form[1]/button[1]'
PHOTO_OR_VIDEO ='//form[1]/div[1]/label[1]'
TAG = '//span[contains(text(),"Tag")]'
LOCATION = '//span[contains(text(),"Location")]'
FEELING = '//span[contains(text(),"Feeling")]'
DELETE_BUTTON = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]//*[name()="svg"][2]'
LIKE_BUTTON ='//div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]//*[name()="svg"]'
SEND_BUTTON = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/button[1]'
SEE_COMMENT_BUTTON = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/span[1]'
EDIT_BUTTON = '//body/div[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/*[1]'
LOG_IN_BUTTON = '//button[contains(text(),"Log In")]'
EXIT_COMMENT = '//span[contains(text(),"x")]'



class Post(Setup,unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        self.driver = Setup.init(self)
        return self.driver

    """Tests wetechsocial uploading post with text ."""

    def test_share_text_correctly(self):
        self.driver.find_element(By.XPATH,TEXT).send_keys("Hello, my name is Aviva")
        self.driver.find_element(By.XPATH,SHARE).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, SHARE)))



    """Tests wetechsocial uploading  post with no text."""

    def test_share_text_incorrectly(self):
        self.driver.find_element(By.XPATH,TEXT).send_keys("")
        self.driver.find_element(By.XPATH,SHARE).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, SHARE)))
        self.driver.refresh()



    """Tests wetechsocial uploading  post with photo ."""

    def test_share_image_correctly(self):
        self.driver.find_element(By.XPATH,PHOTO_OR_VIDEO).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, PHOTO_OR_VIDEO)))
        path = r'\\Users\aviva\OneDrive\Pictures\Saved Pictures\log.jpg'
        pyautogui.write(path,interval=0.25)
        pyautogui.press('enter')
        self.driver.find_element(By.XPATH, SHARE).click()
        time.sleep(5)

    """Tests wetechsocial uploading  post with text and photo."""

    def test_share_text_with_image(self):
        self.driver.find_element(By.XPATH,TEXT).send_keys("Hello, Aviva")
        self.driver.find_element(By.XPATH,PHOTO_OR_VIDEO).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, PHOTO_OR_VIDEO)))
        path = r'\\Users\aviva\OneDrive\Pictures\Saved Pictures\pog.jpg'
        pyautogui.write(path,interval=0.25)
        pyautogui.press('enter')
        self.driver.find_element(By.XPATH, SHARE).click()
        time.sleep(5)

    """Tests wetechsocial links in post."""


    def test_Links_in_post(self):
        self.driver.find_element(By.XPATH,TEXT).send_keys("DO NOT WORK")
        self.driver.find_element(By.XPATH,TAG).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, TAG)))
        self.driver.find_element(By.XPATH,LOCATION).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, LOCATION)))
        self.driver.find_element(By.XPATH,FEELING).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, FEELING)))
        self.driver.find_element(By.XPATH,SHARE).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, SHARE)))

    """Tests wetechsocial comment on post."""

    def test_comment_on_post(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,INPUT_COMMENT)))
        self.driver.find_element(By.XPATH,INPUT_COMMENT).send_keys("Nice picture")
        self.driver.find_element(By.XPATH,SEND_BUTTON).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, SEND_BUTTON)))

    """Tests wetechsocial see comment in post."""

    def test_see_comment(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,SEE_COMMENT_BUTTON)))
        self.driver.find_element(By.XPATH,SEE_COMMENT_BUTTON).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, SEE_COMMENT_BUTTON)))
        self.driver.find_element(By.XPATH,EXIT_COMMENT).click()


    """Tests wetechsocial like and unlike on post."""

    def test_like_unlike_post(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,LIKE_BUTTON)))
        self.driver.find_element(By.XPATH,LIKE_BUTTON).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, LIKE_BUTTON)))



    """Tests wetechsocial delete post."""

    def test_delete_post(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,DELETE_BUTTON)))
        self.driver.find_element(By.XPATH,DELETE_BUTTON).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, DELETE_BUTTON)))
        pyautogui.press('enter')



    """Tests wetechsocial edit post."""

    def test_edit_post(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,EDIT_BUTTON)))
        self.driver.find_element(By.XPATH,EDIT_BUTTON).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, EDIT_BUTTON)))
        self.driver.find_element(By.XPATH,INPUT).send_keys("Changes are not saved")
        self.driver.find_element(By.XPATH,SAVE).click()
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()





