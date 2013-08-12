"""
Run these tests with 'manage.py test'.
"""

from django.test import TestCase
from django.utils import unittest 
import views
import random
import string

class XmlApiTest(unittest.TestCase):

    def test_get_files(self):
        file_list = views.get_files()
        self.assertTrue(len(file_list) > 0)

    def test_get_file_data(self):
        file_list = views.get_files()
        xml_data = views.get_file_data (file_list[0])
        self.assertTrue(len(xml_data.a) > 0)


class ViewTest(TestCase):
   random_file_name = ''.join(random.choice(string.ascii_letters) for x in range(20))
   
   def test_0_list(self):
       response = self.client.get('/')
       self.assertContains(response, '1.xml')
       self.assertNotContains(response, self.random_file_name)

   def test_1_create(self):
       params = {'file_name':self.random_file_name, 'a':'aaa'}
       response = self.client.post('/create', params)  
       self.assertRedirects(response, '/list')
       self.assertContains(response, self.random_file_name)

   def test_2_read(self):
       response = self.client.get('/show/' + self.random_file_name)
       self.assertContains(response, self.random_file_name)
       self.assertContains(response, 'aaa')

   def test_3_update(self):
       params = {'a': 'AAAA'}
       response = self.client.post('/update/' + self.random_file_name, params)  
       self.assertRedirects(response, '/list')
       response = self.client.get('/show/' + self.random_file_name)
       self.assertContains(response, self.random_file_name)
       self.assertContains(response, 'AAAA')

   def test_3_delete(self):
       response = self.client.get('/delete/' + self.random_file_name)  
       self.assertRedirects(response, '/list')
       self.assertContains(response, '1.xml')
       self.assertNotContains(response, self.random_file_name)

