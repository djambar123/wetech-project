
import unittest
from Setup import *

PROFILE = '//body/div[@id="root"]/div[1]/div[2]/div[1]/div[3]/a[1]/img[1]'

class UI(Setup, unittest.TestCase):


    @classmethod
    def setUp(self):
        self.driver = Setup.init(self)
        return self.driver

    def test_upper_bur(self):
             self.driver.find_element(By.XPATH, PROFILE).click()
             sleep(3)
             UpperBur = self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[2]/div[1]").get_attribute("innerText")
             sleep(3)
             assert UpperBur == "WeTech\nSearch\nLOGOUT"

    def test_Ui_feed(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            feed = self.driver.find_element(By.XPATH,"//span[contains(text(),'Feed')]").get_attribute("innerText")
            assert feed == "Feed"


    def test_Ui_even(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            event = self.driver.find_element(By.XPATH,"//span[contains(text(),'Event')]").get_attribute("innerText")
            assert event == "Event"

    def test_ui_video(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            video = self.driver.find_element(By.XPATH,"//span[contains(text(),'Video')]").get_attribute("innerText")
            assert video == "Video"

    def test_ui_people(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            people=self.driver.find_element(By.XPATH,"//span[contains(text(),'People')]").get_attribute("innerText")
            assert people == "People"

    def test_ui_following(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            following=self.driver.find_element(By.XPATH,"//h6[contains(text(),'My Followings')]").get_attribute("innerText")
            assert following == 'My Followings'

    # def test_ui_found(self):
    #         self.driver.find_element(By.XPATH, PROFILE).click()
    #         sleep(3)
    #         not_found = self.driver.find_element(By.XPATH,"//ul[contains(text(),'not found')]").get_attribute("innerText")
    #         assert not_found == 'not found'


    def test_ui_profile_picture(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            profile_picture = self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/img[2]").get_attribute("innerText")
            assert profile_picture == ""

    def test_ui_text_picture(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            text_profile= self.driver.find_element(By.XPATH,"//h4[contains(text(),'')]").get_attribute("innerText")
            assert text_profile == "betty melaku"

    def test_ui_userinfromtion(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            user_information=self.driver.find_element(By.XPATH,"//h4[contains(text(),'User information')]").get_attribute("innerText")
            assert user_information == 'User information'

    def test_ui_contry(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            country= self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]").get_attribute("innerText")
            assert country == "Country: Israel\nCity: גן יבנה"

    def test_ui_city(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            city=self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]").get_attribute("innerText")
            assert city == "Country: Israel\nCity: גן יבנה"

    def test_ui_Relationship(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            Relationship= self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]").get_attribute("innerText")
            assert Relationship == "Relationship: It's private ☺"

    def test_ui_user(self):
            self.driver.find_element(By.XPATH, PROFILE).click()
            sleep(3)
            user= self.driver.find_element(By.CSS_SELECTOR,"body.INDlangdirLTR.INDpositionLeft.INDDesktop.INDChrome.INDhasDragTooltip:nth-child(2) div.profile div.profileRight div.profileRightBottom div.rightBar div.rightBarWrapper div.rigthBarInfo > h4.rightBarTitleFirstPart:nth-child(3)").get_attribute("innerText")
            assert user == "User Friend's"

    def testA_square(self):

        self.driver.find_element(By.XPATH,PROFILE).click()
        self.driver.find_element(By.CSS_SELECTOR,"#button").click()
        sleep(2)