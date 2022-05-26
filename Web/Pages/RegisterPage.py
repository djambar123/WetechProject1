import allure
from Web.Locators.RegisterLocators import RegisterLocators
from allure_commons.types import AttachmentType


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.user_name = RegisterLocators.user_name_txtbox
        self.user_lastname = RegisterLocators.user_lastname_txtbox
        self.profil_pic = RegisterLocators.profil_pic_txtbox
        self.cover_pic = RegisterLocators.cover_pic_txtbox
        self.email_txt = RegisterLocators.email_txtbox
        self.contry_txt = RegisterLocators.contry_txtbox
        self.city_txt = RegisterLocators.city_txtbox
        self.password_txt = RegisterLocators.password_txtbox
        self.conf_password = RegisterLocators.conf_password_txtbox
        self.register_button = RegisterLocators.register_btn_name_txtbox

    @allure.step
    def enter_user(self, user):
        self.driver.find_element_by_xpath(self.user_name).clear()
        self.driver.find_element_by_xpath(self.user_name).send_keys(user)

    @allure.step
    def enter_lastname(self, lastname):
        self.driver.find_element_by_xpath(self.user_lastname).clear()
        self.driver.find_element_by_xpath(self.user_lastname).send_keys(lastname)

    @allure.step
    def enter_profile_pic(self, profilePic):
        self.driver.find_element_by_xpath(self.profil_pic).clear()
        self.driver.find_element_by_xpath(self.profil_pic).send_keys(profilePic)

    @allure.step
    def enter_cover_pic(self, cover):
        self.driver.find_element_by_xpath(self.cover_pic).clear()
        self.driver.find_element_by_xpath(self.cover_pic).send_keys(cover)

    @allure.step
    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email_txt).clear()
        self.driver.find_element_by_xpath(self.email_txt).send_keys(email)

    @allure.step
    def enter_contry(self, contry):
        self.driver.find_element_by_xpath(self.contry_txt).clear()
        self.driver.find_element_by_xpath(self.contry_txt).send_keys(contry)

    @allure.step
    def enter_city(self, city):
        self.driver.find_element_by_xpath(self.city_txt).clear()
        self.driver.find_element_by_xpath(self.city_txt).send_keys(city)

    @allure.step
    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_txt).clear()
        self.driver.find_element_by_xpath(self.password_txt).send_keys(password)

    @allure.step
    def enter_conf_password(self, confi_password):
        self.driver.find_element_by_xpath(self.conf_password).clear()
        self.driver.find_element_by_xpath(self.conf_password).send_keys(confi_password)

    @allure.step
    def click_signup_btn(self):
        self.driver.find_element_by_xpath(self.register_button).click()

    @allure.step
    def validation(self,locator,massege):
        valid = self.driver.find_element_by_xpath(locator).get_attribute("validationMessage")

        try:
            assert valid == massege
        except Exception as e:
            raise allure.attach(self.driver.get_screenshot_as_png(),self.driver.save_screenshot("screenshot"),attachment_type=AttachmentType.PNG)

