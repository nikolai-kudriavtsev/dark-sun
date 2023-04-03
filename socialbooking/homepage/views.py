from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Featured

class HomePageView(TemplateView):
    template_name = "homepage/index.html" # templates/home.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured'] = Featured.objects.all()
        return context