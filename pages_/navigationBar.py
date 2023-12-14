from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigatonBar(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.__clickToButtonLocator = (By.ID, "bigCookie")

    def clickToButton(self):
        clickToButtonElement= self._find_element(*self.__clickToButtonLocator)
        self._click(clickToButtonElement)
