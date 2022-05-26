import allure
from Web.Pages.RegisterPage import RegisterPage
from Web.Base.base import Base
import pytest
from Web.Locators.RegisterLocators import RegisterLocators
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures('set_up')
class TestRegister(Base):

    @pytest.mark.sanity
    def test_register_success(self):
        driver = self.driver
        reg = RegisterPage(driver)
        reg.enter_user('dani')
        reg.enter_lastname('jambi')
        reg.enter_profile_pic('file:///Users/dnylgmbr/Desktop/one/268217.webp')
        reg.enter_cover_pic('file:///Users/dnylgmbr/Desktop/one/268217.webp')
        reg.enter_email('dj@walla.com')
        reg.enter_contry('israel')
        reg.enter_city('hadera')
        reg.enter_password('123456')
        reg.enter_conf_password('123456')
        self.driver.implicitly_wait(10)
        reg.click_signup_btn()
        valid = self.driver.find_element_by_xpath(RegisterLocators.logout_btn).get_attribute('innerText')
        self.driver.refresh()
        if valid == "LOGOUT":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),self.driver.save_screenshot("screenshot"), attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.driver.quit()
            assert False
            #allure.attach( self.driver.get_screenshot_as_png(),name= 'screenshot', attachment_type=AttachmentType.PNG)

    # @pytest.mark.skip
    def test_register_user_null(self):
        driver = self.driver
        reg = RegisterPage(driver)
        reg.enter_user('')
        reg.enter_lastname('jambi')
        reg.enter_profile_pic('file:///Users/dnylgmbr/Desktop/one/268239.webp')
        reg.enter_cover_pic('file:///Users/dnylgmbr/Desktop/one/268217.webp')
        reg.enter_email('dj@gmail.com')
        reg.enter_contry('israel')
        reg.enter_city('hadera')
        reg.enter_password('123456')
        reg.enter_conf_password('123456')
        reg.click_signup_btn()
        self.driver.implicitly_wait(10)
        reg.validation(RegisterLocators.user_name_txtbox,"Please fill out this fiel.")

    @pytest.mark.skip
    def test_register_lastname_null(self):
        driver = self.driver
        reg = RegisterPage(driver)
        reg.enter_user('dani')
        reg.enter_lastname('')
        reg.enter_profile_pic('file:///Users/dnylgmbr/Desktop/one/268239.webp')
        reg.enter_cover_pic('file:///Users/dnylgmbr/Desktop/one/268217.webp')
        reg.enter_email('dj@gmail.com')
        reg.enter_contry('israel')
        reg.enter_city('hadera')
        reg.enter_password('123456')
        reg.enter_conf_password('123456')
        reg.click_signup_btn()
        self.driver.implicitly_wait(10)
        reg.validation(RegisterLocators.user_lastname_txtbox,"Please fill out this field.")


    @pytest.mark.skip
    def test_register_profilePic_null(self):
        driver = self.driver
        reg = RegisterPage(driver)
        reg.enter_user('dani')
        reg.enter_lastname('jambi')
        reg.enter_profile_pic('')
        reg.enter_cover_pic('file:///Users/dnylgmbr/Desktop/one/268217.webp')
        reg.enter_email('dj@gmail.com')
        reg.enter_contry('israel')
        reg.enter_city('hadera')
        reg.enter_password('123456')
        reg.enter_conf_password('123456')
        reg.click_signup_btn()
        self.driver.implicitly_wait(10)
        reg.validation(RegisterLocators.profil_pic_txtbox,"Please fill out this field.")
