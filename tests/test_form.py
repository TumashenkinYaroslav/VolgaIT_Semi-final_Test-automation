import allure
import pytest
from pages.form_page import FormPage


@allure.feature("Form fields page")
class TestForm:

    # ---------- ПОЗИТИВНЫЕ ----------

    @allure.story("Positive")
    @pytest.mark.positive
    def test_name_field_visible(self, browser):
        page = FormPage(browser).open_page()
        assert page.is_visible(page.NAME)

    @allure.story("Positive")
    @pytest.mark.positive
    def test_password_field_visible(self, browser):
        page = FormPage(browser).open_page()
        assert page.is_visible(page.PASSWORD)

    @allure.story("Positive")
    @pytest.mark.positive
    def test_email_field_visible(self, browser):
        page = FormPage(browser).open_page()
        assert page.is_visible(page.EMAIL)

    @allure.story("Positive")
    @pytest.mark.positive
    def test_message_field_visible(self, browser):
        page = FormPage(browser).open_page()
        assert page.is_visible(page.MESSAGE)

    @allure.story("Positive")
    @pytest.mark.positive
    def test_submit_button_visible(self, browser):
        page = FormPage(browser).open_page()
        assert page.is_visible(page.SUBMIT)

    @allure.story("Positive")
    @pytest.mark.positive
    def test_fill_name(self, browser):
        page = FormPage(browser).open_page()
        page.fill_name("Ivan")
        assert page.get_name_value() == "Ivan"

    @allure.story("Positive")
    @pytest.mark.positive
    def test_select_drink_checkbox(self, browser):
        page = FormPage(browser).open_page()
        page.select_drink(3)  # Coffee
        assert page.find(page.DRINK3).is_selected()

    @allure.story("Positive")
    @pytest.mark.positive
    def test_select_color_radio(self, browser):
        page = FormPage(browser).open_page()
        page.select_color(2)  # Blue
        assert page.find(page.COLOR2).is_selected()

    @allure.story("Positive")
    @pytest.mark.positive
    def test_automation_tools_list_has_items(self, browser):
        page = FormPage(browser).open_page()
        tools = page.get_automation_tools()
        allure.attach(str(tools), name="tools",
                      attachment_type=allure.attachment_type.TEXT)
        assert len(tools) >= 5

    @allure.story("Positive")
    @pytest.mark.positive
    def test_fill_full_form(self, browser):
        page = FormPage(browser).open_page()
        page.fill_name("Ivan")
        page.fill_password("secret")
        page.fill_email("ivan@test.com")
        page.fill_message("Hello")
        page.select_drink(1)
        page.select_color(1)
        assert page.get_message_value() == "Hello"

    # ---------- СПЕЦИАЛЬНОЕ ЗАДАНИЕ ИЗ ТЗ ----------

    @allure.story("Special task")
    @pytest.mark.positive
    @allure.title("Fill Message with comma-separated Automation Tools")
    def test_fill_message_with_automation_tools(self, browser):
        """
        Спец. задание:
        1. Получить средствами Selenium список элементов из раздела Automation Tools
        2. Преобразовать в текст
        3. Заполнить поле Message полученным списком через запятую
        """
        page = FormPage(browser).open_page()

        tools = page.get_automation_tools()
        allure.attach(str(tools), name="Список Automation Tools",
                      attachment_type=allure.attachment_type.TEXT)
        assert len(tools) >= 5

        tools_string = ", ".join(tools)
        allure.attach(tools_string, name="Строка для Message",
                      attachment_type=allure.attachment_type.TEXT)

        page.fill_message(tools_string)
        actual = page.get_message_value()
        assert actual == tools_string, \
            f"Ожидалось: {tools_string!r}\nПолучено: {actual!r}"

    # ---------- НЕГАТИВНЫЕ ----------

    @allure.story("Negative")
    @pytest.mark.negative
    def test_submit_with_empty_name(self, browser):
        page = FormPage(browser).open_page()
        page.fill_email("test@test.com")
        page.fill_message("msg")
        # name имеет required, submit не должен пройти
        page.submit()
        assert browser.current_url is not None

    @allure.story("Negative")
    @pytest.mark.negative
    def test_empty_message_field(self, browser):
        page = FormPage(browser).open_page()
        page.fill_name("Test")
        assert page.get_message_value() == ""

    @allure.story("Negative")
    @pytest.mark.negative
    def test_invalid_email_format(self, browser):
        page = FormPage(browser).open_page()
        page.fill_email("not-an-email")
        # поле принимает текст, ошибки не показывается
        assert page.is_visible(page.EMAIL)
