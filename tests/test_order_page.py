import allure
import pytest
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.page_order import OrderPage
import data


class TestOrderPage:

    @allure.title('Проверка оформления заказа')
    @allure.description('Заполняем форму "Для кого" и "О заказе", ожидаем успешного подтвержения заказа. Используем два'
                        'набора данных из списка client_data')
    @pytest.mark.parametrize('button, for_whom_form_list, about_form_list', data.client_data_for_order)
    def test_new_order(self, driver, button, for_whom_form_list, about_form_list):
        order = OrderPage(driver)
        order.wait_for_load_main_page()

        order.cookie_pass()

        order.move_to_element(button)
        order.wait_for_clickable_element(button)
        order.click_on_element(button)

        order.form_for_whom_fill(for_whom_form_list)
        order.click_on_element(OrderPageLocators.NEXT_BUTTON)
        order.form_about_rent_fill(about_form_list)
        order.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        order.wait_for_clickable_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        order.click_on_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        order.wait_for_clickable_element(OrderPageLocators.CONFIRM_ORDER_STATUS)
        order_confirm_text = order.driver.find_element(*OrderPageLocators.CONFIRM_ORDER_STATUS).text
        order.click_on_element(OrderPageLocators.SHOW_STATUS_BUTTON)
        order.wait_for_clickable_element(MainPageLocators.SAMOKAT_LOGO)
        order.click_on_element(MainPageLocators.SAMOKAT_LOGO)
        assert "Заказ оформлен" in order_confirm_text