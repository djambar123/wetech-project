from Setup import *
import unittest


class Syllabus(Setup,unittest.TestCase):

    driver = None

    # Execute before all test methode
    @classmethod
    def setUp(self):
        self.driver = Setup.init(self)
        return self.driver

    def test_syllabus(self):
        sleep(3)
        #
        buttons = self.driver.find_elements(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/ul[1]/ul[1]/li")
        p = 0
        # clicking buttons in syllabus
        while p < len(buttons):
            html_link = self.driver.find_elements(By.CLASS_NAME,"links")
            html_link[p].click()
            sleep(10)
            self.driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[2]").click()
            sleep(3)
            self.driver.back()
            sleep(3)
            p += 1

    # Execute after all test methode
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
