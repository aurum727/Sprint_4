from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import allure


class OrderPage(BasePage):

    @allure.step('Ожидаем загрузки главной страницы до появления кликабельной кнопки "Заказать"')
    def wait_for_load_main_page(self):
        self.wait_for_clickable_element(MainPageLocators.HOME_ORDER_KEY)

    @allure.step('Заполяем форму "Для кого самокат" данными из списка {for_whom_data_list}')
    def form_for_whom_fill(self, for_whom_data_list):
        self.set_text_to_field(OrderPageLocators.NAME_FIELD, for_whom_data_list[0])
        self.set_text_to_field(OrderPageLocators.SURNAME_FIELD, for_whom_data_list[1])
        self.set_text_to_field(OrderPageLocators.ADRES_FIELD, for_whom_data_list[2])
        self.click_on_element(OrderPageLocators.SUBWAY_STATION_FIELD)

        method, locator = OrderPageLocators.SUBWAY_STATION_VALUE
        subway_station_locator = method, locator.format(for_whom_data_list[3])

        self.wait_for_clickable_element(subway_station_locator)
        self.click_on_element(subway_station_locator)
        self.set_text_to_field(OrderPageLocators.PHONE_FIELD,for_whom_data_list[4])

    @allure.step('Заполяем форму "Про аренду" данными из списка {about_order_list}')
    def form_about_rent_fill(self, about_order_list):
        self.set_text_to_field(OrderPageLocators.DELIVERY_DATE_FIELD, about_order_list[0])
        self.driver.find_element(*OrderPageLocators.DELIVERY_DATE_FIELD).send_keys(Keys.ESCAPE)

        self.click_on_element(OrderPageLocators.TERM_OF_USE_FIELD)
        method, locator = OrderPageLocators.TERM_OF_USE_VALUE
        term_of_use_locator = method, locator.format(about_order_list[1])
        self.wait_for_clickable_element(term_of_use_locator)
        self.click_on_element(term_of_use_locator)

        method, locator = OrderPageLocators.COLOR_CHECK
        color = method, locator.format(about_order_list[2])
        self.click_on_element(color)

        self.set_text_to_field(OrderPageLocators.COMMENT_FIELD, about_order_list[3])


