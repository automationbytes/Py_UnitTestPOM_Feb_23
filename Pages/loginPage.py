from selenium.webdriver.common.by import By

from Locators.locators import locators
from selenium import webdriver

class loginPage():

    def __init__(self,driver):
        self.driver =driver
      #  driver =

    def enterUserName(self,userName):
        self.driver.find_element(By.XPATH,locators.username_inputbox_xpath).send_keys(userName)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, locators.password_inputbox_xpath).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.ID, locators.login_button_id).click()
