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
    if Client.objects.filter(id_num=cli_num).exists():
        print(cli_num)
        is_valid = {
            "valid":False
        }
    else:
        client = Client(clinician=user,id_num=cli_num)
        print(client)
        client.save()
        is_valid = {
            "valid":True
        }
    return is_valid

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
            

            
            