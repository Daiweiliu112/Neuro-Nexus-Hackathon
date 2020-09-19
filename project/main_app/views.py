from django.shortcuts import render, redirect
from .forms import UploadImageForm, UploadFileForm
from . import utils
from django.http import JsonResponse
import accounts.models as account_models

# Create your views here.

def index(request):
    return render(request,'main_app/index copy.html')

def signin(request):
    return render(request, 'main_app/src/sign-in/signin.html')

def signin_test(request):
    return render(request, 'main_app/src/sign-in/sign_in.html')

def dashboard(request):
    current_user = request.user
    print(current_user)
    context = {"testing": '''<image class="image-fluid" height="255" width= "100%" src="/static/I_Spy 1.png" />'''}
    return render(request,'main_app/src/dashboard/dashboard_upload.html',context)

def dashboard_test(request):
    current_user = request.user
    print("current user: ", current_user)
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
        form = UploadFileForm(request.POST,request.FILES)
        print(request.POST['title'])
        if form.is_valid():
            print("valid form")
            #image_form = form.save(commit=False)
            clinician = account_models.Clinician.objects.get(user=request.user)
            #print("clincian:",clincian.user.email)
            default_coord = [0,0,0,0]
            image_model = account_models.Image(image=request.FILES['file'],title=request.POST['title'],clinician=clinician,coords=default_coord)
            image_model.save()
            #form.coords = [0,0,0,0]
            #form.save()
            #utils.save_uploaded_file(request.POST['title'],request.FILES)
            print("Image Saved")
            return redirect('../dashboard_uploaded/')
        #return redirect('../dashboard_uploaded/')
    else:
        form = UploadFileForm()
        #form = UploadImageForm()
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