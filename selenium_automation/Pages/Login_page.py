import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class login():

    def __init__(self,driver):
        self.driver=driver
        self.username=(By.XPATH,'//input[@id="username"]')
        self.password = (By.XPATH, '//input[@id="password"]')
        self.sign_in = (By.XPATH, '//input[@id="signInBtn"]')
        self.checkbox=(By.XPATH, '//input[@type="checkbox"]')
        self.dropdown=(By.XPATH,'//select[@class="form-control"]')

    def enter_credentials(self):
        self.driver.find_element(*self.username).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password).send_keys("learning")
        dropdown = Select(self.driver.find_element(*self.dropdown))
        dropdown.select_by_visible_text("Student")
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.sign_in).click()
        time.sleep(5)













