import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.discount
@pytest.mark.testSuite
class TestDiscountpret():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_discountpret(self):
        self.driver.get("http://34.118.122.203/en/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("hummin")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(1) img").click()
        regular_price = self.driver.find_element(By.CLASS_NAME, "regular-price").text
        reduced_price = self.driver.find_element(By.CLASS_NAME, "current-price-value").text
        assert '19.12' in reduced_price
        assert '19.12' not in regular_price


if __name__ == '__main__':
    pytest.main()
