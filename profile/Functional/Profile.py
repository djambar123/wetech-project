from Setup import *
import unittest

PROFILE = '//body/div[@id="root"]/div[1]/div[2]/div[1]/div[3]/a[1]/img[1]'
SERCH = '//body/div[@id="root"]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]'
BUTTON_SERCH = "//button[contains(text(),'Search')]"

class ProfileBar(Setup ,unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        self.driver = Setup.init(self)
        return self.driver

    def test_Search(self):

        """Tests wetechsocial search feature. Searches for Existing user "simha" then
                        verified that some results show up."""

        self.driver.find_element(By.XPATH, PROFILE).click()
        sleep(2)
        self.driver.find_element(By.XPATH,SERCH).send_keys("simha")
        sleep(2)
        self.driver.find_element(By.XPATH, BUTTON_SERCH).click()
        sleep(3)

        srech= self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]").get_attribute("innerText")
        assert srech == "simha amara\nFrom : israel\nLive's in : rehovot\nFriends : 4 Followings"


    def test_Search_invalid(self):
        """Tests wetechsocial search feature. Searches for field = Null then
                                       verified that some results show up."""

        self.driver.find_element(By.XPATH, PROFILE).click()
        self.driver.find_element(By.XPATH, SERCH).send_keys('')
        self.driver.find_element(By.XPATH, BUTTON_SERCH).click()
        sleep(3)

    def test_Search_incorrectly(self):
        """Tests wetechsocial search feature. Searches for integers- "12354", then
                                verified that some results show up."""

        self.driver.find_element(By.XPATH, PROFILE).click()
        self.driver.find_element(By.XPATH, SERCH).send_keys("123456")
        sleep(2)
        self.driver.find_element(By.XPATH, BUTTON_SERCH).click()
        sleep(2)


    def testButtonlogout(self):

        LOGOUT= "//span[contains(text(),'logout')]"
        self.driver.find_element(By.XPATH,LOGOUT).click()
        sleep(3)

    def testButton_logo(self):
        self.driver.find_element(By.XPATH,PROFILE).click()
        sleep(2)
        LOGO="//span[contains(text(),'WeTech')]"
        self.driver.find_element(By.XPATH,LOGO).click()
        sleep(3)
        namelogo =self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]").get_attribute("innerText")
        assert namelogo == "WeTech"


    def testBotton_Toggle_theme(self):

        self.driver.find_element(By.XPATH,PROFILE).click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Toggle theme')]").click()
        sleep(4)


    # Execute after all test methode
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    # def testSelecting_friends(self):
    #
    #     self.driver.find_element(By.XPATH,PROFILE).click()
    #     sleep(5)
    #     self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/a[1]").click()
    #     sleep(5)

