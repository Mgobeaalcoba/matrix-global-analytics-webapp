from django.test import TestCase, Client
from django.urls import reverse
from .models import Curso

class CursosTestCase(TestCase):
    def setUp(self):
        # Crea objetos Curso para usar en las pruebas
        Curso.objects.create(
            titulo="Curso 1",
            descripcion="Descripción del Curso 1",
            precio=1000,
            imagen="../../../static/i/curso1.jpg"
        )
        Curso.objects.create(
            titulo="Curso 2",
            descripcion="Descripción del Curso 2",
            precio=2000,
            imagen="../../../static/i/curso2.jpg"
        )

    def test_cursos_count(self):
        # Verifica que se hayan creado dos objetos Curso
        self.assertEqual(Curso.objects.count(), 2)

    def test_curso_attributes(self):
        # Verifica los atributos de un objeto Curso específico
        curso = Curso.objects.get(titulo="Curso 1")
        self.assertEqual(curso.descripcion, "Descripción del Curso 1")
        self.assertEqual(curso.precio, 1000)
        self.assertEqual(curso.imagen, "../../../static/i/curso1.jpg")


class CursosViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_cursos_view(self):
        # Crear un curso de prueba
        Curso.objects.create(
            titulo="Curso de prueba",
            descripcion="Descripción del curso de prueba",
            precio=1000,
            imagen="../../../static/i/test_logo.jpg"
        )

        # Obtener la URL para la vista de cursos
        url = reverse('cursos')

        # Realizar una solicitud GET a la vista de cursos
        response = self.client.get(url)

        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)

        # Verificar que el template correcto está siendo utilizado
        self.assertTemplateUsed(response, 'cursos/cursos.html')

        # Verificar que el curso creado está presente en el contexto de la vista
        cursos = response.context['cursos']
        self.assertEqual(len(cursos), 1)
        curso = cursos[0]
        self.assertEqual(curso.titulo, "Curso de prueba")
        self.assertEqual(curso.descripcion, ['Descripción del curso de prueba'])
        self.assertEqual(curso.precio, 1000)
        self.assertEqual(curso.imagen, "../../../static/i/test_logo.jpg")

