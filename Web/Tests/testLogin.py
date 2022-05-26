from Web.Pages.LoginPage import LoginPage
from Web.Base.base import Base
import pytest
import allure
from Web.Locators.LoginLocators import LoginLocators
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures('set_up')
class TestLogin(Base):


    @pytest.mark.sanity
    def test_login_success(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.find_element_by_xpath(LoginLocators.login_page_xpath).click()
        login.enter_email("dj@mac.com")
        login.enter_password('123456')
        login.click_login()
        self.driver.implicitly_wait(10)
        try:
            assert driver.title == "WeTech"
        except Exception as e:
            raise allure.attach(self.driver.get_screenshot_as_png(),self.driver.save_screenshot("screenshot"),attachment_type=AttachmentType.PNG)


    # @pytest.mark.skip
    def test_login_invalid_user(self):
        em = 'dj'
        ps = '123456'
        driver = self.driver
        login = LoginPage(driver)
        driver.find_element_by_xpath(LoginLocators.login_page_xpath).click()
        login.enter_email(em)
        login.enter_password(ps)
        login.click_login()
        self.driver.implicitly_wait(10)
        login.validation(LoginLocators.email_txtbox_name,"Please include an '@' in the email address. 'dj' is missing an '@'.")


    @pytest.mark.sanity
    def test_login_invalid_pass(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.find_element_by_xpath(LoginLocators.login_page_xpath).click()
        login.enter_email("dj@mac.com")
        login.enter_password('12')
        login.click_login()
        self.driver.implicitly_wait(10)
        login.validation(LoginLocators.pass_txtbox_name,"Please lengthen this text to 6 characters or more (you are currently using 2 characters).")



    @pytest.mark.skip
    def test_login_invalid_user_null(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.find_element_by_xpath(LoginLocators.login_page_xpath).click()
        login.enter_email("")
        login.enter_password('123456')
        login.click_login()
        self.driver.implicitly_wait(10)
        login.validation(LoginLocators.email_txtbox_name,"Please fill out this field.")


    @pytest.mark.sanity
    def test_login_invalid_pass_null(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.find_element_by_xpath(LoginLocators.login_page_xpath).click()
        login.enter_email("dj@mac.com")
        login.enter_password('')
        login.click_login()
        self.driver.implicitly_wait(10)
        login.validation(LoginLocators.pass_txtbox_name,"Please fill out this field.")

