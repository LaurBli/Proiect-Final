import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.testSuite
@pytest.mark.order
class TestOrderStatus():
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

    def test_orderStatus(self):
        self.driver.get("http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "passwd").click()
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        self.driver.find_element(By.CSS_SELECTOR, ".ladda-label").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, "#subtab-AdminParentOrders > .link"))
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminParentOrders > .link").click()
        self.driver.find_element(By.LINK_TEXT, "Orders").click()
        self.driver.find_element(By.ID, "order_reference").click()
        self.driver.find_element(By.ID, "order_reference").clear()
        self.driver.find_element(By.ID, "order_reference").send_keys("KVIZLDDCT")
        self.driver.find_element(By.NAME, "order[actions][search]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
        order_status = self.driver.find_element(By.XPATH, '//*[@id="order_grid_table"]//button[9]').text
        self.driver.find_element(By.CSS_SELECTOR, ".js-dropdown-item:nth-child(9)").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, "#header_shopname > span").click()
        self.vars["win7818"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win7818"])
        self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
        self.driver.find_element(By.ID, "field-email").click()
        self.driver.find_element(By.ID, "field-email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "field-password").click()
        self.driver.find_element(By.ID, "field-password").send_keys("123456789")
        self.driver.find_element(By.ID, "submit-login").click()
        self.driver.find_element(By.CSS_SELECTOR, "#history-link > .link-item").click()
        assert order_status in self.driver.find_element(By.ID, 'content').text
        self.driver.get("http://34.118.122.203/administration/index.php?controller=AdminLogin&token=1e53b83c6f3b96a3ca75976d5bab155e")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("user@example.com")
        self.driver.find_element(By.ID, "passwd").click()
        self.driver.find_element(By.ID, "passwd").send_keys("VTR6WmtBCvnZ")
        self.driver.find_element(By.CSS_SELECTOR, ".ladda-label").click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, "#subtab-AdminParentOrders > .link"))
        self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminParentOrders > .link").click()
        self.driver.find_element(By.LINK_TEXT, "Orders").click()
        self.driver.find_element(By.ID, "order_reference").click()
        self.driver.find_element(By.NAME, "order[actions][search]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
        order_status = self.driver.find_element(By.XPATH, '//*[@id="order_grid_table"]//button[9]').text
        self.driver.find_element(By.CSS_SELECTOR, ".js-dropdown-item:nth-child(9)").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, "#header_shopname > span").click()
        self.vars["win2750"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win2750"])
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.XPATH, '//*[@id="_desktop_user_info"]/div/a[2]'))
        self.driver.find_element(By.XPATH, '//*[@id="_desktop_user_info"]/div/a[2]').click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.CSS_SELECTOR, "#history-link .material-icons"))
        self.driver.find_element(By.CSS_SELECTOR, "#history-link .material-icons").click()
        assert order_status in self.driver.find_element(By.ID, 'content').text


if __name__ == '__main__':
    pytest.main()
