from selenium import webdriver
import time
import sys
import unittest
sys.path.insert(1, '/home/istignedec/Github/selenium/project2/pages')
from loginPage import LoginPage
from homePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls): # setUpClass methods runs only once, setUp runs before/after every method
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_01_login_ok(self):
        
        driver = self.driver
        
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        time.sleep(2)

        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()

    def test_02_login_failed(self):
        
        driver = self.driver
        
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login = LoginPage(driver)
        login.enter_username("Admin1") # invalid username
        login.enter_password("admin123")
        login.click_login()
        msg = login.check_invalid_username()
        self.assertEqual(msg, "Invalid credentials")

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/istignedec/Github/selenium/project2/reports'))
    
