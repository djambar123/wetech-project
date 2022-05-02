from selenium import webdriver

class Start():

    def setup(self):
        driver = webdriver.Chrome("/Users/dnylgmbr/PycharmProjects/wetech/drivers/chromedriver")
        driver.get('https://wetechsocial.herokuapp.com/')
        driver.maximize_window()
        return driver