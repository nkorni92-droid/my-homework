from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page Object для главной страницы с товарами"""
    
    # Локаторы
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    
    # Кнопки добавления товаров
    ADD_BACKPACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    ADD_BOLT_TSHIRT = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    
    # Кнопки удаления товаров (появляются после добавления)
    REMOVE_BACKPACK = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    REMOVE_BOLT_TSHIRT = (By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt")
    REMOVE_ONESIE = (By.CSS_SELECTOR, "#remove-sauce-labs-onesie")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def is_loaded(self) -> bool:
        """Проверить, что страница загружена"""
        title = self.driver.find_element(*self.PAGE_TITLE)
        return title.text == "Products"
    
    def add_backpack_to_cart(self):
        """Добавить рюкзак в корзину"""
        self.driver.find_element(*self.ADD_BACKPACK).click()
    
    def add_bolt_tshirt_to_cart(self):
        """Добавить футболку Bolt в корзину"""
        self.driver.find_element(*self.ADD_BOLT_TSHIRT).click()
    
    def add_onesie_to_cart(self):
        """Добавить комбинезон в корзину"""
        self.driver.find_element(*self.ADD_ONESIE).click()
    
    def add_all_items_to_cart(self):
        """Добавить все нужные товары в корзину"""
        self.add_backpack_to_cart()
        self.add_bolt_tshirt_to_cart()
        self.add_onesie_to_cart()
    
    def get_cart_count(self) -> str:
        """Получить количество товаров в корзине"""
        badge = self.driver.find_element(*self.SHOPPING_CART_BADGE)
        return badge.text
    
    def go_to_cart(self):
        """Перейти в корзину"""
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()