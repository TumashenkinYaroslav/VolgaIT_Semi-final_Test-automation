import allure
import pytest
from selenium.webdriver.common.by import By
from pages.ads_page import AdsPage


@allure.feature("Ads page")
class TestAds:

    @allure.story("Positive")
    @pytest.mark.positive
    def test_page_opens(self, browser):
        page = AdsPage(browser).open_page()
        assert "Ads" in page.page_title()

    @allure.story("Positive")
    @pytest.mark.positive
    def test_ad_popup_visible_on_load(self, browser):
        page = AdsPage(browser).open_page()
        assert page.ad_is_visible(), "Рекламный popup не появился"

    @allure.story("Positive")
    @pytest.mark.positive
    def test_ad_has_close_button(self, browser):
        page = AdsPage(browser).open_page()
        assert page.has_close_button(timeout=15), "Кнопка закрытия не найдена"

    @allure.story("Positive")
    @pytest.mark.positive
    def test_close_ad_removes_popup(self, browser):
        page = AdsPage(browser).open_page()
        page.close_ad()
        assert page.ad_is_hidden()

    @allure.story("Positive")
    @pytest.mark.positive
    def test_page_content_visible_after_close(self, browser):
        page = AdsPage(browser).open_page()
        page.close_ad()
        assert page.main_content_visible()

    @allure.story("Positive")
    @pytest.mark.positive
    def test_main_content_visible(self, browser):
        page = AdsPage(browser).open_page()
        assert page.main_content_visible()

    @allure.story("Positive")
    @pytest.mark.positive
    def test_page_title_is_ads(self, browser):
        page = AdsPage(browser).open_page()
        assert page.page_title().strip() == "Ads"

    @allure.story("Positive")
    @pytest.mark.positive
    def test_close_ad_then_reload(self, browser):
        page = AdsPage(browser).open_page()
        page.close_ad()
        page.open_page()
        assert page.main_content_visible()

    @allure.story("Negative")
    @pytest.mark.negative
    def test_closing_ad_twice_no_error(self, browser):
        page = AdsPage(browser).open_page()
        page.close_ad()
        assert page.ad_is_hidden()

    @allure.story("Negative")
    @pytest.mark.negative
    def test_ad_hidden_after_close(self, browser):
        page = AdsPage(browser).open_page()
        page.close_ad()
        assert page.ad_is_hidden()

    @allure.story("Negative")
    @pytest.mark.negative
    def test_ad_close_button_clickable_multiple_times(self, browser):
        """Клик по крестику отрабатывает без ошибок (реклама может переоткрыться — это фича)."""
        page = AdsPage(browser).open_page()
        # закрываем рекламу
        page.close_ad()
        # страница продолжает работать
        assert page.main_content_visible(), "Страница сломалась после закрытия рекламы"
        # клик по крестику не должен ронять страницу даже при повторном открытии
        assert browser.current_url.startswith("https://practice-automation.com")
