from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import (
    ClientClinicianLink,
    Client,
    )
import json
# from django.db.models import Max
from statistics import stdev, mean
import logging

# DEBUGGING
logger = logging.getLogger(__name__)

def check_cli_num(user,data):
    # print(type(data))
    for key in data:
        print(key)
        print('*************************')

    for key, value in data.items():
        if key == "cli_num":
            cli_num = value
            clients = user.client_set.all()
            for client in clients:
                if client.id_num = cli_num:
                    return JsonResponse({"valid":False}, status = 200)
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
            

            
            