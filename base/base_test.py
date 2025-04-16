from pages.home_page import HomePage
from pages.cooperation_page import CooperationPage
from config.data import Data

import pytest

class BaseTest:

    data = Data

    home_page = HomePage
    cooperation_page = CooperationPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.data = Data()
        request.cls.driver = driver
        request.cls.home_page = HomePage(driver)
        request.cls.cooperation_page = CooperationPage(driver)