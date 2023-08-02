import allure
import pytest
from pages.page_main import MainPage
from urls import AdressSite
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class TestMainPage:

    answers_list = [
                    [0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                    [1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                    'можете просто сделать несколько заказов — один за другим.'],
                    [2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                    'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                    'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                    [3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                    [4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
                    [5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете '
                    'кататься без передышек и во сне. Зарядка не понадобится.'],
                    [6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
                    [7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
                   ]

    @allure.title('Проверка соответствия ответов на вопросы на главной странице.')
    @allure.description('Поочередно проверяем ответы на вопросы. Сверяем с эталонными из списка answer_list')
    @pytest.mark.parametrize('answer_number, answer_text', answers_list)
    def test_checking_answers(self, driver, answer_number, answer_text,):
        main_page = MainPage(driver)
        main_page.wait_for_load_page()
        answer_from_page = main_page.get_answer_for_question_by_number(answer_number)
        assert answer_from_page == answer_text

    @allure.title('Проверка перехода на главную страницу сайта Самокат по ссылке в header')
    @allure.description('Нажимаем на ссылку, сверяем URL загрузившейся страницы со строкой AdressSite.main_page')
    def test_check_transition_samokat_link(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_element(MainPageLocators.SAMOKAT_LOGO)
        assert AdressSite.main_page in driver.current_url

    @allure.title('Проверка перехода на главную страницу Яндекса по ссылке в header')
    @allure.description('Нажимаем на ссылку, переходим в другую закладку, '
                        'ожидаем загрузки страницы и появления элемента с логотипом Яндекс,'
                        'сверяем URL загрузившейся страницы со строкой AdressSite.yandex_page')
    def test_check_transition_yandex_link(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_element(MainPageLocators.YANDEX_LOGO)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, '//div[@class="headline"]/a[contains(@class, "headline__logo")]')))
        assert AdressSite.yandex_page in driver.current_url