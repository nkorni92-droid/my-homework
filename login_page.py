"""
Класс страницы логина SauceDemo
"""
from typing import Union
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Страница логина SauceDemo.
    Содержит методы для авторизации пользователя.
    """

    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.

        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> None:
        """
        Ввести имя пользователя в поле.

        Args:
            username: Имя пользователя
        """
        self.input_text(self.USERNAME_INPUT, username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        """
        Ввести пароль в поле.

        Args:
            password: Пароль пользователя
        """
        self.input_text(self.PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку Login")
    def click_login_button(self) -> None:
        """Нажать кнопку Login для входа в систему."""
        self.click(self.LOGIN_BUTTON)

    @allure.step("Выполнить логин с username='{username}'")
    def login(self, username: str, password: str) -> None:
        """
        Выполнить полный процесс логина.

        Args:
            username: Имя пользователя
            password: Пароль пользователя
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Получить текст ошибки")
    def get_error_message(self) -> str:
        """
        Получить текст сообщения об ошибке.

        Returns:
            Текст сообщения об ошибке
        """
        return self.get_text(self.ERROR_MESSAGE)

    @allure.step("Проверить наличие ошибки логина")
    def is_error_displayed(self) -> bool:
        """
        Проверить, отображается ли сообщение об ошибке.

        Returns:
            True если ошибка отображается, иначе False
        """
        return self.is_element_visible(self.ERROR_MESSAGE)