import inspect

import pytest
import logging

from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        fileHandler = logging.FileHandler("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Dispatch\\Logs\\Automation.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s: %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger

    def selectDropdown(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)