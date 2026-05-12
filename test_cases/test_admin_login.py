

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_pages.Login_Admin_Page import Login_Admin_page
from utilities.read_properties import Read_Config
from utilities.custom_logs import log_maker

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

class TestAdminLogin:

    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = log_maker.log_gen()



    # def __init__(self,driver):
    #     self.driver = driver

    def test_title_verification(self,setup):
        self.logger.info("********Test_admin_login**********")
        self.logger.info("********title verification of admin logs**********")
        self.driver = setup
        self.driver.get(self.admin_page_url)

        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"

        if act_title == exp_title:
            self.logger.info("********title verification of admin are matched **********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("********test_title verification not matched**********")
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.admin_lp = Login_Admin_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()

        wait = WebDriverWait(self.driver, 50)
        dashboard_text = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Dashboard']"))
        ).text

        if dashboard_text == "Dashboard":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin.png")
            self.driver.close()
            assert False

    def test_invalid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.admin_lp = Login_Admin_page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()

        error_message = self.driver.find_element(
            By.XPATH, "//div[@class='message-error validation-summary-errors']"
        ).text

        if "No customer account found" in error_message:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin.png")
            assert False