from django.shortcuts import render, redirect 
from user.forms import auth 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from user.forms import registration

def auth_view(request):
    if request.method == "GET":
        context={
            "form" : auth 
        }
        return render(request, template_name='auth.html', context=context)
    elif request.method == "POST":
        data=request.POST
        form = auth(data=data)
        if form.is_valid():
            user= authenticate(
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password'),
            )
        if user:
            login(request, user)
            return redirect('/')
        else:
            form.add_error('usernsme', 'error')
    return render(request, template_name='auth.html', context={'form': form})

def registration_view(request):
    if request.method == "GET":
        context={
            "form" : registration 
        }
        return render(request, template_name='registration.html', context=context)
    elif request.method == "POST":
        data=request.POST
        form = registration(data=data)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            if password == password2:
                User.objects.create_user(
                    username = form.cleaned_data.get('username'),
                    password = form.cleaned_data.get('password')
                )
                return redirect ('/user/login/')
            else:
                form.add_error(password, error="the password didn't match")

        context = {
            'form':form
        }
        return render(request, template_name='registration.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')