import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.testSuite
@pytest.mark.order
class TestBackendorderproducts():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_backendorderproducts(self):
        self.driver.get("http://34.118.122.203/en/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.CSS_SELECTOR, ".featured-products:nth-child(2) .js-product:nth-child(1) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary"))
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
        self.driver.find_element(By.CSS_SELECTOR, ".featured-products:nth-child(2) .js-product:nth-child(2) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary"))
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
        self.driver.find_element(By.CSS_SELECTOR, ".featured-products:nth-child(2) .js-product:nth-child(3) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary"))
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()
        product_1_name = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[1]//a').text
        product_1_price = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[1]//strong').text
        product_2_name = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[2]//a').text
        product_2_price = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[2]//strong').text
        product_3_name = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[3]//a').text
        product_3_price = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[3]//strong').text
        self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
        self.driver.find_element(By.ID, "field-id_gender-1").click()
        self.driver.find_element(By.ID, "field-firstname").click()
        self.driver.find_element(By.ID, "field-firstname").send_keys("Laur")
        self.driver.find_element(By.ID, "field-lastname").click()
        self.driver.find_element(By.ID, "field-lastname").send_keys("Smith")
        self.driver.find_element(By.ID, "field-email").click()
        self.driver.find_element(By.ID, "field-email").send_keys("abcd@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(9) > .col-md-6 label").click()
        self.driver.find_element(By.NAME, "continue").click()
        self.driver.find_element(By.ID, "field-address1").click()
        self.driver.find_element(By.ID, "field-address1").send_keys("Ohio street")
        self.driver.find_element(By.ID, "field-city").click()
        self.driver.find_element(By.ID, "field-city").send_keys("Ohio")
        self.driver.find_element(By.ID, "field-id_state").click()
        dropdown = self.driver.find_element(By.ID, "field-id_state")
        dropdown.find_element(By.XPATH, "//option[. = 'Idaho']").click()
        self.driver.find_element(By.ID, "field-postcode").click()
        self.driver.find_element(By.ID, "field-postcode").send_keys("56854")
        self.driver.find_element(By.NAME, "confirm-addresses").click()
        self.driver.find_element(By.NAME, "confirmDeliveryOption").click()
        self.driver.find_element(By.ID, "payment-option-3").click()
        self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ps-shown-by-js > .btn").click()
        order_id = self.driver.find_element(By.ID, 'order-reference-value').text
        order_id_number = order_id.replace('Order reference: ', '')
        self.driver.get("http://34.118.122.203/administration")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "passwd").click()
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        self.driver.find_element(By.ID, "submit_login").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, "#subtab-AdminParentOrders > .link"))
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminParentOrders > .link").click()
        self.driver.find_element(By.LINK_TEXT, "Orders").click()
        self.driver.find_element(By.ID, "order_reference").click()
        self.driver.find_element(By.ID, "order_reference").clear()
        self.driver.find_element(By.ID, "order_reference").send_keys(order_id_number)
        self.driver.find_element(By.NAME, "order[actions][search]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".column-reference").click()
        assert product_1_name in self.driver.find_element(By.ID, 'orderProductsTable').text
        assert product_1_price in self.driver.find_element(By.ID, 'orderProductsTable').text
        assert product_2_name in self.driver.find_element(By.ID, 'orderProductsTable').text
        assert product_2_price in self.driver.find_element(By.ID, 'orderProductsTable').text
        assert product_3_name in self.driver.find_element(By.ID, 'orderProductsTable').text
        assert product_3_price in self.driver.find_element(By.ID, 'orderProductsTable').text
