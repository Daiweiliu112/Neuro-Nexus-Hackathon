from django.utils.crypto import get_random_string

def save_uploaded_file(title, f):
    path = "templates/main_app/uploaded/" + title + ".png"
    with open(path,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def get_room_name():
    return get_random_string(length=32)