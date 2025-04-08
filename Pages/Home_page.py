

from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.product_titles = (By.XPATH, '//h4[@class="card-title"]//a')
        self.add_to_cart_buttons = (By.XPATH, '//button[@class="btn btn-info"]')

    def add_selected_products_to_cart(self):
        target_products = ["Nokia Edge", "Blackberry"]
        product_elements = self.driver.find_elements(*self.product_titles)

        for index, product in enumerate(product_elements, start=1):
            if product.text in target_products:
                self.driver.find_element(
                    By.XPATH, f'(//button[@class="btn btn-info0"])[{index}]').click()
