from django.views.generic import ListView
from .models import Product


class HomeView(ListView):
    model = Product
    template_name = "home.html"
