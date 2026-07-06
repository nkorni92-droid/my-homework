from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Откройте страницу
        driver.get("https://gitflic.ru/")
        time.sleep(3)  # Даем время для полной загрузки
        
        # ===== АВТОРИЗАЦИЯ ПОЛЬЗОВАТЕЛЯ 1 =====
        # Находим кнопку входа
        login_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, 'login') or contains(text(), 'Войти')]")
        ))
        login_btn.click()
        time.sleep(2)
        
        # Вводим логин и пароль для пользователя 1
        # ВАЖНО: замените на реальные данные
        username_field = wait.until(EC.presence_of_element_located(
            (By.ID, "username")  # или By.NAME
        ))
        username_field.send_keys("your_username_1")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("your_password_1")
        
        # Нажимаем кнопку входа
        submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_btn.click()
        time.sleep(3)
        
        # Ждем перехода на главную
        wait.until(EC.url_contains("gitflic.ru"))
        
        # Переходим в профиль пользователя 1
        driver.get("https://gitflic.ru/profile")  # или /user/username
        time.sleep(2)
        url_user1 = driver.current_url
        print(f"URL пользователя 1: {url_user1}")
        
        # Получаем cookie для дальнейшего использования
        cookies_user1 = driver.get_cookies()
        print("Cookie пользователя 1:", cookies_user1)
        
        # ===== ВЫХОД ИЗ АККАУНТА =====
        # Очищаем все cookie
        driver.delete_all_cookies()
        driver.refresh()
        time.sleep(2)
        
        # ===== АВТОРИЗАЦИЯ ПОЛЬЗОВАТЕЛЯ 2 =====
        # Открываем страницу логина
        driver.get("https://gitflic.ru/login")
        time.sleep(2)
        
        # Вводим данные пользователя 2
        username_field = wait.until(EC.presence_of_element_located(
            (By.ID, "username")
        ))
        username_field.send_keys("your_username_2")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("your_password_2")
        
        submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_btn.click()
        time.sleep(3)
        
        wait.until(EC.url_contains("gitflic.ru"))
        
        # Переходим в профиль пользователя 2
        driver.get("https://gitflic.ru/profile")
        time.sleep(2)
        url_user2 = driver.current_url
        print(f"URL пользователя 2: {url_user2}")
        
        # ===== ПРОВЕРКА =====
        assert url_user1 != url_user2, f"URL одинаковые: {url_user1} == {url_user2}"
        print("✅ Тест пройден: URL для пользователей различаются!")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_session_storage_auth()