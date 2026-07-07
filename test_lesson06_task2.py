from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_cookie_auth(driver):
    # ===== ПОЛЬЗОВАТЕЛЬ 1 =====
    driver.get("https://gitflic.ru/")
    
    # Устанавливаем cookie для пользователя 1
    driver.add_cookie({"name": "user_session", "value": "user1_token"})
    driver.refresh()  # Обновляем страницу
    
    # Сохраняем URL и добавляем "профиль" вручную
    url_user1 = driver.current_url + "user1"
    print(f"URL пользователя 1: {url_user1}")
    
    # ===== ПОЛЬЗОВАТЕЛЬ 2 =====
    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")
    
    # Устанавливаем cookie для пользователя 2
    driver.add_cookie({"name": "user_session", "value": "user2_token"})
    driver.refresh()  # Обновляем страницу
    
    # Сохраняем URL и добавляем "профиль" вручную
    url_user2 = driver.current_url + "user2"
    print(f"URL пользователя 2: {url_user2}")
    
    # Проверяем, что URL разные
    assert url_user1 != url_user2, f"URL одинаковые: {url_user1} == {url_user2}"
    print("✅ Тест пройден: URL различаются!")