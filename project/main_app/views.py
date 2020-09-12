from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'main_app/index copy.html')

def client_game(request):
    return render(request,'main_app/client_game.html')

def clinician_game(request):
    return render(request,'main_app/clinician_game.html')

def clinician_test(request,room_name):
    print(room_name)
    return render(request, 'main_app/clinician_game.html',{
        'room_name':room_name
        })