from Setup import *
import unittest


class UI_Feed(Setup, unittest.TestCase):
    """Tests UI in wetechsocial Feed Page ."""

    driver = None

    # Execute before all test methode
    @classmethod
    def setUp(self):
        self.driver = Setup.init(self)
        return self.driver

    def test_toggle_theme(self):
        # check if the page turn dark
        self.driver.find_element(By.CLASS_NAME,"ToggleButton").click()

    def test_upper_bur(self):
        UPPER_BUR_LINK = "//body[1]/div[2]/div[1]/div[2]/div[1]"

        sleep(3)
        UpperBur = self.driver.find_element(By.XPATH,UPPER_BUR_LINK).get_attribute("innerText")
        sleep(3)
        assert UpperBur == "WeTech\nSearch\nLOGOUT"

    def test_search_page(self):
        SEARCH_BUTTON = "//button[contains(text(),'Search')]"
        PEOPLE_TEXT = "//body[1]/div[2]/div[1]/div[2]/div[2]/h1[1]"

        # search page UI
        sleep(3)
        self.driver.find_element(By.XPATH, SEARCH_BUTTON).click()
        sleep(2)
        value = self.driver.find_element(By.XPATH,PEOPLE_TEXT).get_attribute("innerText")
        sleep(3)
        assert value == "People"

    def test_sideBurWrapper(self):
        SIDE_BUR_LINK = "//body[1]/div[2]/div[1]/div[2]/div[2]/div[1]"

        # side bur UI
        sleep(3)
        sideBur = self.driver.find_element(By.XPATH,SIDE_BUR_LINK).get_attribute("innerText")
        sleep(3)
        assert sideBur == "Feed\nEvent\nVideo\nPeople\nMy Followings"

    def test_share(self):
        SHARE_POST = "//body[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]"

        # share post UI
        sleep(3)
        share = self.driver.find_element(By.XPATH,SHARE_POST).get_attribute("innerText")
        assert share == "Photo or Video\nTag\nLocation\nFeeling\nShare"

    def test_right_feed(self):
        RIGHT_FEED = "//body[1]/div[2]/div[1]/div[2]/div[2]/div[3]"

        # right feed UI
        sleep(3)
        value = self.driver.find_element(By.XPATH,RIGHT_FEED).get_attribute("innerText")
        assert value == "Syllabus\nHTML\nCSS\nJAVASCRIPT"

    # Execute after all test methode
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


