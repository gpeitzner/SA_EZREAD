import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


class test6(unittest.TestCase):

    def setUp(self):
        HUB_URL = "test.ezread.ml"
        HOST_URL = "test.ezread.ml"
        self.driver = webdriver.Remote(
            command_executor="http://"+HUB_URL+":4444/wd/hub", desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.get("http://"+HOST_URL+":8000/login")
        time.sleep(5)

    def test6(self):
        email_input = self.driver.find_element_by_id("email")
        email_input.send_keys("admin@ezread.ml")
        password_input = self.driver.find_element_by_id("password")
        password_input.send_keys("1234")
        login_button = self.driver.find_element_by_class_name(
            "MuiButton-label")
        login_button.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
