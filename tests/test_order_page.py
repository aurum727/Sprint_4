import allure
import pytest
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.page_order import OrderPage


class TestOrderPage:

    client_data = [
                    [
                        MainPageLocators.HEADER_ORDER_KEY,
                        ['Иванов', 'Иванович', 'Мухина', 'Сокольники', '+79224560099'],
                        ['28.08.2023', 'сутки', 'чёрный жемчуг', 'Без коментариев']],
                    [
                        MainPageLocators.HOME_ORDER_KEY,
                        ['Павел', 'Золотов', 'Ленина', 'Лубянка', '+79112223344'],
                        ['20.08.2023', 'четверо суток', 'серая безысходность', 'Скорее везите']]
                    ]

    @allure.title('Проверка оформления заказа')
    @allure.description('Заполняем форму "Для кого" и "О заказе", ожидаем успешного подтвержения заказа. Используем два'
                        'набора данных из списка client_data')
    @pytest.mark.parametrize('button, for_whom_form_list, about_form_list', client_data)
    def test_new_order(self, driver, button, for_whom_form_list, about_form_list):
        order = OrderPage(driver)
        order.wait_for_load_main_page()

        try:
            driver.find_element(*MainPageLocators.COOKIE_BUTTON).click()
        except:
            pass

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