from selenium.webdriver.common.by import By


class OrderFormPageLocators:

    # Поле Имя
    first_name_field = By.XPATH, "//input[@placeholder='* Имя']"
    # Поле Фамилия
    last_name_field = By.XPATH, "//input[@placeholder='* Фамилия']"
    # Поле Адрес
    address_field = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    # Поле Станция метро
    metro_station_field = By.XPATH, "//input[@placeholder='* Станция метро']"
    # Выпадающий список со станциями метро
    metro_stations_list = [By.CLASS_NAME, 'select-search__select']
    # Поле Телефон
    phone_number_field = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    # Заголовок формы Про аренду
    title_about_rent_form = By.CLASS_NAME, 'Order_Header__BZXOb'
    # Поле выбора даты аренды
    rent_date_field = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    # Календарь для выбора даты аренды
    rent_date_calendar = By.CLASS_NAME, 'react-datepicker__month-container'
    # Сегодняшняя дата в календаре
    today_date_calendar = By.CLASS_NAME, 'react-datepicker__day--today'
    # Завтрашняя дата в календаре
    tomorrow_date_calendar = By.XPATH, "following-sibling::div[1]"
    # Поле выбора даты аренды
    rent_duration_field = By.CLASS_NAME, 'Dropdown-placeholder'
    # Поле выбора даты аренды в активном состоянии
    rent_duration_field_selected = By.CLASS_NAME, 'Dropdown-placeholder is-selected'
    # Выпадающий список со сроками аренды
    rent_duration_dropdown = By.CLASS_NAME, 'Dropdown-menu'
    # Выбранный срок аренды
    rent_duration_choose = By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='сутки']"
    # Поле выбора цвета
    choose_color_field = By.XPATH, '//div[text()="Цвет самоката"]'
    # Цвет серый
    checkbox = By.ID, 'black'
    # Поле комментарий
    comment_field = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    # Кнопка Далее
    continue_button = By.XPATH, '//button[text()="Далее"]'
    # Кнопка Заказать
    order_button = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'
    # Кнопка Да
    yes_button = By.XPATH, '//button[text()="Да"]'
    # Всплывающее окно подтверждения заказа
    confirm_order_pop_up = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'
    # Всплывающее окно с данными о созданном заказе
    order_created_pop_up = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'
