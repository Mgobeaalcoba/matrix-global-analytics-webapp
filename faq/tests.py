from django.test import TestCase, Client
from django.template.loader import render_to_string
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
        self.assertEqual(faq_item.__str__(), '¿Pregunta de prueba?')

class TestFAQTemplate(TestCase):
    def setUp(self):
        # Crea algunos items de FAQ de ejemplo
        self.faq_item1 = FAQ.objects.create(
            question="Pregunta 1",
            answer="Respuesta 1"
        )
        self.faq_item2 = FAQ.objects.create(
            question="Pregunta 2",
            answer="Respuesta 2"
        )

    def test_faq_template(self):
        # Renderiza el template con los items de FAQ
        rendered_template = render_to_string('faq/preguntas_frecuentes.html', {'faq_items': [self.faq_item1, self.faq_item2]})

        # Verifica que el contenido esperado esté presente en el template renderizado
        self.assertInHTML('<h2>Pregunta 1</h2>', rendered_template)
        self.assertInHTML('<li>Respuesta 1</li>', rendered_template)
        self.assertInHTML('<h2>Pregunta 2</h2>', rendered_template)
        self.assertInHTML('<li>Respuesta 2</li>', rendered_template)
