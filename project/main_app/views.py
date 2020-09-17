from django.shortcuts import render, redirect
from .forms import UploadFileForm
from . import utils
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,'main_app/index copy.html')

def signin(request):
    return render(request, 'main_app/src/sign-in/signin.html')

def signin_test(request):
    return render(request, 'main_app/src/sign-in/sign_in.html')

def dashboard(request):
    return render(request,'main_app/src/dashboard/dashboard.html')

def dashboard_test(request):
    return render(request,'main_app/src/dashboard/dashboard_.html')

def child_image(request):
    return render(request, 'main_app/src/child-image/child-image.html')

def child_image_test(request):
    return render(request, 'main_app/src/child-image/child_image.html')

def clinician_image(request):
    return render(request, 'main_app/src/clinician-image/clinician-image.html')

def signup(request):
    return render(request,'main_app/src/create_account/create_account.html')

def download_csv(request):
    return render(request,'main_app/src/download_data/download_data.html')

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        print(request.POST['title'])
        if form.is_valid():
            #utils.save_uploaded_file(request.POST['title'],request.FILES)
            redirect('main_app/dashboard/')
    else:
        form = UploadFileForm()
    return render(request,'main_app/index.html',{'form':form})

def make_meeting(request):
    room_name = utils.get_room_name()
    print(room_name)
    client_room_name = "localhost/main_app/"
    #return render(request,'main_app/room_name.html',{'room_name':room_name})
    data = {'room_name':room_name}
    return JsonResponse(data)
def client_game(request):
    return render(request,'main_app/client_game.html')

def clinician_game(request):
    return render(request,'main_app/clinician_game.html')

def clinician_test(request,room_name):
    print("clinician:" + room_name)
    return render(request, 'main_app/clinician_game.html',{
        'room_name':room_name
    })

def client_test(request,room_name):
    print("client" + room_name)
    return render(request,"main_app/client_game.html",{
        'room_name':room_name
    })
            
