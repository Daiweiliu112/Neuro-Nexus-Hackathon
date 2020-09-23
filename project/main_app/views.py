from django.shortcuts import render, redirect
from .forms import UploadImageForm, UploadFileForm
from . import utils
from django.http import JsonResponse
import accounts.models as account_models
from django.conf.urls import url
from django.http import HttpResponseRedirect
import json

# Create your views here.


def check_cli_num(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        logger.error(data)
        user = request.user
        analytics.check_cli_num(user,data)
        return HttpResponse("It's cool man!")

def index(request):
    return render(request,'main_app/index copy.html')

def signin(request):
    return render(request, 'main_app/src/sign-in/signin.html')

def signin_test(request):
    return render(request, 'main_app/src/sign-in/sign_in.html')

def dashboard(request):
    #current_user = request.user
    context = {"testing": '''<image class="image-fluid" height="255" width= "100%" src="/static/I_Spy 1.png" />'''}
    return render(request,'main_app/src/dashboard/dashboard_collection.html',context)

def dashboard_test(request):
    if request.user.is_authenticated:
        current_user = request.user
        print("current user: ", current_user)
        clinician = account_models.Clinician.objects.get(user=request.user)
        collections = account_models.ImageSet.objects.filter(clinician=clinician)
        collections_row = len(collections) // 3
        collections_remainder = len(collections) % 3
        collections_array = []
        for i in range(collections_row):
            starting_index = i * 3
            temp = [collections[starting_index],collections[starting_index + 1],collections[starting_index + 2]]
        if collections_remainder > 0:
            last_index = 3 * collections_row
            temp = []
            for i in range(collections_remainder):
                temp.append(collections[last_index+i])
            collections_array.append(temp)
        images = account_models.Image.objects.filter(clinician=clinician)
        print("Image: ", images)
        print(len(images))
        image_row = len(images) // 3
        remain = len(images) % 3
        image_array = []
        for i in range(image_row):
            starting_index = i * 3
            temp = [images[starting_index], images[starting_index + 1], images[starting_index + 2]]
            image_array.append(temp)
        if remain > 0:
            last_index = 3 * image_row
            temp = []
            for i in range(remain):
                temp.append(images[last_index + i])
            image_array.append(temp)
        print(image_array)
        context = {
            "images":image_array,
            "collections":collections_array,
        }
        print(context)
        return render(request,'main_app/src/dashboard/dashboard_.html',context)
    else:
        return redirect('accounts:signin')

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
    if request.user.is_authenticated:
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
                print("image url:", image_model.image.url)
                print("Image time:",image_model.created)
                print("Image detail:",image_model.pk)
                print("Image id:",image_model.id)
                return redirect('main_app:editview',pk=image_model.pk)
        else:
            form = UploadFileForm()
            #form = UploadImageForm()
        return render(request,'main_app/index.html',{'form':form})
    else:
        return redirect('accounts:signin')

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
            
def edit_view(request,pk):
    print(pk)
    if request.user.is_authenticated:
        image_model = account_models.Image.objects.get(pk=pk)
        print("image url:",image_model.image.url)
        print("image title:", image_model.title)
        context ={
            "image":image_model
        }
        return render(request,'main_app/src/edit_view/clinician_image.html',context=context)
    else:
        redirect('accounts:signin')
    return render(request,'main_app/src/edit_view/clinician_image.html')

def save_image_edit(request):
    print(request.POST.get("points"))
    print(request.POST)
    image_pk = request.POST.get("image_pk")
    image_model = account_models.Image.objects.get(pk=image_pk)
    print(image_model.coords)
    points = json.loads(request.POST.get("points"))
    print(points["top_left"])
    points_arr = [points["top_left"][0],points["top_left"][1],points["bottom_right"][0],points["bottom_right"][1]]
    print(points_arr)
    image_model.coords = points_arr 
    #image_model.coords = points_arr
    image_model.save()
    print("coord check:",image_model.coords)
    return JsonResponse({"worked":True})

def create_collection_view(request):
    if request.user.is_authenticated:
        current_user = request.user
        clinician = account_models.Clinician.objects.get(user=current_user)
        collections = account_models.ImageSet.objects.filter(clinician=clinician)
        #collections_pk = collections.pk
        images = account_models.Image.objects.filter(clinician=clinician)
        print("Image: ", images)
        print(len(images))
        image_row = len(images) // 3
        remain = len(images) % 3
        image_array = []
        for i in range(image_row):
            starting_index = i * 3
            temp = [images[starting_index], images[starting_index + 1], images[starting_index + 2]]
            image_array.append(temp)
        if remain > 0:
            last_index = 3 * image_row
            temp = []
            for i in range(remain):
                temp.append(images[last_index + i])
            image_array.append(temp)
        print(image_array)
        context = {
            "images":image_array,
        }
        print(context)
        return render(request,'main_app/src/dashboard/dashboard_collection.html',context)
    return render(request,'main_app/src/dashboard/dashboard_collection.html')

def create_collection(request):
    images_id = json.loads(request.POST.get("selected_image"))
    print(images_id)
    current_user = request.user
    clinician = account_models.Clinician.objects.get(user=current_user)
    print(clinician)
    collection_pk = json.loads(request.POST.get("collection_pk"))
    if(collection_pk < 0):
        image_set = account_models.ImageSet()
    else:
        image_set = account_models.ImageSet.objects.get(pk=collection_pk)
    
    image_set.clinician = clinician
    image_set.title = json.loads(request.POST.get("title"))
    fields = image_set._meta.get_fields()
    print(type(fields[3]))
    i = 3
    #for image_id in images_id:
    #    temp_model = fields[i]
    #    temp_model = account_models.Image.objects.get(pk=image_id)
        
    #    i+=1
    image_set.pic1 = account_models.Image.objects.get(pk=images_id[0])
    image_set.pic2 = account_models.Image.objects.get(pk=images_id[1])
    image_set.pic3 = account_models.Image.objects.get(pk=images_id[2])
    image_set.pic4 = account_models.Image.objects.get(pk=images_id[3])
    image_set.pic5 = account_models.Image.objects.get(pk=images_id[4])
    image_set.pic6 = account_models.Image.objects.get(pk=images_id[5])
    image_set.pic7 = account_models.Image.objects.get(pk=images_id[6])
    image_set.pic8 = account_models.Image.objects.get(pk=images_id[7])
    image_set.pic9 = account_models.Image.objects.get(pk=images_id[8])
    image_set.pic10 = account_models.Image.objects.get(pk=images_id[9])
    image_set.pic11 = account_models.Image.objects.get(pk=images_id[10])
    for i in range(3,14):
        print(fields[i])
    image_set.save()
    print(image_set.pic1.pk)
    return JsonResponse({"sucess":True})

def edit_collection_view(request,pk):
    if request.user.is_authenticated:
        print(pk)
        collection_model = account_models.ImageSet.objects.get(pk=pk)
        collection_image = [[collection_model.pic1,collection_model.pic2,collection_model.pic3],
                            [collection_model.pic4,collection_model.pic5,collection_model.pic6],
                            [collection_model.pic7,collection_model.pic8,collection_model.pic9],
                            [collection_model.pic10,collection_model.pic11]
        ]
        current_user = request.user
        clinician = clinician = account_models.Clinician.objects.get(user=current_user)
        image_array = get_images(clinician)

        context = {
            "collection":collection_image,
            "images": image_array,
            "collection_pk":pk,
        }
        return render(request,'main_app/src/dashboard/dashboard_collection.html',context)


    return render(request,'main_app/src/dashboard/dashboard_collection.html')

def get_images(clinician):
    #clinician = account_models.Clinician.objects.get(user=current_user)
    #collections = account_models.ImageSet.objects.filter(clinician=clinician)
    #collections_pk = collections.pk
    images = account_models.Image.objects.filter(clinician=clinician)
    #print("Image: ", images)
    #print(len(images))
    image_row = len(images) // 3
    remain = len(images) % 3
    image_array = []
    for i in range(image_row):
        starting_index = i * 3
        temp = [images[starting_index], images[starting_index + 1], images[starting_index + 2]]
        image_array.append(temp)
    if remain > 0:
        last_index = 3 * image_row
        temp = []
        for i in range(remain):
            temp.append(images[last_index + i])
        image_array.append(temp)
    return image_array    
