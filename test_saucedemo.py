from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestSauceDemo:
    """Тесты для интернет-магазина SauceDemo"""
    
    # Тестовые данные
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    
    FIRST_NAME = "Иван"
    LAST_NAME = "Петров"
    POSTAL_CODE = "123456"
    
    EXPECTED_TOTAL = "$58.29"
    EXPECTED_ITEMS = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    
    def test_complete_purchase(self, driver):
        """
        Полный тест покупки товаров в интернет-магазине
        """
        # Инициализация страниц
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        
        # 1. Открыть сайт магазина
        login_page.open()
        
        # 2. Авторизоваться как standard_user
        login_page.login(self.USERNAME, self.PASSWORD)
        assert inventory_page.is_loaded(), "Страница товаров не загрузилась"
        
        # 3. Добавить товары в корзину
        inventory_page.add_all_items_to_cart()
        
        # Проверить, что в корзине 3 товара
        cart_count = inventory_page.get_cart_count()
        assert cart_count == "3", f"Ожидалось 3 товара в корзине, но получено {cart_count}"
        
        # 4. Перейти в корзину
        inventory_page.go_to_cart()
        assert cart_page.is_loaded(), "Страница корзины не загрузилась"
        
        # Проверить содержимое корзины
        cart_items_count = cart_page.get_cart_items_count()
        assert cart_items_count == 3, f"Ожидалось 3 товара, но в корзине {cart_items_count}"
        
        # Проверить, что все нужные товары в корзине
        for item in self.EXPECTED_ITEMS:
            assert cart_page.is_item_in_cart(item), f"Товар '{item}' не найден в корзине"
        
        # 5. Нажать Checkout
        cart_page.click_checkout()
        assert checkout_page.is_checkout_step_one_loaded(), "Форма оформления не загрузилась"
        
        # 6. Заполнить форму данными
        checkout_page.fill_checkout_form(
            self.FIRST_NAME,
            self.LAST_NAME,
            self.POSTAL_CODE
        )
        checkout_page.click_continue()
        
        # Проверить, что перешли на страницу подтверждения
        assert checkout_page.is_checkout_step_two_loaded(), "Страница подтверждения не загрузилась"
        
        # 7. Прочитать итоговую стоимость
        total_text = checkout_page.get_total()
        print(f"Итоговая стоимость: {total_text}")
        
        # 8. Проверить, что итоговая сумма равна $58.29
        assert total_text == f"Total: {self.EXPECTED_TOTAL}", \
            f"Ожидалась сумма {self.EXPECTED_TOTAL}, но получено {total_text}"
        
        print("Тест пройден успешно!")
        print(f"Все товары добавлены в корзину: {', '.join(self.EXPECTED_ITEMS)}")
        print(f"Итоговая сумма: {total_text}")