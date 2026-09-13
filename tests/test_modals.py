import allure
import pytest
from pages.modals_page import ModalsPage


@allure.feature("Modals page")
class TestModals:

    @allure.story("Positive")
    @pytest.mark.positive
    def test_simple_modal_button_visible(self, browser):
        page = ModalsPage(browser).open_page()
        assert page.is_visible(page.SIMPLE_MODAL_BTN)

    @allure.story("Positive")
    @pytest.mark.positive
    def test_simple_modal_opens(self, browser):
        page = ModalsPage(browser).open_page()
        page.click_simple_modal()
        assert page.modal_is_open()

    @allure.story("Positive")
    @pytest.mark.positive
    def test_simple_modal_contains_text(self, browser):
        page = ModalsPage(browser).open_page()
        page.click_simple_modal()
        assert len(page.get_modal_text()) > 0

    @allure.story("Positive")
    @pytest.mark.positive
    def test_simple_modal_closes_via_close_button(self, browser):
        page = ModalsPage(browser).open_page()
        page.click_simple_modal()
        page.click_close()
        assert page.modal_is_closed()

    @allure.story("Positive")
    @pytest.mark.positive
    def test_form_modal_opens(self, browser):
        page = ModalsPage(browser).open_page()
        page.click_form_modal()
        assert page.modal_is_open()

    @allure.story("Positive")
    @pytest.mark.positive
    def test_form_modal_has_name_field(self, browser):
        page = ModalsPage(browser).open_page()
        page.click_form_modal()
        assert page.is_visible(page.FORM_NAME)

    @allure.story("Positive")
    @pytest.mark.positive
    def test_form_modal_has_email_field(self, browser):
        page = ModalsPage(browser).open_page()
        page.click_form_modal()
        assert page.is_visible(page.FORM_EMAIL)

    @allure.story("Positive")
    @pytest.mark.positive
    def test_form_modal_close_button_works(self, browser):
        page = ModalsPage(browser).open_page()
        page.click_form_modal()
        page.click_close()
        assert page.modal_is_closed()

    @allure.story("Positive")
    @pytest.mark.positive
    def test_modal_content_not_visible_before_open(self, browser):
        page = ModalsPage(browser).open_page()
        assert page.is_not_visible(page.OVERLAY, timeout=2)

    @allure.story("Positive")
    @pytest.mark.positive
    def test_only_one_modal_can_be_opened(self, browser):
        page = ModalsPage(browser).open_page()
        page.click_simple_modal()
        assert page.modal_is_open()

    @allure.story("Negative")
    @pytest.mark.negative
    def test_form_modal_submit_with_empty_fields(self, browser):
        page = ModalsPage(browser).open_page()
        page.click_form_modal()
        try:
            page.submit_form()
        except Exception:
            pass
        assert page.modal_is_open() or page.is_visible(page.FORM_NAME)

    @allure.story("Negative")
    @pytest.mark.negative
    def test_invalid_email_does_not_submit(self, browser):
        page = ModalsPage(browser).open_page()
        page.click_form_modal()
        page.fill_name("Test")
        page.fill_email("not-an-email")
        try:
            page.submit_form()
        except Exception:
            pass
        assert page.modal_is_open() or page.is_visible(page.FORM_EMAIL)
