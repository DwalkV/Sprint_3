from selenium.webdriver.common.by import By

from tests.locators import Locators


class TestConstructor():
    def test_transfer_to_sauce(self, driver):
        driver.find_element(By.XPATH, Locators.sauce).click()
        select = driver.find_element(By.XPATH, ".//span[contains(text(),'Соусы')]/parent::div").get_attribute('class')
        assert select == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_transfer_to_filling(self, driver):
        driver.find_element(By.XPATH, Locators.filling).click()
        select = driver.find_element(By.XPATH, ".//span[contains(text(),'Начинки')]/parent::div").get_attribute('class')
        assert select == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_transfer_to_bread(self, driver):
        driver.find_element(By.XPATH, Locators.filling).click()
        driver.find_element(By.XPATH, Locators.bread).click()
        select = driver.find_element(By.XPATH, ".//span[contains(text(),'Булки')]/parent::div").get_attribute('class')
        assert select == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
