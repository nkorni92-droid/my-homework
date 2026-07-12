
from pages.slow_calculator_page import SlowCalculatorPage


class TestSlowCalculator:

    def test_calculator_with_delay(self, driver):
        calculator = SlowCalculatorPage(driver)
        
        calculator.open()
        calculator.set_delay("45")
        calculator.perform_calculation("7", "+", "8", "=")
        
        result = calculator.wait_for_result("15", timeout=55)
        
        assert result == "15", f"Ожидался результат '15', но получено '{result}'"
        print(f"Тест пройден успешно! Результат: {result}")