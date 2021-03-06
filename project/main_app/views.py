<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import UploadImageForm, UploadFileForm, SpinnerUpdateForm, VoicePicForm, VoiceWordsForm, RecordFormLight
from . import utils
from django.http import HttpResponse, JsonResponse
=======
from django.shortcuts import render, redirect 
from .forms import UploadImageForm, UploadFileForm, SpinnerUpdateForm, VoicePicForm, VoiceWordsForm, RecordForm
from . import utils
from django.http import HttpResponse,JsonResponse
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
from accounts.models import (
    Client,
    ImageSet,
    Image,
<<<<<<< HEAD
    Score,
    VoiceRecordPop,
    Record
)
=======
    Score
    )
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
from django.contrib.auth.models import User
import json
import logging
from . import analytics
from django.utils import timezone
import csv
from django.contrib import messages
from django.core import serializers

# DEBUGGING
logger = logging.getLogger(__name__)

# Create your views here.

# def get_csv(request):
# 	# response content type
#     if request.method == 'POST':
#         cli_id = json.loads(request.body)
#         logger.error(cli_id)
#         user = request.user
#         try:
#             client = Client.objects.get(clinician=request.user,id_num=cli_id)
#             utils.export_as_csv(client)
#             is_valid = {
#                 "valid":True
#             }
#         except:
#             is_valid = {
#                 "valid":False
#             }
#         return JsonResponse(is_valid)

# def get_csv(request):
<<<<<<< HEAD


def get_csv(request):
    # response content type
=======
def get_csv(request):
	# response content type
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
    if request.is_ajax and request.method == "GET":
        cli_id = request.GET.get("cli_id")
        # cli_id = json.loads(request.body)
        logger.error(cli_id)
        user = request.user
        # try:
<<<<<<< HEAD
        # does this client have a link to a given clinician
        # client = Client.objects.get(clinician=request.user,id_num=cli_id)
=======
            # does this client have a link to a given clinician
            # client = Client.objects.get(clinician=request.user,id_num=cli_id)
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15

        # Error - there is NO client that is connected to the active clinician, whether data exists is inconsequential
        try:
            client = Client.objects.get(id_num=cli_id)
        except:
            is_valid = {
<<<<<<< HEAD
                "valid": False
            }
            return JsonResponse(is_valid, status=201)
        print(client)
        # queryset is an array of score objects for a given client
=======
                "valid":False
            }
            return JsonResponse(is_valid, status=201)
        print(client)
        # queryset is an array of score objects for a given client 
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
        queryset = Score.objects.filter(user=client)
        print(queryset)
        if queryset.exists():

            meta = queryset[0]._meta
            field_names = [field.name for field in meta.fields]
<<<<<<< HEAD
            name = "Client_Data_Model_Instance_" + \
                str(client.id) + str(timezone.now())
=======
            name = "Client_Data_Model_Instance_" + str(client.id) + str(timezone.now())
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15

            print(name)

            response = HttpResponse(content_type='text/csv')
<<<<<<< HEAD
            response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
                name)
=======
            response['Content-Disposition'] = 'attachment; filename={}.csv'.format(name)
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15

            print("DEBUG_1")

            writer = csv.writer(response)
            writer.writerow(field_names)
            for obj in queryset:
<<<<<<< HEAD
                row = writer.writerow([getattr(obj, field)
                                       for field in field_names])

            print("DEBUG_2")

            return response

        # Error - there is a client with that id that is connected to the active clinician BUT NO data exists
        else:
            is_valid = {
                "valid": False
=======
                row = writer.writerow([getattr(obj, field) for field in field_names])

            print("DEBUG_2")


            return response

        # Error - there is a client with that id that is connected to the active clinician BUT NO data exists
        else: 
            is_valid = {
                "valid":False
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
            }
            return JsonResponse(is_valid, status=202)
        # Success - Here there is a client that is connected to the active clinician AND data exists
        is_valid = {
<<<<<<< HEAD
            "valid": True
=======
            "valid":True
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
        }
        return JsonResponse(is_valid, status=200)


def check_cli_num(request):
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        cli_num = request.GET.get("cli_num")
        logger.error(cli_num)
        user = request.user
<<<<<<< HEAD
        response = analytics.check_cli_num(user, cli_num)
        return JsonResponse(response)


=======
        response = analytics.check_cli_num(user,cli_num)
        return JsonResponse(response)

>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
def save_cli_data(request):
    if request.method == 'POST':
        cli_data = json.loads(request.body)
        logger.error(cli_data)
        user = request.user
<<<<<<< HEAD
        analytics.save_cli_data(user, cli_data)
        return HttpResponse("Success")


def get_client_data(request):
    if request.method == "GET":
        clients = Client.objects.filter(clinician=request.user)
=======
        analytics.save_cli_data(user,cli_data)
        return HttpResponse("Success")

def get_client_data(request):
    if request.method == "GET":
        clients = Client.objects.filter(clinician = request.user)
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
        clients_id = []
        for client in clients:
            clients_id.append(client.id_num)
        print(clients_id)
        clients_json = {
<<<<<<< HEAD
            "clients": clients_id
        }
        return JsonResponse(clients_json)


def index(request):
    return render(request, 'main_app/index copy.html')

=======
            "clients":clients_id
        }
        return JsonResponse(clients_json)

def index(request):
    return render(request,'main_app/index copy.html')
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15

def signin(request):
    return render(request, 'main_app/src/sign-in/signin.html')

<<<<<<< HEAD

def signin_test(request):
    return render(request, 'main_app/src/sign-in/sign_in.html')


def dashboard(request):
    # current_user = request.user
    context = {
        "testing": '''<image class="image-fluid" height="255" width= "100%" src="/static/I_Spy 1.png" />'''}
    return render(request, 'main_app/src/dashboard/dashboard_collection.html', context)

# This function loads the dashboard


def dashboard_test(request):

    # Checking if the user that is requesting is authenticated
    if request.user.is_authenticated:
        current_user = request.user
        print("current user: ", current_user)
        # clinician = account_models.Clinician.objects.get(user=request.user)

        # Filtering collection for requested user
        # Filter out the collections for the requested user
        collections = ImageSet.objects.filter(clinician=request.user)
=======
def signin_test(request):
    return render(request, 'main_app/src/sign-in/sign_in.html')

def dashboard(request):
    #current_user = request.user
    context = {"testing": '''<image class="image-fluid" height="255" width= "100%" src="/static/I_Spy 1.png" />'''}
    return render(request,'main_app/src/dashboard/dashboard_collection.html',context)

# This function loads the dashboard
def dashboard_test(request):

    if request.user.is_authenticated:                               # Checking if the user that is requesting is authenticated
        current_user = request.user
        print("current user: ", current_user)
        #clinician = account_models.Clinician.objects.get(user=request.user)

        # Filtering collection for requested user
        collections = ImageSet.objects.filter(clinician=request.user)       # Filter out the collections for the requested user
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
        # This part is for showing 3 collections per row
        collections_row = len(collections) // 3
        collections_remainder = len(collections) % 3
        collections_array = []
        for i in range(collections_row):
            starting_index = i * 3
<<<<<<< HEAD
            temp = [collections[starting_index],
                    collections[starting_index + 1], collections[starting_index + 2]]
=======
            temp = [collections[starting_index],collections[starting_index + 1],collections[starting_index + 2]]
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
        if collections_remainder > 0:
            last_index = 3 * collections_row
            temp = []
            for i in range(collections_remainder):
                temp.append(collections[last_index+i])
            collections_array.append(temp)
<<<<<<< HEAD

=======
        
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
        # This part is for showing 3 images per row
        images = Image.objects.filter(clinician=request.user)
        print("Image: ", images)
        print(len(images))
        image_row = len(images) // 3
        remain = len(images) % 3
        image_array = []
        for i in range(image_row):
            starting_index = i * 3
<<<<<<< HEAD
            temp = [images[starting_index],
                    images[starting_index + 1], images[starting_index + 2]]
=======
            temp = [images[starting_index], images[starting_index + 1], images[starting_index + 2]]
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
            image_array.append(temp)
        if remain > 0:
            last_index = 3 * image_row
            temp = []
            for i in range(remain):
                temp.append(images[last_index + i])
            image_array.append(temp)
        print(image_array)
        # Put the images and collections as JSON object
        context = {
<<<<<<< HEAD
            "images": image_array,
            "collections": collections_array,
        }
        print(context)
        return render(request, 'main_app/src/dashboard/dashboard_.html', context)
    else:
        return redirect('accounts:signin')


def child_image(request):
    return render(request, 'main_app/src/child-image/child-image.html')


=======
            "images":image_array,
            "collections":collections_array,
        }
        print(context)
        return render(request,'main_app/src/dashboard/dashboard_.html',context)
    else:
        return redirect('accounts:signin')

def child_image(request):
    return render(request, 'main_app/src/child-image/child-image.html')

>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
def child_image_test(request):
    return render(request, 'main_app/src/child-image/child_image.html')


def signup(request):
<<<<<<< HEAD
    return render(request, 'main_app/src/create_account/create_account.html')


def download_csv(request):
    return render(request, 'main_app/src/download_data/download_data.html')


def upload_file(request):
    if request.user.is_authenticated:               # Check if the user requesting access is authenticated user
        if request.method == "POST":
            # Get the file from the POST request
            form = UploadFileForm(request.POST, request.FILES)
            print(request.POST['title'])
            if form.is_valid():                     # Check if the form was valid
                print("valid form")
                # image_form = form.save(commit=False)
                # clinician = account_models.Clinician.objects.get(user=request.user)
                # print("clincian:",clincian.user.email)
                # Set default coordinates of point 1 and 2 to be 0,0
                default_coord = [0, 0, 0, 0]

                # Make an Image Object for database and save the image
                image_model = Image(
                    image=request.FILES['file'], title=request.POST['title'], clinician=request.user, coords=default_coord)
                image_model.save()
                # form.coords = [0,0,0,0]
                # form.save()
                # utils.save_uploaded_file(request.POST['title'],request.FILES)
                print("Image Saved")
                print("image url:", image_model.image.url)
                print("Image time:", image_model.created)
                print("Image detail:", image_model.pk)
                print("Image id:", image_model.id)
                # Redirect the user to editing page
                return redirect('main_app:editview', pk=image_model.pk)
        else:
            form = UploadFileForm()
            # form = UploadImageForm()
        return render(request, 'main_app/index.html', {'form': form})
=======
    return render(request,'main_app/src/create_account/create_account.html')

def download_csv(request):
    return render(request,'main_app/src/download_data/download_data.html')

def upload_file(request):
    if request.user.is_authenticated:               # Check if the user requesting access is authenticated user
        if request.method == "POST":                
            form = UploadFileForm(request.POST,request.FILES)   # Get the file from the POST request
            print(request.POST['title'])
            if form.is_valid():                     # Check if the form was valid
                print("valid form")
                #image_form = form.save(commit=False)
                #clinician = account_models.Clinician.objects.get(user=request.user)
                #print("clincian:",clincian.user.email)
                default_coord = [0,0,0,0]           # Set default coordinates of point 1 and 2 to be 0,0

                # Make an Image Object for database and save the image
                image_model = Image(image=request.FILES['file'],title=request.POST['title'],clinician=request.user,coords=default_coord)
                image_model.save()
                #form.coords = [0,0,0,0]
                #form.save()
                #utils.save_uploaded_file(request.POST['title'],request.FILES)
                print("Image Saved")
                print("image url:", image_model.image.url)
                print("Image time:",image_model.created)
                print("Image detail:",image_model.pk)
                print("Image id:",image_model.id)
                return redirect('main_app:editview',pk=image_model.pk)      # Redirect the user to editing page
        else:
            form = UploadFileForm()
            #form = UploadImageForm()
        return render(request,'main_app/index.html',{'form':form})
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
    else:
        return redirect('accounts:signin')

# Generates the URL for session
<<<<<<< HEAD


def make_meeting(request):
    room_name = utils.get_room_name()                       # Generates random string
    print(request.POST.get("pk"))
    # Gets the public key of collection which clinician chose
    pk = request.POST.get("pk")
    client_num = request.POST.get("client_num")
    # Gets the ClientID from the Client Number which clinician chose
    client_id = Client.objects.get(id_num=client_num).pk
    print(request.META['HTTP_HOST'])
    # Returns the domain name
    domain_name = request.META['HTTP_HOST']

    # Generates the url for client and clinician
    client_room_name = domain_name + "/main_app/client/" + room_name + "/" + pk
    clinician_room_name = domain_name + "/main_app/cli/" + \
        room_name + '/' + pk + "/" + str(client_num)
    # return render(request,'main_app/room_name.html',{'room_name':room_name})

    # Put the URL as JSON Object to send it to user
    data = {'clinician': clinician_room_name,
            'client': client_room_name
            }
    return JsonResponse(data)


def client_game(request):
    return render(request, 'main_app/client_game.html')


def clinician_game(request):
    return render(request, 'main_app/clinician_game.html')

# Loads the clinician page of the session


def clinician_test(request, room_name, pk, client_id):
    print("clinician:" + room_name)
    print("pk:", pk)
    # Gets collection with the public key that clinician chose
    collection = ImageSet.objects.get(pk=pk)
=======
def make_meeting(request):
    room_name = utils.get_room_name()                       # Generates random string
    print(request.POST.get("pk"))
    pk = request.POST.get("pk")                             # Gets the public key of collection which clinician chose
    client_num = request.POST.get("client_num") 
    client_id = Client.objects.get(id_num=client_num).pk    # Gets the ClientID from the Client Number which clinician chose
    print(request.META['HTTP_HOST'])
    domain_name = request.META['HTTP_HOST']                 # Returns the domain name

    # Generates the url for client and clinician
    client_room_name = domain_name + "/main_app/client/" + room_name + "/" + pk 
    clinician_room_name = domain_name + "/main_app/cli/" + room_name + '/' + pk + "/" + str(client_num)
    #return render(request,'main_app/room_name.html',{'room_name':room_name})
    
    # Put the URL as JSON Object to send it to user
    data = {'clinician':clinician_room_name,
            'client':client_room_name
            }
    return JsonResponse(data)

def client_game(request):
    return render(request,'main_app/client_game.html')

def clinician_game(request):
    return render(request,'main_app/clinician_game.html')

# Loads the clinician page of the session
def clinician_test(request,room_name,pk,client_id):
    print("clinician:" + room_name)
    print("pk:",pk)
    collection = ImageSet.objects.get(pk=pk)        # Gets collection with the public key that clinician chose
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
    # Gets the images in the collection
    images = [
        collection.pic1,
        collection.pic2,
        collection.pic3,
        collection.pic4,
        collection.pic5,
        collection.pic6,
        collection.pic7,
        collection.pic8,
        collection.pic9,
        collection.pic10,
        collection.pic11,
    ]
    print(images)
<<<<<<< HEAD
    return render(request, 'main_app/clinician_game.html', {
        'room_name': room_name,
        "set_images": images
    })

# Loads the client page of the session


def client_test(request, room_name, pk):
    print("client" + room_name)
    # Gets collection with the public key that clinician chose
    collection = ImageSet.objects.get(pk=pk)
=======
    return render(request, 'main_app/clinician_game.html',{
        'room_name':room_name,
        "set_images":images
    })

# Loads the client page of the session
def client_test(request,room_name,pk):
    print("client" + room_name)
    collection = ImageSet.objects.get(pk=pk)        # Gets collection with the public key that clinician chose 
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
    # Gets the image in the collection
    images = [
        collection.pic1,
        collection.pic2,
        collection.pic3,
        collection.pic4,
        collection.pic5,
        collection.pic6,
        collection.pic7,
        collection.pic8,
        collection.pic9,
        collection.pic10,
        collection.pic11,
    ]
    print(images)
<<<<<<< HEAD
    return render(request, "main_app/client_game.html", {
        'room_name': room_name,
        "set_images": images
    })

# Editing image's area of interest and title


def edit_view(request, pk):
    print(pk)
    if request.user.is_authenticated:
        # Load the image model from database
        image_model = Image.objects.get(pk=pk)
        print("image url:", image_model.image.url)
        print("image title:", image_model.title)
        # Gets the area of the interest coordinates of the image
        image_points = image_model.coords
        # The structre is save [x1,y1,x2,y2] where x1 and y1 is top left of the rectangle and x2,y2 is bottom right of the rectangle
        # Default is 0,0 and 0,0
        if(image_points == [0, 0, 0, 0]):
            image_points = None
        print(image_points)
        context = {
            "image": image_model,
            "points": image_points
        }
        return render(request, 'main_app/src/edit_view/edit_view.html', context=context)
    else:
        redirect('accounts:signin')


def save_image_edit(request):
    print(request.POST.get("points"))
    print(request.POST)
    # Gets the public key of the image
    image_pk = request.POST.get("image_pk")
    # Gets the Image model corresponding to public key
    image_model = Image.objects.get(pk=image_pk)
    print(image_model.coords)
    # Gets the points of the area of interest
    points = json.loads(request.POST.get("points"))
    print(points["top_left"])
    # Parse the data so we have only two points (Top Left and Bottom Right)
    points_arr = [points["top_left"][0], points["top_left"][1],
                  points["bottom_right"][0], points["bottom_right"][1]]
    print(points_arr)
    image_model.coords = points_arr
    image_model.title = json.loads(request.POST.get("title"))
    # image_model.coords = points_arr
    # Save the Image model to database
    image_model.save()
    print("coord check:", image_model.coords)
    return JsonResponse({"worked": True})

# Loads the creation of collection view/page


def create_collection_view(request):
    if request.user.is_authenticated:
        current_user = request.user
        # clinician = account_models.Clinician.objects.get(user=current_user)
        # Loads the ImageSet for the clinician
        collections = ImageSet.objects.filter(clinician=request.user)
        # collections_pk = collections.pk
        # Loads the images that is uploaded by the clinician
        images = Image.objects.filter(clinician=request.user)
=======
    return render(request,"main_app/client_game.html",{
        'room_name':room_name,
        "set_images":images
    })
            
# Editing image's area of interest and title
def edit_view(request,pk):
    print(pk)
    if request.user.is_authenticated:
        image_model = Image.objects.get(pk=pk)                  # Load the image model from database
        print("image url:",image_model.image.url)
        print("image title:", image_model.title)
        image_points = image_model.coords                       # Gets the area of the interest coordinates of the image
                                                                # The structre is save [x1,y1,x2,y2] where x1 and y1 is top left of the rectangle and x2,y2 is bottom right of the rectangle
        if(image_points == [0,0,0,0]):                          # Default is 0,0 and 0,0
            image_points = None                                 
        print(image_points)
        context ={
            "image":image_model,
            "points":image_points
        }
        return render(request,'main_app/src/edit_view/edit_view.html',context=context)
    else:
        redirect('accounts:signin')

def save_image_edit(request):
    print(request.POST.get("points"))
    print(request.POST)
    image_pk = request.POST.get("image_pk")                     # Gets the public key of the image
    image_model = Image.objects.get(pk=image_pk)                # Gets the Image model corresponding to public key
    print(image_model.coords)
    points = json.loads(request.POST.get("points"))             # Gets the points of the area of interest
    print(points["top_left"])
    points_arr = [points["top_left"][0],points["top_left"][1],points["bottom_right"][0],points["bottom_right"][1]]      # Parse the data so we have only two points (Top Left and Bottom Right)
    print(points_arr)
    image_model.coords = points_arr 
    image_model.title = json.loads(request.POST.get("title"))
    #image_model.coords = points_arr
    image_model.save()                                          # Save the Image model to database
    print("coord check:",image_model.coords)
    return JsonResponse({"worked":True})

# Loads the creation of collection view/page
def create_collection_view(request):
    if request.user.is_authenticated:
        current_user = request.user
        #clinician = account_models.Clinician.objects.get(user=current_user)
        collections = ImageSet.objects.filter(clinician=request.user)           # Loads the ImageSet for the clinician
        #collections_pk = collections.pk
        images = Image.objects.filter(clinician=request.user)                   # Loads the images that is uploaded by the clinician
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
        print("Image: ", images)
        print(len(images))
        # These are for showing 3 enteries per row
        image_row = len(images) // 3
        remain = len(images) % 3
        image_array = []
        for i in range(image_row):
            starting_index = i * 3
<<<<<<< HEAD
            temp = [images[starting_index],
                    images[starting_index + 1], images[starting_index + 2]]
=======
            temp = [images[starting_index], images[starting_index + 1], images[starting_index + 2]]
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
            image_array.append(temp)
        if remain > 0:
            last_index = 3 * image_row
            temp = []
            for i in range(remain):
                temp.append(images[last_index + i])
            image_array.append(temp)
        print(image_array)
        context = {
<<<<<<< HEAD
            "images": image_array,
        }
        print(context)
        return render(request, 'main_app/src/dashboard/dashboard_collection.html', context)
    return render(request, 'main_app/src/dashboard/dashboard_collection.html')

# Handles the request when clinician creates collection


def create_collection(request):
    # Gets the public keys of the selected Image Model
    images_id = json.loads(request.POST.get("selected_image"))
    print(images_id)
    current_user = request.user
    # clinician = account_models.Clinician.objects.get(user=current_user)
    # print(clinician)
    # Gets the public key of the ImageSet Model
    collection_pk = json.loads(request.POST.get("collection_pk"))
    # If the public key is below 0, create new ImageSet Model.
=======
            "images":image_array,
        }
        print(context)
        return render(request,'main_app/src/dashboard/dashboard_collection.html',context)
    return render(request,'main_app/src/dashboard/dashboard_collection.html')

# Handles the request when clinician creates collection
def create_collection(request):
    images_id = json.loads(request.POST.get("selected_image"))          # Gets the public keys of the selected Image Model
    print(images_id)
    current_user = request.user
    #clinician = account_models.Clinician.objects.get(user=current_user)
    #print(clinician)
    collection_pk = json.loads(request.POST.get("collection_pk"))       # Gets the public key of the ImageSet Model
    # If the public key is below 0, create new ImageSet Model. 
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
    if(collection_pk < 0):
        image_set = ImageSet()
    else:
        image_set = ImageSet.objects.get(pk=collection_pk)
<<<<<<< HEAD

=======
    
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
    image_set.clinician = request.user
    image_set.title = json.loads(request.POST.get("title"))
    fields = image_set._meta.get_fields()
    print(type(fields[3]))
    i = 3
<<<<<<< HEAD
    # for image_id in images_id:
    #    temp_model = fields[i]
    #    temp_model = account_models.Image.objects.get(pk=image_id)

    #    i+=1

    # Save the selected Image Models to the ImageSet Model
=======
    #for image_id in images_id:
    #    temp_model = fields[i]
    #    temp_model = account_models.Image.objects.get(pk=image_id)
        
    #    i+=1

    # Save the selected Image Models to the ImageSet Model 
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
    image_set.pic1 = Image.objects.get(pk=images_id[0])
    image_set.pic2 = Image.objects.get(pk=images_id[1])
    image_set.pic3 = Image.objects.get(pk=images_id[2])
    image_set.pic4 = Image.objects.get(pk=images_id[3])
    image_set.pic5 = Image.objects.get(pk=images_id[4])
    image_set.pic6 = Image.objects.get(pk=images_id[5])
    image_set.pic7 = Image.objects.get(pk=images_id[6])
    image_set.pic8 = Image.objects.get(pk=images_id[7])
    image_set.pic9 = Image.objects.get(pk=images_id[8])
    image_set.pic10 = Image.objects.get(pk=images_id[9])
    image_set.pic11 = Image.objects.get(pk=images_id[10])
<<<<<<< HEAD
    for i in range(3, 14):
        print(fields[i])
    # Save the ImageSet Model to database
    image_set.save()
    print(image_set.pic1.pk)
    return JsonResponse({"sucess": True})

# Handles request of editing the entry of Images in existing ImageSet


def edit_collection_view(request, pk):
    if request.user.is_authenticated:
        print(pk)
        # Loads the ImageSet Model with given public key
        collection_model = ImageSet.objects.get(pk=pk)
        collection_image = [[collection_model.pic1, collection_model.pic2, collection_model.pic3],
                            [collection_model.pic4, collection_model.pic5,
                                collection_model.pic6],
                            [collection_model.pic7, collection_model.pic8,
                                collection_model.pic9],
                            [collection_model.pic10, collection_model.pic11]
                            ]
        current_user = request.user
        # clinician = Clinician.objects.get(user=current_user)
        image_array = get_images(current_user)
        title = collection_model.title
        context = {
            "collection": collection_image,
            "images": image_array,
            "collection_pk": pk,
            "collection_title": title
        }
        return render(request, 'main_app/src/dashboard/dashboard_collection.html', context)

    return render(request, 'main_app/src/dashboard/dashboard_collection.html')
=======
    for i in range(3,14):
        print(fields[i])
    image_set.save()                                            # Save the ImageSet Model to database
    print(image_set.pic1.pk)
    return JsonResponse({"sucess":True})

# Handles request of editing the entry of Images in existing ImageSet
def edit_collection_view(request,pk):
    if request.user.is_authenticated:
        print(pk)
        collection_model = ImageSet.objects.get(pk=pk)          # Loads the ImageSet Model with given public key
        collection_image = [[collection_model.pic1,collection_model.pic2,collection_model.pic3],
                            [collection_model.pic4,collection_model.pic5,collection_model.pic6],
                            [collection_model.pic7,collection_model.pic8,collection_model.pic9],
                            [collection_model.pic10,collection_model.pic11]
        ]
        current_user = request.user
        #clinician = Clinician.objects.get(user=current_user)
        image_array = get_images(current_user)
        title = collection_model.title
        context = {
            "collection":collection_image,
            "images": image_array,
            "collection_pk":pk,
            "collection_title":title
        }
        return render(request,'main_app/src/dashboard/dashboard_collection.html',context)


    return render(request,'main_app/src/dashboard/dashboard_collection.html')
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15


# Helper function for getting Image models uploaded by the clinician
def get_images(clinician):
<<<<<<< HEAD
    # clinician = account_models.Clinician.objects.get(user=current_user)
    # collections = account_models.ImageSet.objects.filter(clinician=clinician)
    # collections_pk = collections.pk
    # Loads all the Image models uploaded by clinician
    images = Image.objects.filter(clinician=clinician)
    # print("Image: ", images)
    # print(len(images))
=======
    #clinician = account_models.Clinician.objects.get(user=current_user)
    #collections = account_models.ImageSet.objects.filter(clinician=clinician)
    #collections_pk = collections.pk
    images = Image.objects.filter(clinician=clinician)          # Loads all the Image models uploaded by clinician
    #print("Image: ", images)
    #print(len(images))
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15

    # Show only 3 enteries per row
    image_row = len(images) // 3
    remain = len(images) % 3
    image_array = []
    for i in range(image_row):
        starting_index = i * 3
<<<<<<< HEAD
        temp = [images[starting_index],
                images[starting_index + 1], images[starting_index + 2]]
=======
        temp = [images[starting_index], images[starting_index + 1], images[starting_index + 2]]
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
        image_array.append(temp)
    if remain > 0:
        last_index = 3 * image_row
        temp = []
        for i in range(remain):
            temp.append(images[last_index + i])
        image_array.append(temp)
<<<<<<< HEAD
    return image_array

#################################################################
# Spinner Stuff


def spinner(request):
    return render(request, 'main_app/src/spinner/spinner.html')


def spinner_update(request):
    if request.method == 'POST':
        s_form = SpinnerUpdateForm(
            request.POST, request.FILES, instance=request.user.spinner)
        if s_form.is_valid():
            s_form.save()
            messages.success(request, f"Your spinner has been updated.")
            # cant just be spinner_update, must have main_app
            return redirect('main_app:spinner_update')
    else:
        s_form = SpinnerUpdateForm(instance=request.user.spinner)

    context = {
        's_form': s_form
    }

    return render(request, 'main_app/src/spinner/spinner_update.html', context)

=======
    return image_array  

#################################################################
#Spinner Stuff

def spinner(request):
    return render(request, 'main_app/src/spinner/spinner.html' )

def spinner_update(request):
    if request.method == 'POST':
        s_form = SpinnerUpdateForm(request.POST, request.FILES, instance=request.user.spinner)
        if s_form.is_valid():
            s_form.save()
            messages.success(request, f"Your spinner has been updated.")
            #cant just be spinner_update, must have main_app
            return redirect('main_app:spinner_update') 
    else:
        s_form = SpinnerUpdateForm(instance=request.user.spinner)
        

    context = {
        's_form':s_form
    }

    return render(request, 'main_app/src/spinner/spinner_update.html', context)  
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15

def main(request):
    return render(request, 'main_app/src/voice_games/main.html')

<<<<<<< HEAD

def main2(request):
    return render(request, 'main_app/src/voice_games/main2.html')


def pop(request):
    # currently it can create an new object everytime it submit but the content is hardcoded here.
    '''
    p_form = RecordFormLight(request.POST, request.FILES)
    if request.method == 'POST':#need to filter a specific object with a session id to keep incrementing
        p = Record(user_id = request.user.id, date = timezone.now(), correct = 0, incorrect = 0, notes = "Pop game notes")
        p.save(force_insert=True)


    context = {
        'p_form': p_form,
    }
    '''
    return render(request, 'main_app/src/voice_games/pop.html')
def pop_cli(request):
    return render(request, 'main_app/src/voice_games/pop_cli.html')
def pop_nvb(request):
    return render(request, 'main_app/src/voice_games/pop_nvb.html')


def pancake(request):
    return render(request, 'main_app/src/voice_games/pancake.html')
def pancake_cli(request):
    return render(request, 'main_app/src/voice_games/pancake_cli.html')
def pancake_nvb(request):
    return render(request, 'main_app/src/voice_games/pancake_nvb.html')

def cookies(request):
    return render(request, 'main_app/src/voice_games/cookies.html')


def light(request):
    return render(request, 'main_app/src/voice_games/light.html')
def light_cli(request):
    return render(request, 'main_app/src/voice_games/light_cli.html')
def light_nvb(request):
    return render(request, 'main_app/src/voice_games/light_nvb.html')


def custom_setup(request):
    if request.method == 'POST':
        v_form = VoicePicForm(request.POST, request.FILES,
                              instance=request.user.voice_game2)
        w_form = VoiceWordsForm(
            request.POST, request.FILES, instance=request.user.voice_words2)
=======
def main2(request):
    return render(request, 'main_app/src/voice_games/main2.html')

def pop(request):
    return render(request, 'main_app/src/voice_games/pop.html')

def pancake(request):
    return render(request, 'main_app/src/voice_games/pancake.html')

def light(request):
    return render(request, 'main_app/src/voice_games/lights.html')

def custom_setup(request):
    if request.method == 'POST':
        v_form = VoicePicForm(request.POST, request.FILES, instance=request.user.voice_game2)
        w_form = VoiceWordsForm(request.POST, request.FILES, instance=request.user.voice_words2)
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
        if v_form.is_valid() and w_form.is_valid():
            v_form.save()
            w_form.save()
            messages.success(request, f"Your game has been updated.")
<<<<<<< HEAD
            # cant just be spinner_update, must have main_app
            return redirect('main_app:custom_setup')
    else:
        v_form = VoicePicForm(instance=request.user.voice_game2)
        w_form = VoiceWordsForm(instance=request.user.voice_words2)

    context = {
        'v_form': v_form,
        'w_form': w_form
    }

    return render(request, 'main_app/src/voice_games/custom_setup.html', context)


def custom_game(request):
    return render(request, 'main_app/src/voice_games/custom_game.html')
def custom_game_cli(request):
    return render(request, 'main_app/src/voice_games/custom_game_cli.html' )
=======
            #cant just be spinner_update, must have main_app
            return redirect('main_app:custom_setup') 
    else:
        v_form = VoicePicForm(instance=request.user.voice_game2)
        w_form = VoiceWordsForm(instance=request.user.voice_words2)
        

    context = {
        'v_form':v_form,
        'w_form':w_form
    }
  
    return render(request, 'main_app/src/voice_games/custom_setup.html', context)

def custom_game(request):
    return render (request, 'main_app/src/voice_games/custom_game.html')

def post_voice(request):
    if request.is_ajax and request.method == "POST":
        form = RecordForm(request.POST)

        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance,])
            return JsonResponse({"instance":ser_instance}, status = 200)
        else:
            return JsonResponse({"error": form.errors}, status = 400)
    return JsonResponse({"error":""}, status = 400)
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
