from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма заказа №1
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    TELEPHONE_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    METRO_STATION_DROPDOWN = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_1 = (By.XPATH, '//li[5]')
    METRO_STATION_2 = (By.XPATH, '//li[8]')
    APPLY_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")

    # Форма заказа №2
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR_MENU = (By.XPATH, "//div[contains(@class, 'react-datepicker__day')]")
    SPECIFIC_CALENDAR_CELL = (By.XPATH, "(//div[contains(@class, 'react-datepicker__day')])[{}]")
    DURATION_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    DURATION_SELECT = (By.XPATH, "//div[@class='Dropdown-menu']//div[2]")
    COLOUR_SELECT = (By.XPATH, "//label[contains(text(),'чёрный жемчуг')]")
    COMMENT_SECTION = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")

    # Окно "Заказ оформлен"

    ORDER_DONE_HEADER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    CHECK_STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")

    # Лого на странице

    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")




