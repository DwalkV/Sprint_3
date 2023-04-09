from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

mail = 'daria_volk_8_628@yandex.ru'
password = '8628628'

class TestAuthorization():
    def test_authorization_from_main_page(self, driver):
        driver.find_element(By.XPATH, Locators.login_from_main_page).click()
        driver.find_element(By.XPATH, Locators.name_or_email_locator).send_keys(mail)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(password)
        driver.find_element(By.XPATH, Locators.log_in).click()
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.email_field_in_lk)))
        email_after = driver.find_element(By.XPATH, Locators.email_field_in_lk).get_attribute('value')
        assert email_after == mail

    def test_authorization_from_lk(self, driver):
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        driver.find_element(By.XPATH, Locators.name_or_email_locator).send_keys(mail)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(password)
        driver.find_element(By.XPATH, Locators.log_in).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.lk_from_main_locator)))
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.email_field_in_lk)))
        email_after = driver.find_element(By.XPATH, Locators.email_field_in_lk).get_attribute('value')
        assert email_after == mail

    def test_authorization_from_registration_form(self, driver):
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        driver.find_element(By.XPATH, Locators.registration_locator).click()
        driver.find_element(By.XPATH, Locators.login_from_restore_or_registration).click()
        driver.find_element(By.XPATH, Locators.name_or_email_locator).send_keys(mail)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(password)
        driver.find_element(By.XPATH, Locators.log_in).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.lk_from_main_locator)))
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.email_field_in_lk)))
        email_after = driver.find_element(By.XPATH, Locators.email_field_in_lk).get_attribute('value')
        assert email_after == mail

    def test_authorization_from_restore_password_form(self, driver):
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        driver.find_element(By.XPATH, Locators.forgot_password).click()
        driver.find_element(By.XPATH, Locators.login_from_restore_or_registration).click()
        driver.find_element(By.XPATH, Locators.name_or_email_locator).send_keys(mail)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(password)
        driver.find_element(By.XPATH, Locators.log_in).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.lk_from_main_locator)))
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.email_field_in_lk)))
        email_after = driver.find_element(By.XPATH, Locators.email_field_in_lk).get_attribute('value')
        assert email_after == mail
