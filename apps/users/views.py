from django.shortcuts import render, redirect
from apps.users.forms import LoginForms, RegisterForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

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
            messages.success(request, 'Usuário logado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Ops... Algo deu errado, tente novamente.')
            return redirect('login')

    return render(request, 'users/login.html', {'form':form})

def register(request):
    register = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            if form['password'].value() != form['confirm_password'].value():
                messages.error(request, 'As senhas não conferem!')
                return redirect('register')
            
            name=form['name_register'].value()
            email=form['email'].value()
            password=form['password'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, 'Esse nome de usuário já está em uso!')
                return redirect('register')
                
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )

            user.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('login')


    return render(request, 'users/register.html', {'form' : register})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')