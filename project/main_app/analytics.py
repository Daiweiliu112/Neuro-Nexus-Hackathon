from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import (
    Client
    )
import json
from django.http import JsonResponse
# from django.db.models import Max
from statistics import stdev, mean
import logging

# DEBUGGING
logger = logging.getLogger(__name__)

def check_cli_num(user,data):
    cli_num = data
    print(data)
    if Client.objects.filter(id_num=cli_num).exists():
        print("exists")
        return JsonResponse({"valid":False}, status = 200)
    else:
        client = Client(clinician=user,id_num=cli_num)
        print(client)
        client.save()
    return JsonResponse({"valid":True}, status = 200)

def save_cli_data(user,data):
    # print(type(data))
    for key in data:
        print(key)
        print('*************************')

    for key, value in data.items():
        if key == "cli_num":
            cli_num = value
            client = Client.objects.get(id_num=cli_num)
        if key == "trial_data":
            print(key)
            

            
            