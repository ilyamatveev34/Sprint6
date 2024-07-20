import allure

from locators.starting_page_locators import TestStartingPageLocators
from pages.base_page import BasePage
from data import DZEN_URL


class StartingPage(BasePage):

    @allure.step('Нажать кнопку Заказать в верхней части страницы')
    def click_order_button_upper(self):
        self.find_element_with_wait(TestStartingPageLocators.order_button_upper)
        self.click_on_element(TestStartingPageLocators.order_button_upper)

    @allure.step('Скролл до кнопки Заказать в теле страницы')
    def scroll_to_order_button_middle(self):
        self.scroll_to_element(TestStartingPageLocators.order_button_middle)
        self.find_element_with_wait(TestStartingPageLocators.order_button_middle)

    @allure.step('Нажать кнопку Заказать в теле страницы')
    def click_order_button_middle(self):
        self.scroll_to_order_button_middle()
        self.click_on_element(TestStartingPageLocators.order_button_middle)

    @allure.step('Закрытиь окно куки')
    def accept_cookie_button(self):
        self.find_element_with_wait(TestStartingPageLocators.accept_cookie_button)
        self.click_on_element(TestStartingPageLocators.accept_cookie_button)

    @allure.step('Скролл до блока Вопросы о важном')
    def scroll_to_faq(self):
        self.scroll_to_element(TestStartingPageLocators.accordion_button_7)
        self.find_element_with_wait(TestStartingPageLocators.accordion_button_7)

    @allure.step('Нажать на вопрос')
    def click_question(self, question_locator):
        self.find_element_with_wait(question_locator)
        self.click_on_element(question_locator)

    @allure.step('Получить текст ответа')
    def get_answer_text(self, answer_locator):
        self.find_element_with_wait(answer_locator)
        answer = self.get_text_on_element(answer_locator)
        return answer

    @allure.step('Нажать на логотип Яндекс')
    def click_logo_yandex_open_dzen_page(self):
        self.find_element_with_wait(TestStartingPageLocators.yandex_logo)
        self.click_on_element(TestStartingPageLocators.yandex_logo)
        self.switch_to_next_tab()
        self.wait_url_to_be(DZEN_URL)

    @allure.step('Нажать на логотип Самокат')
    def click_logo_open_starting_page(self):
        self.find_element_with_wait(TestStartingPageLocators.scooter_logo)
        self.click_on_element(TestStartingPageLocators.scooter_logo)
