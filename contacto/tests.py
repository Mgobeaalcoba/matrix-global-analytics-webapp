from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from .models import Email

class TestEmailModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configurar datos de prueba una vez al inicio de la clase
        cls.email = Email.objects.create(
            nombre='John',
            apellido='Doe',
            telefono='123456789',
            email='john@example.com',
            asunto='Consulta',
            consulta='Esto es una consulta de ejemplo.'
        )

    def test_email_instance_creation(self):
        # Verificar si la instancia de Email se creó correctamente
        self.assertIsInstance(self.email, Email)

    def test_email_str_representation(self):
        # Verificar la representación de cadena de Email
        expected_str = 'John Doe'
        self.assertEqual(str(self.email), expected_str)

class TestContactoViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('formulario_contacto')
        self.valid_data = {
            'nombre': 'John',
            'apellido': 'Doe',
            'email': 'john@example.com',
            'telefono': '123456789',
            'asunto': 'Consulta de prueba',
            'consulta': 'Esto es una consulta de prueba.'
        }

    def test_formulario_contacto_post(self):
        # Enviar una solicitud POST con datos válidos
        response = self.client.post(self.url, self.valid_data)

        # Verificar si se creó correctamente un objeto Email en la base de datos
        self.assertEqual(Email.objects.count(), 1)

        # Verificar si se redirige correctamente después de enviar el formulario
        self.assertEqual(response.status_code, 200)

        # Verificar si el mensaje de respuesta es el esperado
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'message': 'Gracias por comunicarte con MGA. A la brevedad nos pondremos en contacto contigo.'}
        )

        # Verificar si se envió el correo electrónico correctamente
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Consulta de prueba')
        self.assertEqual(mail.outbox[0].body, f"""
        Nombre: John
        Apellido: Doe
        Email: john@example.com
        Teléfono: 123456789
        Asunto: Consulta de prueba
        Consulta: Esto es una consulta de prueba.
        """)

    def test_formulario_contacto_get(self):
        # Enviar una solicitud GET al formulario de contacto
        response = self.client.get(self.url)

        # Verificar si se devuelve el código de estado HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar si se está utilizando la plantilla correcta
        self.assertTemplateUsed(response, 'contacto/formulario_contacto.html')

class TestContactoHTML(TestCase):
    def setUp(self):
        self.url = reverse('formulario_contacto')

    def test_contacto_html(self):
        # Enviar una solicitud GET al formulario de contacto
        response = self.client.get(self.url)

        # Verificar si se devuelve el código de estado HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar si se utiliza la plantilla correcta
        self.assertTemplateUsed(response, 'contacto/formulario_contacto.html')

        # Verificar la existencia de elementos HTML en el contenido de la respuesta
        self.assertContains(response, '<title>Contacto</title>')
        self.assertContains(response, '<form action="#" method="post">')
        self.assertContains(response, '<label for="nombre">Nombre:</label>')
        self.assertContains(response, '<label for="apellido">Apellido:</label>')
        self.assertContains(response, '<label for="email">Email:</label>')
        self.assertContains(response, '<label for="telefono">Teléfono:</label>')
        self.assertContains(response, '<label for="asunto">Asunto:</label>')
        self.assertContains(response, '<label for="consulta">Consulta:</label>')
        self.assertContains(response, '<button type="submit" class="btn btn-primary">Enviar Consulta</button>')
        self.assertContains(response, '<a href="/" class="btn btn-secondary btn-volver">Volver</a>')
