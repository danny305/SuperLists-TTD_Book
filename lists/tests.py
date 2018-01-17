from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string


from lists.views import home_page
from lists.models import Item



# Create your tests here.


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):

        #The proceeding two lines test our implementation and not constants
        response = self.client.get('/')                         #Utilizing django Test Client tool (built in way to check template used
        self.assertTemplateUsed(response,'home.html')          # This test method ONLY works on responses retrieved by the test client

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')


        # response = self.client.post('/', data={'item_text': 'A new list item'})
        # self.assertEqual(Item.objects.count(),1)
        # new_item = Item.objects.first()
        # self.assertEqual(new_item.text, 'A new list item')
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response['location'], '/')



        # self.assertIn('A new list item', response.content.decode())
        # self.assertTemplateUsed(response, 'home.html')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data = {'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')








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


    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(),0)


    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')











#12-30-17 2:20 pm
# This was a practice example while leading up to the HomePageTest code.
# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)




if __name__=='__main__':
    print (HomePageTest().test_home_page_returns_correct_html())