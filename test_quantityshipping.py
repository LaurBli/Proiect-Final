# Generated by Selenium IDE
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestQuantityshipping():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_quantityshipping(self):
        # Test name: quantity_shipping
        # Step # | name | target | value
        # 1 | open | http://34.118.122.203/en/ |
        self.driver.get("http://34.118.122.203/en/")
        # 2 | setWindowSize | 1920x1040 |
        self.driver.set_window_size(1920, 1040)
        # 3 | click | name=s |
        self.driver.find_element(By.NAME, "s").click()
        # 4 | type | name=s | empire
        self.driver.find_element(By.NAME, "s").send_keys("empire")
        # 5 | sendKeys | name=s | ${KEY_ENTER}
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        # 6 | click | css=.thumbnail > img |
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        self.driver.implicitly_wait(2)
        # 7 | click | css=.add-to-cart |
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        # 8 | click | css=.cart-content-btn > .btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()
        assert '7.00' in self.driver.find_element(By.XPATH,'//*[@id="cart-subtotal-shipping"]/span[2]').text
        assert '133.00' in self.driver.find_element(By.XPATH,'//*[@class="product-price"]/strong').text
        # 9 | click | css=.touchspin-up |
        self.driver.find_element(By.XPATH,'//*[@class="input-group-btn-vertical"]/button[1]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="cart"]').click()

        assert '266.00' in self.driver.find_element(By.XPATH,'//*[@class="product-price"]/strong').text
        assert 'Free' in self.driver.find_element(By.XPATH,'//*[@id="cart-subtotal-shipping"]/span[2]').text


if __name__ == '__main__':
    pytest.main()