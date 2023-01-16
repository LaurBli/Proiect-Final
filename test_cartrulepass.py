# Generated by Selenium IDE
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.discount
class TestCartrulepass():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        # 1 | open | http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e&redirect=AdminDashboard |
        self.driver.get(
            "http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e&redirect=AdminDashboard")
        # 2 | setWindowSize | 1936x1056 |
        self.driver.set_window_size(1936, 1056)
        # 3 | click | id=email |
        self.driver.find_element(By.ID, "email").click()
        # 4 | type | id=email | user@example.com
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        # 5 | click | id=passwd |
        self.driver.find_element(By.ID, "passwd").click()
        # 6 | type | id=passwd | VTR6WmtBCvnZ
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        # 7 | click | css=.ladda-label |
        self.driver.find_element(By.CSS_SELECTOR, ".ladda-label").click()
        # 8 | mouseOver | css=.ladda-label |
        element = self.driver.find_element(By.CSS_SELECTOR, ".ladda-label")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 9 | mouseOut | css=.ladda-label |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset((element), 0, 0).perform()
        # 10 | click | css=#subtab-AdminCatalog > .link |
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()

    def teardown_method(self, method):
        self.driver.get(
            "http://34.118.122.203/administration/index.php?controller=AdminCartRules&conf=1&token=7ed6c7391ba2d0f7d26b9578904c11d8")
        # 78 | click | css=.icon-caret-down |
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
        # 79 | click | linkText=Delete |
        self.driver.find_element(By.LINK_TEXT, "Discounts").click()
        # 80 | click | id=popup_ok |
        self.driver.find_element(By.CSS_SELECTOR, ".icon-caret-down").click()
        # 81 | click | css=#header_shopname > span |
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        # 82 | selectWindow | handle=${win3515} |
        self.driver.find_element(By.ID, "popup_ok").click()
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_cartrulepass(self):
        reduction_amount = '25'
        discount_name = 'Buy 3 games to get a discount'
        # Test name: cart_rule_pass
        # Step # | name | target | value

        self.driver.implicitly_wait(2)
        # 11 | click | linkText=Discounts |
        self.driver.find_element(By.LINK_TEXT, "Discounts").click()
        # 12 | click | css=#page-header-desc-cart_rule-new_cart_rule > div |
        self.driver.find_element(By.CSS_SELECTOR, "#page-header-desc-cart_rule-new_cart_rule > div").click()
        # 13 | click | id=name_1 |
        self.driver.find_element(By.ID, "name_1").click()
        # 14 | type | id=name_1 | Buy 3 games to get a discount
        self.driver.find_element(By.ID, "name_1").send_keys(discount_name)
        # 15 | click | id=code |
        self.driver.find_element(By.ID, "code").click()
        # 16 | click | linkText=Generate |
        self.driver.find_element(By.LINK_TEXT, "Generate").click()
        code = self.driver.find_element(By.ID, 'code').get_attribute('value')
        # 17 | click | id=cart_rule_link_conditions |
        self.driver.find_element(By.ID, "cart_rule_link_conditions").click()
        # 18 | click | id=customerFilter |
        self.driver.find_element(By.ID, "customerFilter").click()
        # 19 | type | id=customerFilter | laur
        self.driver.find_element(By.ID, "customerFilter").send_keys("laur")
        # 20 | click | css=.ac_even |
        self.driver.find_element(By.CSS_SELECTOR, ".ac_even").click()
        # 21 | click | name=minimum_amount |
        self.driver.find_element(By.NAME, "minimum_amount").click()
        self.driver.find_element(By.NAME, "minimum_amount").clear()
        # 22 | type | name=minimum_amount | 200
        self.driver.find_element(By.NAME, "minimum_amount").send_keys("200")
        # 23 | click | name=minimum_amount_tax |
        self.driver.find_element(By.NAME, "minimum_amount_tax").click()
        # 24 | select | name=minimum_amount_tax | label=Tax included
        dropdown = self.driver.find_element(By.NAME, "minimum_amount_tax")
        dropdown.find_element(By.XPATH, "//option[. = 'Tax included']").click()
        # 25 | click | id=product_restriction |
        self.driver.find_element(By.ID, "product_restriction").click()
        # 26 | click | linkText=Product selection |
        self.driver.find_element(By.LINK_TEXT, "Product selection").click()
        # 27 | click | id=product_rule_type_1 |
        self.driver.find_element(By.ID, "product_rule_type_1").click()
        # 28 | select | id=product_rule_type_1 | label=Categories
        dropdown = self.driver.find_element(By.ID, "product_rule_type_1")
        dropdown.find_element(By.XPATH, "//option[. = 'Categories']").click()
        # 29 | click | linkText=Add |
        self.driver.find_element(By.LINK_TEXT, "Add").click()
        # 30 | click | id=product_rule_1_1_choose_link |
        self.driver.find_element(By.ID, "product_rule_1_1_choose_link").click()
        # 31 | mouseOver | id=product_rule_1_1_choose_link |
        element = self.driver.find_element(By.ID, "product_rule_1_1_choose_link")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 32 | mouseOut | id=product_rule_1_1_choose_link |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, 0, 0).perform()
        # 33 | runScript | window.scrollTo(0,0) |
        self.driver.execute_script("window.scrollTo(0,0)")
        # 34 | addSelection | id=product_rule_select_1_1_1 | label=regexp:\sGames
        dropdown = self.driver.find_element(By.ID, "product_rule_select_1_1_1")
        self.driver.implicitly_wait(2)
        dropdown.find_element(By.XPATH, "//option[@value='10']").click()
        # 35 | click | id=product_rule_select_1_1_add |
        self.driver.find_element(By.ID, "product_rule_select_1_1_add").click()
        # 36 | click | css=.fancybox-item |
        self.driver.find_element(By.CSS_SELECTOR, ".fancybox-item").click()
        # 37 | mouseOver | id=cart_rule_link_actions |
        element = self.driver.find_element(By.ID, "cart_rule_link_actions")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 38 | click | id=cart_rule_link_actions |
        element = self.driver.find_element(By.ID, "cart_rule_link_actions")
        self.driver.execute_script("arguments[0].click();", element)
        # WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.ID, "cart_rule_link_actions"))
        # self.driver.find_element(By.ID, "cart_rule_link_actions").click()
        # 39 | click | id=apply_discount_amount |
        self.driver.find_element(By.ID, "apply_discount_amount").click()
        # 40 | click | id=reduction_amount |
        self.driver.find_element(By.ID, "reduction_amount").click()
        self.driver.find_element(By.ID, "reduction_amount").clear()
        # 41 | type | id=reduction_amount | 25
        self.driver.find_element(By.ID, "reduction_amount").send_keys(reduction_amount)
        # 42 | click | name=reduction_tax |
        self.driver.find_element(By.NAME, "reduction_tax").click()
        # 43 | select | name=reduction_tax | label=Tax included
        dropdown = self.driver.find_element(By.NAME, "reduction_tax")
        self.driver.implicitly_wait(1)
        # 44 | click | css=#desc-cart_rule-save > span |
        self.driver.find_element(By.CSS_SELECTOR, "#desc-cart_rule-save > span").click()

        # 45 | click | css=#header_shopname > span |
        self.vars["window_handles"] = self.driver.window_handles
        # 46 | selectWindow | handle=${win5744} |
        self.driver.find_element(By.CSS_SELECTOR, "#header_shopname > span").click()
        # 47 | click | css=a > .hidden-sm-down |
        self.vars["win5744"] = self.wait_for_window(2000)
        # 48 | click | id=field-email |
        self.driver.switch_to.window(self.vars["win5744"])
        # 49 | type | id=field-email | user@example.com
        self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
        # 50 | click | id=field-password |
        self.driver.find_element(By.ID, "field-email").click()
        # 51 | type | id=field-password | 123456789
        self.driver.find_element(By.ID, "field-email").send_keys("user@example.com")
        # 52 | click | id=submit-login |
        self.driver.find_element(By.ID, "field-password").click()
        # 53 | click | name=s |
        self.driver.find_element(By.ID, "field-password").send_keys("123456789")
        # 54 | type | name=s | suburbia
        self.driver.find_element(By.ID, "submit-login").click()
        # 55 | sendKeys | name=s | ${KEY_ENTER}
        self.driver.find_element(By.NAME, "s").click()
        # 56 | click | css=.thumbnail > img |
        self.driver.find_element(By.NAME, "s").send_keys("suburbia")
        # 57 | click | css=.add-to-cart |
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        # 58 | click | css=.cart-content-btn > .btn-secondary |
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        # 59 | click | name=s |
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        # 60 | type | name=s | twilight
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        # 61 | sendKeys | name=s | ${KEY_ENTER}
        self.driver.find_element(By.NAME, "s").click()
        # 62 | click | css=.thumbnail > img |
        self.driver.find_element(By.NAME, "s").send_keys("twilight")
        # 63 | click | css=.add-to-cart |
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        # 64 | click | css=.cart-content-btn > .btn-secondary |
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        # 65 | click | name=s |
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        # 66 | click | css=#ui-id-2 > .product |
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        # 67 | click | css=.add-to-cart |
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("wall")
        # 68 | click | css=.cart-content-btn > .btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, "#ui-id-2 > .product").click()
        # 69 | click | linkText=Have a promo code? |
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        # 70 | click | name=discount_name |
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()
        # 71 | type | name=discount_name | 135TG135
        self.driver.find_element(By.LINK_TEXT, "Have a promo code?").click()
        # 72 | click | css=.btn > span |
        self.driver.find_element(By.NAME, "discount_name").click()
        # 76 | click | css=#subtab-AdminCatalog > .link |
        self.driver.find_element(By.NAME, "discount_name").send_keys(code)
        # 77 | click | linkText=Discounts |
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        assert discount_name in self.driver.find_element(By.XPATH,
                                                         '//ul//span[@class="label"]').text
        assert reduction_amount in self.driver.find_element(By.XPATH,
                                                            '//li/div[@class="float-xs-right"]').text
        before_discount = self.driver.find_element(By.XPATH, '//*[@id="cart-subtotal-products"]/span[2]').text
        after_discount = self.driver.find_element(By.XPATH,
                                                  '//*[@class="card-block cart-summary-totals js-cart-summary-totals"]/div[1]/span[2]').text
        assert before_discount != after_discount


if __name__ == '__main__':
    pytest.main()
