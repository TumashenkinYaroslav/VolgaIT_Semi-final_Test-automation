from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FormPage(BasePage):
    PATH = "/form-fields/"

    # Поля
    NAME = (By.ID, "name-input")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    EMAIL = (By.ID, "email")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.ID, "submit-btn")

    # Чекбоксы "любимый напиток"
    DRINK1 = (By.ID, "drink1")
    DRINK2 = (By.ID, "drink2")
    DRINK3 = (By.ID, "drink3")
    DRINK4 = (By.ID, "drink4")
    DRINK5 = (By.ID, "drink5")

    # Радио "любимый цвет"
    COLOR1 = (By.ID, "color1")
    COLOR2 = (By.ID, "color2")
    COLOR3 = (By.ID, "color3")
    COLOR4 = (By.ID, "color4")
    COLOR5 = (By.ID, "color5")

    # Select "Do you like automation?"
    AUTOMATION_SELECT = (By.ID, "automation")

    def open_page(self):
        return self.open(self.PATH)

    def fill_name(self, v: str):
        return self.type(self.NAME, v)

    def fill_password(self, v: str):
        return self.type(self.PASSWORD, v)

    def fill_email(self, v: str):
        return self.type(self.EMAIL, v)

    def fill_message(self, v: str):
        return self.type(self.MESSAGE, v)

    def submit(self):
        # Используем self.click() — там есть fallback на JS-клик
        return self.click(self.SUBMIT)

    def get_name_value(self) -> str:
        return self.get_attribute(self.NAME, "value")

    def get_message_value(self) -> str:
        return self.get_attribute(self.MESSAGE, "value")

    def select_drink(self, index: int):
        boxes = [self.DRINK1, self.DRINK2, self.DRINK3, self.DRINK4, self.DRINK5]
        self.click(boxes[index - 1])
        return self

    def select_color(self, index: int):
        radios = [self.COLOR1, self.COLOR2, self.COLOR3, self.COLOR4, self.COLOR5]
        self.click(radios[index - 1])
        return self

    def get_automation_tools(self):
        """
        Возвращает список строк из <ul> после label 'Automation tools'.
        Именно сюда смотрит спец. задание из ТЗ.
        """
        label = self.driver.find_element(
            By.XPATH, "//label[normalize-space()='Automation tools']"
        )
        ul = label.find_element(By.XPATH, "following-sibling::ul[1]")
        items = ul.find_elements(By.TAG_NAME, "li")
        return [li.text.strip() for li in items if li.text.strip()]
