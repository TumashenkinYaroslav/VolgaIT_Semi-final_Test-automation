from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class AdsPage(BasePage):
    PATH = "/ads/"

    OVERLAY = (By.CSS_SELECTOR, ".pum-overlay")
    MAIN_CONTENT = (By.CSS_SELECTOR, "main, article, .entry-content, h1")
    PAGE_TITLE = (By.TAG_NAME, "h1")

    def open_page(self):
        return self.open(self.PATH)

    def wait_for_ad(self, timeout: int = 15) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: any(o.is_displayed()
                              for o in d.find_elements(*self.OVERLAY))
            )
            return True
        except TimeoutException:
            return False

    def ad_is_visible(self, timeout: int = 15) -> bool:
        return self.wait_for_ad(timeout)

    def ad_is_hidden(self, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: not any(o.is_displayed()
                                  for o in d.find_elements(*self.OVERLAY))
            )
            return True
        except TimeoutException:
            return False

    def find_close_button(self, timeout: int = 15):
        import time
        self.wait_for_ad(timeout=15)
        deadline = time.time() + timeout
        while time.time() < deadline:
            for o in self.driver.find_elements(*self.OVERLAY):
                if o.is_displayed():
                    for b in o.find_elements(By.CSS_SELECTOR, ".pum-close"):
                        if b.is_displayed():
                            return b
            time.sleep(0.3)
        return None

    def has_close_button(self, timeout: int = 15) -> bool:
        return self.find_close_button(timeout=timeout) is not None

    def close_ad(self):
        btn = self.find_close_button(timeout=15)
        if btn is None:
            raise AssertionError("Не нашли кнопку закрытия рекламы")
        self.driver.execute_script("arguments[0].click();", btn)
        return self

    def page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def main_content_visible(self) -> bool:
        return self.is_visible(self.MAIN_CONTENT, timeout=5)
