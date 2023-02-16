from django.shortcuts import render, redirect
from django.http import response
from authorization.forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
from authorization.models import User


# Create your views here.


def index(request):
    return render(request, template_name='authorization/html/index.html')


def test(request):
    return render(request, template_name='mock/test.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(user_name=username).first() and User.objects.filter(password=password).first():
            return redirect('/index/')

    return render(request, 'authorization/html/login.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        user_name = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(email, user_name, password)
        if User.objects.filter(email=email).first():
            pass
        if User.objects.filter(user_name=user_name).first():
            pass
        user = User.objects.create(email=email, password=password, user_name=user_name)
        User.save(user)
    return render(request, template_name='authorization/html/register.html')


@csrf_exempt
def logout(request):
    return render(request, template_name='authorization/html/login.html')
    # return redirect(login)
