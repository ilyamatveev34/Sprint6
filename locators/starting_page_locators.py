from selenium.webdriver.common.by import By


class TestStartingPageLocators:

    # Кнопка Заказать в верхней части страницы
    order_button_upper = By.CLASS_NAME, 'Button_Button__ra12g'
    # Кнопка Заказать в теле страницы
    order_button_middle = By.CLASS_NAME, 'Button_Middle__1CSJM'
    # Логотип Яндекс
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    # Логотип Самокат
    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    # Принять куки
    accept_cookie_button = By.ID, 'rcc-confirm-button'
    # Первый вопрос
    accordion_button_0 = By.ID, 'accordion__heading-0'
    # Второй вопрос
    accordion_button_1 = By.ID, 'accordion__heading-1'
    # Третий вопрос
    accordion_button_2 = By.ID, 'accordion__heading-2'
    # Четвертый вопрос
    accordion_button_3 = By.ID, 'accordion__heading-3'
    # Пятый вопрос
    accordion_button_4 = By.ID, 'accordion__heading-4'
    # Шестой вопрос
    accordion_button_5 = By.ID, 'accordion__heading-5'
    # Седьмой вопрос
    accordion_button_6 = By.ID, 'accordion__heading-6'
    # Восьмой вопрос
    accordion_button_7 = By.ID, 'accordion__heading-7'
    # Первый ответ
    answer_0 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-0"]:not([hidden]) p'
    # Второй ответ
    answer_1 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-1"]:not([hidden]) p'
    # Третий ответ
    answer_2 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-2"]:not([hidden]) p'
    # Четвертый ответ
    answer_3 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-3"]:not([hidden]) p'
    # Пятый ответ
    answer_4 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-4"]:not([hidden]) p'
    # Шестой ответ
    answer_5 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-5"]:not([hidden]) p'
    # Седьмой ответ
    answer_6 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-6"]:not([hidden]) p'
    # Восьмой ответ
    answer_7 = By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-7"]:not([hidden]) p'
