from django.shortcuts import render, redirect
from users.forms import LoginForms, RegisterForms
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            name = form['name_login'].value()
            password = form['password'].value()

        user = auth.authenticate(
            request,
            username = name,
            password = password
        )

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'users/login.html', {'form':form})

def register(request):
    register = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            if form['password'].value() != form['confirm_password'].value():
                return redirect('register')
            
            name=form['name_register'].value()
            email=form['email'].value()
            password=form['password'].value()

            if User.objects.filter(username=name).exists():
                return redirect('register')
                
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )

            user.save()
            return redirect('login')


    return render(request, 'users/register.html', {'form' : register})

def logout(request):
    pass