import allure
import pytest
from locators.order_form_page_locators import OrderFormPageLocators
from data import test_data_user1, test_data_user2


class TestOrderFormPage:

    @allure.title('Проверка флоу позитивного сценария оформления заказа через верхнюю кнопку Заказать')
    @allure.description('Проверка перехода в форму заказа при нажатии кнопки Заказать в верхней части страницы и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [test_data_user1])
    def test_complete_order_form_order_button_upper(self, driver, starting_page, order_page, name, last_name, address, station, number, comment):
        starting_page.click_order_button_upper()
        order_page.personal_information_fields(name, last_name, address, station, number)
        order_page.rental_info_fields(comment)
        order_page.click_yes_button_confirm_popup()
        assert driver.find_element(*OrderFormPageLocators.order_created_pop_up).is_displayed()

    @allure.title('Проверка флоу позитивного сценария оформления заказа через нижнюю кнопку Заказать')
    @allure.description('Проверка перехода в форму заказа при нажатии кнопки Заказать в теле страницы и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [test_data_user2])
    def test_complete_order_form_order_button_middle(self, driver, starting_page, order_page, name, last_name, address, station, number, comment):
        starting_page.click_order_button_middle()
        order_page.personal_information_fields(name, last_name, address, station, number)
        order_page.rental_info_fields(comment)
        order_page.click_yes_button_confirm_popup()
        assert driver.find_element(*OrderFormPageLocators.order_created_pop_up).is_displayed()
