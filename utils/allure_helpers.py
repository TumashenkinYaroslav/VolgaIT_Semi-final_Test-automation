import allure


def attach_screenshot(driver, name: str = "screenshot"):
    png = driver.get_screenshot_as_png()
    allure.attach(png, name=name, attachment_type=allure.attachment_type.PNG)


def attach_text(text: str, name: str = "text"):
    allure.attach(text, name=name, attachment_type=allure.attachment_type.TEXT)


def step(title: str):
    return allure.step(title)
