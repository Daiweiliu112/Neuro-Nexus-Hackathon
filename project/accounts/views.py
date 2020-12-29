from django.shortcuts import render,redirect
from .forms import RegisterForm, UserAuthForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from . import models
def home(request):
    return render(request, "accounts/web_home/index.html")

def signin(request):
    # When the request from the client is POST, then authenticate the user
    if request.method == "POST":
        form = UserAuthForm(request.POST)       # Load the value of the fields from client
        print(request.POST)

        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=user,password=password)        # Get User Object with given username and password
        print(user,password)
        # If the user object is not null, that means that there is a user with give email and password
        if user is not None:
            login(request,user)
            print("login successful")
            return redirect('/main_app/dashboard/')     # redirects to dashboard
        else:
            print("login failed")
    # If it is loading the page, load the form then show the form
    else:
        form = UserAuthForm()
    return render(request, 'accounts/sign-in/sign_in.html',{'form':form})

def signin2(request):
    # When the request from the client is POST, then authenticate the user
    if request.method == "POST":
        form = UserAuthForm(request.POST)       # Load the value of the fields from client
        print(request.POST)

        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=user,password=password)        # Get User Object with given username and password
        print(user,password)
        # If the user object is not null, that means that there is a user with give email and password
        if user is not None:
            login(request,user)
            print("login successful")
            return redirect('/main_app/dashboard/')     # redirects to dashboard
        else:
            print("login failed")
    # If it is loading the page, load the form then show the form
    else:
        form = UserAuthForm()
    return render(request, 'accounts/web_home/signin2.html',{'form':form})

def signup(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST) # If the request is POST then load the value of the fields from client
        print(request.POST['email'])
        print(request.POST['password1'])
        # If the form is valid then proceed on saving the infomation
        if form.is_valid():
            new_user = form.save(commit=False)  # Loads the value from client but not save the Object to Database
            #clinician_model = models.Clinician(title="clincian",user=new_user)
            new_user.username = request.POST['email']   # Put Email as username for the User Objects
            new_user.save()                             # Save the User Object in the Database
            #clinician_model.save()
            print(new_user)
            print("valid form")
            return redirect('/accounts/signin/')        # After Sign Up, redirect the client to Sign In page
        else:
            print("form invalid")
    else:
        # If it is loading the page, load the form
        form = RegisterForm()
    return render(request,'accounts/create_account/create_account.html',{'form':form})

def logout_view(request):
    logout(request)     # Logs out the user
    return redirect('accounts:signin')