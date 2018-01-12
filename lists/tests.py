from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string


from lists.views import home_page



# Create your tests here.


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):

        #The proceeding two lines test our implementation and not constants
        response = self.client.get('/')                         #Utilizing django Test Client tool (built in way to check template used
        self.assertTemplateUsed(response,'home.html')          # This test method ONLY works on responses retrieved by the test client

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')




        # html = response.content.decode('utf8')                  #We can delete this and all the 3 proceeding tests bc the
        # self.assertTrue(html.startswith('<!DOCTYPE html>'))     #assertTemplateUsed test confirms if we are using the right template
        # self.assertIn('<title>To-Do lists</title>',html)
        # self.assertTrue(html.strip().endswith('</html>'))




        # request = HttpRequest()
        # response = home_page(request)
        # html = response.content.decode('utf8')
        # expected_html = render_to_string('home.html')   #12-30-17 8:25 pm    new way to manually render the template
        # self.assertEqual(html,expected_html)            #ourselves in the testand then compare that to what the view returns.
                                                        #(Use django's functionrender_to_string that allows us to do this




        # print(repr(html))                      #checking to see why the startswith(<html>) did not work turn out its <!DOCTYPE html>.
        # self.assertTrue(html.startswith('<!DOCTYPE html>'))
        # self.assertIn('<title>To-Do lists</title>',html)
        # self.assertTrue(html.strip().endswith('</html>'))




        # def test_root_url_resolves_to_home_page_view(self):       #Was the first test written but got supplanted by the
        #     found = resolve('/')                                  #test_home_page_returns_correct_html func bc the
        #     self.assertEqual(found.func,home_page)                #Test Client implicitly tests for the resolve of the root url


#12-30-17 2:20 pm
# This was a practice example while leading up to the HomePageTest code.
# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)




if __name__=='__main__':
    print (HomePageTest().test_home_page_returns_correct_html())