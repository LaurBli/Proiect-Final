import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.testSuite
@pytest.mark.discount
class TestCartrulefail():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_cartrulefail(self):
        reduction_amount = '25'
        discount_name = 'Buy 3 games to get a discount'
        self.driver.get(
            "http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e&redirect=AdminDashboard")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "passwd").click()
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        self.driver.find_element(By.CSS_SELECTOR, ".ladda-label").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ladda-label")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset((element), 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.LINK_TEXT, "Discounts").click()
        self.driver.find_element(By.CSS_SELECTOR, "#page-header-desc-cart_rule-new_cart_rule > div").click()
        self.driver.find_element(By.ID, "name_1").click()
        self.driver.find_element(By.ID, "name_1").send_keys(discount_name)
        self.driver.find_element(By.ID, "code").click()
        self.driver.find_element(By.LINK_TEXT, "Generate").click()
        code = self.driver.find_element(By.ID, 'code').get_attribute('value')
        self.driver.find_element(By.ID, "cart_rule_link_conditions").click()
        self.driver.find_element(By.ID, "customerFilter").click()
        self.driver.find_element(By.ID, "customerFilter").send_keys("laur")
        self.driver.find_element(By.CSS_SELECTOR, ".ac_even").click()
        self.driver.find_element(By.NAME, "minimum_amount").click()
        self.driver.find_element(By.NAME, "minimum_amount").clear()
        self.driver.find_element(By.NAME, "minimum_amount").send_keys("200")
        self.driver.find_element(By.NAME, "minimum_amount_tax").click()
        dropdown = self.driver.find_element(By.NAME, "minimum_amount_tax")
        dropdown.find_element(By.XPATH, "//option[. = 'Tax included']").click()
        self.driver.find_element(By.ID, "product_restriction").click()
        self.driver.find_element(By.LINK_TEXT, "Product selection").click()
        self.driver.find_element(By.ID, "product_rule_type_1").click()
        dropdown = self.driver.find_element(By.ID, "product_rule_type_1")
        dropdown.find_element(By.XPATH, "//option[. = 'Categories']").click()
        self.driver.find_element(By.LINK_TEXT, "Add").click()
        self.driver.find_element(By.ID, "product_rule_1_1_choose_link").click()
        element = self.driver.find_element(By.ID, "product_rule_1_1_choose_link")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, 0, 0).perform()
        self.driver.execute_script("window.scrollTo(0,0)")
        dropdown = self.driver.find_element(By.ID, "product_rule_select_1_1_1")
        self.driver.implicitly_wait(2)
        dropdown.find_element(By.XPATH, "//option[@value='10']").click()
        self.driver.find_element(By.ID, "product_rule_select_1_1_add").click()
        self.driver.find_element(By.CSS_SELECTOR, ".fancybox-item").click()
        element = self.driver.find_element(By.ID, "cart_rule_link_actions")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "cart_rule_link_actions")
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element(By.ID, "apply_discount_amount").click()
        self.driver.find_element(By.ID, "reduction_amount").click()
        self.driver.find_element(By.ID, "reduction_amount").clear()
        self.driver.find_element(By.ID, "reduction_amount").send_keys(reduction_amount)
        self.driver.find_element(By.NAME, "reduction_tax").click()
        dropdown = self.driver.find_element(By.NAME, "reduction_tax")
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CSS_SELECTOR, "#desc-cart_rule-save > span").click()
        assert 'Successful creation.' in self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div').text
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, "#header_shopname > span").click()
        self.vars["win5744"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win5744"])
        self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
        self.driver.find_element(By.ID, "field-email").click()
        self.driver.find_element(By.ID, "field-email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "field-password").click()
        self.driver.find_element(By.ID, "field-password").send_keys("123456789")
        self.driver.find_element(By.ID, "submit-login").click()
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("suburbia")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("twilight")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()
        self.driver.find_element(By.LINK_TEXT, "Have a promo code?").click()
        self.driver.find_element(By.NAME, "discount_name").click()
        self.driver.find_element(By.NAME, "discount_name").send_keys(code)
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        time.sleep(2)
        alert = self.driver.find_element(By.XPATH, '//*[@id="promo-code"]/div/div/span')
        alert_text = alert.get_attribute('innerText')
        assert 'You have not reached the minimum amount required to use this voucher' in alert_text
        before_discount = self.driver.find_element(By.XPATH, '//*[@id="cart-subtotal-products"]/span[2]').text
        after_discount = self.driver.find_element(By.XPATH,
                                                  '//*[@class="card-block cart-summary-totals js-cart-summary-totals"]/div[1]/span[2]').text
        assert before_discount == after_discount
        self.driver.get(
            "http://34.118.122.203/administration/index.php?controller=AdminCartRules&conf=1&token=7ed6c7391ba2d0f7d26b9578904c11d8")
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
        self.driver.find_element(By.LINK_TEXT, "Discounts").click()
        self.driver.find_element(By.CSS_SELECTOR, ".icon-caret-down").click()
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        self.driver.find_element(By.ID, "popup_ok").click()


if __name__ == '__main__':
    pytest.main()
