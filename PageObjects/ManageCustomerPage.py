import time

from selenium.webdriver.common.by import By


class ManageCustomerAccountPage:

    lnkManageCust = (By.XPATH, "//a[@id='ContentPlaceHolder1_lnkManageCusAccount']/div")
    txtManageCust = (By.XPATH, "//span[text()='Manage Customer Account']")
    txtKeyCustName = (By.XPATH, "//input[@id='txtMasterCustomerName']")
    lnksubAccount = (By.XPATH, "//fieldset[@id='divShippinLink']/a/i")
    txtsubCustname = (By.XPATH, "//input[@id='txtSubCustomerName']")
    txtsoldToNumber = (By.XPATH, "//input[@id='txtSoldToNumber']")
    txtShipToNumber = (By.XPATH, "//input[@id='txtShipToNumber']")
    btnAdd = (By.XPATH, "//a[@id='btnAddCustomer']")
    msgConfirm = (By.XPATH, "//span[@id='lblErrorMsg']")
    txtCustName = (By.XPATH, "//input[@id='txtSearchCustomerName']")
    btnSearch = (By.XPATH, "//button[@id='ContentPlaceHolder1_btnSearch']/i")

    def __init__(self, driver):
        self.driver = driver

    def clickOnManageCust(self):
        self.driver.find_element(*self.lnkManageCust).click()
        time.sleep(4)

    def verifyCustAccPage(self):
        flag = False
        act_text = self.driver.find_element(*self.txtManageCust).text
        if act_text == "Manage Customer Account":
            flag = True
        return flag

    def setKeyCustName(self):
        return self.driver.find_element(*self.txtKeyCustName)

    def clickOnSubAccount(self):
        self.driver.find_element(*self.lnksubAccount).click()

    def setSubCustomerName(self):
        return self.driver.find_element(*self.txtsubCustname)

    def setSoldToNumber(self):
        return self.driver.find_element(*self.txtsoldToNumber)

    def setShipToNumber(self):
        return self.driver.find_element(*self.txtShipToNumber)

    def clickOnAddButton(self):
        self.driver.find_element(*self.btnAdd).click()
        time.sleep(3)

    def verifyConfirmMsg(self):
        act_msg = self.driver.find_element(*self.msgConfirm).text
        flag = False
        if act_msg == "Customer account added successfully":
            flag = True
        return flag

    def enterCustomerName(self):
        return self.driver.find_element(*self.txtCustName)

    def clickOnSearchButton(self):
        self.driver.find_element(*self.btnSearch).click()
        time.sleep(3)

    def verifySearchedCustomer(self, Name):
        act_name = self.driver.find_element_by_xpath("//table[@id='tableCustomer']/tbody/tr/td[3]/div").text
        flag = False
        if act_name == Name:
            flag = True
        return flag
