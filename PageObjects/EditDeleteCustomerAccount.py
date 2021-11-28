import time

from selenium.webdriver.common.by import By


class EditDeleteCustomerAccountPage:
    msg = (By.XPATH, "//span[@id='lblErrorMsg']")
    maxRows = (By.XPATH, "//table[@id='tableCustomer']/tbody/tr")
    btnUpdate = (By.XPATH, "//a[@id='btnAddCustomer']")
    msgUpdate = (By.XPATH, "//span[@id='lblErrorMsg']")
    iconEdit = (By.XPATH, "//i[@id='ContentPlaceHolder_1317_btnEdit']")
    lnkAddMore = (By.XPATH, "//a[@id='addMoreLink']")
    rows_cust = (By.XPATH, "//div[@class='table-side-box']/div[2]/fieldset[3]/div")

    def __init__(self, driver):
        self.driver = driver

    def validateCustomer(self):
        act_msg = self.driver.find_element(*self.msg).text
        flag = False
        if act_msg == "Customer name is already exists":
            flag = True
        return flag

    def getMaxRows(self):
        return len(self.driver.find_elements_by_xpath("//table[@id='tableCustomer']/tbody//tr"))

    def validateAndSelectRecord(self, Name):
        n = self.getMaxRows()
        flag = False
        for r in range(1, n + 1):
            name = self.driver.find_element_by_xpath(
                "//table[@id='tableCustomer']/tbody//tr[" + str(r) + "]//td[3]").text
            if name == Name:
                self.driver.find_element_by_xpath(
                    "//table[@id='tableCustomer']/tbody//tr[" + str(r) + "]//td[1]/i[1]").click()
                flag = True
                break
        return flag

    def clickOnAddMore(self):
        self.driver.find_element(*self.lnkAddMore).click()
        time.sleep(2)

    def getRowsCust(self):
        return len(self.driver.find_elements_by_xpath("//div[@class='table-side-box']/div[2]/fieldset[3]/div"))

    def updateCustInfo(self, custname, shipTo, soldTo):
        n = self.getRowsCust()
        for r in range(1, n + 1):
            name = self.driver.find_element_by_xpath("//div[@class='table-side-box']/div[2]/fieldset["
                                                     "3]/div[" + str(r) + "]/fieldset/input").text
            if name == "":
                self.driver.find_element_by_xpath("//div[@class='table-side-box']/div[2]/fieldset["
                                                  "3]/div[" + str(r) + "]/fieldset/input").send_keys(custname)
                self.driver.find_element_by_xpath("//input[@id='ContentPlaceHolder_2_txtSoldToNumber']").send_keys(
                    shipTo)
                self.driver.find_element_by_xpath("//input[@id='ContentPlaceHolder_2_txtShipToNumber']").send_keys(
                    soldTo)
                break

    def deleteCustomerAcc(self, Name):
        n = self.getMaxRows()
        for r in range(1, n + 1):
            name = self.driver.find_element_by_xpath(
                "//table[@id='tableCustomer']/tbody//tr[" + str(r) + "]//td[3]").text
            if name == Name:
                self.driver.find_element_by_xpath(
                    "//table[@id='tableCustomer']/tbody//tr[" + str(r) + "]//td[1]/i[2]").click()
                time.sleep(2)
                self.driver.find_element_by_xpath("//button[text()='Confirm']").click()
                break
                time.sleep(2)

    def verifyDelCustomer(self):
        flag = False
        act_msg = self.driver.find_element_by_xpath("//span[text()='No records found']").text
        if act_msg == "No records found":
            flag = True
        return flag

    def clickOnUpdate(self):
        self.driver.find_element(*self.btnUpdate).click()
        time.sleep(2)
        flag = False
        act_msg = self.driver.find_element(*self.msgUpdate).text
        if act_msg == "Customer account updated successfully":
            flag = True
        return flag
