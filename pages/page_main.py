from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):

    @allure.step('ожидаем загрузки главной страницы до повления блока элементов с вопросами')
    def wait_for_load_page(self):
        self.wait_for_clickable_element(MainPageLocators.QUESTIONS_LABEL)

    @allure.step('Получаем ответ на вопрос по его порядковому номер начиная с нуля {number}')
    def get_answer_for_question_by_number(self, number):
        method, locator = MainPageLocators.QUESTION_BY_NUMBER
        question_locator = method, locator.format(number)
        self.move_to_element(question_locator)
        self.wait_for_clickable_element(question_locator)
        self.click_on_element(question_locator)

        method, locator = MainPageLocators.ANSWER_BY_NUMBER
        answer_locator = method, locator.format(number)
        answer_text = self.driver.find_element(*answer_locator).text
        return answer_text