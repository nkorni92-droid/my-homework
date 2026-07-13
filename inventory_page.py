"""
Класс страницы инвентаря (каталог товаров) SauceDemo
"""
from typing import List, Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Страница каталога товаров SauceDemo.
    Содержит методы для работы с товарами и корзиной.
    """

    # Локаторы
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCTS_LIST = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы каталога.

        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)

    @allure.step("Проверить, что открыта страница каталога")
    def is_inventory_page(self) -> bool:
        """
        Проверить, что открыта страница каталога товаров.

        Returns:
            True если страница каталога открыта, иначе False
        """
        return self.is_element_visible(self.PRODUCTS_TITLE)

    @allure.step("Получить заголовок страницы")
    def get_page_title(self) -> str:
        """
        Получить заголовок страницы каталога.

        Returns:
            Текст заголовка страницы
        """
        return self.get_text(self.PRODUCTS_TITLE)

    @allure.step("Получить список всех товаров")
    def get_products(self) -> List[WebElement]:
        """
        Получить список всех товаров на странице.

        Returns:
            Список элементов товаров
        """
        return self.find_elements(self.PRODUCTS_LIST)

    @allure.step("Получить количество товаров на странице")
    def get_products_count(self) -> int:
        """
        Получить количество товаров на странице.

        Returns:
            Количество товаров
        """
        products = self.get_products()
        return len(products)

    @allure.step("Добавить товар в корзину по индексу: {product_index}")
    def add_product_to_cart_by_index(self, product_index: int) -> None:
        """
        Добавить товар в корзину по индексу.

        Args:
            product_index: Индекс товара (начиная с 0)
        """
        buttons = self.find_elements(self.ADD_TO_CART_BUTTON)
        if 0 <= product_index < len(buttons):
            buttons[product_index].click()
        else:
            raise IndexError(f"Товар с индексом {product_index} не найден")

    @allure.step("Получить количество товаров в корзине")
    def get_cart_count(self) -> Optional[int]:
        """
        Получить количество товаров в корзине.

        Returns:
            Количество товаров в корзине или None если корзина пуста
        """
        try:
            badge = self.find_element(self.SHOPPING_CART_BADGE)
            return int(badge.text)
        except Exception:
            return None

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Перейти на страницу корзины."""
        self.click(self.SHOPPING_CART)