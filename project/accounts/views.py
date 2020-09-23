from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from . import models
def home(request):
    return render(request, "accounts/home.html")


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        print(request.POST)
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=user,password=password)
        print(user,password)
        if user is not None:
            login(request,user)
            print("login successful")
            return redirect('/main_app/dashboard/')
        else:
            print("login failed")


    else:
        form = AuthenticationForm()
    return render(request, 'accounts/sign-in/sign_in.html',{'form':form})

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(request.POST['email'])
        print(request.POST['password1'])
        if form.is_valid():
            new_user = form.save(commit=False)
            #clinician_model = models.Clinician(title="clincian",user=new_user)
            new_user.username = request.POST['email']
            new_user.save()
            #clinician_model.save()
            print(new_user)
            print("valid form")
            return redirect('/accounts/signin/')
        else:
            print("form invalid")
    else:
        form = RegisterForm()
    return render(request,'accounts/create_account/create_account.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('accounts:signin')