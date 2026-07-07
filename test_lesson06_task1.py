import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    start_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
    )
    start_button.click()
    
    hello_text = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )
    
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot("screenshots/dynamic_loading.png")
    
    assert hello_text.text == "Hello World!"
    
    driver.quit()
