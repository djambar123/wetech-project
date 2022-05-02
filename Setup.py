import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Setup:
    def init(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(("https://wetechsocial.herokuapp.com"))
        driver.find_element(By.XPATH, '//button[contains(text(),"Log into Account")]').click()
        driver.find_element(By.XPATH, '//form[1]/input[1]').send_keys("melakubetty@gmail.com")
        driver.find_element(By.XPATH, '//form[1]/input[2]').send_keys("123456")
        driver.find_element(By.XPATH, '//button[contains(text(),"Log In")]').click()
        time.sleep(3)
        driver.refresh()
        return driver
