from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random


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
        searchButton = driver.find_element(
            By.XPATH, '//button[@type="submit"]')

        searchBar.send_keys("London")
        pause()
        searchButton.click()
        pause()

        # Date Selection Steps
        dateButton = driver.find_element(By.XPATH,
                                         '//button[@role="menuitem"]//span[contains(text(), "Dates")]')
        applyButton = driver.find_element(By.XPATH,
                                          '//span[contains(text(), "Apply")]')

        dateButton.click()
        pause()

        ran1 = random.randint(15, 22)
        ran2 = random.randint(23, 30)

        date1 = driver.find_element(
            By.XPATH, '//td[contains(text(), "%s"]' % str(ran1))
        date2 = driver.find_element(
            By.XPATH, '//td[contains(text(), "%s"]' % str(ran2))

        date1.click()
        pause()

        date2.click()
        pause()

        applyButton.click()
        pause()


ab = airBnb()
ab.test()
