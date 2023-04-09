
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

class TestLk:

    def test_transfer_to_lk(self, driver,  login):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.lk_from_main_locator)))
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.lettering_in_lk)))
        check = driver.find_element(By.XPATH, Locators.lettering_in_lk).text
        assert check == 'В этом разделе вы можете изменить свои персональные данные'

    def test_transfer_from_lk_to_constructor(self, driver, login):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.lk_from_main_locator)))
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        driver.find_element(By.XPATH, Locators.conctructor).click()
        check = driver.find_element(By.XPATH, Locators.take_burger).text
        assert check == 'Соберите бургер'

    def test_transfer_from_lk_to_logo(self, driver, login):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.lk_from_main_locator)))
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        driver.find_element(By.XPATH, Locators.logo).click()
        check = driver.find_element(By.XPATH, Locators.take_burger).text
        assert check == 'Соберите бургер'

    def test_log_out(self, driver, login):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.lk_from_main_locator)))
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        driver.find_element(By.XPATH, Locators.log_out).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.entrance)))
        checks = driver.find_element(By.XPATH, Locators.entrance).text
        assert 'Вход' in checks