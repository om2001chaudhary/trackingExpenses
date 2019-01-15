from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from sessionApp.forms import userLoginForm
from clientApp.views import dashBoard

def userSignUp(request):

    if request.user.username:
        return redirect(dashBoard)

    message = ''
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User()
            user.username = username
            user.set_password(password)
            user.save()
            message = 'User registration done successfully please click to login!'

    return render(request , 'signup.html' , {'form':form , 'msg':message})


def userLogin(request):

    if request.user.username:
        return redirect(dashBoard)

    message = ''
    form = userLoginForm()
    if request.method == 'POST':
        form = userLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username=username,
                password=password
            )
            if user is None:
                message = 'Invalid user!'
            else:
                login(request, user)
                return redirect(dashBoard)

    return render(request , 'login.html' , {'form':form , 'msg':message})


def userLogout(request):

    logout(request)
    return redirect(userSignUp)