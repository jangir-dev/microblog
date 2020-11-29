from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField("Заголовок", max_length=40)
	author = models.CharField("Автор", max_length=80)
	content = models.TextField("Контент")
	pub_date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Пост"
		verbose_name_plural = "Посты"
		ordering = ['-pub_date']
