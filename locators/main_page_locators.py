from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTIONS_LABEL = By.XPATH, "//div[contains(@class, 'Home_FourPart')]/div[text()='Вопросы о важном']"
    QUESTION_BY_NUMBER = By.XPATH, "//div[@id='accordion__heading-{}' and @class='accordion__button']"
    ANSWER_BY_NUMBER = By.XPATH, "//div[@id='accordion__panel-{}' and @class='accordion__panel']/p"

    HEADER_ORDER_KEY = By.XPATH, "//div[contains(@class,'Header_Nav')]/button[text()='Заказать']"
    HOME_ORDER_KEY = By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']"
    SAMOKAT_LOGO = By.XPATH, "//a[contains(@class,'Header_LogoScooter')]"
    YANDEX_LOGO = By.XPATH, "//a[contains(@class,'Header_LogoYandex')]"
    COOKIE_BUTTON = By.XPATH, "//button[contains(@class,'App_CookieButton') and text()='да все привыкли']"