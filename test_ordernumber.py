import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.testSuite
@pytest.mark.order
class TestOrdernumber():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_ordernumber(self):
        self.driver.get("http://34.118.122.203/en/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("empire")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
        self.driver.find_element(By.ID, "field-id_gender-1").click()
        self.driver.find_element(By.ID, "field-firstname").click()
        self.driver.find_element(By.ID, "field-firstname").send_keys("Laur")
        self.driver.find_element(By.ID, "field-lastname").click()
        self.driver.find_element(By.ID, "field-lastname").send_keys("Smith")
        self.driver.find_element(By.ID, "field-email").click()
        self.driver.find_element(By.ID, "field-email").send_keys("random@gmail.com")
        self.driver.find_element(By.ID, "field-birthday").click()
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
        self.driver.find_element(By.CSS_SELECTOR, ".condition-label > .js-terms").click()
        self.driver.find_element(By.ID, "payment-option-3").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ps-shown-by-js > .btn").click()
        order_number = self.driver.find_element(By.XPATH, '//*[@id="order-reference-value"]').text
        good_order_number = order_number.replace('Order reference: ', '')
        self.driver.get(
            "http://34.118.122.203/administration/index.php?controller=AdminDashboard&token=439eb29f8901e56895dc8022ccef73eb")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "passwd").click()
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "submit_login").click()
        self.driver.find_element(By.CSS_SELECTOR, '#subtab-AdminParentOrders').click()
        self.driver.find_element(By.XPATH, '//*[@id="subtab-AdminOrders"]/a').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//*[@id="order_reference"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="order_reference"]').clear()
        self.driver.find_element(By.XPATH, '//*[@id="order_reference"]').send_keys(good_order_number)
        self.driver.find_element(By.XPATH, '//*[@id="order_grid_table"]/thead/tr[2]/td[11]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="order_grid_table"]/tbody/tr').click()
        self.driver.implicitly_wait(10)
        back_order_number = self.driver.find_element(By.XPATH, '//*[@class="d-inline"]/strong[2]').text
        assert good_order_number == back_order_number


if __name__ == '__main__':
    pytest.main()
