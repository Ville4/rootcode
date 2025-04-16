from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure

class CooperationPage(BasePage):

    PAGE_URL = Links.COOPERATION_PAGE

    NAME_FIELD = ("xpath","//input[@placeholder='Введите имя']")
    PHONE_NUMBER_FIELD = ("xpath", "//input[@placeholder='Введите телефон']")
    EMAIL_FIELD = ("xpath", "//input[@placeholder='Введите почту']")
    NAME_COMPANY_FIELD = ("xpath", "//input[@placeholder='Введите название компании']")
    ABOUT_PROJECT_TEXTAREA = ("xpath", "//textarea[@placeholder='Расскажите о проекте']")
    AGREEMENT_CHECKBOX = ("xpath", "//input[@type='checkbox']")
    CHECKBOX_CLICKABLE_SPAN = ("xpath", "//span[@class='checkbox__icon']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")


    def enter_name(self,name):
        with allure.step(f"Name '{name}' is entered"):
            self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD)).send_keys(name)


    def enter_phone_number(self,phone_number):
        with allure.step(f"Phone number '{phone_number}' is entered"):
            self.wait.until(EC.element_to_be_clickable(self.PHONE_NUMBER_FIELD)).send_keys(phone_number)

    def enter_email(self, email):
        with allure.step(f"Email '{email}' is entered"):
            self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)

    def enter_name_compony(self, name_compony):
        with allure.step(f"Compony name '{name_compony}' is entered"):
            self.wait.until(EC.element_to_be_clickable(self.NAME_COMPANY_FIELD)).send_keys(name_compony)

    def enter_info_about_project(self, info_about_project):
        with allure.step(f"Info about project '{info_about_project}' is entered"):
            self.wait.until(EC.element_to_be_clickable(self.ABOUT_PROJECT_TEXTAREA)).send_keys(info_about_project)

    @allure.step("Check checkbox")
    def checkbox_is_selected(self):

        checkbox_span = self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_CLICKABLE_SPAN))
        checkbox = self.wait.until(EC.presence_of_element_located(self.AGREEMENT_CHECKBOX))

        if not checkbox.is_selected():
            checkbox_span.click()

        assert checkbox.is_selected(), "Checkbox не выбран"

    @allure.step("Check submit button")
    def make_sure_submit_button_is_active(self):
        button = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        assert button.is_enabled(), "Submit button is not active"
