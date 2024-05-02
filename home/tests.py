from django.test import TestCase
from django.urls import reverse
from bs4 import BeautifulSoup
from django.template.loader import render_to_string

class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class HomeTemplateTest(TestCase):
    def test_home_template(self):
        expected_html = render_to_string('home.html')
        soup = BeautifulSoup(expected_html, 'html.parser')
        self.assertEqual(soup.title.string, 'MGA Home')  # Suponiendo que 'home.html' tiene un título
