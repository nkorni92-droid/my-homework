import pytest
from selenium import webdriver


def test_cookie_auth():
    driver = webdriver.Chrome()
    
    # Пользователь 1
    driver.get("https://gitflic.ru/")
    driver.add_cookie({"name": "session", "value": "user1_token"})
    driver.refresh()
    url_user1 = driver.current_url + "/user1"
    
    # Пользователь 2
    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")
    driver.add_cookie({"name": "session", "value": "user2_token"})
    driver.refresh()
    url_user2 = driver.current_url + "/user2"
    
    assert url_user1 != url_user2
    
    driver.quit()