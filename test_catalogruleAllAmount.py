import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.testSuite
@pytest.mark.discount
class TestCatalogruleAllAmount():
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

    def test_catalogruleAllAmount(self):
        discount = '3.00'
        self.driver.get("http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e")
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
        actions.move_to_element_with_offset(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.LINK_TEXT, "Discounts"))
        self.driver.find_element(By.LINK_TEXT, "Discounts").click()
        self.driver.find_element(By.ID, "subtab-AdminSpecificPriceRule").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-toolbar").click()
        self.driver.find_element(By.CSS_SELECTOR, "#page-header-desc-specific_price_rule-new_specific_price_rule > div").click()
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("All3")
        self.driver.find_element(By.ID, "reduction").click()
        self.driver.find_element(By.ID, "reduction").clear()
        self.driver.find_element(By.ID, "reduction").send_keys(discount)
        self.driver.find_element(By.ID, "specific_price_rule_form_submit_btn").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, "#header_shopname > span").click()
        self.vars["win5197"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win5197"])
        self.driver.find_element(By.CSS_SELECTOR, "#category-16 > .dropdown-item").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(1) img").click()
        discount_flag = self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li').text
        discount_amount = self.driver.find_element(By.XPATH, '//span[@class="discount discount-amount"]').text
        current_price = self.driver.find_element(By.CLASS_NAME, 'current-price-value').text
        regular_price = self.driver.find_element(By.XPATH, '//div[@class="product-discount"]/span').text
        assert discount in discount_flag
        assert discount in discount_amount
        assert float(regular_price.replace('$', '')) - float(discount) == float(current_price.replace('$', ''))
        self.driver.find_element(By.CSS_SELECTOR, "#category-16 > .dropdown-item").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(2) img").click()
        assert discount in discount_flag
        assert discount in discount_amount
        assert float(regular_price.replace('$', '')) - float(discount) == float(current_price.replace('$', ''))
        self.driver.find_element(By.CSS_SELECTOR, "#category-16 > .dropdown-item").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(3) img").click()
        assert discount in discount_flag
        assert discount in discount_amount
        assert float(regular_price.replace('$', '')) - float(discount) == float(current_price.replace('$', ''))
        self.driver.find_element(By.CSS_SELECTOR, "#category-16 > .dropdown-item").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(4) img").click()
        assert discount in discount_flag
        assert discount in discount_amount
        assert float(regular_price.replace('$', '')) - float(discount) == float(current_price.replace('$', ''))
        self.driver.get("http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e")
        # 32 | click | id=passwd |
        self.driver.find_element(By.ID, "email").click()
        # 33 | type | id=passwd | VTR6WmtBCvnZ
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        # 34 | click | id=submit_login |
        self.driver.find_element(By.ID, "passwd").click()
        # 35 | click | css=#subtab-AdminCatalog > .link |
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        # 36 | click | linkText=Discounts |
        self.driver.find_element(By.ID, "submit_login").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link"))
        # 37 | click | id=subtab-AdminSpecificPriceRule |
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.LINK_TEXT, "Discounts"))
        # 38 | click | css=.icon-caret-down |
        self.driver.find_element(By.LINK_TEXT, "Discounts").click()
        # 39 | click | linkText=Delete |
        self.driver.find_element(By.ID, "subtab-AdminSpecificPriceRule").click()
        # 40 | mouseOver | linkText=Delete |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-default:nth-child(2)").click()
        # 47 | click | css=#header_shopname > span |
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        # 48 | selectWindow | handle=${win1665} |
        self.driver.find_element(By.ID, "popup_ok").click()
