# Practice-Automation UI Tests

UI-автотесты для страниц practice-automation.com на Python + Selenium + Pytest + Allure.

## Страницы под тестами

| Страница | URL | Тестов |
|---|---|---|
| Calendars | /calendars/ | 13 |
| Modals | /modals/ | 12 |
| Ads | /ads/ | 11 |
| Form Fields | /form-fields/ | 14 |
| Итого | | 50 |

## Стек

- Python 3.12+
- Selenium 4
- Pytest
- Allure
- Page Object Model

## Структура проекта

    practice-automation-tests/
    ├── README.md
    ├── requirements.txt
    ├── pytest.ini
    ├── conftest.py
    ├── pages/
    │   ├── base_page.py
    │   ├── calendars_page.py
    │   ├── modals_page.py
    │   ├── ads_page.py
    │   └── form_page.py
    ├── tests/
    │   ├── test_calendars.py
    │   ├── test_modals.py
    │   ├── test_ads.py
    │   └── test_form.py
    └── utils/
        └── allure_helpers.py

## Установка

    pip install -r requirements.txt

## Запуск

    pytest --alluredir=allure-results
    pytest tests/test_modals.py --alluredir=allure-results
    allure generate allure-results -o allure-report --clean
    allure open allure-report

## Тест-кейсы

### Calendars (13 тестов)

Позитивные (10):
1. test_calendar_input_visible — поле даты отображается
2. test_calendar_input_clickable — поле кликабельно
3. test_format_hint_visible — подсказка формата видна
4. test_format_hint_is_yyyy_mm_dd — формат YYYY-MM-DD
5. test_type_valid_date — ввод валидной даты
6. test_valid_date_no_error — после валидной даты нет ошибки
7. test_clear_input — очистка поля
8. test_accepts_various_dates — принимает разные даты
9. test_field_accepts_keystrokes — после клика поле активно
10. test_retype_replaces_value — повторный ввод заменяет значение

Негативные (3):
1. test_invalid_date_text_no_crash — невалидный текст
2. test_empty_input_no_crash — пустой ввод
3. test_far_future_date_no_crash — 2099 год

### Modals (12 тестов)

Позитивные (10):
- Simple modal: кнопка, открытие, текст, закрытие
- Form modal: открытие, поля name/email, закрытие
- test_modal_content_not_visible_before_open
- test_only_one_modal_can_be_opened

Негативные (2):
- test_form_modal_submit_with_empty_fields
- test_invalid_email_does_not_submit

### Ads (11 тестов)

Позитивные (8):
- test_page_opens
- test_ad_popup_visible_on_load
- test_ad_has_close_button
- test_close_ad_removes_popup
- test_page_content_visible_after_close
- test_main_content_visible
- test_page_title_is_ads
- test_close_ad_then_reload

Негативные (3):
- test_closing_ad_twice_no_error
- test_ad_hidden_after_close
- test_ad_close_button_clickable_multiple_times

### Form Fields (14 тестов)

Позитивные (11):
- Проверка видимости полей: name, password, email, message, submit
- test_fill_name
- test_select_drink_checkbox
- test_select_color_radio
- test_automation_tools_list_has_items
- test_fill_full_form
- test_fill_message_with_automation_tools (спец. задание)

Негативные (3):
- test_submit_with_empty_name
- test_empty_message_field
- test_invalid_email_format

## Специальное задание из ТЗ

Тест test_fill_message_with_automation_tools:
1. Средствами Selenium получить список элементов из раздела Automation Tools
2. Преобразовать в текст
3. Заполнить поле Message полученным списком через запятую

Реализация в pages/form_page.py:

    def get_automation_tools(self):
        label = self.driver.find_element(
            By.XPATH, "//label[normalize-space()='Automation tools']"
        )
        ul = label.find_element(By.XPATH, "following-sibling::ul[1]")
        items = ul.find_elements(By.TAG_NAME, "li")
        return [li.text.strip() for li in items if li.text.strip()]

Ожидаемый результат: Selenium, Playwright, Cypress, Appium, Katalon Studio

## Allure-отчёт

Все тесты аннотированы:
- @allure.feature — группировка по странице
- @allure.story — Positive / Negative / Special task
- @allure.title — читаемое имя
- @pytest.mark.positive / @pytest.mark.negative — маркеры

При падении теста conftest.py автоматически прикрепляет скриншот.

## Паттерн проектирования

Используется Page Object Model:
- BasePage — общие методы (click, type, is_visible)
- Каждая страница — отдельный класс с локаторами и методами
- Тесты не работают с селекторами напрямую

## Результаты

50 passed in 243.13s

## Allure-отчёт онлайн

Интерактивный отчёт со всеми 50 тестами:
https://tumashenkinyaroslav.github.io/VolgaIT_Semi-final_Test-automation/allure-report/
