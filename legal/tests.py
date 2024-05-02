from django.test import TestCase
from django.urls import reverse

class LegalViewsTestCase(TestCase):
    def test_terminos_de_uso_view(self):
        response = self.client.get(reverse('terminos_de_uso'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'legal/terminos_de_uso.html')

    def test_politica_de_privacidad_view(self):
        response = self.client.get(reverse('politica_de_privacidad'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'legal/politica_de_privacidad.html')
