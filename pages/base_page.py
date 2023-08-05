import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    @allure.step('Загружаем главную страницу сайта Самокат')
    def __init__(self,driver):
        self.driver = driver

    @allure.step('Нажимаем на элемент с локатором {element_locator}')
    def click_on_element(self, element_locator):
        self.driver.find_element(*element_locator).click()

    @allure.step('Заполняем поле {element_locator} текстом {text}')
    def set_text_to_field(self, element_locator, text):
        self.driver.find_element(*element_locator).send_keys(text)

    @allure.step('Скролим страницу для элемента {element_locator}')
    def move_to_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидаем кликабельного элемента {element_locator}')
    def wait_for_clickable_element(self, element_locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((element_locator)))

    @allure.step('Ожидаем видимого элемента {element_locator}')
    def wait_for_invisibility_element(self, element_locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element((element_locator)))