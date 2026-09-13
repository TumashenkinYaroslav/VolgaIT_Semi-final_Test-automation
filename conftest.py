import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="function")
def browser():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser")
        if driver is not None:
            os.makedirs("allure-results", exist_ok=True)
            ts = time.strftime("%Y%m%d-%H%M%S")
            path = f"allure-results/screenshot-{item.name}-{ts}.png"
            try:
                driver.save_screenshot(path)
                import allure
                allure.attach.file(
                    path,
                    name=f"screenshot-{item.name}",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception:
                pass
