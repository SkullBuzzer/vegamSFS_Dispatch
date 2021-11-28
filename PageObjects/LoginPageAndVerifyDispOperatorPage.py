import time

from selenium.webdriver.common.by import By


class LoginPage_VerifyDispOperatorPage:
    txtUserName = (By.ID, "ContentPlaceHolder_userNameTextBox")
    txtPassword = (By.ID, "ContentPlaceHolder_passwordTextbox")
    btnLogin = (By.ID, "ContentPlaceHolder_loginButton")
    lnkUserProfile = (By.XPATH, "//a[@id='userPropfile']")
    btnSignOut = (By.XPATH, "//a[@id='signOut']")
    lnkLoginAgain = (By.XPATH, "//a[@id='ContentPlaceHolder_lnkLoginAgain']")
    msgError = (By.XPATH, "//span[@id='ContentPlaceHolder_lblErrorMessage']")
    lnkAdmin = (By.CSS_SELECTOR, "a[id='lnkAdmin']")
    lnkConfigDispArea = (By.XPATH, "//a[@id='ContentPlaceHolder1_lnkDispatch']/div")
    bredDispArea = (By.XPATH, "//span[text()='Configure Dispatch Area']")
    lnkManageOperator = (By.XPATH, "//div[@class='outer-rect-dark-org']")
    bredManageOperator = (By.XPATH, "//span[text()='Manage Dispatch Operators']")

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self):
        self.driver.find_element(*self.txtUserName).clear()
        return self.driver.find_element(*self.txtUserName)

    def setPassword(self):
        self.driver.find_element(*self.txtPassword).clear()
        return self.driver.find_element(*self.txtPassword)

    def clickOnLogin(self):
        self.driver.find_element(*self.btnLogin).click()
        time.sleep(5)

    def msgLoginError(self):
        return self.driver.find_element(*self.msgError)

    def clickOnSignOut(self):
        self.driver.find_element(*self.lnkUserProfile).click()
        time.sleep(3)
        self.driver.find_element(*self.btnSignOut).click()

    def clickOnLoginAgain(self):
        self.driver.find_element(*self.lnkLoginAgain).click()
        time.sleep(2)

    def clickOnAdminTab(self):
        self.driver.find_element(*self.lnkAdmin).click()
        time.sleep(5)

    def clickOnConfigDisp(self):
        self.driver.find_element(*self.lnkConfigDispArea).click()
        time.sleep(2)

    def verifyConfigDispAreaPage(self):
        return self.driver.find_element(*self.bredDispArea)

    def clickOnManageOperator(self):
        self.driver.find_element(*self.lnkManageOperator).click()
        time.sleep(3)

    def verifyManageOperatorPage(self):
        return self.driver.find_element(*self.bredManageOperator)
