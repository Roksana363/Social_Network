from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from .models import LoginForm


class RegisterForm(forms.Mo):
    name = forms.CharField(max_length=100, label = "Имя")
    login = forms.CharField(label = "Логин")
    email = forms.EmailField(label = "Email")
    password = forms.CharField(widget=forms.PasswordInput,
                               label = "пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput,
                                       label = "Подтверждение")
    age = forms.IntegerField(max_value=101, label = "Возраст")
    work = forms.ChoiceField(label = "Работа",
                             choices = [
                                 ('Работает', 'Работает'),
                                 ('Безработный', 'Безработный'),
                                 ('Студент', 'Студент'),
                             ], widget = forms.Select()
                             )
    hobby = forms.ChoiceField(label = "Увлечения",
                             choices = [
                                 ('Игри', 'Игры'),
                                 ('Спорт', 'Спорт'),
                                 ('Еда', 'Еда'),
                                 ('Танцы', 'Танцы'),
                             ], widget = forms.CheckboxSelectMultiple,
                                required = False,
                             )
    class Meta(UserCreationForm.Meta):
        model = LoginForm
        fields = [
            'name',
            'login',
            'email',
            'password',
            'confirm_password',
            'age',
            'work',
            'hobby'
        ]