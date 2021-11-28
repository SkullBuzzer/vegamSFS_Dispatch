import pytest

from PageObjects.EditDeleteCustomerAccount import EditDeleteCustomerAccountPage
from PageObjects.LoginPageAndVerifyDispOperatorPage import LoginPage_VerifyDispOperatorPage
from PageObjects.ManageCustomerPage import ManageCustomerAccountPage
from TestData.testData_ManageCustomerAccount import TestData_CustomerAccount
from Utilities.BaseClass import BaseClass


class Test_006_EditDeleteCustomerAccount(BaseClass):
    def test_addExistingCustomerAccount(self, getData):
        self.log = self.getLogger()
        self.log.info("***************** Test_006_EditDeleteCustomerAccount ******************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['UserName'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("********************** Login Successful ***********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        self.log.info("************ Test Add Existing customer account started ************")
        mcap = ManageCustomerAccountPage(self.driver)
        mcap.clickOnManageCust()
        self.log.info("******* Successfully accessed manage cust account page *******")
        self.log.info("************** Entering existing customer account details ***********")
        mcap.setKeyCustName().send_keys(getData['KeyAccountName'])
        mcap.clickOnSubAccount()
        mcap.setSubCustomerName().send_keys(getData['CustomerName'])
        mcap.setSoldToNumber().send_keys(getData['SoldToNumber'])
        mcap.setShipToNumber().send_keys(getData['ShipToNumber'])
        mcap.clickOnAddButton()
        edca = EditDeleteCustomerAccountPage(self.driver)
        status = edca.validateCustomer()
        assert status == True

        self.log.info("************ Test Add Existing customer account passed ************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    def test_editCustomerAccount(self, getData1):
        self.log = self.getLogger()
        self.log.info("****************** Test edit customer account started ****************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData1['UserName'])
        lp.setPassword().send_keys(getData1['Password'])
        lp.clickOnLogin()
        self.log.info("********************** Login Successful ***********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        mcap = ManageCustomerAccountPage(self.driver)
        mcap.clickOnManageCust()
        self.log.info("******* Successfully accessed manage cust account page *******")

        self.log.info("************** Modifying existing customer account details ***********")
        edca = EditDeleteCustomerAccountPage(self.driver)
        status = edca.validateAndSelectRecord(getData1['KeyAccountName'])
        assert status == True
        edca.clickOnAddMore()
        edca.updateCustInfo(getData1['CustomerName'], getData1['SoldToNumber'], getData1['ShipToNumber'])
        status = edca.clickOnUpdate()
        assert status == True
        self.log.info("****************** Test edit customer account passed ****************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    def test_deleteCustomerAccount(self, getData1):
        self.log = self.getLogger()
        self.log.info("****************** Test delete customer account started ****************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData1['UserName'])
        lp.setPassword().send_keys(getData1['Password'])
        lp.clickOnLogin()
        self.log.info("********************** Login Successful ***********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        mcap = ManageCustomerAccountPage(self.driver)
        mcap.clickOnManageCust()
        self.log.info("******* Successfully accessed manage cust account page *******")
        edca = EditDeleteCustomerAccountPage(self.driver)
        edca.deleteCustomerAcc(getData1['KeyAccountName1'])
        mcap.enterCustomerName().send_keys(getData1['KeyAccountName1'])
        mcap.clickOnSearchButton()
        status = edca.verifyDelCustomer()
        assert status == True
        self.log.info("****************** Test Delete customer account passed ****************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.fixture(params=TestData_CustomerAccount.test_data_add_Exst)
    def getData(self, request):
        return request.param

    @pytest.fixture(params=TestData_CustomerAccount.test_data_edit)
    def getData1(self, request):
        return request.param
