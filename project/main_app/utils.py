from django.utils.crypto import get_random_string
from django.http import HttpResponse
from django.utils import timezone
import csv
import logging

# DEBUGGING
logger = logging.getLogger(__name__)

def save_uploaded_file(title, f):
    path = "templates/main_app/uploaded/" + title + ".png"
    with open(path,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def get_room_name():
    name = get_random_string(length=32)
    return name

def export_as_csv(self, request, queryset):

    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    name = "Client_Data_Model_Instance " + meta + "_" + str(timezone.localtime(timezone.now()))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(name)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])
    
    return response
