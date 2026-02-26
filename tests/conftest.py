import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    chrome_options = Options()

    # 🔒 Isola o navegador
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-infobars")

    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("driver")

        if report.failed and driver is not None:
            os.makedirs("screenshots", exist_ok=True)

            file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
            file_path = os.path.join("screenshots", file_name)

            driver.save_screenshot(file_path)

            # 🔥 Anexa screenshot no relatório HTML
            if hasattr(report, "extra"):
                from pytest_html import extras
                report.extra.append(extras.image(file_path))
            else:
                report.extra = []
                from pytest_html import extras
                report.extra.append(extras.image(file_path))
