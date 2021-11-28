import time

import pytest

from PageObjects.AddDispOperatorGroup import AddDispOperatorPage
from PageObjects.DefineSearchCriteria import SearchCriteria
from PageObjects.EditDispatchOperatorsGroupPage import EditDispatchOperatorsGroup
from PageObjects.LoginPageAndVerifyDispOperatorPage import LoginPage_VerifyDispOperatorPage
from TestData.testData_editOperatorGroup import TestData_editGroup
from Utilities.BaseClass import BaseClass


class Test_004_editDispatchOperatorsGroup(BaseClass):
    def test_editDispOperatorGroup(self, getData):
        self.log = self.getLogger()
        self.log.info("*************** Test_004_editDispatchOperatorsGroup ******************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['Username'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("*********************** Login Successful *********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        lp.clickOnManageOperator()
        self.log.info("****************** Successfully accessed Manage operator module ********************")

        self.log.info("****************** test editDispOperatorGroup started ********************")
        edog = EditDispatchOperatorsGroup(self.driver)
        edog.clickOnSearchicon()
        edog.clickOnResetLink()
        status = edog.validateAndClickOnEdit(getData['Groupname'])
        assert status == True
        edog.setOperatorName().send_keys(getData['OperatorName'])
        status = edog.validateOperatorNameAndSelect()
        assert status == True
        addgrp = AddDispOperatorPage(self.driver)
        addgrp.clickOnSave()
        addgrp.clickOnClose()
        self.log.info("****************** test editDispOperatorGroup passed ********************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    def test_deleteOperatorGroup(self, getData):
        self.log = self.getLogger()
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['Username'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("*********************** Login Successful *********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        lp.clickOnManageOperator()
        self.log.info("****************** Successfully accessed Manage operator module ********************")

        self.log.info("****************** test deleteDispOperatorGroup started ********************")
        edog = EditDispatchOperatorsGroup(self.driver)
        edog.clickOnSearchicon()
        edog.clickOnResetLink()
        status = edog.validateGroupNameAndDelete(getData['Groupname1'])
        assert status == True
        self.driver.refresh()
        time.sleep(3)
        edog.clickOnSearchicon()
        edog.setGroupName().send_keys(getData['Groupname1'])
        sc = SearchCriteria(self.driver)
        sc.clickOnSearchButton()
        act_msg = edog.verifyRecord()
        if act_msg == "No records found":
            assert True
            self.log.info("****************** test deleteDispOperatorGroup passed ********************")
        else:
            self.log.info("****************** test deleteDispOperatorGroup failed ********************")
            assert False
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.fixture(params=TestData_editGroup.test_data)
    def getData(self, request):
        return request.param
