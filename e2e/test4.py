import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


class test4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub", desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.get("http://192.168.1.100:8080/login")
        time.sleep(5)

    def test_correct_authentication(self):
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
