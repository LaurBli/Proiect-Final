import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.testSuite
@pytest.mark.discount
class TestCatalogRuleCondition():
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

    def test_CatalogRuleCondition(self):
        discount_percentage = '15'
        self.driver.get(
            "http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e&redirect=AdminDashboard")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "passwd").click()
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        self.driver.find_element(By.CSS_SELECTOR, ".ladda-label").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
        self.driver.find_element(By.LINK_TEXT, "Discounts").click()
        self.driver.find_element(By.ID, "subtab-AdminSpecificPriceRule").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#page-header-desc-specific_price_rule-new_specific_price_rule > div").click()
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("Games15")
        self.driver.find_element(By.ID, "from").click()
        self.driver.find_element(By.LINK_TEXT, "1").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-current").click()
        # # 16 | click | css=.form-wrapper |
        # self.driver.find_element(By.CSS_SELECTOR, ".form-wrapper").click()
        # 17 | click | id=to |
        self.driver.find_element(By.ID, "to").click()
        self.driver.find_element(By.LINK_TEXT, "30").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(10) > .col-lg-8").click()
        self.driver.find_element(By.ID, "reduction_type").click()
        dropdown = self.driver.find_element(By.ID, "reduction_type")
        dropdown.find_element(By.XPATH, "//option[. = 'Percentage']").click()
        self.driver.find_element(By.ID, "reduction_tax").click()
        dropdown = self.driver.find_element(By.ID, "reduction_tax")
        dropdown.find_element(By.XPATH, "//option[. = 'Tax included']").click()
        self.driver.find_element(By.ID, "reduction").click()
        self.driver.find_element(By.ID, "reduction").clear()
        self.driver.find_element(By.ID, "reduction").send_keys(discount_percentage)
        self.driver.find_element(By.ID, "add_condition_group").click()
        element = self.driver.find_element(By.ID, "add_condition_group")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset((element), 0, 0).perform()
        self.driver.find_element(By.ID, "id_category").click()
        dropdown = self.driver.find_element(By.ID, "id_category")
        dropdown.find_element(By.XPATH, "//option[. = '(10) Games']").click()
        self.driver.find_element(By.ID, "add_condition_category").click()
        element = self.driver.find_element(By.ID, "add_condition_category")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset((element), 0, 0).perform()
        self.driver.find_element(By.ID, "specific_price_rule_form_submit_btn").click()
        self.driver.get("http://34.118.122.203")
        # 39 | sendKeys | name=s | ${KEY_ENTER}
        self.driver.find_element(By.NAME, "s").click()
        # 40 | click | css=.thumbnail > img |
        self.driver.find_element(By.NAME, "s").send_keys("suburbia")
        # 41 | click | css=#subtab-AdminCatalog > .link |
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        # 42 | click | linkText=Discounts |
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        assert f'SAVE {discount_percentage}%' in self.driver.find_element(By.XPATH,
                                                                          '//span[@class="discount discount-percentage"]').text
        regular_price = self.driver.find_element(By.CLASS_NAME, "regular-price").text
        reduced_price = self.driver.find_element(By.CLASS_NAME, "current-price-value").text
        assert regular_price != reduced_price
        self.driver.get("http://34.118.122.203/administration")
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
        self.driver.find_element(By.LINK_TEXT, "Discounts").click()
        self.driver.find_element(By.ID, "subtab-AdminSpecificPriceRule").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-default:nth-child(2)").click()
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        self.driver.find_element(By.ID, "popup_ok").click()


if __name__ == '__main__':
    pytest.main()
