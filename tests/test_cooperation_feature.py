from base.base_test import BaseTest
from pages.cooperation_page import CooperationPage
import allure
import pytest
from pages.home_page import HomePage


@allure.feature("Cooperation page functionality")
class TestCooperationPageFeature(BaseTest):

    @allure.title("Filling out the cooperation form with valid data")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_form_ready_to_submit(self):

        self.home_page.open()
        self.cooperation_page.scroll_to_element(HomePage.COOPERATION_LINK)
        self.home_page.click_cooperation_link()
        self.cooperation_page.is_openned()
        self.cooperation_page.scroll_to_element(CooperationPage.NAME_FIELD)
        self.cooperation_page.enter_name(self.data.NAME)
        self.cooperation_page.enter_phone_number(self.data.PHONE_NUMBER)
        self.cooperation_page.enter_email(self.data.EMAIL)
        self.cooperation_page.enter_name_compony(self.data.COMPANY_NAME)
        self.cooperation_page.enter_info_about_project(self.data.INFO_ABOUT_COMPANY)
        self.cooperation_page.checkbox_is_selected()
        self.cooperation_page.make_sure_submit_button_is_active()
        self.cooperation_page.make_screenshot()