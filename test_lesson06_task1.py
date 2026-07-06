from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_dynamic_loading():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # 1. Откройте страницу
        driver.get ("https://the-internet.herokuapp.com/dynamic_loading/2")
        
        # 2. Найдите и нажмите на кнопку Start
        # Правильный селектор: кнопка с текстом "Start"
        start_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Start']")
        ))
        start_button.click()
        
        # 3. Дождитесь появления текста "Hello World!"
        hello_text = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h4[text()='Hello World!']")
        ))
        
        # 4. Сделайте скриншот страницы
        driver.save_screenshot("screenshots/dynamic_loading.png")
        
        # 5. Проверьте, что появившийся текст равен "Hello World!"
        assert hello_text.text == "Hello World!", \
            f"Ожидался текст 'Hello World!', получен '{hello_text.text}'"
        
        print("Тест успешно пройден!")
        
    finally:
        # Закрываем браузер
        driver.quit()