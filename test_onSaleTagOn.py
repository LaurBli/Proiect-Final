import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.testSuite
@pytest.mark.discount
class TestOnSaleTagOn():
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

    def test_onSaleTagOn(self):
        self.driver.get("http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "passwd").click()
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        self.driver.find_element(By.CSS_SELECTOR, ".ladda-label").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog span"))
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog span").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.LINK_TEXT, "Products"))
        self.driver.find_element(By.LINK_TEXT, "Products").click()
        self.driver.find_element(By.NAME, "filter_column_name").click()
        self.driver.find_element(By.NAME, "filter_column_name").clear()
        self.driver.find_element(By.NAME, "filter_column_name").send_keys('suburbia')
        self.driver.find_element(By.NAME, "products_filter_submit").click()
        self.driver.find_element(By.LINK_TEXT, "Suburbia: Collector\'s Edition").click()
        self.driver.find_element(By.LINK_TEXT, "Pricing").click()
        self.driver.find_element(By.ID, "form_step2_on_sale").click()
        element = self.driver.find_element(By.ID, "submit")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "submit").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#tab-AdminDashboard > .link").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#tab-AdminDashboard > .link")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, "#header_shopname > span").click()
        self.vars["win2688"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win2688"])
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("suburbia")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        assert 'on sale!' in self.driver.find_element(By.ID, 'js-product-list').text.lower()
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        assert 'on sale!' in self.driver.find_element(By.ID, 'content').text.lower()
        self.driver.get("http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "passwd").click()
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        self.driver.find_element(By.ID, "submit_login").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link"))
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.LINK_TEXT, "Products"))
        self.driver.find_element(By.LINK_TEXT, "Products").click()
        self.driver.find_element(By.NAME, "filter_column_name").click()
        self.driver.find_element(By.NAME, "filter_column_name").clear()
        self.driver.find_element(By.NAME, "filter_column_name").send_keys('suburbia')
        self.driver.find_element(By.NAME, "products_filter_submit").click()
        self.driver.find_element(By.LINK_TEXT, "Suburbia: Collector\'s Edition").click()
        self.driver.find_element(By.LINK_TEXT, "Pricing").click()
        self.driver.find_element(By.ID, "form_step2_on_sale").click()
        element = self.driver.find_element(By.ID, "submit")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "submit").click()
