import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1200, 600')
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    yield browser
    browser.quit()

@pytest.fixture(scope='function')
def login(driver):
    driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.XPATH, ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys('daria_volk_8_628@yandex.ru')
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('8628628')
    driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    return driver


