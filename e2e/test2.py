import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class test2(unittest.TestCase):

    def setUp(self):
        HUB_URL = "test.ezread.ml"
        HOST_URL = "test.ezread.ml"
        self.driver = webdriver.Remote(
            command_executor="http://"+HUB_URL+":4444/wd/hub", desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.get("http://"+HOST_URL+":8000/register")
        time.sleep(5)

    def test2(self):
        first_name_input = self.driver.find_element_by_id("nombre")
        first_name_input.send_keys("Juan")
        last_name_input = self.driver.find_element_by_id("apellido")
        last_name_input.send_keys("Perez")
        phone_input = self.driver.find_element_by_id("telefono")
        phone_input.send_keys("12345678")
        email_input = self.driver.find_element_by_id("correo")
        email_input.send_keys("juanperez@gmail.com")
        password_input = self.driver.find_element_by_id("password")
        password_input.send_keys("1234")
        signup_button = self.driver.find_element_by_class_name(
            "MuiButton-label")
        signup_button.click()
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
