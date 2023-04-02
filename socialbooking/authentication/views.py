from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.urls import reverse_lazy

from .models import User
from .forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    template_name = 'authentication/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()

        subject = 'Верификация аккаунта'
        message = render_to_string('authentication/verification_email.html', {
            'user': user,
            'domain': self.request.META['HTTP_HOST'],
            'token': user.verification_token
        })
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = form.cleaned_data['email']
        send_mail(subject, message, from_email, [to_email], fail_silently=False)

        user = authenticate(
            self.request,
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)
        return redirect(self.success_url, permanent=True)

class UserVerificationView(View):
    def get(self, request, token):
        try:
            user = User.objects.get(verification_token=token)
            user.is_verified = True
            user.save()
            return render(request, 'authentication/verification_success.html')
        except User.DoesNotExist:
            return render(request, 'authentication/verification_failure.html')

class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
