from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_dynamic_loading(driver):
    wait = WebDriverWait(driver, 10)
    
    # 1. Откройте страницу
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    # 2. Найдите и нажмите на кнопку Start
    start_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Start']")
    ))
    start_button.click()
    
    # 3. Дождитесь появления текста "Hello World!"
    hello_text = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//h4[text()='Hello World!']")
    ))
    
    # 4. Сделайте скриншот страницы
    os.makedirs("screenshots", exist_ok=True)  # Создаём папку, если её нет
    driver.save_screenshot("screenshots/dynamic_loading.png")
    
    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert hello_text.text == "Hello World!", \
        f"Ожидался текст 'Hello World!', получен '{hello_text.text}'"
    