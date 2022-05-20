from BaseApp import BasePage
from selenium.webdriver.common.by import By

#Локаторы
class Locators:
    LOCATOR_INSTALL = (By.CSS_SELECTOR , "a.b-btn.btn-main.header-main-btn.b-btn_green")

#Поиск элементов
class SearchHelper(BasePage):

    #Поиск кнопки установки
    def Click_button_install(self):
        search_field = self.find_element(Locators.LOCATOR_INSTALL)
        search_field.click()
