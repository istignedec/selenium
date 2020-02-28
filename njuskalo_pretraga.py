import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PretragaNjuskalo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_pretrazi_njuskalo_hr(self):
        driver = self.driver
        driver.get("http://www.njuskalo.hr")
        self.assertIn("Njuskalo", driver.title)
        elem = driver.find_element_by_id("keywords")
        elem.send_keys("antensko pojačalo")
        elem.send_keys(Keys.RETURN)
        assert "Trenutno nema oglasa koji zadovoljavaju postavljene kriterije pretrage." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
