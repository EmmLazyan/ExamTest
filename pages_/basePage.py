from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common_.utilities_.customLogger import *



class BasePage():

    def __init__(self, driver: webdriver):
        self.driver = driver

    def _find_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))
        except:
            return element
            logger("Error: Element not Found")
            exit(1)

    def _click(self, webElement):
        webElement.click()






