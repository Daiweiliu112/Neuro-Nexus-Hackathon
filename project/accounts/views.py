from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User


def home(request):
    return render(request, "accounts/home.html")


def signin(request):
    return render(request, 'accounts/sign-in/sign_in.html')

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(request.POST['email'])
        print(request.POST['password1'])
        if form.is_valid():
            print("valid form")
        else:
            print("form invalid")
        return redirect('accounts/signin/')
        
    else:
        form = RegisterForm()
    return render(request,'accounts/create_account/create_account.html',{'form':form})