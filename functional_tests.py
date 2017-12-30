from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new online to-do app. She goes to
        #check out its homepage
        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists
        self.assertIn('Django', self.browser.title)
        self.fail('I made it fail. Finish the test!')

        #She is invitedto enter a to-do item straight away


if __name__== '__main__':
    help(unittest.TestCase.fail)
    unittest.main(warnings='ignore')



try:
    browser = webdriver.Firefox()
    response = browser.get('http://localhost:8000')
    assert 'Django' in browser.title, 'Browser title was: {}'.format(browser.title)
    print('Congrats a Django web app opened on FireFox!!')

except:
    print('Django website did not open')

finally:
    browser.quit()

