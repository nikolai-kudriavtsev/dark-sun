from django.urls import path
from .views import StayListView, StayDetailView

urlpatterns = [
    path('', StayListView.as_view(), name='stay_list'),
    path('<int:pk>/', StayDetailView.as_view(), name='stay_detail'),
    path('<int:pk>/', StayDetailView.as_view(), name='add_to_cart'),
]