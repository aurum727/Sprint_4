from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']"
    SURNAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADRES_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    SUBWAY_STATION_FIELD = By.XPATH, "//input[@placeholder='* Станция метро']"
    SUBWAY_STATION_VALUE = By.XPATH, "//li[@class='select-search__row']//div[text()='{}']"
    PHONE_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON =By.XPATH, "//div[contains(@class,'Order_NextButton__1_rCA')]/button[text()='Далее']"

    DELIVERY_DATE_FIELD = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    TERM_OF_USE_FIELD = By.XPATH, "//div[contains(@class,'Dropdown-placeholder')]"
    TERM_OF_USE_VALUE = By.XPATH, "//div[@class='Dropdown-option' and text()='{}']"
    COLOR_CHECK = By.XPATH, "//label[text()='{}']/input"
    COMMENT_FIELD  = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    MAKE_ORDER_BUTTON = By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']"
    CONFIRM_ORDER_BUTTON = By.XPATH, "//div[contains(@class,'Order_Modal')]//button[text()='Да']"
    CONFIRM_ORDER_STATUS = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"
    ORDER_STATUS_MODAL_BUTTON = By.XPATH, "//div[contains(@class, 'Order_NextButton') and text()='Посмотреть статус']"
    SHOW_STATUS_BUTTON = By.XPATH, "//button[text()='Посмотреть статус']"
