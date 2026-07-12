from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа"""
    
    # Локаторы для формы
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "#cancel")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    # Локаторы для страницы подтверждения
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    FINISH_BUTTON = (By.CSS_SELECTOR, "#finish")
    
    # Локаторы для итоговой информации
    SUBTOTAL_LABEL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    TAX_LABEL = (By.CSS_SELECTOR, ".summary_tax_label")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")
    PAYMENT_INFO = (By.CSS_SELECTOR, ".summary_info > div:nth-child(1)")
    SHIPPING_INFO = (By.CSS_SELECTOR, ".summary_info > div:nth-child(2)")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def is_checkout_step_one_loaded(self) -> bool:
        """Проверить, что первый шаг оформления загружен"""
        title = self.driver.find_element(*self.PAGE_TITLE)
        return title.text == "Checkout: Your Information"
    
    def is_checkout_step_two_loaded(self) -> bool:
        """Проверить, что второй шаг оформления загружен"""
        title = self.driver.find_element(*self.PAGE_TITLE)
        return title.text == "Checkout: Overview"
    
    def enter_first_name(self, first_name: str):
        """Ввести имя"""
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
    
    def enter_last_name(self, last_name: str):
        """Ввести фамилию"""
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
    
    def enter_postal_code(self, postal_code: str):
        """Ввести почтовый индекс"""
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)
    
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        """Заполнить всю форму оформления"""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
    
    def click_continue(self):
        """Нажать кнопку Continue"""
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
    
    def click_finish(self):
        """Нажать кнопку Finish"""
        self.driver.find_element(*self.FINISH_BUTTON).click()
    
    def get_subtotal(self) -> str:
        """Получить промежуточную сумму"""
        return self.driver.find_element(*self.SUBTOTAL_LABEL).text
    
    def get_tax(self) -> str:
        """Получить налог"""
        return self.driver.find_element(*self.TAX_LABEL).text
    
    def get_total(self) -> str:
        """Получить итоговую сумму"""
        total_text = self.driver.find_element(*self.TOTAL_LABEL).text
        return total_text
    
    def get_total_amount(self) -> float:
        """Получить итоговую сумму как число"""
        total_text = self.get_total()
        # Извлекаем число из строки вида "Total: $58.29"
        amount_str = total_text.split("$")[1]
        return float(amount_str)