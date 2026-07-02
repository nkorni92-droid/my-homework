import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNavigation:
    BASE_URL = "https://httpbin.org/"
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()
    
    def test_navigation_and_url_check(self):
        self.driver.get(self.BASE_URL)
        html_form_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "HTML form"))
        )
        html_form_link.click()

        expected_url = f"{self.BASE_URL}forms/post"
        self.wait.until(EC.url_to_be(expected_url))
        assert self.driver.current_url == expected_url, \
           f"{expected_url}, {self.driver.current_url}"
        print(f" {self.driver.current_url}")
        self.driver.back()
        self.wait.until(EC.url_to_be(self.BASE_URL))
        assert self.driver.current_url == self.BASE_URL, \
            f" {self.BASE_URL},  {self.driver.current_url}"
        print(f" {self.driver.current_url}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])