import allure
from pages.page_main import MainPage
from urls import AdressSite
from locators.main_page_locators import MainPageLocators


class TestMainPageTransitionLink:

    @allure.title('Проверка перехода на главную страницу сайта Самокат по ссылке в header')
    @allure.description('Нажимаем на ссылку, сверяем URL загрузившейся страницы со строкой AdressSite.main_page')
    def test_check_transition_samokat_link(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_load_page()
        main_page.click_on_element(MainPageLocators.SAMOKAT_LOGO)
        assert AdressSite.main_page in driver.current_url

    @allure.title('Проверка перехода на главную страницу Яндекса по ссылке в header')
    @allure.description('Нажимаем на ссылку, переходим в другую закладку, '
                        'ожидаем загрузки страницы и появления элемента с логотипом Яндекс,'
                        'сверяем URL загрузившейся страницы со строкой AdressSite.yandex_page')
    def test_check_transition_yandex_link(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_load_page()
        main_page.click_on_element(MainPageLocators.YANDEX_LOGO)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        main_page.wait_for_invisibility_element(MainPageLocators.YANDEX_MAIN_PAGE_LOGO)
        assert AdressSite.yandex_page in driver.current_url
