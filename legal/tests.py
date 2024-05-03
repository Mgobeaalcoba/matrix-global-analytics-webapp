from django.test import TestCase
from django.template.loader import render_to_string
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

class TestTerminosDeUsoTemplate(TestCase):
    def test_template_rendering(self):
        # Renderiza el template
        rendered_template = render_to_string('legal/terminos_de_uso.html')

        # Verifica que el título esté presente en el template renderizado
        self.assertInHTML('<title>Marcas</title>', rendered_template)
        self.assertInHTML('<a class="open_menu color-main bg-light radius_full"><i class="fas fa-bars lh-40"></i></a>', rendered_template)
        self.assertInHTML('<div class="mb-35 f-18 semibold title">Acerca de</div>', rendered_template)
        self.assertInHTML('<a href="/preguntas-frecuentes/" class="link color-main">FAQ</a>', rendered_template)
        self.assertInHTML('<div class="mb-35 f-18 semibold title">Información</div>', rendered_template)
        self.assertInHTML('<a href="/ultimos-proyectos/" class="link color-main">Últimos Proyectos</a>', rendered_template)
        self.assertInHTML('<h2 class="terms-title">Términos y Condiciones de Uso del Sitio Web</h2>', rendered_template)
        self.assertInHTML('<h2 class="terms-title">Website Usage Terms and Conditions</h2>', rendered_template)

class TestPoliticaDePrivacidadTemplate(TestCase):
    def test_template_rendering(self):
        # Renderiza el template
        rendered_template = render_to_string('legal/politica_de_privacidad.html')

        # Verifica que el título esté presente en el template renderizado
        self.assertInHTML('<title>Marcas</title>', rendered_template)
        self.assertInHTML('<h2 class="terms-title">Politica de Privacidad del sitio</h2>', rendered_template)
        self.assertInHTML('<h2 class="terms-title">Website Privacy Policy</h2>', rendered_template)
        self.assertInHTML('<h3 class="terms-subtitle">Información que es recogida</h3>', rendered_template)
        self.assertInHTML('<h3 class="terms-subtitle">Uso de información recogida</h3>', rendered_template)
        self.assertInHTML('<h3 class="terms-subtitle">Cookies</h3>', rendered_template)
        self.assertInHTML('<h3 class="terms-subtitle">Enlaces a Terceros</h3>', rendered_template)
        self.assertInHTML('<h3 class="terms-subtitle">Control de su información personal</h3>', rendered_template)
