from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.locators import locators
from selenium import webdriver

class homePage():

    def __init__(self,driver):
        self.driver =driver
      #  driver =


    def selectFilterOption(self,option):
        dropdown = Select(self.driver.find_element(By.XPATH,locators.sort_select_xpath))
        dropdown.select_by_visible_text(option)

    def click_Logout(self):
        pass