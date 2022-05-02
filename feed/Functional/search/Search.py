from Setup import *
import unittest

searchInput = '//body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]'
searchButton = "//button[contains(text(),'Search')]"


class Search(Setup, unittest.TestCase):

    driver = None

    # Execute before all test methode
    @classmethod
    def setUp(self):
        self.driver = Setup.init(self)
        return self.driver

    def test_search_correctly(self):

        """Tests wetechsocial search feature. Searches for Existing user "simha" then
                verified that some results show up."""

        sleep(3)
        # Checks if the word "simha" is in the field
        self.driver.find_element(By.XPATH, searchInput).send_keys("simha")
        sleep(2)
        self.driver.find_element(By.XPATH, searchButton).click()
        name = self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[2]/div[2]/div[1]").get_attribute(
            "innerText")
        sleep(2)
        assert name == "simha amara\nFrom : israel\nLive's in : rehovot\nFriends : 4 Followings"

    def test_search_incorrectly(self):

        """Tests wetechsocial search feature. Searches for integers- "4561", then
                        verified that some results show up."""

        sleep(3)
        # Checks if the digits is in the field
        self.driver.find_element(By.XPATH, searchInput).send_keys("84685")
        sleep(2)
        self.driver.find_element(By.XPATH, searchButton).click()
        sleep(2)

    def test_search_Null(self):

        """Tests wetechsocial search feature. Searches for field = Null then
                                verified that some results show up."""
        sleep(3)
        # Checks if the field Null
        self.driver.find_element(By.XPATH, searchInput).clear()
        sleep(2)
        self.driver.find_element(By.XPATH, searchButton).click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]")
        sleep(2)

    # Execute after all test methode
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
