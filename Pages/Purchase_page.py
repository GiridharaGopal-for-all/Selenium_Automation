
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PurchasePage():

    def __init__(self, driver):
        self.driver = driver
        self.country_input = (By.ID, "country")
        self.country_suggestions = (By.XPATH, '//div[@class="suggestions"]//ul//a')
        self.terms_checkbox = (By.XPATH, '//*[@for="checkbox2"]')
        self.purchase_button = (By.XPATH, '//*[@value="Purchase"]')
        self.success_message = (By.XPATH, '//*[@class="alert alert-success alert-dismissible"]//strong')

    def complete_purchase(self):
        self.driver.find_element(*self.country_input).send_keys('Ind')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.country_suggestions))
        country_elements = self.driver.find_elements(*self.country_suggestions)
        for index, country in enumerate(country_elements, start=1):
            if country.text == "India":
                country.click()
                break
        self.driver.find_element(*self.terms_checkbox).click()
        self.driver.find_element(*self.purchase_button).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.success_message))
        success_text = self.driver.find_element(*self.success_message).text
        assert success_text == 'Success!'
