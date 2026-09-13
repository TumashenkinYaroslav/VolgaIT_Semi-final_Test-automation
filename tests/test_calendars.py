import allure
import pytest
from pages.calendars_page import CalendarsPage


@allure.feature("Calendars page")
class TestCalendars:

    # ---------- ПОЗИТИВНЫЕ ----------

    @allure.story("Positive")
    @pytest.mark.positive
    def test_calendar_input_visible(self, browser):
        page = CalendarsPage(browser).open_page()
        assert page.is_visible(page.DATE_INPUT)

    @allure.story("Positive")
    @pytest.mark.positive
    def test_calendar_input_clickable(self, browser):
        page = CalendarsPage(browser).open_page()
        page.click_input()
        assert page.is_visible(page.DATE_INPUT)

    @allure.story("Positive")
    @pytest.mark.positive
    def test_format_hint_visible(self, browser):
        page = CalendarsPage(browser).open_page()
        hint = page.get_format_hint()
        assert hint != "", "Подсказка формата не отображается"

    @allure.story("Positive")
    @pytest.mark.positive
    def test_format_hint_is_yyyy_mm_dd(self, browser):
        page = CalendarsPage(browser).open_page()
        hint = page.get_format_hint().upper()
        assert "YYYY" in hint and "MM" in hint and "DD" in hint, \
            f"Неожиданный формат: {hint}"

    @allure.story("Positive")
    @pytest.mark.positive
    def test_type_valid_date(self, browser):
        page = CalendarsPage(browser).open_page()
        page.type_date("2025-12-25")
        assert page.get_input_value() == "2025-12-25"

    @allure.story("Positive")
    @pytest.mark.positive
    def test_valid_date_no_error(self, browser):
        page = CalendarsPage(browser).open_page()
        page.type_date("2025-01-15")
        assert page.get_error_text() == ""

    @allure.story("Positive")
    @pytest.mark.positive
    def test_clear_input(self, browser):
        page = CalendarsPage(browser).open_page()
        page.type_date("2025-12-25")
        page.type_date("")
        assert page.get_input_value() == ""

    @allure.story("Positive")
    @pytest.mark.positive
    def test_accepts_various_dates(self, browser):
        page = CalendarsPage(browser).open_page()
        for d in ["2024-01-01", "2025-06-15", "2030-12-31"]:
            page.type_date(d)
            assert page.get_input_value() == d

    @allure.story("Positive")
    @pytest.mark.positive
    def test_field_accepts_keystrokes(self, browser):
        page = CalendarsPage(browser).open_page()
        page.click_input()
        # после клика поле активно и принимает ввод
        page.type_date("2025-07-04")
        assert page.get_input_value() == "2025-07-04"

    @allure.story("Positive")
    @pytest.mark.positive
    def test_retype_replaces_value(self, browser):
        page = CalendarsPage(browser).open_page()
        page.type_date("2025-01-01")
        page.type_date("2026-02-02")
        assert page.get_input_value() == "2026-02-02"

    # ---------- НЕГАТИВНЫЕ ----------

    @allure.story("Negative")
    @pytest.mark.negative
    def test_invalid_date_text_no_crash(self, browser):
        page = CalendarsPage(browser).open_page()
        page.type_date("not-a-date")
        assert page.is_visible(page.DATE_INPUT)

    @allure.story("Negative")
    @pytest.mark.negative
    def test_empty_input_no_crash(self, browser):
        page = CalendarsPage(browser).open_page()
        page.type_date("")
        assert page.is_visible(page.DATE_INPUT)

    @allure.story("Negative")
    @pytest.mark.negative
    def test_far_future_date_no_crash(self, browser):
        page = CalendarsPage(browser).open_page()
        page.type_date("2099-12-31")
        assert page.is_visible(page.DATE_INPUT)
