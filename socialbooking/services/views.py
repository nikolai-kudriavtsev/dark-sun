from django.views.generic import ListView, DetailView
from .models import StayService

class StayServiceListView(ListView):
    model = StayService
    template_name = 'services/list.html'
    context_object_name = 'services'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['services'] = StayService.objects.all()
    #     return context

class StayServiceDetailView(DetailView):
    model = StayService
    template_name = 'services/detail.html'
    context_object_name = 'service'