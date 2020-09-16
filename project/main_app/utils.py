

def save_uploaded_file(title, f):
    path = "templates/main_app/uploaded/" + title + ".png"
    with open(path,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)