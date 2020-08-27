from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'main_app/index copy.html')

def signin(request):
    return render(request, 'main_app/src/sign-in/signin.html')

def dashboard(request):
    return render(request,'main_app/src/dashboard/dashboard.html')

def child_image(request):
    return render(request, 'main_app/src/child-image/child-image.html')

def clinician_image(request):
    return render(request, 'main_app/src/clinician-image/clinician-image.html')