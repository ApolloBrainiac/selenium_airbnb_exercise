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

        


ab = airBnb()
ab.test()
