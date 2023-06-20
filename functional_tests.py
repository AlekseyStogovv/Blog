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
        self.assertIn('Сайт Алексея Стогова', self.browser.title)


    def test_home_page_header(self):
        # В шапке сайта написано "Алексей .."
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Алексей Стогов', header.text)


    def test_home_page_blog(self):
        # под шапкой расположен блог со статьями.
        self.browser.get('http://127.0.0.1:8000')
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)


    def test_home_page_articles_look_correct(self):
        #У каждой статьи есть заголовок и один абзац с текстом
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(
            By.CLASS_NAME,
            'article-title')
        article_summary = self.browser.find_element(
            By.CLASS_NAME,'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)




if __name__ == '__main__':
    unittest.main()




