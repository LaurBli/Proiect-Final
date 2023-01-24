import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.testSuite
@pytest.mark.cart
class TestQuantityshipping():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_quantityshipping(self):
        self.driver.get("http://34.118.122.203/en/")
        self.driver.set_window_size(1920, 1040)
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("empire")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()
        assert '7.00' in self.driver.find_element(By.XPATH, '//*[@id="cart-subtotal-shipping"]/span[2]').text
        assert '133.00' in self.driver.find_element(By.XPATH, '//*[@class="product-price"]/strong').text
        self.driver.find_element(By.XPATH, '//*[@class="input-group-btn-vertical"]/button[1]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="cart"]').click()

        assert '266.00' in self.driver.find_element(By.XPATH, '//*[@class="product-price"]/strong').text
        assert 'Free' in self.driver.find_element(By.XPATH, '//*[@id="cart-subtotal-shipping"]/span[2]').text


if __name__ == '__main__':
    pytest.main()
