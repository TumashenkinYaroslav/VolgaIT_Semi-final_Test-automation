from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class ModalsPage(BasePage):
    PATH = "/modals/"

    SIMPLE_MODAL_BTN = (By.ID, "simpleModal")
    FORM_MODAL_BTN = (By.ID, "formModal")

    OVERLAY = (By.CSS_SELECTOR, ".pum-overlay")
    MODAL_CONTENT = (By.CSS_SELECTOR, ".pum-content")
    CLOSE_BTN = (By.CSS_SELECTOR, ".pum-close")

    FORM_NAME = (By.CSS_SELECTOR, "input[name='g1051-name']")
    FORM_EMAIL = (By.CSS_SELECTOR, "input[name='g1051-email']")
    FORM_MESSAGE = (By.CSS_SELECTOR, "textarea[name='g1051-message']")
    FORM_SUBMIT = (By.CSS_SELECTOR, "button[type='submit'].pushbutton-wide")

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

    def get_modal_text(self, timeout: int = 5) -> str:
        """Ждём непустой текст в видимом overlay. Fallback — весь текст overlay."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: any(
                    o.is_displayed() and o.text.strip()
                    for o in d.find_elements(*self.OVERLAY)
                )
            )
        except TimeoutException:
            pass

        for o in self.driver.find_elements(*self.OVERLAY):
            if o.is_displayed():
                # Сначала пробуем .pum-content
                try:
                    content_el = o.find_element(By.CSS_SELECTOR, ".pum-content")
                    if content_el.text.strip():
                        return content_el.text
                except Exception:
                    pass
                # Fallback — весь текст overlay
                if o.text.strip():
                    return o.text
        return ""

    def click_close(self):
        for o in self.driver.find_elements(*self.OVERLAY):
            if o.is_displayed():
                btn = o.find_element(By.CSS_SELECTOR, ".pum-close")
                self.driver.execute_script("arguments[0].click();", btn)
                return self
        raise AssertionError("Не нашли видимую модалку для закрытия")

    def fill_name(self, value: str):
        return self.type(self.FORM_NAME, value)

    def fill_email(self, value: str):
        return self.type(self.FORM_EMAIL, value)

    def fill_message(self, value: str):
        return self.type(self.FORM_MESSAGE, value)

    def submit_form(self):
        return self.click(self.FORM_SUBMIT)
