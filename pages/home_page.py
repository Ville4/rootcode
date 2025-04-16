from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure


class HomePage(BasePage):

    PAGE_URL = Links.HOST

    COOPERATION_LINK = ("xpath", "//a[@class='uppercase p1 opacity-60']")

    @allure.step("Click on cooperation link")
    def click_cooperation_link(self):
        self.wait.until(EC.element_to_be_clickable(self.COOPERATION_LINK)).click()