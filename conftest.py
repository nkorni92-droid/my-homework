import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия драйвера Firefox"""
    firefox_options = Options()
    firefox_options.add_argument("--start-maximized")
    
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.implicitly_wait(10)
    
    yield driver
    driver.quit()