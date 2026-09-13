from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CalendarsPage(BasePage):
    PATH = "/calendars/"

    DATE_INPUT = (By.ID, "g1065-1-selectorenteradate")
    DATE_FORMAT_HINT = (By.ID, "g1065-1-selectorenteradate-text-format")
    DATE_ERROR = (By.ID, "g1065-1-selectorenteradate-text-error")

    def open_page(self):
        return self.open(self.PATH)

    def click_input(self):
        return self.click(self.DATE_INPUT)

    def type_date(self, value: str):
        return self.type(self.DATE_INPUT, value)

    def get_input_value(self) -> str:
        return self.get_attribute(self.DATE_INPUT, "value")

    def get_format_hint(self) -> str:
        try:
            return self.get_text(self.DATE_FORMAT_HINT)
        except Exception:
            return ""

    def get_error_text(self) -> str:
        try:
            el = self.find(self.DATE_ERROR)
            return el.text if el.is_displayed() else ""
        except Exception:
            return ""
