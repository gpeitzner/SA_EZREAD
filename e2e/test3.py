import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class test3(unittest.TestCase):

    def setUp(self):
        HUB_URL = "localhost"
        HOST_URL = "192.168.1.100"
        self.driver = webdriver.Remote(
            command_executor="http://"+HUB_URL+":4444/wd/hub", desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.get("http://"+HOST_URL+":8080/register")
        time.sleep(5)

    def test3(self):
        publisher_area = self.driver.find_element_by_xpath(
            "//input[@value='publisher']")
        publisher_area.click()
        name_input = self.driver.find_element_by_id("nombre")
        name_input.send_keys("Editorial Vita")
        address_input = self.driver.find_element_by_id("direccion")
        address_input.send_keys("15 Calle B 23-32 Zona 10 de Guatemala, Guatemala")
        email_input = self.driver.find_element_by_id("correo")
        email_input.send_keys("editorialvita@gmail.com")
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
