import allure

from Web.Locators.LoginLocators import LoginLocators
from allure_commons.types import AttachmentType

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_txtbox_name = LoginLocators.email_txtbox_name
        self.pass_txtbox_name = LoginLocators.pass_txtbox_name
        self.login_btn_name = LoginLocators.login_btn_name
        self.login_page_xpath = LoginLocators.login_page_xpath

    @allure.step
    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email_txtbox_name).clear()
        self.driver.find_element_by_xpath(self.email_txtbox_name).send_keys(email)

    @allure.step
    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.pass_txtbox_name).clear()
        self.driver.find_element_by_xpath(self.pass_txtbox_name).send_keys(password)

    @allure.step
    def click_login(self):
        self.driver.find_element_by_xpath(self.login_btn_name).click()

    @allure.step
    def validation(self, locator, massege):
        valid = self.driver.find_element_by_xpath(locator).get_attribute("validationMessage")

        try:
            assert valid == massege
        except Exception as e:
            raise allure.attach(self.driver.get_screenshot_as_png(), self.driver.save_screenshot("screenshot"),
                                attachment_type=AttachmentType.PNG)