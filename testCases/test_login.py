import pytest
from selenium.common.exceptions import NoSuchElementException

from PageObjects.LoginPageAndVerifyDispOperatorPage import LoginPage_VerifyDispOperatorPage
from TestData.testData_loginPage import TestDataLoginPage
from Utilities.BaseClass import BaseClass


class Test_001_LoginPage_verifyDispOperatorPage(BaseClass):
    def test_login(self, getData):
        self.log = self.getLogger()
        self.log.info("********************** Test_001_LoginPage_verifyDispOperatorPage **********************")
        self.log.info("***************** Test login started *********************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['Username'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()

        try:
            lp.clickOnSignOut()
        except NoSuchElementException:
            self.log.info("******************* Logout is not required for invalid cred ******************")
        try:
            lp.clickOnLoginAgain()
        except NoSuchElementException:
            self.log.info("******************* Not required to click on Login Again link for invalid cred "
                          "******************")

        actErrorMsg = lp.msgLoginError().text
        actTitle = self.driver.title
        if actTitle == "iPAS-CC":
            assert True
            self.log.info("*************** Login Successful ******************")
        elif actTitle != "iPAS-CC":
            if actErrorMsg == "Sorry, your login failed":
                assert True
                self.log.info("**************** login Failed due to wrong credentials ********************")

    def test_verifyManageOperator(self):
        self.log = self.getLogger()
        self.log.info("********* Test verify manage operator module started **********")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys("cc")
        lp.setPassword().send_keys("1")
        lp.clickOnLogin()
        self.log.info("*************** Login Successful ******************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        actText = lp.verifyConfigDispAreaPage().text

        if actText == "Configure Dispatch Area":
            assert True
        else:
            assert False

        lp.clickOnManageOperator()
        actText = lp.verifyManageOperatorPage().text

        if actText == "Manage Dispatch Operators":
            assert True
            self.log.info("**************** Test verify manage operator is passed *******************")
        else:
            self.log.info("**************** Test verify manage operator is failed *****************")
            assert False

    @pytest.fixture(params=TestDataLoginPage.test_data_lp)
    def getData(self, request):
        return request.param

