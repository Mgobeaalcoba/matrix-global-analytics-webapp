from django.test import TestCase, Client
from precios.views import precios
from precios.models import Paquete

class TestPaqueteModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configurar datos de prueba una vez al inicio de la clase
        Paquete.objects.create(
            titulo='Paquete de prueba',
            precio=100,
            caracteristicas='Características del paquete de prueba'
        )

    def test_titulo_max_length(self):
        paquete = Paquete.objects.get(id=1)
        max_length = paquete._meta.get_field('titulo').max_length
        self.assertEqual(max_length, 100)

    def test_precio_decimal_places(self):
        paquete = Paquete.objects.get(id=1)
        decimal_places = paquete._meta.get_field('precio').decimal_places
        self.assertEqual(decimal_places, 0)

    def test_paquete_str_method(self):
        paquete = Paquete.objects.get(id=1)
        self.assertEqual(str(paquete), 'Paquete de prueba')

class TestPreciosView(TestCase):
    def setUp(self):
        # Configurar datos de prueba
        self.client = Client()

    def test_precios_view(self):
        # Crear objetos de prueba
        paquete1 = Paquete.objects.create(
            titulo='Paquete 1',
            precio=100,
            caracteristicas='Características del paquete 1'
        )
        paquete2 = Paquete.objects.create(
            titulo='Paquete 2',
            precio=200,
            caracteristicas='Características del paquete 2'
        )

        # Realizar solicitud HTTP GET
        response = self.client.get('/precios/')

        # Verificar que se recibe una respuesta HTTP 200 OK
        self.assertEqual(response.status_code, 200)

        # Verificar que se renderiza el template correcto
        self.assertTemplateUsed(response, 'precios/precios.html')

        # Verificar que los paquetes están presentes en el contexto
        self.assertIn('paquetes', response.context)
        paquetes_en_contexto = response.context['paquetes']
        self.assertEqual(len(paquetes_en_contexto), 2)
        self.assertIn(paquete1, paquetes_en_contexto)
        self.assertIn(paquete2, paquetes_en_contexto)

