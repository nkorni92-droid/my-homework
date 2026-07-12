from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object для страницы корзины"""
    
    # Локаторы
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "#continue-shopping")
    
    # Товары в корзине
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def is_loaded(self) -> bool:
        """Проверить, что страница корзины загружена"""
        title = self.driver.find_element(*self.PAGE_TITLE)
        return title.text == "Your Cart"
    
    def get_cart_items_count(self) -> int:
        """Получить количество товаров в корзине"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    
    def get_item_names(self) -> list:
        """Получить названия всех товаров в корзине"""
        items = self.driver.find_elements(*self.ITEM_NAMES)
        return [item.text for item in items]
    
    def is_item_in_cart(self, item_name: str) -> bool:
        """Проверить, есть ли товар в корзине"""
        names = self.get_item_names()
        return item_name in names
    
    def click_checkout(self):
        """Нажать кнопку Checkout"""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()