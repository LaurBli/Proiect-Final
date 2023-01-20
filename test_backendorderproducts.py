# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestBackendorderproducts():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_backendorderproducts(self):
    # Test name: backend_order_products
    # Step # | name | target | value
    # 1 | open | http://34.118.122.203/en/ | 
    self.driver.get("http://34.118.122.203/en/")
    # 2 | setWindowSize | 1936x1056 | 
    self.driver.set_window_size(1936, 1056)
    # 3 | click | css=.featured-products:nth-child(2) .js-product:nth-child(1) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".featured-products:nth-child(2) .js-product:nth-child(1) img").click()
    # 4 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    WebDriverWait(self.driver, 10).until(lambda s:s.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary"))
    # 5 | click | css=.cart-content-btn > .btn-secondary | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    # 6 | click | css=.logo | 
    self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
    # 7 | click | css=.featured-products:nth-child(2) .js-product:nth-child(2) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".featured-products:nth-child(2) .js-product:nth-child(2) img").click()
    # 8 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary"))
    # 9 | click | css=.cart-content-btn > .btn-secondary | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    # 10 | click | css=.logo | 
    self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
    # 11 | click | css=.featured-products:nth-child(2) .js-product:nth-child(3) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".featured-products:nth-child(2) .js-product:nth-child(3) img").click()
    # 12 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary"))
    # 13 | click | css=.cart-content-btn > .btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()
    product_1_name = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[1]//a').text
    product_1_price = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[1]//strong').text
    product_2_name = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[2]//a').text
    product_2_price = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[2]//strong').text
    product_3_name = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[3]//a').text
    product_3_price = self.driver.find_element(By.XPATH, '//*[@class="cart-items"]//li[3]//strong').text
    # 14 | click | css=.text-sm-center > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
    # 15 | click | id=field-id_gender-1 | 
    self.driver.find_element(By.ID, "field-id_gender-1").click()
    # 16 | click | id=field-firstname | 
    self.driver.find_element(By.ID, "field-firstname").click()
    # 17 | type | id=field-firstname | Laur
    self.driver.find_element(By.ID, "field-firstname").send_keys("Laur")
    # 18 | click | id=field-lastname | 
    self.driver.find_element(By.ID, "field-lastname").click()
    # 19 | type | id=field-lastname | Smith
    self.driver.find_element(By.ID, "field-lastname").send_keys("Smith")
    # 20 | click | id=field-email | 
    self.driver.find_element(By.ID, "field-email").click()
    # 21 | type | id=field-email | abcd@gmail.com
    self.driver.find_element(By.ID, "field-email").send_keys("abcd@gmail.com")
    # 22 | click | css=.form-group:nth-child(9) > .col-md-6 label | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(9) > .col-md-6 label").click()
    # 23 | click | name=continue | 
    self.driver.find_element(By.NAME, "continue").click()
    # 24 | click | id=field-address1 | 
    self.driver.find_element(By.ID, "field-address1").click()
    # 25 | type | id=field-address1 | Ohio street
    self.driver.find_element(By.ID, "field-address1").send_keys("Ohio street")
    # 26 | click | id=field-city | 
    self.driver.find_element(By.ID, "field-city").click()
    # 27 | type | id=field-city | Ohio
    self.driver.find_element(By.ID, "field-city").send_keys("Ohio")
    # 28 | click | id=field-id_state | 
    self.driver.find_element(By.ID, "field-id_state").click()
    # 29 | select | id=field-id_state | label=Idaho
    dropdown = self.driver.find_element(By.ID, "field-id_state")
    dropdown.find_element(By.XPATH, "//option[. = 'Idaho']").click()
    # 30 | click | id=field-postcode | 
    self.driver.find_element(By.ID, "field-postcode").click()
    # 31 | type | id=field-postcode | 56854
    self.driver.find_element(By.ID, "field-postcode").send_keys("56854")
    # 32 | click | name=confirm-addresses | 
    self.driver.find_element(By.NAME, "confirm-addresses").click()
    # 33 | click | name=confirmDeliveryOption | 
    self.driver.find_element(By.NAME, "confirmDeliveryOption").click()
    # 34 | click | id=payment-option-3 | 
    self.driver.find_element(By.ID, "payment-option-3").click()
    # 35 | click | id=conditions_to_approve[terms-and-conditions] | 
    self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
    # 36 | click | css=.ps-shown-by-js > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".ps-shown-by-js > .btn").click()
    order_id = self.driver.find_element(By.ID, 'order-reference-value').text
    order_id_number = order_id.replace('Order reference: ', '')
    self.driver.get("http://34.118.122.203/administration")
    # 37 | click | id=email | 
    self.driver.find_element(By.ID, "email").click()
    # 38 | type | id=email | user@example.com
    self.driver.find_element(By.ID, "email").send_keys("user@example.com")
    # 39 | click | id=passwd | 
    self.driver.find_element(By.ID, "passwd").click()
    # 40 | type | id=passwd | VTR6WmtBCvnZ
    self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
    # 41 | click | id=submit_login | 
    self.driver.find_element(By.ID, "submit_login").click()
    WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, "#subtab-AdminParentOrders > .link"))
    # 42 | click | css=#subtab-AdminParentOrders > .link | 
    self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminParentOrders > .link").click()
    # 43 | click | linkText=Orders | 
    self.driver.find_element(By.LINK_TEXT, "Orders").click()
    # 44 | click | id=order_reference | 
    self.driver.find_element(By.ID, "order_reference").click()
    self.driver.find_element(By.ID, "order_reference").clear()
    # 45 | type | id=order_reference | JPMMVPRHT 
    self.driver.find_element(By.ID, "order_reference").send_keys(order_id_number)
    # 46 | click | name=order[actions][search] | 
    self.driver.find_element(By.NAME, "order[actions][search]").click()
    # 47 | click | css=.column-reference | 
    self.driver.find_element(By.CSS_SELECTOR, ".column-reference").click()
    assert product_1_name in self.driver.find_element(By.ID,'orderProductsTable').text
    assert product_1_price in self.driver.find_element(By.ID,'orderProductsTable').text
    assert product_2_name in self.driver.find_element(By.ID,'orderProductsTable').text
    assert product_2_price in self.driver.find_element(By.ID,'orderProductsTable').text
    assert product_3_name in self.driver.find_element(By.ID,'orderProductsTable').text
    assert product_3_price in self.driver.find_element(By.ID,'orderProductsTable').text