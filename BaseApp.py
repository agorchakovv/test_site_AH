from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    #инициализируем драйвер и передаем в переменную базовый url
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://alihelper.net/ru/"
    #Явные ожидания поиска элемента по локатору
    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
    #Открытие базового url
    def go_to_site(self):
        return self.driver.get(self.base_url)



    