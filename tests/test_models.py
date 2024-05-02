# Importa el modelo Email y Curso, y pytest
from contacto.models import Email
from cursos.models import Curso
import pytest

# Define la clase de pruebas
class TestModels:
    # Define la prueba para crear un objeto Email
    @pytest.mark.django_db
    def test_create_email(self):
        # Crea un objeto Email
        email = Email.objects.create(
            nombre="John",
            apellido="Doe",
            telefono="123456789",
            email="john@example.com",
            asunto="Consulta",
            consulta="¿Cómo puedo contactarlos?"
        )

        # Verifica que el objeto Email se haya guardado correctamente en la base de datos
        assert Email.objects.count() == 1
        assert email.nombre == "John"
        assert email.apellido == "Doe"
        assert email.telefono == "123456789"
        assert email.email == "john@example.com"
        assert email.asunto == "Consulta"
        assert email.consulta == "¿Cómo puedo contactarlos?"

    # Define la prueba para crear un objeto Curso
    @pytest.mark.django_db
    def test_create_curso(self):
        # Crea un objeto Curso
        curso = Curso.objects.create(
            titulo="Test Curso",
            descripcion="This is a test description",
            precio=1000,
            imagen="../../../static/i/test_logo.jpg"
        )

        # Verifica que el objeto Curso se haya guardado correctamente en la base de datos
        assert Curso.objects.count() == 1
        assert curso.titulo == "Test Curso"
        assert curso.descripcion == "This is a test description"
        assert curso.precio == 1000
        assert curso.imagen == "../../../static/i/test_logo.jpg"
