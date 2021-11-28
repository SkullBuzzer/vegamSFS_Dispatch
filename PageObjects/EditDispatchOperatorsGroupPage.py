import time

from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.common.by import By


class EditDispatchOperatorsGroup:
    iconSearch = (By.XPATH, "//div[@class='define_search_criteria mr-2']")
    lnkReset = (By.XPATH, "//a[@class='text-centerfull-width bold reset-btn']")
    maxRows = (By.XPATH, "//table[@class='table table-bordered table-striped']/tbody/tr")
    txtoperatorName = (By.XPATH, "//input[@id='txtOperatorName']")
    maxRows1 = (By.XPATH, "//div[@id='tableOperatorsList']/table/tbody/tr")
    txtgroupName = (By.XPATH, "//input[@id='txt_6055']")
    msg = (By.XPATH, "//span[text()='No records found']")

    def __init__(self, driver):
        self.driver = driver

    def clickOnSearchicon(self):
        self.driver.find_element(*self.iconSearch).click()

    def clickOnResetLink(self):
        self.driver.find_element(*self.lnkReset).click()
        time.sleep(3)

    def getMaxRows(self):
        return len(self.driver.find_elements(*self.maxRows))

    def validateAndClickOnEdit(self, Name):
        flag = False
        for x in range(1, self.getMaxRows() + 1):
            groupName = self.driver.find_element_by_xpath("//table[@class='table table-bordered "
                                                          "table-striped']/tbody/tr[" + str(x) + "]/td[2]").text

            if groupName == Name:
                self.driver.find_element_by_xpath("//table[@class='table table-bordered "
                                                  "table-striped']/tbody/tr[" + str(x) + "]/td/span/div/i[1]").click()
                flag = True
        return flag

    def setOperatorName(self):
        return self.driver.find_element(*self.txtoperatorName)

    time.sleep(3)

    def getMaxRows1(self):
        return len(self.driver.find_elements(*self.maxRows1))

    def validateOperatorNameAndSelect(self):
        flag = False
        for x in range(1, self.getMaxRows1() + 1):
            actName = self.driver.find_element_by_xpath(
                "//div[@id='tableOperatorsList']/table/tbody/tr[" + str(x) + "]/td[2]").text
            if actName == "ANN JESS":
                self.driver.find_element_by_xpath(
                    "//div[@id='tableOperatorsList']/table/tbody/tr[" + str(x) + "]/td[1]/i").click()
                flag = True
        return flag

    def validateGroupNameAndDelete(self, Name):
        flag = False
        for x in range(1, self.getMaxRows() + 1):
            actName = self.driver.find_element_by_xpath(
                "//div[@id='divTable_428']/table/tbody/tr[" + str(x) + "]/td[2]").text
            if actName == Name:
                self.driver.find_element_by_xpath(
                    "//div[@id='divTable_428']/table/tbody/tr[" + str(x) + "]/td[1]/span/div/i[2]").click()
                '''try:
                    alert = self.driver.switch_to.alert
                    alert.accept()
                except NoAlertPresentException:
                    print("No alert Present")'''
                time.sleep(3)
                self.driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[1]").click()
                flag = True
        return flag

    def setGroupName(self):
        return self.driver.find_element(*self.txtgroupName)

    def verifyRecord(self):
        return self.driver.find_element(*self.msg).text