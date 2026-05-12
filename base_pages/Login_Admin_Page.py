# from  selenium import  webdriver
from selenium.webdriver.common.by import By


class Login_Admin_Page:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    login_button = "//button[@type='submit']"
    link_logout =  "Logout"


    def __init__(self, driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout).click()