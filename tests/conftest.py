import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime

# Global variable to store pytest_html plugin reference
pytest_html = None

@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture
def login_cred():
    return ["rahulshettyacademy", "learning"]

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        extras.append(pytest_html.extras.url("https://rahulshettyacademy.com/loginpagePractise/"))

        if report.failed:
            driver = getattr(item.instance, "driver", None)
            if driver:
                screenshots_dir = "screenshots"
                os.makedirs(screenshots_dir, exist_ok=True)
                file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                file_path = os.path.join(screenshots_dir, file_name)
                driver.save_screenshot(file_path)
                extras.append(pytest_html.extras.image(file_path))  # correct method for image

    report.extras = extras

