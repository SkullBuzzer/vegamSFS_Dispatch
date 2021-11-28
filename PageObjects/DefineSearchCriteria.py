import time

from selenium.webdriver.common.by import By


class SearchCriteria:
    txtSearchByGName = (By.XPATH, "//input[@id='txt_6055']")
    btnSearch = (By.XPATH, "//button[@class='btn btn-primary']")
    iconSearch = (By.XPATH, "//div[@class='define_search_criteria mr-2']")
    dropdown = (By.XPATH, "//select[@id='drp_6056']")
    txtOperatorName = (By.XPATH, "//input[@id='txt_6058']")

    def __init__(self, driver):
        self.driver = driver

    def searchByGroupName(self):
        self.driver.find_element(*self.iconSearch).click()
        return self.driver.find_element(*self.txtSearchByGName)

    def dropdownSelect(self):
        return self.driver.find_element(*self.dropdown)

    def clickOnSearchButton(self):
        self.driver.find_element(*self.btnSearch).click()
        time.sleep(3)

    def verifySearchedRecord(self, Name):
        flag = False
        actname = self.driver.find_element_by_xpath("//span[text()='Relabel Group 1']").text
        if actname == Name:
            flag = True
        return flag

    def verifySearchByOperationType(self, Name):
        actText = self.driver.find_element_by_xpath("//table[@class='table table-bordered "
                                                    "table-striped']/tbody/tr/td[3]/span").text
        flag = False
        if actText == Name:
            flag = True
        return flag

    def setOperatorName(self):
        return self.driver.find_element(*self.txtOperatorName)
