import pytest

from PageObjects.LoginPageAndVerifyDispOperatorPage import LoginPage_VerifyDispOperatorPage
from PageObjects.ManageCustomerPage import ManageCustomerAccountPage
from TestData.testData_ManageCustomerAccount import TestData_CustomerAccount
from Utilities.BaseClass import BaseClass


class Test_005_AddCustomerAccount(BaseClass):

    def test_verifyCustAccountPage(self, getData):
        self.log = self.getLogger()
        self.log.info("***************** Test_005_AddCustomerAccount ******************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['UserName'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("********************** Login Successful ***********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        self.log.info("************ Test verify customer account started ************")
        mcap = ManageCustomerAccountPage(self.driver)
        mcap.clickOnManageCust()
        status = mcap.verifyCustAccPage()
        assert status == True
        self.log.info("******* Successfully accessed manage cust account page *******")

        self.log.info("******* test verify customer account page is passed ***********")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    def test_addNewCustomerAccount(self, getData):
        self.log = self.getLogger()
        self.log.info("*********** Test Add new customer account started **************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['UserName'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("********************** Login Successful ***********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        mcap = ManageCustomerAccountPage(self.driver)
        mcap.clickOnManageCust()
        self.log.info("******* Successfully accessed manage cust account page *******")

        self.log.info("************** Entering customer account details ***********")
        mcap.setKeyCustName().send_keys(getData['KeyAccountName'])
        mcap.clickOnSubAccount()
        mcap.setSubCustomerName().send_keys(getData['CustomerName'])
        mcap.setSoldToNumber().send_keys(getData['SoldToNumber'])
        mcap.setShipToNumber().send_keys(getData['ShipToNumber'])
        mcap.clickOnAddButton()
        status = mcap.verifyConfirmMsg()
        assert status == True

        self.log.info("*********** Test Add new customer account passed **************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    def test_searchCustomer(self, getData, getData1):
        self.log = self.getLogger()
        self.log.info("*********** Test search customer account started **************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['UserName'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("********************** Login Successful ***********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        mcap = ManageCustomerAccountPage(self.driver)
        mcap.clickOnManageCust()
        self.log.info("******* Successfully accessed manage cust account page *******")
        mcap.enterCustomerName().send_keys(getData1['KeyAccountName'])
        mcap.clickOnSearchButton()
        status = mcap.verifySearchedCustomer(getData1['KeyAccountName'])
        assert status == True

        self.log.info("*********** Test search customer account passed **************")

    @pytest.fixture(params=TestData_CustomerAccount.test_data_addCust)
    def getData(self, request):
        return request.param

    @pytest.fixture(params=TestData_CustomerAccount.test_data_add_Exst)
    def getData1(self, request):
        return request.param
