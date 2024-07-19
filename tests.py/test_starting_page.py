import allure
import pytest
from locators.starting_page_locators import TestStartingPageLocators
from data import expected_answer_texts, DZEN_URL, BASE_URL


class TestStartingPage:

    @allure.title('Проверка раздела Вопросы о важном')
    @allure.description('Проверка появления соответствующего текста ответа при нажатии на каждый вопрос')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_text', [
        (TestStartingPageLocators.accordion_button_0, TestStartingPageLocators.answer_0, expected_answer_texts['question 0']),
        (TestStartingPageLocators.accordion_button_1, TestStartingPageLocators.answer_1, expected_answer_texts['question 1']),
        (TestStartingPageLocators.accordion_button_2, TestStartingPageLocators.answer_2, expected_answer_texts['question 2']),
        (TestStartingPageLocators.accordion_button_3, TestStartingPageLocators.answer_3, expected_answer_texts['question 3']),
        (TestStartingPageLocators.accordion_button_4, TestStartingPageLocators.answer_4, expected_answer_texts['question 4']),
        (TestStartingPageLocators.accordion_button_5, TestStartingPageLocators.answer_5, expected_answer_texts['question 5']),
        (TestStartingPageLocators.accordion_button_6, TestStartingPageLocators.answer_6, expected_answer_texts['question 6']),
        (TestStartingPageLocators.accordion_button_7, TestStartingPageLocators.answer_7, expected_answer_texts['question 7'])

    ])
    def test_click_question_shows_answer_faq(self, driver, starting_page, question_locator, answer_locator, expected_text):
        starting_page.scroll_to_faq()
        starting_page.click_question(question_locator)
        answer = starting_page.get_answer_text(answer_locator)
        assert answer == expected_text

    @allure.title('Проверка нажатия на логотип Яндекс')
    @allure.description('Проверка открытия страницы Яндекс.Дзен в соседней вкладке при нажатии на логотип Яндекс')
    def test_click_yandex_logo_open_dzen_page(self, driver, starting_page):
        starting_page.click_logo_yandex_open_dzen_page()
        assert driver.current_url == DZEN_URL

    @allure.title('Проверка нажатия на логотип Самокат')
    @allure.description('Проверка перехода на главную страницу при нажатии на логотип Самокат')
    def test_click_logo_samokat_open_starting_page(self, driver, starting_page):
        starting_page.click_order_button_upper()
        starting_page.click_logo_open_starting_page()
        assert driver.current_url == BASE_URL
