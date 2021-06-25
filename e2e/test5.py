import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


class test5(unittest.TestCase):

    def setUp(self):
        HUB_URL = "test.ezread.ml"
        HOST_URL = "test.ezread.ml"
        self.driver = webdriver.Remote(
            command_executor="http://"+HUB_URL+":4444/wd/hub", desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.get("http://"+HOST_URL+":8080/register")
        time.sleep(5)

    def test5(self):
        publisher_area = self.driver.find_element_by_xpath(
            "//input[@value='publisher']")
        publisher_area.click()
        name_input = self.driver.find_element_by_id("nombre")
        name_input.send_keys("Editorial Vita")
        address_input = self.driver.find_element_by_id("direccion")
        address_input.send_keys(
            "15 Calle B 23-32 Zona 10 de Guatemala, Guatemala")
        email_input = self.driver.find_element_by_id("correo")
        email_input.send_keys("editorialvita@gmail.com")
        signup_button = self.driver.find_element_by_class_name(
            "MuiButton-label")
        signup_button.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
