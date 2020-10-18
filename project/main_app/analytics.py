from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import (
    Client,
    Score,
    GameTrain,
    Game
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
    # for key in data:
    #     logger.error(key)
    #     logger.error('*************************')
    count = 0
    for key, value in data.items():
        print("key {}: {}".format(count,key))
        print("value {}: {}".format(count,value))
        count += 1

    # Initialize arrays for temporary holding of game data/stats
    total_cli = []
    time_t = []
    incor_cli = []
    cor_cli = []
    cor = []
    computed_nums = []

    for key, value in data.items():
        #
        if key == "cli_num":
            # print("DEBUG 1")
            cli_num = value
            client = Client.objects.get(id_num=cli_num)
        # access and pull out/apart the game info/stats
        if key == "trial_data":
            # print("DEBUG 2")
            for inner_value in range(len(value)):
                print("DEBUG 2")

                print(value[inner_value]) 
                # added ifs incase the clinician skips a trial
                # otherwise there is an empty value and the array's don't like it
                try:
                    total_cli = total_cli + [value[inner_value]['totalClicks']]
                except:
                    total_cli = total_cli + [0]
                
                time_t = time_t + [value[inner_value]['timeElapsed']]

                # try:
                #     incor_cli = incor_cli + [value[inner_value]['incorrectClicks']]
                # except: 
                #     incor_cli = incor_cli + [0]

                if isinstance(value[inner_value]['incorrectClicks'],int) == True:
                    incor_cli = incor_cli + [value[inner_value]['incorrectClicks']]
                else:
                    incor_cli = incor_cli + [0]

                # try: 
                #     cor_cli = cor_cli + [value[inner_value]['correctClicks']]
                # except: 
                #     cor_cli = cor_cli + [0]
                    
                if isinstance(value[inner_value]['correctClicks'],int) == True:
                    cor_cli = cor_cli + [value[inner_value]['correctClicks']]
                else:
                    cor_cli = cor_cli + [0]

                if value[inner_value]['correct'] == True:
                    cor = cor + [1]
                else:
                    cor = cor + [0]
                # print(type(value[inner_value]))
                # for trial in range(len(inner_value):
                #     print(value[inner_value][trial])     
            print(total_cli)
            print(time_t)
            print(incor_cli)
            print(cor_cli)
            print(cor)
            # pretty simple stats - just getting the percent correct - saving in decimal form
            try:
                computed_nums = [sum(cor)/len(cor)]
            except:
                computed_nums = [0.0]

            # check if this game's game model instance has been created if not, make one
            try:
                game = Game.objects.get(title="Find the Thing")
            except:
                game = Game(
                    title = "Find the Thing",
                    body = "You find the thing"
                )
                game.save()



            # check if an existing game train exists for this game, otherwise make one
            try: 
                game_train = GameTrain.objects.get(user=client,game=game)
            except:
                game_train = GameTrain(  
                    user = client,
                    game = game,
                    index = 1
                    )    
                game_train.save()

            # check the current highest index for a game from this client 
            # with a matched game train, otherwise start at index 1
            try:
                score = Score.objects.all().filter(user=client,game_train=game_train).order_by('-index')[0]
                index = score.index
            except:
                index = 1

            #  Make a game train if there isn't one
            # game_train = GameTrain.objects.get(pk=1)

            # Create the  score model tied to the active user (who is tied to the active clinician)
            score = Score(
                user=client,
                total_cli=total_cli,
                time_t=time_t,
                incor_cli=incor_cli,
                cor_cli=cor_cli,
                cor=cor,
                computed_nums=computed_nums,
                index=index,
                game_train=game_train,
                )

            # Save the new score instance + update the game_train index
            print(score)
            score.save()
            game_train.index += 1
            game_train.save()

