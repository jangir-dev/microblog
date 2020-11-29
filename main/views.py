from django.views.generic import TemplateView, ListView
from .models import Blog

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'main/index.html'

class AboutPageView(TemplateView):
	template_name = 'main/about.html'

class WallView(ListView):
	model = Blog
	template_name = 'main/wall.html'
	context_object_name = "posts"
