from django.shortcuts import render, redirect
from .forms import UploadFileForm
from . import utils
from django.http import JsonResponse
from accounts.models import (
    Client,
    )
from django.contrib.auth.models import User

# Create your views here.

def check_cli_num(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the client number from the client side.
        cli_id = request.GET.get("cli_id", None)
        # check for the existing client number in the database.
        user = request.user
        if Client.objects.filter(id_num = cli_id).exists():
            # if cli_num found return not valid .
            return JsonResponse({"valid":False}, status = 200)
        else:
            user = request.user
            # if cli_num not found, then clinician can create a new client.
            client = Client(clinician=user,id_num=cli_id)
            client.save()
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)
    
def index(request):
    return render(request,'main_app/index copy.html')

def signin(request):
    return render(request, 'main_app/src/sign-in/signin.html')

def signin_test(request):
    return render(request, 'main_app/src/sign-in/sign_in.html')

def dashboard(request):
    context = {"testing": '''<image class="image-fluid" height="255" width= "100%" src="/static/I_Spy 1.png" />'''}
    return render(request,'main_app/src/dashboard/dashboard_upload.html',context)

def dashboard_test(request):
    context = {"testing": '''<image class="image-fluid" height="255" width= "100%" src="/static/I_Spy 1.png" />'''}
    return render(request,'main_app/src/dashboard/dashboard_.html',context)

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
            print("valid form")
            #utils.save_uploaded_file(request.POST['title'],request.FILES)
            return redirect('../dashboard_uploaded/')
        return redirect('../dashboard_uploaded/')
    else:
        form = UploadFileForm()
    return render(request,'main_app/index.html',{'form':form})

def make_meeting(request):
    room_name = utils.get_room_name()
    print(room_name)
    client_room_name = "/main_app/client/" + room_name + "/"
    clinician_room_name = "/main_app/cli/" + room_name + '/'
    #return render(request,'main_app/room_name.html',{'room_name':room_name})
    data = {'clinician':clinician_room_name,
            'client':client_room_name
            }
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
            
def edit_view(request):
    return render(request,'main_app/src/edit_view/clinician_image.html')
