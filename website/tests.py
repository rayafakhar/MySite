from django.test import TestCase

from django.urls import reverse

class PageRoutingTests(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('website:index'))
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get(reverse('website:about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get(reverse('website:contact'))
        self.assertEqual(response.status_code, 200)

    def test_elements_page(self):
        response = self.client.get(reverse('website:elements'))
        self.assertEqual(response.status_code, 200)

    def test_blog_home_page(self):
        response = self.client.get(reverse('website:blog_home'))
        self.assertEqual(response.status_code, 200)

    def test_blog_single_page(self):
        response = self.client.get(reverse('website:blog_single'))
        self.assertEqual(response.status_code, 200)

