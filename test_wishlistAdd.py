import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.testSuite
@pytest.mark.account
class TestWishlistAdd():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_wishlistAdd(self):
        self.driver.get("http://34.118.122.203/en/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
        self.driver.find_element(By.ID, "field-email").click()
        self.driver.find_element(By.ID, "field-email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "field-password").click()
        self.driver.find_element(By.ID, "field-password").send_keys("123456789")
        self.driver.find_element(By.ID, "submit-login").click()
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("empire")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".wishlist-button-add > .material-icons").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CSS_SELECTOR, ".wishlist-list-item > p").click()
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").clear()
        self.driver.find_element(By.NAME, "s").send_keys("humming")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(1) img").click()
        self.driver.find_element(By.XPATH, '//*[@class="wishlist-button-add wishlist-button-product"]').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CSS_SELECTOR, ".wishlist-list-item > p").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CSS_SELECTOR, "#wishlist-link .material-icons").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CSS_SELECTOR, ".wishlist-list-item-link").click()
        assert 'After The Empire (Kickstarter Deluxe Edition)' in self.driver.find_element(By.XPATH,
                                                                                           '//li[1]//div[2]/p[1]').text
        assert 'Hummingbird printed t-shirt' in self.driver.find_element(By.XPATH,
                                                                         '//li[2]//div[2]/p[1]').text
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".wishlist-products-item:nth-child(2) .wishlist-button-add > .material-icons").click()
        self.driver.find_element(By.CSS_SELECTOR, ".show .btn-primary").click()
        time.sleep(0.5)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".wishlist-products-item:nth-child(1) .wishlist-button-add > .material-icons").click()
        self.driver.find_element(By.CSS_SELECTOR, ".show .btn-primary").click()
        assert 'After The Empire (Kickstarter Deluxe Edition)' not in self.driver.find_element(By.XPATH,
                                                                                               '//*[@class="wishlist-list-empty"]').text
        assert 'Hummingbird printed t-shirt' not in self.driver.find_element(By.XPATH,
                                                                             '//*[@class="wishlist-list-empty"]').text


if __name__ == '__main__':
    pytest.main()
