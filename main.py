import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Auntminnietest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get('https://www.auntminnie.com/')

    def tearDown(self):
        print(f'Title: {self.driver.title}')

    # testing case
    def test_Title(self):
        print(f'Title of the main page: {self.driver.title}')
        assert self.driver.title == 'AuntMinnie.com - Radiology News and Education'

    def test_Search(self):
        self.driver.find_element(By.CSS_SELECTOR, '#nav-search-btn').send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, '#txtSearch').send_keys('ct scan', Keys.ENTER)
        assert self.driver.title == 'Radiology, Search'

    def test_advanceSearch(self):
        self.test_Search()
        btn = Select(self.driver.find_element(By.ID, 'selectSearchChoice'))
        btn.select_by_visible_text('Any word in the phrase')
        self.driver.find_element(By.ID, 'btnSearchAdvancedTop').click()
        title = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[1]/div[2]/div[3]/h4')))
        assert title.text == 'Articles'

    # you can use @unittest.SkipTest if you dont have comment for skipping test
    # or you can use @unittest.skipIf(conditional) if you have conditional to run the testcase
    @unittest.skip('I am skip this test because i have not filled in username and password')
    def test_Login(self):
        self.driver.find_element(By.ID, 'nav-gear-btn').click()
        self.driver.find_element(By.CLASS_NAME, 'UserInfoPartName').find_element(By.NAME, 'Sign in').click()
        self.driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_pnlOutputText_Area2_ctl00_Login1_txtCN"]').send_keys('')
        self.driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_pnlOutputText_Area2_ctl00_Login1_txtPassword"]').send_keys('')
        self.driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_pnlOutputText_Area2_ctl00_Login1_cmdSignIn"]').click()
        assert not self.driver.find_element(By.CLASS_NAME, 'textredsmall')


if __name__ == '__main__':
    unittest.main()
