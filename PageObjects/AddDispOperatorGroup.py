import time
from selenium.webdriver.common.by import By


class AddDispOperatorPage:
    btnNewGroup = (By.XPATH, "//button[@id='ContentPlaceHolder1_btnAddGroup']")
    txtGroupName = (By.XPATH, "//input[@data-bind='value: GroupName']")
    dropdown = (By.XPATH, "//select[@class='form-control w-100 custom-select h-30']")
    txtOperatorName = (By.XPATH, "//input[@id='txtOperatorName']")
    lstOperator = (By.XPATH, "//tbody[@id='tbdOperatorsList']/tr/td[2]")
    checkBoxoperator = (By.XPATH, "//tbody[@id='tbdOperatorsList']/tr/td[1]/i")
    btnClose = (By.XPATH, "//span[@class='float-right mr-1 cursor-pointer']")
    allCheckboxes = (By.XPATH, "//table[@class='table table-bordered table-striped']/tbody/tr/td[1]/i")
    allOperators = (By.XPATH, "//table[@class='table table-bordered table-striped']/tbody/tr/td/i")

    def __init__(self, driver):
        self.driver = driver

    def clickOnNewGroup(self):
        self.driver.find_element(*self.btnNewGroup).click()
        time.sleep(5)

    def setGroupName(self):
        return self.driver.find_element(*self.txtGroupName)

    def clickOnDropdown(self):
        return self.driver.find_element(*self.dropdown)

    def setOperatorName(self):
        self.driver.find_element(*self.txtOperatorName).clear()
        return self.driver.find_element(*self.txtOperatorName)

    def verifyOperatorName(self, Name):
        actname = self.driver.find_element(*self.lstOperator).text
        if actname == Name:
            flag = True
        else:
            flag = False
        return flag

    def clickOnCheckBox(self):
        self.driver.find_element(*self.checkBoxoperator).click()
        time.sleep(5)

    def clickOnSave(self):
        button = self.driver.find_element_by_xpath("//button[@id='btnSaveInfo']")
        self.driver.execute_script("arguments[0].click();", button)

    def clickOnClose(self):
        self.driver.find_element(*self.btnClose).click()

    def clickOnAllCheckboxes(self):
        checkboxes = self.driver.find_elements(*self.allCheckboxes)
        for checkbox in checkboxes:
            checkbox.click()

    def clickOnDisplayedCheckbox(self):
        operators = self.driver.find_elements(*self.allOperators)
        for operator in operators:
            operator.click()
