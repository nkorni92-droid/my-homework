"""
Конфигурация тестов и фикстуры
"""
import pytest
from typing import Generator
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, None, None]:
    """
    Фикстура для создания и закрытия драйвера.

    Yields:
        Экземпляр WebDriver
    """
    options = Options()
    options.add_argument("--headless")  # Для CI/CD
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver: WebDriver) -> LoginPage:
    """
    Фикстура для страницы логина.

    Args:
        driver: Экземпляр WebDriver

    Returns:
        Объект страницы логина
    """
    return LoginPage(driver)


@pytest.fixture(scope="function")
def inventory_page(driver: WebDriver, login_page: LoginPage) -> InventoryPage:
    """
    Фикстура для страницы каталога с авторизованным пользователем.

    Args:
        driver: Экземпляр WebDriver
        login_page: Объект страницы логина

    Returns:
        Объект страницы каталога
    """
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(driver)