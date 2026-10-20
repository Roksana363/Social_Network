from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.

def register(request):
    register = RegisterForm()
    if request.method == 'POST':
        register = RegisterForm()
        name = request.POST.get('name')
        login = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        age = request.POST.get('age')
        work = request.POST.getlist('work')
        hobby = request.POST.getlist('hobby')
    context = {
        'register': register
    }
    return render(request, 'register.html', context)