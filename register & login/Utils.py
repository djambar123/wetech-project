from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from Setup import Setup
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from Source import *

WE =  "//h3[@class='loginLogo']"
PER =  "//span[@class='LoginDesc']"
SIGN =  "//button[contains(text(),'Log In')]"
LOGIN = "//button[@class='loginRegisterButton']"
PAGELOG = "//button[@class='loginRegisterButton']"




class CHEACK(Setup, unittest.TestCase):

    driver = None

    # Execute before all test methode
    @classmethod
    def setUp(self):
        self.driver = Setup.init_start(self)
        return self.driver

    def test_register(self):
        user_name = "hfc"
        user_LastName = "fyxh"
        Url_profile_pic = "asxasc"
        Url_cover_pic = "file:///Users/dnylgmbr/Desktop/one/17354.webp"
        Emil = "dj@gmail.com"
        contry = "zxc"
        city = "zxc"
        password = "123456"
        conf_password = "123456"
        lis = [user_name,user_LastName,Url_profile_pic,Url_cover_pic,Emil,contry,city,password,conf_password]
        reg = self.driver.find_elements(By.XPATH,"//form[@class='loginBox']/child::*")
        num = 0
        for i in reg:
            if i.tag_name == "input":
                if num < 9:
                    i.send_keys(lis[num])
                    num+=1
            else:
                i.click()
                sleep(3)

                #m = driver.find_element(By.CLASS_NAME("loginInput"))

        try:
            listItems = self.driver.find_elements(By.TAG_NAME, "input")
            for e in listItems:
                isRequired = e.get_attribute("validationMessage")
                if isRequired == "Please fill out this field.":
                    print(e)
                    print("alert Exists in page")
        except :
            print("alert does not Exist in page")

                # alert = driver.switch_to.alert
                # alert.accept()
                # print("alert accepted")




    def test_log(self,Emil,password):
        self.driver.find_element(By.XPATH,"//button[@class='loginRegisterButton']").click()
        lis = [Emil,password]
        log = self.driver.find_elements(By.XPATH, "//form[@class='loginBox']/child::*")
        num = 0
        for i in log:
            if i.tag_name == "input":
                if num < 2:
                    i.send_keys(lis[num])
                    num += 1
            else:
                self.driver.find_element(By.XPATH,"//button[@class='loginButton']").click()
                sleep(1)
            self.driver.close()
        # logout = driver.find_element(By.XPATH, "//span[contains(text(),'logout')][1]").get_attribute("innerText")
        # assert logout == "logout"



    def test_ui_signup(self):
        self.driver.find_element(By.XPATH,PAGELOG).click()
        title = self.driver.find_element(By.XPATH,WE).get_attribute("innerText")
        assert title == "WeTechSocial"

        text = self.driver.find_element(By.XPATH,PER).get_attribute("innerText")
        assert text == "connect with friends and the world around you on We-Tech Social"

        signUp = self.driver.find_element(By.XPATH,SIGN).get_attribute("innerText")
        assert signUp == "Sign Up"

        log = self.driver.find_element(By.XPATH,LOGIN).get_attribute("innerText")
        assert log == "Log into Account"





    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
