import string
import time
import random
import pytest

from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Add_Customer_Page import Add_Customer_Page

from utilities.read_properties import Read_Config
from utilities.custom_logs import log_maker


class Test_03_Add_New_Customer:

    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    logs = log_maker.log_gen()

    def test_add_new_customer(self, setup):

        self.logs.info("************ Test_03_Add_New_Customer started ************")

        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()

        # Login Page
        self.admin_lp = Login_Admin_Page(self.driver)

        self.admin_lp.click_login()

        self.logs.info("************ Login completed ************")
        self.logs.info("************ Starting add customer test ************")

        # Add Customer Page
        self.add_customer = Add_Customer_Page(self.driver)

        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.add_customer.click_addnew()

        self.logs.info("************ Providing customer info started ************")

        email = generate_random_email()

        self.add_customer.enter_email(email)
        self.add_customer.enter_password("Test@123")
        self.add_customer.enter_firstname("Jack")
        self.add_customer.enter_lastname("Shaw")
        self.add_customer.select_gender("Male")
        self.add_customer.enter_dob("11/11/1991")
        self.add_customer.enter_companyname("MyCompany")
        self.add_customer.select_tax_exempt()
        self.add_customer.select_newsletter("Test store 2")

        self.logs.info("********** Test store 2 selected **********")

        self.add_customer.select_customer_role("Guests")
        self.add_customer.select_manager_of_vendor("Vendor 1")
        self.add_customer.enter_admin_comments("Test admin comment")

        self.add_customer.click_save()

        time.sleep(3)

        customer_add_success_text = "The new customer has been added successfully"

        success_text = self.driver.find_element(
            By.XPATH,
            "//div[@class='content-wrapper']/div[1]"
        ).text

        if customer_add_success_text in success_text:

            self.logs.info("Test new customer added passed")

            self.driver.close()

            assert True

        else:

            self.logs.info("Test new customer added failed")

            self.driver.save_screenshot(
                ".\\screenshots\\test_add_new_customer.png"
            )

            self.driver.close()

            assert False


def generate_random_email():

    username = ''.join(
        random.choices(
            string.ascii_lowercase + string.digits,
            k=8
        )
    )

    domain = random.choice([
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "example.com"
    ])

    return f"{username}@{domain}"