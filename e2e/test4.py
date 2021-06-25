import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


class test4(unittest.TestCase):

    def setUp(self):
        HUB_URL = "test.ezread.ml"
        HOST_URL = "test.ezread.ml"
        self.driver = webdriver.Remote(
            command_executor="http://"+HUB_URL+":4444/wd/hub", desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.get("http://"+HOST_URL+":8000/register")
        time.sleep(5)

    def test4(self):
        first_name_input = self.driver.find_element_by_id("nombre")
        first_name_input.send_keys("Juan")
        last_name_input = self.driver.find_element_by_id("apellido")
        last_name_input.send_keys("Perez")
        phone_input = self.driver.find_element_by_id("telefono")
        phone_input.send_keys("12345678")
        email_input = self.driver.find_element_by_id("correo")
        email_input.send_keys("juanperez@gmail.com")
        signup_button = self.driver.find_element_by_class_name(
            "MuiButton-label")
        signup_button.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
