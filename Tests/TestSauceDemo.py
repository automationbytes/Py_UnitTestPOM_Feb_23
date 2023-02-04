import unittest
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Util.ExcelReader import readExcel
from Pages.loginPage import loginPage
from Pages.homePage import homePage

class sauceLabsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://www.saucedemo.com/")
    #
    # def test_1_login(self):
    #     login = loginPage(self.driver)
    #     login.enterUserName("standard_user")
    #     login.enterPassword("secret_sauce")
    #     login.clickLoginButton()
    #
    # def test_2_sorting(self):
    #     home = homePage(self.driver)
    #     home.selectFilterOption("Price (high to low)")
    def test_1_login(self):
        login = loginPage(self.driver)
        login.enterUserName(readExcel("Datasheet1.xlsx","Test1","Username"))
        login.enterPassword("Datasheet1.xlsx","Test1","Password")
        login.clickLoginButton()

    def test_2_sorting(self):
        home = homePage(self.driver)
        home.selectFilterOption("Datasheet1.xlsx","Test1","Filteroption")

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main
