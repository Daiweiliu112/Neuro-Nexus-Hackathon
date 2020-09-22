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
        if key == "trial_data":

            cli_num = value
            clients = user.client_set.all()
            for client in clients:
                if client.id_num = cli_num:
                    send_error

    #     nick_name = request.GET.get("nick_name", None)
    #     # check for the nick name in the database.
    #     if Friend.objects.filter(nick_name = nick_name).exists():
    #         # if nick_name found return not valid new friend
    #         return JsonResponse({"valid":False}, status = 200)
    #     else:
    #         # if nick_name not found, then user can create a new friend.
    #         return JsonResponse({"valid":True}, status = 200)
    # return JsonResponse({}, status = 400)

            
            