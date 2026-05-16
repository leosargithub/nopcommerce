import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logs import log_maker
from utilities import excel_utils
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

class TestAdminDataDrivenLogin:

    admin_page_url = Read_Config.get_admin_page_url()
    # username = Read_Config.get_username()
    # password = Read_Config.get_password()
    # invalid_username = Read_Config.get_invalid_username()
    logger = log_maker.log_gen()

    path = ".//test_data//admin_data_login.xlsx"

    status_list = []


    # def __init__(self,driver):
    #     self.driver = driver



    def test_valid_admin_login_data_driven(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)

        self.admin_lp = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.path, "Sheet2")
        print("num of rows", self.rows)




        for r in range(2,self.rows+1):
             self.username = excel_utils.read_data(self.path, "Sheet2", r,1)
             self.password = excel_utils.read_data(self.path,"Sheet2", r,2)
             self.exp_login = excel_utils.read_data(self.path, "Sheet2", r, 3)
             self.admin_lp.enter_username(self.username)
             self.admin_lp.enter_password(self.password)
             self.admin_lp.click_login()
             time.sleep(5)
             act_title = self.driver.title
             exp_title = "nopCommerce demo store. Login"

             if act_title == exp_title:
                 if self.exp_login == "Yes":
                     self.logger.info("test data is passed")
                     self.status_list.append("Pass")
                     self.admin_lp.click_logout()
                 elif self.exp_login == "No":
                      self.logger.info("test data is failed")
                      self.status_list.append("Fail")

             elif act_title != exp_title:
                 if self.exp_login == "Yes":
                     self.logger.info("test data is failed")
                     self.status_list.append("Fail")
                 elif self.exp_login == "No":
                     self.logger.info("test data is passed")
                     self.status_list.append("Pass")

        print("Status list is", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test admin data driven test is failed")
            assert False
        else:
            self.logger.info("Test admin data driven test is passed")
            assert True









