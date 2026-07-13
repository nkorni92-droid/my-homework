"""
Тесты для страницы каталога товаров SauceDemo
"""
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Каталог товаров")
@allure.severity(allure.severity_level.CRITICAL)
class TestInventory:
    """Тесты для проверки функциональности каталога товаров"""

    @allure.title("Успешная авторизация и переход в каталог")
    @allure.description("Тест проверяет, что после успешной авторизации открывается страница каталога товаров")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_successful_login(self, login_page: LoginPage) -> None:
        """
        Проверка успешной авторизации.

        Args:
            login_page: Страница логина
        """
        with allure.step("Открыть страницу логина"):
            login_page.open()

        with allure.step("Ввести корректные учетные данные"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")

        with allure.step("Нажать кнопку Login"):
            login_page.click_login_button()

        with allure.step("Проверить, что открыта страница каталога"):
            inventory_page = InventoryPage(login_page.driver)
            with allure.step("Заголовок страницы должен быть 'Products'"):
                assert inventory_page.get_page_title() == "Products", \
                    f"Ожидался заголовок 'Products', получен '{inventory_page.get_page_title()}'"

    @allure.title("Отображение товаров в каталоге")
    @allure.description("Тест проверяет, что на странице каталога отображаются товары")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_products_displayed(self, inventory_page: InventoryPage) -> None:
        """
        Проверка отображения товаров в каталоге.

        Args:
            inventory_page: Страница каталога
        """
        with allure.step("Получить список товаров на странице"):
            products_count = inventory_page.get_products_count()

        with allure.step("Проверить, что количество товаров больше 0"):
            assert products_count > 0, "Товары не отображаются на странице каталога"

        with allure.step(f"На странице отображается {products_count} товаров"):
            pass

    @allure.title("Добавление товара в корзину")
    @allure.description("Тест проверяет добавление товара в корзину и обновление счетчика")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_product_to_cart(self, inventory_page: InventoryPage) -> None:
        """
        Проверка добавления товара в корзину.

        Args:
            inventory_page: Страница каталога
        """
        with allure.step("Проверить, что корзина пуста"):
            cart_count = inventory_page.get_cart_count()
            assert cart_count is None, "Корзина должна быть пустой"

        with allure.step("Добавить первый товар в корзину"):
            inventory_page.add_product_to_cart_by_index(0)

        with allure.step("Проверить счетчик корзины"):
            cart_count = inventory_page.get_cart_count()
            assert cart_count == 1, f"Ожидался 1 товар в корзине, получено {cart_count}"

    @allure.title("Добавление нескольких товаров в корзину")
    @allure.description("Тест проверяет добавление нескольких товаров и корректность счетчика")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_multiple_products_to_cart(self, inventory_page: InventoryPage) -> None:
        """
        Проверка добавления нескольких товаров в корзину.

        Args:
            inventory_page: Страница каталога
        """
        with allure.step("Добавить три товара в корзину"):
            for i in range(3):
                with allure.step(f"Добавить товар {i + 1}"):
                    inventory_page.add_product_to_cart_by_index(i)

        with allure.step("Проверить счетчик корзины"):
            cart_count = inventory_page.get_cart_count()
            with allure.step(f"В корзине должно быть 3 товара, получено {cart_count}"):
                assert cart_count == 3, f"Ожидалось 3 товара в корзине, получено {cart_count}"

    @allure.title("Проверка URL страницы каталога")
    @allure.description("Тест проверяет корректность URL после авторизации")
    @allure.severity(allure.severity_level.MINOR)
    def test_inventory_page_url(self, inventory_page: InventoryPage) -> None:
        """
        Проверка URL страницы каталога.

        Args:
            inventory_page: Страница каталога
        """
        with allure.step("Получить текущий URL"):
            current_url = inventory_page.get_current_url()

        with allure.step("Проверить, что URL содержит 'inventory'"):
            assert "inventory" in current_url, \
                f"URL должен содержать 'inventory', текущий URL: {current_url}"