from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class BasePage:
    BASE_URL = "https://practice-automation.com"
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def open(self, path: str = ""):
        self.driver.get(self.BASE_URL + path)
        return self

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_visible(self, locator, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_not_visible(self, locator, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def click(self, locator):
        el = self.find_clickable(locator)
        # Прокручиваем элемент в центр экрана, чтобы его не перекрывала шапка
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", el
        )
        try:
            el.click()
        except Exception:
            # Fallback: JS-клик, если элемент перекрыт другим
            self.driver.execute_script("arguments[0].click();", el)
        return self

    def type(self, locator, text: str, clear: bool = True):
        el = self.find_visible(locator)
        if clear:
            el.clear()
        el.send_keys(text)
        return self

    def get_text(self, locator) -> str:
        return self.find_visible(locator).text

    def get_attribute(self, locator, name: str):
        return self.find(locator).get_attribute(name)

    def press_escape(self):
        from selenium.webdriver.common.keys import Keys
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        return self
