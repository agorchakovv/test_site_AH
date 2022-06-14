import pytest
from selenium import webdriver

#Фикстура открытия и закрытия браузера
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="/chromedriver")
    yield driver
    driver.quit()