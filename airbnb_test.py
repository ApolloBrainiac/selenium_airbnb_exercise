from selenium import webdriver
from selenium.webdriver.common.by import By
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
        dateButton.click()
        pause()

        ran1 = random.randint(15, 22)
        ran2 = random.randint(23, 30)

        date1 = driver.find_element(
            By.XPATH, '(//td[@role="button" and contains(text(), "%s")])[2]' % str(ran1))
        date1.click()
        pause()

        date2 = driver.find_element(
            By.XPATH, '(//td[@role="button" and contains(text(), "%s")])[2]' % str(ran2))
        date2.click()
        pause()

        applyButton = driver.find_element(By.XPATH,
                                          '//span[contains(text(), "Apply")]')
        applyButton.click()
        pause()

        # Guest Selection Steps
        guestButton = driver.find_element(By.XPATH,
                                          '//button[@role="menuitem"]//div[contains(text(), "Guests")]')
        guestButton.click()
        pause()

        # XPATHS for Guest Buttons
        aduButton = driver.find_element(By.XPATH,
                                        '(//div[@role="menu"]//button[@type="button"])[2]')
        chiButton = driver.find_element(By.XPATH,
                                        '(//div[@role="menu"]//button[@type="button"])[4]')
        infButton = driver.find_element(By.XPATH,
                                        '(//div[@role="menu"]//button[@type="button"])[6]')

        # Add one guest of each type Adult/Child/Infant
        aduButton.click()
        pause()
        chiButton.click()
        pause()
        infButton.click()
        pause()

        # Apply guest selections
        applyButton = driver.find_element(By.XPATH,
                                          '//span[contains(text(), "Apply")]')
        applyButton.click()
        pause()

        # Closes browser
        driver.close()


ab = airBnb()
ab.test()