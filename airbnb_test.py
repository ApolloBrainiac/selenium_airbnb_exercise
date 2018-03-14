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
        pause()
        searchButton.click()
        pause()

        # Date Selection Steps
        dateButton = driver.find_element(By.XPATH,
        	'//span[contains(text(), "Dates"]')
        applyButton = driver.find_element(By.XPATH,
        	'//span[contains(text(), "Apply"]')
        dateButton.cick()
        pause()

        date1 = driver.find_element(By.XPATH, '//td[contains(text(), "15"]')
        date2 = driver.find_element(By.XPATH, '//td[contains(text(), "23"]')

        date1.click()
        pause()

        date2.click()
        pause()

        applyButton.click()
        pause()


ab = airBnb()
ab.test()
