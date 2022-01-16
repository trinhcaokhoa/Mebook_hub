from django.test import TestCase
from django.urls import reverse


def homepage_status(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

def homepage_url_name(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)

def homepage_template(self):  
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'homepages.html')
