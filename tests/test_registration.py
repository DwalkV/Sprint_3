from faker import Faker
from selenium.webdriver.common.by import By
from locators import Locators

faker = Faker()

class TestRegistration:
    def test_registration_valid_data_success(self, driver):
        name = faker.name()
        email = faker.email()
        password = faker.password()
        print(name, email, password)
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        driver.find_element(By.XPATH, Locators.registration_locator).click()
        driver.find_element(By.XPATH, Locators.name_or_email_locator).send_keys(name)
        driver.find_element(By.XPATH, Locators.email_field_in_registration).send_keys(email)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(password)
        driver.find_element(By.XPATH, Locators.log_in).click()
        log_in = driver.find_element(By.XPATH, Locators.log_in).text
        assert log_in == 'Зарегистрироваться'


    def test_registration_short_password(self, driver):
        name = faker.name()
        email = faker.email()
        driver.find_element(By.XPATH, Locators.lk_from_main_locator).click()
        driver.find_element(By.XPATH, Locators.registration_locator).click()
        driver.find_element(By.XPATH, Locators.name_or_email_locator).send_keys(name)
        driver.find_element(By.XPATH, Locators.email_field_in_registration).send_keys(email)
        driver.find_element(By.XPATH, Locators.password_field).send_keys('123')
        driver.find_element(By.XPATH, Locators.log_in).click()
        error = driver.find_element(By.XPATH, Locators.wrong_password).text
        assert error == 'Некорректный пароль'


