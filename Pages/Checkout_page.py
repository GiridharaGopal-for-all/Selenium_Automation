# checkout_page.py

from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.cart_checkout_button = (By.XPATH, '//a[@class="nav-link btn btn-primary"]')
        self.individual_prices = (By.XPATH, '//*[@class="table table-hover"]//tr//td[4]//strong')
        self.total_price_text = (By.XPATH, '//*[@class="table table-hover"]//tr//td//h3//strong')
        self.proceed_button = (By.XPATH, '//button[@class="btn btn-success"]')

    def verify_and_proceed_to_checkout(self):
        self.driver.find_element(*self.cart_checkout_button).click()
        item_prices = self.driver.find_elements(*self.individual_prices)
        calculated_total = 0
        for price in item_prices:
            amount = int(price.text.strip().split(" ")[1])
            calculated_total += amount
        print(f"Calculated total from items: {calculated_total}")
        displayed_total_text = self.driver.find_element(*self.total_price_text).text
        displayed_total = int(displayed_total_text.strip().split(" ")[1])
        print(f"Displayed total: {displayed_total}")
        assert calculated_total == displayed_total
        self.driver.find_element(*self.proceed_button).click()
