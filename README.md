# PageObject Tests with Allure Reporting

## Описание проекта

Проект содержит автоматизированные тесты для сайта SauceDemo с использованием паттерна PageObject и отчетностью Allure.

## Структура проекта
lesson_10/
├── pages/ # Page Object классы
│ ├── base_page.py # Базовый класс страницы
│ ├── login_page.py # Страница логина
│ └── inventory_page.py # Страница каталога товаров
├── tests/ # Тестовые файлы
│ ├── conftest.py # Фикстуры и конфигурация
│ └── test_inventory.py # Тесты каталога товаров
├── requirements.txt # Зависимости проекта
├── pytest.ini # Конфигурация pytest
└── README.md # Документация проекта