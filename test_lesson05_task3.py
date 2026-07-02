import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLinksPage:
    LINKS_URL = "https://httpbin.org/links/10"
    
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()
    
    def test_links_count_and_visibility(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(self.LINKS_URL)
        print(f"✓ Открыта страница: {self.LINKS_URL}")
        all_links = wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
        )
        print(f"✓ Найдено ссылок на странице: {len(all_links)}")
        expected_count = 9
        actual_count = len(all_links)
        assert actual_count == expected_count, \
            f"Ожидалось {expected_count} ссылок, но найдено {actual_count}"
        print(f"✓ Количество ссылок соответствует ожидаемому: {expected_count}")
        hidden_links = []
        for i, link in enumerate(all_links, 1):
            if not link.is_displayed():
                hidden_links.append(f"Ссылка {i}: '{link.text}'")
        
        assert len(hidden_links) == 0, \
            f"Найдены неотображаемые ссылки: {', '.join(hidden_links)}"
        print("✓ Все ссылки отображаются на странице")
        first_link = all_links[0]
        first_link_text = first_link.text
        assert "1" in first_link_text, \
            f"Текст первой ссылки должен содержать '1', но получен: '{first_link_text}'"
        print(f"✓ Текст первой ссылки содержит '1': '{first_link_text}'")
        print("\nВсе найденные ссылки:")
        for i, link in enumerate(all_links, 1):
            print(f"  {i}. Текст: '{link.text}' | Отображается: {link.is_displayed()}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
