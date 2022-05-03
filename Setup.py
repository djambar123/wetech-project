
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import *



class Setup:
    def init(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(("https://wetechsocial.herokuapp.com"))
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Log into Account")]').click()
        self.driver.find_element(By.XPATH, '//form[1]/input[1]').send_keys("melakubetty@gmail.com")
        self.driver.find_element(By.XPATH, '//form[1]/input[2]').send_keys("123456")
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Log In")]').click()
        sleep(3)
        self.driver.refresh()
        return self.driver
