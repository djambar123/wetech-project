from Setup import *
import unittest


class UI_Search(Setup, unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        self.driver = Setup.init(self)
        return self.driver

    def test_toggle_theme(self):
        # check if the page turn dark
        self.driver.find_element(By.CLASS_NAME,"ToggleButton").click()


    def test_upper_bur(self):

        sleep(3)
        UpperBur = self.driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[1]").get_attribute("innerText")
        sleep(3)
        assert UpperBur == "WeTech\nSearch\nLOGOUT"


    def test_search_page(self):
        SEARCH_BUTTON = "//button[contains(text(),'Search')]"
        PEOPLE_TEXT = "//body[1]/div[2]/div[1]/div[2]/div[2]/h1[1]"

        sleep(3)
        self.driver.find_element(By.XPATH, SEARCH_BUTTON).click()
        sleep(2)
        value = self.driver.find_element(By.XPATH,PEOPLE_TEXT).get_attribute("innerText")
        sleep(3)
        assert value == "People"

    def test_sideBurWrapper(self):

        # side bur UI
        sleep(3)
        sideBur = self.driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[2]/div[1]").get_attribute("innerText")
        sleep(3)
        assert sideBur == "Feed\nEvent\nVideo\nPeople\nMy Followings"

    def test_share(self):
        SHARE_POST = "//body[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]"

        # share post UI
        sleep(3)
        share = self.driver.find_element(By.XPATH,SHARE_POST).get_attribute("innerText")
        assert share == "Photo or Video\nTag\nLocation\nFeeling\nShare"

    def test_right_feed(self):
        sleep(3)
        value = self.driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[2]/div[2]/div[3]").get_attribute("innerText")
        assert value == "Syllabus\nHTML\nCSS\nJAVASCRIPT"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


