from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Blog

	# Тестируем модели приложения main

class PostModelTest(TestCase):      

	def setUp(self):
		"""Создаю метод для создания тестовой записи в тестовой базе"""
		Blog.objects.create(title="Test", author="Jangir", content="Test text", pub_date=timezone.now())

	def test_models_correctly(self):
		"""Сохраняю в переменной post наш тестовый пост. Далее получаю контент в отдельной переменной. 
		И сравниваю значения с прогнозируемым. """
		post = Blog.objects.get(id=1)
		test_post_title = f'{post.title}'
		self.assertEqual(test_post_title, "Test")


		# Тестируем домашнюю страницу

class HomepageViewTest(TestCase):

	def test_does_home_exist(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_by_name_home(self):
		response = self.client.get(reverse('home'))     # Проверка соответствия url и имени url
		self.assertEqual(response.status_code, 200)

	def test_view_correct_template(self):                       # Проверка правильного шаблона
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "main/index.html")


		# Тестируем страницу About

class AboutViewTest(TestCase):

	def test_does_about_exist(self):
		response = self.client.get('/about/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_by_name_about(self):
		response = self.client.get(reverse('about'))
		self.assertEqual(response.status_code, 200)

	def test_view_correct_about_template(self):
		response = self.client.get(reverse('about'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/about.html')

class WallPageTest(TestCase):

	def test_does_wallpage_exist(self):
		response = self.client.get('/wall/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_by_name_wallpage(self):
		response = self.client.get(reverse('wall'))
		self.assertEqual(response.status_code, 200)

	def test_view_correct_wallpage_template(self):
		response = self.client.get(reverse('wall'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/wall.html')