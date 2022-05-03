from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from Source import *

we =  "//h3[@class='loginLogo']"
per =  "//span[@class='LoginDesc']"
sign =  "//button[contains(text(),'Log In')]"
login = "//button[@class='loginRegisterButton']"
pageLog = "//button[@class='loginRegisterButton']"


class Cheak(Start):

    def test_register(self, user_name,user_LastName,url_profile_pic,url_cover_pic,Emil,contry,city,password,conf_password):
        driver = Start.setup(self)
        lis = [user_name,user_LastName,url_profile_pic,url_cover_pic,Emil,contry,city,password,conf_password]
        reg = driver.find_elements(By.XPATH,"//form[@class='loginBox']/child::*")
        num = 0
        for i in reg:
            if i.tag_name == "input":
                if num < 9:
                    i.send_keys(lis[num])
                    num+=1
            else:
                driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
                sleep(3)

                #m = driver.find_element(By.CLASS_NAME("loginInput"))

        try:
            listItems = driver.find_elements(By.TAG_NAME, "input")
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


        driver.close()




    def test_log(self,Emil,password):
        driver = Start.setup(self)
        driver.find_element(By.XPATH,"//button[@class='loginRegisterButton']").click()
        lis = [Emil,password]
        log = driver.find_elements(By.XPATH, "//form[@class='loginBox']/child::*")
        num = 0
        for i in log:
            if i.tag_name == "input":
                if num < 2:
                    i.send_keys(lis[num])
                    num += 1
            else:
                driver.find_element(By.XPATH,"//button[@class='loginButton']").click()
                sleep(1)
            driver.close()
        # logout = driver.find_element(By.XPATH, "//span[contains(text(),'logout')][1]").get_attribute("innerText")
        # assert logout == "logout"



    def test_ui_signup(self):
        driver = Start.setup(self)
        driver.find_element(By.XPATH,pageLog).click()
        title = driver.find_element(By.XPATH,we).get_attribute("innerText")
        assert title == "WeTechSocial"

        text = driver.find_element(By.XPATH,per).get_attribute("innerText")
        assert text == "connect with friends and the world around you on We-Tech Social"

        signUp = driver.find_element(By.XPATH,sign).get_attribute("innerText")
        assert signUp == "Sign Up"

        log = driver.find_element(By.XPATH,login).get_attribute("innerText")
        assert log == "Log into Account"



# def test_signup():
#     driver = init()
#     driver.find_element(By.XPATH, "//input[@placeholder='User Name']").send_keys(user_name)
#     driver.find_element(By.XPATH, "//input[@placeholder='User Last Name']").send_keys(user_LastName)
#     driver.find_element(By.XPATH, "//input[@placeholder='User Profile picture']").send_keys(url_profile_pic)
#     driver.find_element(By.XPATH, "//input[@placeholder='cover Picture']").send_keys(url_cover_pic)
#     driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(Emil)
#     driver.find_element(By.XPATH, "//input[@placeholder='Country']").send_keys(contry)
#     driver.find_element(By.CSS_SELECTOR, "input[placeholder='City']").send_keys(city)
#     driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)
#     driver.find_element(By.CSS_SELECTOR, "input[placeholder='PasswordConfirm']").send_keys(conf_password)
#     sleep(3)
#     driver.find_element(By.XPATH,"//button[@type='submit']").click()
#     sleep(3)
#     logout = driver.find_element(By.CLASS_NAME, "MuiButton-label").get_attribute("innerText")
#     assert logout == "LOGOUT"
#     driver.close()
#
#
#
# def test_login():
#     driver = init()
#     driver.find_element(By.XPATH,"//button[@class='loginRegisterButton']").click()
#     driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys(Emil)
#     driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(password)
#     driver.find_element(By.XPATH,"//button[@class='loginButton']").click()
#     sleep(3)
#     logout = driver.find_element(By.CLASS_NAME,"MuiButton-label").get_attribute("innerText")
#     assert logout == "LOGOUT"
#     driver.close()

