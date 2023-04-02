from django.urls import path


from .views import StayServiceListView, StayServiceDetailView

# app_name = 'services'

urlpatterns = [
    path('', StayServiceListView.as_view(), name='service_list'),
    path('<int:pk>/', StayServiceDetailView.as_view(), name='service_detail'),
]
