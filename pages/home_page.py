from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure


class HomePage(BasePage):

    PAGE_URL = Links.HOST

    COOPERATION_LINK = ("xpath", "//div[@class = 'the-nav-menu flex flex-col justify-between desktop:flex-row desktop:items-center']//a[text()='Сотрудничество']")

    @allure.step("Click on cooperation link")
    def click_cooperation_link(self):
        self.wait.until(EC.visibility_of_element_located(self.COOPERATION_LINK)).click()