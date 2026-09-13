from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class ModalsPage(BasePage):
    PATH = "/modals/"

    SIMPLE_MODAL_BTN = (By.ID, "simpleModal")
    FORM_MODAL_BTN = (By.ID, "formModal")

    OVERLAY = (By.CSS_SELECTOR, ".pum-overlay")
    CONTAINER = (By.CSS_SELECTOR, ".pum-container")
    MODAL_CONTENT = (By.CSS_SELECTOR, ".pum-content")
    CLOSE_BTN = (By.CSS_SELECTOR, ".pum-close")

    # Эти селекторы временные — заменим после диагностики
    FORM_NAME = (By.CSS_SELECTOR, ".pum-overlay:not([style*='display: none']) input[type='text'], .pum-overlay:not([style*='display: none']) input[type='email']")
    FORM_EMAIL = (By.CSS_SELECTOR, ".pum-overlay:not([style*='display: none']) input[type='email']")
    FORM_SUBMIT = (By.CSS_SELECTOR, ".pum-overlay:not([style*='display: none']) button, .pum-overlay:not([style*='display: none']) input[type='submit']")

    def open_page(self):
        return self.open(self.PATH)

    def click_simple_modal(self):
        return self.click(self.SIMPLE_MODAL_BTN)

    def click_form_modal(self):
        return self.click(self.FORM_MODAL_BTN)

    def modal_is_open(self, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: any(o.is_displayed()
                              for o in d.find_elements(*self.OVERLAY))
            )
            return True
        except TimeoutException:
            return False

    def modal_is_closed(self, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: not any(o.is_displayed()
                                  for o in d.find_elements(*self.OVERLAY))
            )
            return True
        except TimeoutException:
            return False

    def get_modal_text(self) -> str:
        for o in self.driver.find_elements(*self.OVERLAY):
            if o.is_displayed():
                try:
                    return o.find_element(By.CSS_SELECTOR, ".pum-content").text
                except Exception:
                    return ""
        return ""

    def click_close(self):
        for o in self.driver.find_elements(*self.OVERLAY):
            if o.is_displayed():
                btn = o.find_element(By.CSS_SELECTOR, ".pum-close")
                self.driver.execute_script("arguments[0].click();", btn)
                return self
        raise AssertionError("Не нашли видимую модалку")

    def fill_name(self, value: str):
        return self.type(self.FORM_NAME, value)

    def fill_email(self, value: str):
        return self.type(self.FORM_EMAIL, value)

    def submit_form(self):
        return self.click(self.FORM_SUBMIT)
