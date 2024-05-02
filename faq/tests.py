from django.test import TestCase
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

