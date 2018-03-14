from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class airBnb():

    def test(self):
        baseUrl = 'https://www.airbnb.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        def pause():
        	time.sleep(4)

        # Landing page steps
        searchBar = driver.find_element(By.ID,
        'GeocompleteController-via-SearchBarV2-SearchBarV2')
        searchButton = driver.find_element(By.XPATH, '//button[@type="submit"]')

        searchBar.send_keys("London")
        searchButton.click()
        pause()


ab = airBnb()
ab.test()
