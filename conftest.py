import pytest
from selenium import webdriver

from data import BASE_URL
from pages.order_form_page import OrderFormPage
from pages.starting_page import StartingPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def starting_page(driver):
    starting_page = StartingPage(driver)
    starting_page.accept_cookie_button()
    return starting_page


@pytest.fixture()
def order_page(driver):
    order_page = OrderFormPage(driver)
    return order_page
