import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFormSubmission:
    FORM_URL = "https://httpbin.org/forms/post"
    
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()
    
    def test_form_submission(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(self.FORM_URL)
        custname_field = wait.until(
            EC.presence_of_element_located((By.NAME, "custname"))
        )
        
        custname_field.send_keys("Натали")
        print(f"✓ Введено имя в поле custname")
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit order']"))
        )
        submit_button.click()
        print("✓ Кнопка Submit нажата")
        wait.until(lambda d: d.current_url != self.FORM_URL)
        
        new_url = driver.current_url
        assert new_url != self.FORM_URL, \
            f" {new_url}"
        
        print(f"✓ URL успешно изменился с {self.FORM_URL} на {new_url}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
