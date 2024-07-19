import allure
from locators.order_form_page_locators import OrderFormPageLocators
from pages.base_page import BasePage


class OrderFormPage(BasePage):

    @allure.step('Заполнить поле Имя')
    def set_first_name(self, name):
        self.set_text_to_element(OrderFormPageLocators.first_name_field, name)
        return self

    @allure.step('Заполнить поле Фамилия')
    def set_last_name(self, last_name):
        self.set_text_to_element(OrderFormPageLocators.last_name_field, last_name)
        return self

    @allure.step('Заполнить поле Адрес')
    def set_address(self, address):
        self.set_text_to_element(OrderFormPageLocators.address_field, address)
        return self

    @allure.step('Заполнить поле Метро')
    def set_metro(self, station):
        self.click_on_element(OrderFormPageLocators.metro_station_field)
        self.set_text_to_element(OrderFormPageLocators.metro_station_field, station)
        self.click_on_element(OrderFormPageLocators.metro_stations_list)
        return self

    @allure.step('Заполнить поле Телефон')
    def set_phone(self, number):
        self.set_text_to_element(OrderFormPageLocators.phone_number_field, number)
        return self

    @allure.step('Нажать кнопку Далее')
    def click_next_button(self):
        self.click_on_element(OrderFormPageLocators.continue_button)

    @allure.step('Отображение заголовка второй формы')
    def check_the_title_displaying(self):
        self.check_displaying_of_element(OrderFormPageLocators.title_about_rent_form)

    @allure.step('Заполнить поле Дата аренды')
    def set_rental_date(self):
        self.click_on_element(OrderFormPageLocators.rent_date_field)
        self.find_element_with_wait(OrderFormPageLocators.rent_date_calendar)
        today = self.find_element_with_wait(OrderFormPageLocators.today_date_calendar)
        tomorrow = today.find_element(*OrderFormPageLocators.tomorrow_date_calendar)
        tomorrow.click()
        return self

    @allure.step('Заполнить поле Срок аренды')
    def set_rental_duration(self):
        self.click_on_element(OrderFormPageLocators.rent_duration_field)
        self.find_element_with_wait(OrderFormPageLocators.rent_duration_dropdown)
        self.click_on_element(OrderFormPageLocators.rent_duration_choose)

    @allure.step('Установить в чекбоксе галочку напротив нужного цвета')
    def set_color_field(self):
        self.click_on_element(OrderFormPageLocators.checkbox)
        return self

    @allure.step('Заполнить поле Комментарий')
    def set_comment_field(self, comment):
        self.set_text_to_element(OrderFormPageLocators.comment_field, comment)
        return self

    @allure.step('Нажать кнопку Заказать')
    def click_order_button(self):
        self.click_on_element(OrderFormPageLocators.order_button)
        self.find_element_with_wait(OrderFormPageLocators.confirm_order_pop_up)

    @allure.step('Отображение окна подтверждения после нажатия кнопки Заказать')
    def check_displaying_confirm_popup(self):
        self.check_displaying_of_element(OrderFormPageLocators.confirm_order_pop_up)

    @allure.step('Нажать кнопку Да в окне подтверждения заказа')
    def click_yes_button_confirm_popup(self):
        self.click_on_element(OrderFormPageLocators.yes_button)
        self.find_element_with_wait(OrderFormPageLocators.order_created_pop_up)
        return self

    @allure.step('Заполнить форму Для кого и нажать кнопку Далее')
    def personal_information_fields(self, name, last_name, address, station, number):
        self.set_first_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(station)
        self.set_phone(number)
        self.click_next_button()
        self.check_the_title_displaying()

    @allure.step('Заполнить форму Про аренду и проверить появление окна подтверждения')
    def rental_info_fields(self, comment):
        self.set_rental_date()
        self.set_rental_duration()
        self.set_color_field()
        self.set_comment_field(comment)
        self.click_order_button()
        self.check_displaying_confirm_popup()
