from django.test import TestCase, Client
from django.urls import reverse
from .models import FAQ

class FAQModelTest(TestCase):
    def test_create_faq(self):
        # Crea un objeto FAQ
        faq = FAQ.objects.create(
            question="Test Question",
            answer="Test Answer"
        )

        # Verifica que el objeto FAQ se haya guardado correctamente en la base de datos
        self.assertEqual(FAQ.objects.count(), 1)
        self.assertEqual(faq.question, "Test Question")
        self.assertEqual(faq.answer, "Test Answer")

class FAQViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_faq_view(self):
        # Crear FAQ de prueba
        FAQ.objects.create(
            question="¿Pregunta de prueba?",
            answer="Respuesta de prueba"
        )

        # Obtener la URL para la vista FAQ
        url = reverse('preguntas_frecuentes')

        # Realizar una solicitud GET a la vista FAQ
        response = self.client.get(url)

        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)

        # Verificar que el template correcto esté siendo utilizado
        self.assertTemplateUsed(response, 'faq/preguntas_frecuentes.html')

        # Verificar que el FAQ creado esté presente en el contexto de la vista
        faq_items = response.context['faq_items']
        self.assertEqual(len(faq_items), 1)
        faq_item = faq_items[0]
        self.assertEqual(faq_item.question, "¿Pregunta de prueba?")
        self.assertEqual(faq_item.answer, "Respuesta de prueba")
