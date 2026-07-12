
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
    
    def open(self):
        self.driver.get(self.URL)
    
    def set_delay(self, seconds: str):
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(seconds)
    
    def click_button(self, label: str):
        button_xpath = f"//span[text()='{label}']"
        button = self.driver.find_element(By.XPATH, button_xpath)
        button.click()
    
    def perform_calculation(self, *buttons: str):
        for button in buttons:
            self.click_button(button)
    
    def wait_for_result(self, expected_result: str, timeout: int = 50) -> str:
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(self.RESULT_SCREEN, expected_result)
        )
        return self.get_result()
    
    def get_result(self) -> str:
        result_element = self.driver.find_element(*self.RESULT_SCREEN)
        return result_element.text