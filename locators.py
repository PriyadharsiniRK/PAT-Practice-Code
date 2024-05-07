"""
locator.py
"""




class WebLocators:


   def __init__(self):
       self.usernameLocator = "//input[@name='username']"
       self.passwordLocator = "//input[@name='password']"
       self.buttonLocator = "//button[@type='submit']"
       self.forgotButton ="//p[contains(.,'Forgot your password')]"
       self.invalidCredentials_errormsg="//div/p[contains(@class, 'oxd-text oxd-text--p oxd-alert-content-text')]"
       self.pimMenu ="(//a/span[contains(@class,'oxd-text oxd-text--span oxd-main-menu-item--name')])[2]"
       self.pimAddButton="(//button[contains(@class,'oxd-button oxd-button--medium oxd-button--secondary')])[2]"
       self.pimFirstName="//input[@name='firstName']"
       self.pimMiddleName="//input[@name='middleName']"
       self.pimLastName="//input[@name='lastName']"
       self.pimEmpID="(//input[@class='oxd-input oxd-input--active'])[2]"
       self.pimAddSave="//button[@type='submit']"
       self.pimphotoUpload="(//button[@role='none'])[2]"
       self.pimEditButton="(//button/i[@class='oxd-icon bi-pencil-fill'])[1]"
       self.pimOtherID="(//input[@class='oxd-input oxd-input--active'])[3]"
       self.pimDriverLicenseNO="(//input[@class='oxd-input oxd-input--active'])[4]"
       self.pimLicenseExpiryDate="(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]"
       self.pimNationality ="(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]"
       self.pimMaritalStatus="(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"
       self.pimDeleteButton="//button/i[@class='oxd-icon bi-trash']"
       self.pimDOB = "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[2]"
       self.pimGenderF ="(//input[@type='radio'])[2]"
       self.pimGenderM ="(//input[@type='radio'])[1]"
       self.pimContactDetails="(//a[@class='orangehrm-tabs-item'])[2]"
       self.pimStreet1="(//input[@class='oxd-input oxd-input--active'])[2]"
       self.pimStreet2 = "(//input[@class='oxd-input oxd-input--active'])[3]"
       self.pimCity = "(//input[@class='oxd-input oxd-input--active'])[4]"
       self.pimState = "(//input[@class='oxd-input oxd-input--active'])[5]"
       self.pimPostalCode = "(//input[@class='oxd-input oxd-input--active'])[6]"
       self.pimHome = "(//input[@class='oxd-input oxd-input--active'])[7]"
       self.pimMobile = "(//input[@class='oxd-input oxd-input--active'])[8]"
       self.pimWork = "(//input[@class='oxd-input oxd-input--active'])[9]"
       self.pimWorkEmail = "(//input[@class='oxd-input oxd-input--active'])[10]"
       self.pimOtherEmail = "(//input[@class='oxd-input oxd-input--active'])[11]"
       self.pimEmergencyContact ="(//a[@class='orangehrm-tabs-item'])[3]"
       #self.pimAddButton="(//button[@type='button'])[3]"
       self.pimEmergencyName="(//input[@class='oxd-input oxd-input--active'])[2]"
       self.pimEmergencyRelationship= "(//input[@class='oxd-input oxd-input--active'])[3]"
       self.pimEmergencyMobile= "(//input[@class='oxd-input oxd-input--active'])[5]"
       self.pimDependent = "//a[@class='orangehrm-tabs-item --active']"
       self.pimDependentName = "(//input[@class='oxd-input oxd-input--active'])[2]"
       self.pimDependentRelationship ="(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])"
       self.pimDependentDOB = "//i[@class='oxd-icon bi-calendar oxd-date-input-icon']"
       self.pimSearchButton = "//button[@type='submit']"




