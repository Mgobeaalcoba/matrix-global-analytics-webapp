from django.test import TestCase
from django.urls import reverse
from trabajos.models import PorfolioItem, NewProject, Cliente, Employee, Experience

class TestModels(TestCase):
    def setUp(self):
        # Crear objetos de prueba
        self.cliente = Cliente.objects.create(
            nombre='Cliente de prueba',
            sitio_web='http://www.cliente.com'
        )

        self.empleado = Employee.objects.create(
            name='Empleado de prueba',
            title='Título de prueba',
            description='Descripción del empleado de prueba'
        )

        self.experiencia = Experience.objects.create(
            company='Empresa de prueba',
            years='2020-2022',
            position='Cargo de prueba',
            duration='2 años',
            location='Ubicación de prueba',
            description='Descripción de la experiencia de prueba',
            employee=self.empleado
        )

    def test_porfolioitem_str(self):
        porfolio_item = PorfolioItem.objects.create(
            title='Proyecto de prueba',
            description='Descripción del proyecto de prueba'
        )
        self.assertEqual(str(porfolio_item), 'Proyecto de prueba')

    def test_newproject_str(self):
        new_project = NewProject.objects.create(
            title='Nuevo proyecto de prueba',
            description='Descripción del nuevo proyecto de prueba'
        )
        self.assertEqual(str(new_project), 'Nuevo proyecto de prueba')

    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), 'Cliente de prueba')

    def test_employee_str(self):
        self.assertEqual(str(self.empleado), 'Empleado de prueba')

    def test_experience_str(self):
        self.assertEqual(str(self.experiencia), 'Cargo de prueba at Empresa de prueba')

class TrabajosViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear datos de prueba para las vistas

        # Crear algunos PorfolioItems
        PorfolioItem.objects.create(
            title="Proyecto 1",
            description="Descripción del Proyecto 1",
            image="proyecto1.jpg",
            github_link="https://github.com/proyecto1",
            github_link_img="github1.jpg"
        )
        PorfolioItem.objects.create(
            title="Proyecto 2",
            description="Descripción del Proyecto 2",
            image="proyecto2.jpg",
            github_link="https://github.com/proyecto2",
            github_link_img="github2.jpg"
        )

        # Crear algunos Employee y sus experiencias asociadas
        employee1 = Employee.objects.create(
            name="Empleado 1",
            title="Título del Empleado 1",
            photo="empleado1.jpg",
            description="Descripción del Empleado 1 | Otra descripción del Empleado 1"
        )
        Experience.objects.create(
            company="Empresa 1",
            years="2020-2021",
            position="Posición 1",
            duration="1 año",
            location="Ubicación 1",
            description="Descripción de la experiencia 1",
            employee=employee1
        )
        Experience.objects.create(
            company="Empresa 2",
            years="2018-2020",
            position="Posición 2",
            duration="2 años",
            location="Ubicación 2",
            description="Descripción de la experiencia 2",
            employee=employee1
        )

        employee2 = Employee.objects.create(
            name="Empleado 2",
            title="Título del Empleado 2",
            photo="empleado2.jpg",
            description="Descripción del Empleado 2"
        )
        Experience.objects.create(
            company="Empresa 3",
            years="2019-2020",
            position="Posición 3",
            duration="1 año",
            location="Ubicación 3",
            description="Descripción de la experiencia 3",
            employee=employee2
        )

        # Crear algunos NewProjects
        NewProject.objects.create(
            title="Nuevo Proyecto 1",
            description="Descripción del Nuevo Proyecto 1",
            image="nuevo_proyecto1.jpg",
            github_link="https://github.com/nuevo_proyecto1",
            github_link_img="github_nuevo_proyecto1.jpg"
        )
        NewProject.objects.create(
            title="Nuevo Proyecto 2",
            description="Descripción del Nuevo Proyecto 2",
            image="nuevo_proyecto2.jpg",
            github_link="https://github.com/nuevo_proyecto2",
            github_link_img="github_nuevo_proyecto2.jpg"
        )

        # Crear algunos Clientes
        Cliente.objects.create(
            nombre="Cliente 1",
            sitio_web="https://cliente1.com",
            logo="logo_cliente1.jpg"
        )
        Cliente.objects.create(
            nombre="Cliente 2",
            sitio_web="https://cliente2.com",
            logo="logo_cliente2.jpg"
        )

    def test_quienes_somos_view(self):
        response = self.client.get(reverse('quienes_somos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trabajos/quienes_somos.html')

    def test_nuestro_porfolio_view(self):
        response = self.client.get(reverse('nuestro_porfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trabajos/nuestro_porfolio.html')

    def test_ultimos_proyectos_view(self):
        response = self.client.get(reverse('ultimos_proyectos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trabajos/ultimos_proyectos.html')

    def test_marcas_view(self):
        response = self.client.get(reverse('marcas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trabajos/marcas.html')
