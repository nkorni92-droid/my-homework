from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object для страницы авторизации"""
    
    URL = "https://www.saucedemo.com/"
    
    # Локаторы
    USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        """Открыть страницу авторизации"""
        self.driver.get(self.URL)
    
    def enter_username(self, username: str):
        """Ввести имя пользователя"""
        username_input = self.driver.find_element(*self.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)
    
    def enter_password(self, password: str):
        """Ввести пароль"""
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
    
    def click_login(self):
        """Нажать кнопку Login"""
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
    
    def login(self, username: str, password: str):
        """Выполнить полную авторизацию"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self) -> str:
        """Получить текст ошибки"""
        error = self.driver.find_element(*self.ERROR_MESSAGE)
        return error.text