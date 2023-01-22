
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
        # Test name: order_number
        # Step # | name | target | value
        # 1 | open | /en/ |
        self.driver.get("http://34.118.122.203/en/")
        # 2 | setWindowSize | 1936x1056 |
        self.driver.set_window_size(1936, 1056)
        # 3 | click | name=s |
        self.driver.find_element(By.NAME, "s").click()
        # 4 | type | name=s | empire
        self.driver.find_element(By.NAME, "s").send_keys("empire")
        # 5 | sendKeys | name=s | ${KEY_ENTER}
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        # 6 | click | css=.thumbnail > img |
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        self.driver.implicitly_wait(1)
        # 7 | click | css=.add-to-cart |
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        # 8 | click | css=.cart-content-btn > .btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()
        # 9 | click | css=.text-sm-center > .btn |
        self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
        # 10 | click | id=field-id_gender-1 |
        self.driver.find_element(By.ID, "field-id_gender-1").click()
        # 11 | click | id=field-firstname |
        self.driver.find_element(By.ID, "field-firstname").click()
        # 12 | type | id=field-firstname | Laur
        self.driver.find_element(By.ID, "field-firstname").send_keys("Laur")
        # 13 | click | id=field-lastname |
        self.driver.find_element(By.ID, "field-lastname").click()
        # 14 | type | id=field-lastname | Smith
        self.driver.find_element(By.ID, "field-lastname").send_keys("Smith")
        # 15 | click | id=field-email |
        self.driver.find_element(By.ID, "field-email").click()
        # 16 | type | id=field-email | user@example.com
        self.driver.find_element(By.ID, "field-email").send_keys("random@gmail.com")
        # 17 | click | id=field-birthday |
        self.driver.find_element(By.ID, "field-birthday").click()
        # 18 | click | css=.form-group:nth-child(9) > .col-md-6 label |
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(9) > .col-md-6 label").click()
        # 20 | click | name=continue |
        self.driver.find_element(By.NAME, "continue").click()
        # 21 | click | id=field-address1 |
        self.driver.find_element(By.ID, "field-address1").click()
        # 22 | type | id=field-address1 | Ohio street
        self.driver.find_element(By.ID, "field-address1").send_keys("Ohio street")
        # 23 | click | id=field-city |
        self.driver.find_element(By.ID, "field-city").click()
        # 24 | type | id=field-city | Ohio
        self.driver.find_element(By.ID, "field-city").send_keys("Ohio")
        # 25 | click | id=field-id_state |
        self.driver.find_element(By.ID, "field-id_state").click()
        # 26 | select | id=field-id_state | label=Idaho
        dropdown = self.driver.find_element(By.ID, "field-id_state")
        dropdown.find_element(By.XPATH, "//option[. = 'Idaho']").click()
        # 27 | click | id=field-postcode |
        self.driver.find_element(By.ID, "field-postcode").click()
        # 28 | type | id=field-postcode | 56854
        self.driver.find_element(By.ID, "field-postcode").send_keys("56854")
        # 29 | click | name=confirm-addresses |
        self.driver.find_element(By.NAME, "confirm-addresses").click()
        # 30 | click | name=confirmDeliveryOption |
        self.driver.find_element(By.NAME, "confirmDeliveryOption").click()
        # 31 | click | css=.condition-label > .js-terms |
        self.driver.find_element(By.CSS_SELECTOR, ".condition-label > .js-terms").click()
        # 32 | click | id=payment-option-3 |
        self.driver.find_element(By.ID, "payment-option-3").click()
        # 33 | assertChecked | id=conditions_to_approve[terms-and-conditions] |
        assert self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").is_selected() is True
        # 34 | click | css=.ps-shown-by-js > .btn |
        self.driver.find_element(By.CSS_SELECTOR, ".ps-shown-by-js > .btn").click()
        order_number = self.driver.find_element(By.XPATH, '//*[@id="order-reference-value"]').text
        good_order_number = order_number.replace('Order reference: ', '')
        self.driver.get(
            "http://34.118.122.203/administration/index.php?controller=AdminDashboard&token=439eb29f8901e56895dc8022ccef73eb")
        # 35 | click | id=email |
        self.driver.find_element(By.ID, "email").click()
        # 36 | click | id=passwd |
        self.driver.find_element(By.ID, "passwd").click()
        # 37 | type | id=passwd | VTR6WmtBCvnZ
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        # 38 | click | id=email |
        self.driver.find_element(By.ID, "email").click()
        # 39 | type | id=email | user@example.com
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        # 40 | click | id=submit_login |
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
