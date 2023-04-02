from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from .models import User


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        kiril = [
            RegexValidator(
                "^[а-яА-Я -]*$",
                message="Разрешенные символы (кириллица, пробел и тире).",
            )
        ]
        angl = [
            RegexValidator(
                "^[a-zA-Z0-9-]*$",
                message="Разрешенные символы (латиница, цифры и тире).",
            )
        ]

        # self.fields['username'].validators = angl
        # self.fields['username'].label = 'Логин'
        # self.fields['username'].help_text = 'Обязательное поле. Только латиница, цифры и тире.'
        self.fields["first_name"].validators = kiril
        self.fields["last_name"].validators = kiril
        self.fields["patronymic"].validators = kiril

    check_rule = forms.CharField(
        label="я согласен с правилами регистрации",
        strip=False,
        widget=forms.CheckboxInput(),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "patronymic",
        )
        labels = {"username": "Логин"}
        # validator = {'password1': validators.MinLenghtValidator(6)}
