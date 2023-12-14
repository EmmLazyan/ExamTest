import unittest
from selenium import webdriver
from common_.utilities_.customListener import MyListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

class NavigationBar(unittest):
    def setUp(self):
        self.simpleDriver = webdriver.chrome
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener)

    def click_To_button(self):
        navigationBareObj =
