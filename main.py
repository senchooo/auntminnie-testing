import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Auntminnietest(unittest.TestCase):
    def test_Title(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.auntminnie.com/')
        print(f'Title of the main page: {driver.title}')
        assert driver.title == 'AuntMinnie.com - Radiology News and Education'

    def test_Casetitle(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.auntminnie.com/')
        driver.find_element(By.XPATH, '//*[@id="nav"]/div[1]/ul/li[3]/a').click()
        print(f'Title of the cases page: {driver.title}')
        assert driver.title == 'Radiology Education, Case Study'

    def test_Jobstitle(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.auntminnie.com/')
        driver.find_element(By.XPATH, '//*[@id="nav"]/div[1]/ul/li[9]/a').click()
        print(f'Title of the jobs page: {driver.title}')
        assert driver.title == 'Radiology Jobs'


if __name__ == '__main__':
    unittest.main()
