from django.views.generic import ListView, DetailView
from .models import Stay


class StayListView(ListView):
    model = Stay
    template_name = 'catalog/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stays'] = Stay.objects.all()
        return context

class StayDetailView(DetailView):
    model = Stay
    template_name = 'catalog/detail.html'
