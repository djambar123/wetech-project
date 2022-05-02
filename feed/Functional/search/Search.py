from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def init():
    driver = webdriver.Chrome('../../Driver/chromedriver/chromedriver.exe')
    driver.get("https://wetechsocial.herokuapp.com/")
    driver.maximize_window()
    sleep(3)
    driver.find_element(By.XPATH,"//button[contains(text(),'Log into Account')]").click()
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/input[1]").send_keys("melakubetty@gmail.com")
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/input[2]").send_keys("123456")
    driver.find_element(By.XPATH,"//button[contains(text(),'Log In')]").click()
    return driver


def test_search_correctly():
    """Tests wetechsocial search feature. Searches for Existing user "simha" then
            verified that some results show up."""

    driver = init()
    searchInput = '//body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]'
    searchButton = "//button[contains(text(),'Search')]"
    sleep(3)
    # Checks if the word "simha" is in the field
    driver.find_element(By.XPATH, searchInput).send_keys("simha")
    sleep(2)
    driver.find_element(By.XPATH, searchButton).click()
    name = driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[2]/div[2]/div[1]").get_attribute(
        "innerText")
    sleep(2)
    assert name == "simha amara\nFrom : israel\nLive's in : rehovot\nFriends : 4 Followings"


def test_search_incorrectly():
    """Tests wetechsocial search feature. Searches for integers- "4561", then
                    verified that some results show up."""
    driver = init()
    sleep(3)
    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]').send_keys(
        "84685")
    sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").click()
    sleep(2)


def test_search_Null():
    """Tests wetechsocial search feature. Searches for field = Null then
                            verified that some results show up."""
    driver = init()
    sleep(3)
    # Checks if the field Null
    driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]').clear()
    sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Search')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]")
    sleep(2)
