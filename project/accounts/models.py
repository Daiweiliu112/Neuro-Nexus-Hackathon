from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

IMAGE_MAX_LENGTH=300

############ Game
class Game(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    thumb = models.ImageField(upload_to='main_nav/%Y/%m/%d' ,max_length=IMAGE_MAX_LENGTH,  default="default.png") #

########## GameTrain
class GameTrain(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    index = models.IntegerField(null=True,blank=True) # this should default to 1
    started = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


########## Client (NOT an extended user model!)
class Client(models.Model):
    clinician = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150)
    pronouns = models.CharField(max_length=20)
    id_num = models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True)

######### Score 
class Score(models.Model):
    user = models.ForeignKey(Client,on_delete=models.PROTECT)
    main_data = ArrayField(
                        models.DecimalField(max_digits=12,decimal_places=6,blank=True,null=True), 
                        size=10, # binary correct or incorrect
                    )
    computed_nums = ArrayField(
                        models.DecimalField(max_digits=12,decimal_places=6,blank=True,null=True), 
                        size=1,
                    )
    index = models.IntegerField(null=True,blank=True)
    game_train = models.ForeignKey(GameTrain,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


############ Image
class Image(models.Model):
    image = models.ImageField(upload_to='main_nav/%Y/%m/%d' ,max_length=IMAGE_MAX_LENGTH,  default="default.png") #
    title = models.CharField(max_length=50)
    clinician = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    coords = ArrayField( # bounding box for target object
                        models.PositiveSmallIntegerField(null=True,blank=True), 
                        size=4,
                    )

############ ImageSet
class ImageSet(models.Model):
    clinician = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    pic1 = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='pic1')
    pic2 = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='pic2')
    pic3 = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='pic3')
    pic4 = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='pic4')
    pic5 = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='pic5')
    pic6 = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='pic6')
    pic7 = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='pic7')
    pic8 = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='pic8')
    pic9 = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='pic9')
    pic10 = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='pic10') 
    pic11 = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='pic11')

