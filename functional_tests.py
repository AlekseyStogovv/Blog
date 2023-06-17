from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class BasicInstallTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        #В браузере открылся сайт по адресу .. в заголовке "Сайт .."
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Алексей Стогов', self.browser.title)


    def test_home_page_header(self):
        # В шапке сайта написано "Алексей .."
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Сайт Алексея Стогова', header.text)



if __name__ == '__main__':
    unittest.main()




