from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

from socialbooking.authentication.views import UserRegistrationView, UserVerificationView, UserLoginView, UserLogoutView

from socialbooking.homepage.views import HomePageView
# from socialbooking.catalog.views import CatalogView
# from socialbooking.services.views import ServicesView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('activate/<uuid:token>/', UserVerificationView.as_view(), name='activate'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', login_required(UserLogoutView.as_view()), name='logout'),

    path('catalog/', include('socialbooking.catalog.urls')),
    path('services/', include('socialbooking.services.urls')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path

