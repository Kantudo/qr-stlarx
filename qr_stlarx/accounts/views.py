from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
#rom django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, AuthForm
from django.contrib.auth.decorators import login_required



def signup(request):
    #User.objects.all().delete()
    if request.method == 'POST':
        user_form = SignUpForm(data=request.POST)
        if user_form.is_valid():
            user_data = user_form.cleaned_data
            print(user_data)
            mon_user = User.objects.create_user(username=user_data['username'],
                                            email=user_data['email'],
                                            password=user_data['password1'],
                                            is_active=True
                                            )
            #mon_user.is_active = True
            #mon_user.save()
            user = authenticate(request, username=user_data['username'], password=user_data['password1'])
            login(request, user)
            return redirect('/')
    else:
        user_form = SignUpForm()
    return render(request, 'signup.html', {'form': user_form})

def login_view(request):
    if request.method == 'POST':
        login_form = AuthForm(data=request.POST)
        if login_form.is_valid():
            login_data = login_form.cleaned_data
            user = authenticate(request,
                                username=login_data['username'],
                                password=login_data['password'])
            if user is not None:
                login(request, user)
            return redirect('/')
        else:
            return redirect('/accounts/signup/')
    else:
        login_form = AuthForm()
    return render(request, 'login.html', {'form': login_form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
