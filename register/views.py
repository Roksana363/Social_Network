from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from .forms import RegisterForm
from .models import LoginForm

# def register(request):
#     if request.method == "POST":
#         # Передаем данные из запроса в форму
#         reg_form = RegisterForm()
#
#         if reg_form.is_valid():
#             data = reg_form.cleaned_data
#             user = LoginForm.objects.create(
#                 name=data.post("name"),
#             )
#             user.save()
#     else:
#         reg_form = RegisterForm()
#
#     # Одинаковое имя переменной 'reg_form' используется для обоих случаев
#     return render(request, "register.html", {"reg_form": reg_form})
