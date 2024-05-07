"""
PIMPage.py
"""
from time import sleep

from selenium.webdriver import ActionChains

from Proj1_Data import data
from Proj1_Locators import locators


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Action Chains
from selenium.webdriver import ActionChains


# Keys
from selenium.webdriver.common.keys import Keys


class PIMPage:


   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.driver.implicitly_wait(10)
       self.wait = WebDriverWait(self.driver, 10)
       self.action = ActionChains(self.driver)

   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()


   def quit(self):
       self.driver.quit()

#TC_Login_01
   def login(self):
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
           sleep(5)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimMenu))).click()
           sleep(5)

           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimAddButton))).click()
           sleep(5)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimFirstName))).send_keys(data.WebData().firstName)

           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimMiddleName))).send_keys(
               data.WebData().middleName)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimLastName))).send_keys(
               data.WebData().lastName)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimEmpID))).clear()
           sleep(4)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimEmpID))).send_keys(data.WebData().empID)
           sleep(6)
           # Find the file input element on the webpage
          # file_input = self.wait.until(ec.presence_of_element_located((By.XPATH,locators.WebLocators().pimphotoUpload))).click()

           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimAddSave))).click()
           sleep(5)

           sleep(5)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimFirstName))).send_keys(data.WebData().firstName)
           sleep(6)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimSearchButton))).click()
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimOtherID))).send_keys(data.WebData().otherID)
           sleep(6)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimDriverLicenseNO))).send_keys(
               data.WebData().licenseNo)
           sleep(6)
           # Find the date input element by its ID, name, XPath, or CSS selector
           date_input = self.driver.find_element(By.XPATH,"(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")

           # Clear any existing value in the date input field (optional)
           date_input.click()

           # Send the desired date string to the date input field
           date_input.send_keys('05/20/2024')  # Change to your desired date format

           # Send Enter key to confirm the date selection (optional)
           date_input.send_keys(Keys.RETURN)
           sleep(5)
           if self.driver.current_url == data.WebData().dashboardURL:
               print("Successfully LoggedIn")
           else:
               print("Error in login")
       except NoSuchElementException as e:
           print(e)
       finally:
           self.quit()
   """
   def pimAdd(self):
       try:
           #sleep(5)
           self.wait.until(ec.presence_of_element_located((By.XPATH, locators.WebLocators().pimMenu))).click()
           sleep(5)
       except NoSuchElementException as e:
           print(e)
       finally:
           self.quit()
           """
pim =PIMPage()
pim.login()
#pim.pimAdd()