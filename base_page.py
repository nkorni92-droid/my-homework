"""
Базовый класс страницы с общими методами для всех страниц
"""
from typing import Optional, List, Union
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    """
    Базовый класс для всех страниц приложения.
    Содержит общие методы для работы с элементами.
    """

    def __init__(self, driver: WebDriver, base_url: str = "https://www.saucedemo.com") -> None:
        """
        Инициализация базовой страницы.

        Args:
            driver: Экземпляр WebDriver
            base_url: Базовый URL сайта
        """
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout=10)

    @allure.step("Открыть страницу: {url}")
    def open(self, url: str = "") -> None:
        """
        Открыть указанную страницу.

        Args:
            url: Относительный или абсолютный URL страницы
        """
        full_url = self.base_url + url
        self.driver.get(full_url)

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator: tuple) -> WebElement:
        """
        Найти элемент на странице.

        Args:
            locator: Кортеж (тип локатора, значение локатора)

        Returns:
            Найденный веб-элемент
        """
        return self.driver.find_element(*locator)

    @allure.step("Найти все элементы: {locator}")
    def find_elements(self, locator: tuple) -> List[WebElement]:
        """
        Найти все элементы по локатору.

        Args:
            locator: Кортеж (тип локатора, значение локатора)

        Returns:
            Список найденных веб-элементов
        """
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator: tuple) -> None:
        """
        Кликнуть по элементу.

        Args:
            locator: Кортеж (тип локатора, значение локатора)
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def input_text(self, locator: tuple, text: str) -> None:
        """
        Ввести текст в поле ввода.

        Args:
            locator: Кортеж (тип локатора, значение локатора)
            text: Текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator: tuple) -> str:
        """
        Получить текст элемента.

        Args:
            locator: Кортеж (тип локатора, значение локатора)

        Returns:
            Текст элемента
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Проверить видимость элемента: {locator}")
    def is_element_visible(self, locator: tuple) -> bool:
        """
        Проверить, видим ли элемент на странице.

        Args:
            locator: Кортеж (тип локатора, значение локатора)

        Returns:
            True если элемент видим, иначе False
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        """
        Получить текущий URL страницы.

        Returns:
            Текущий URL
        """
        return self.driver.current_url