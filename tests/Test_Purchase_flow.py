# test_purchase_flow.py

import pytest

from selenium_automation.Pages.Checkout_page import CheckoutPage
from selenium_automation.Pages.Home_page import HomePage
from selenium_automation.Pages.Login_page import login
from selenium_automation.Pages.Purchase_page import PurchasePage


@pytest.mark.usefixtures("browser")  # Assumes 'browser' is a fixture that provides self.driver
class TestPurchaseFlow:

    def test_full_purchase_flow(self):
        # Step 1: Login
        login_page = login(self.driver)
        login_page.enter_credentials()

        # Step 2: Add products to cart
        home_page = HomePage(self.driver)
        home_page.add_selected_products_to_cart()

        # Step 3: Verify cart and proceed to checkout
        checkout_page = CheckoutPage(self.driver)
        checkout_page.verify_and_proceed_to_checkout()

        # Step 4: Complete purchase
        purchase_page = PurchasePage(self.driver)
        purchase_page.complete_purchase()
