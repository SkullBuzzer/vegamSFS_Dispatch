import pytest

from PageObjects.AddDispOperatorGroup import AddDispOperatorPage
from PageObjects.LoginPageAndVerifyDispOperatorPage import LoginPage_VerifyDispOperatorPage
from TestData.testData_addNewGroup import TestDataAddNewGroup
from Utilities.BaseClass import BaseClass


class Test_002_AddNewDispGroup(BaseClass):
    def test_addNewGroupRelabel(self, getData):
        self.log = self.getLogger()
        self.log.info("******************* Test_002_AddNewDispGroup *********************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['Username'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("*********************** Login Successful *********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        lp.clickOnManageOperator()
        self.log.info("****************** Successfully accessed Manage operator module ********************")
        addgrp = AddDispOperatorPage(self.driver)
        self.log.info("******************** Adding New Relabel Group *********************")
        addgrp.clickOnNewGroup()
        addgrp.setGroupName().send_keys(getData['Groupname'])
        self.selectDropdown(addgrp.clickOnDropdown(), getData['OperationType'])
        addgrp.setOperatorName().send_keys(getData['OperatorName'])
        status = addgrp.verifyOperatorName(getData['OperatorName'])
        assert status == True
        self.log.info("***************** Operator Name verified successfully ******************")
        addgrp.clickOnCheckBox()
        addgrp.clickOnSave()
        addgrp.clickOnClose()
        self.log.info("**************** add New Group Relabel is passed **********************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    def test_addNewGroupAllOperators(self, getData):
        self.log = self.getLogger()
        self.log.info("******************* Test_002_AddNewDispGroup *********************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['Username'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("*********************** Login Successful *********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        lp.clickOnManageOperator()
        self.log.info("****************** Successfully accessed Manage operator module ********************")
        addgrp = AddDispOperatorPage(self.driver)
        self.log.info("******************** Adding New Relabel Group *********************")
        addgrp.clickOnNewGroup()
        addgrp.setGroupName().send_keys(getData['Groupname'])
        self.selectDropdown(addgrp.clickOnDropdown(), getData['OperationType'])
        addgrp.clickOnAllCheckboxes()
        self.log.info("****************** selected all the checkboxes *********************")
        addgrp.clickOnSave()
        self.log.info(self.log.info("**************** add New Group Relabel is passed **********************"))
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    def test_addNewGroupDO(self, getData):
        self.log = self.getLogger()
        self.log.info("******************* Test_002_AddNewDispGroup *********************")
        lp = LoginPage_VerifyDispOperatorPage(self.driver)
        lp.setUserName().send_keys(getData['Username'])
        lp.setPassword().send_keys(getData['Password'])
        lp.clickOnLogin()
        self.log.info("*********************** Login Successful *********************")
        lp.clickOnAdminTab()
        lp.clickOnConfigDisp()
        lp.clickOnManageOperator()
        self.log.info("****************** Successfully accessed Manage operator module ********************")
        addgrp = AddDispOperatorPage(self.driver)
        self.log.info("******************** Adding New Relabel Group *********************")
        addgrp.clickOnNewGroup()
        addgrp.setGroupName().send_keys(getData['Groupname'])
        self.selectDropdown(addgrp.clickOnDropdown(), getData['OperationType1'])
        addgrp.setOperatorName().send_keys(getData['OperatorName1'])
        addgrp.clickOnDisplayedCheckbox()
        addgrp.clickOnSave()
        self.log.info("**************** add New Group Relabel is passed **********************")
        lp.clickOnSignOut()
        lp.clickOnLoginAgain()

    @pytest.fixture(params=TestDataAddNewGroup.testData_newGroup)
    def getData(self, request):
        return request.param
