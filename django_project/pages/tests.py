from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView

class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_home_contains_correct_html(self):
        self.assertContains(self.response, "Домашняя страница")

    def test_home_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Такого контента нет...")

    def test_home_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)
        
    def test_about_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_about_contains_correct_html(self):
        self.assertContains(self.response, "О нас")

    def test_about_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Такого контента нет...")

    def test_about_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)