import pytest

from PageObjects.DefineSearchCriteria import SearchCriteria
from PageObjects.LoginPageAndVerifyDispOperatorPage import LoginPage_VerifyDispOperatorPage
from TestData.testData_addNewGroup import TestDataAddNewGroup
from Utilities.BaseClass import BaseClass


class Test_003_DefineSearchCriteria(BaseClass):
    def test_searchByGroupName(self, getData):
        self.log = self.getLogger()
        self.log.info("*************** Test_003_DefineSearchCriteria ******************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['Username'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("*********************** Login Successful *********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        lp.clickOnManageOperator()
        self.log.info("****************** Successfully accessed Manage operator module ********************")
        sc = SearchCriteria(self.driver)
        self.log.info("****************** test search by group name started ********************")
        sc.searchByGroupName().send_keys(getData['Groupname'])
        sc.clickOnSearchButton()
        status = sc.verifySearchedRecord(getData['Groupname'])
        assert status == True
        self.log.info("****************** test search by group name passed ********************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    def test_searchByOperationType(self, getData):
        self.log = self.getLogger()
        self.log.info("*************** Test_003_DefineSearchCriteria ******************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['Username'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("*********************** Login Successful *********************")

        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        lp.clickOnManageOperator()
        self.log.info("****************** Successfully accessed Manage operator module ********************")

        sc = SearchCriteria(self.driver)
        self.log.info("****************** test search by operation type started ********************")

        sc.searchByGroupName().send_keys(getData['Groupname'])
        self.selectDropdown(sc.dropdownSelect(), getData['OperationType'])
        sc.clickOnSearchButton()
        status = sc.verifySearchByOperationType(getData['OperationType'])
        assert status == True
        self.log.info("********************* test search by operation type is passed ********************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    def test_searchByOperatorName(self, getData):
        self.log = self.getLogger()
        self.log.info("*************** Test_003_DefineSearchCriteria ******************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['Username'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("*********************** Login Successful *********************")

        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        lp.clickOnManageOperator()
        self.log.info("****************** Successfully accessed Manage operator module ********************")

        sc = SearchCriteria(self.driver)
        self.log.info("****************** test search by operator Name started ********************")

        sc.searchByGroupName().send_keys(getData['Groupname'])
        self.selectDropdown(sc.dropdownSelect(), getData['OperationType'])
        sc.setOperatorName().send_keys(getData['OperatorName'])
        sc.clickOnSearchButton()
        self.log.info("****************** test search by operator Name passed ********************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.fixture(params=TestDataAddNewGroup.testData_search)
    def getData(self, request):
        return request.param
