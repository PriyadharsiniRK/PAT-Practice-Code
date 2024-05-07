"""
loginPage.py
"""
from time import sleep

from Proj1_Data import data
from Proj1_Locators import locators


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




class LoginPage:


   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.driver.implicitly_wait(10)
       self.wait = WebDriverWait(self.driver, 10)


   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()


   def quit(self):
       self.driver.quit()

#TC_Login_01
   def loginPos(self):
       try:
           self.boot()



           sleep(5)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().usernameLocator))).send_keys(
               data.WebData().username)
           sleep(5)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().passwordLocator))).send_keys(
               data.WebData().password)
           sleep(5)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().buttonLocator))).click()


           if self.driver.current_url == data.WebData().dashboardURL:
               print("Successfully LoggedIn")
           else:
               print("Error in login")


       except NoSuchElementException as e:
           print(e)
       finally:
           self.quit()

   # TC_Login_02
   def loginNeg(self):
       try:
           self.boot()

           sleep(5)
           self.wait.until(
               ec.presence_of_element_located((By.XPATH, locators.WebLocators().usernameLocator))).send_keys(
               data.WebData().username)
           sleep(5)
           self.wait.until(
               ec.presence_of_element_located((By.XPATH, locators.WebLocators().passwordLocator))).send_keys(
               data.WebData().invalid_password)
           sleep(5)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().buttonLocator))).click()
           sleep(5)
           self.wait.until(ec.presence_of_element_located((By.XPATH,locators.WebLocators().invalidCredentials_errormsg))).is_displayed()
           if locators.WebLocators().invalidCredentials_errormsg:
               print("Invalid credentials message dispalyed ")
           else:
               print("Error")


       except NoSuchElementException as e:
           print(e)
       finally:
           self.quit()


obj = LoginPage()
#obj.loginPos() ## calling TC_Login_01 method
obj.loginNeg() ## calling TC_Login_02 method