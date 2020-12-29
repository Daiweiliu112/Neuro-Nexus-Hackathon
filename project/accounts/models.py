from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from PIL import Image as Img
<<<<<<< HEAD
from django.utils import timezone
=======
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15


IMAGE_MAX_LENGTH=300

############ Game
class Game(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    thumb = models.ImageField(upload_to='main_nav/%Y/%m/%d' ,max_length=IMAGE_MAX_LENGTH,  default="default.png") #

########## Client (NOT an extended user model!)
class Client(models.Model):
    clinician = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150)
    pronouns = models.CharField(max_length=20)
    id_num = models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True)

########## GameTrain
class GameTrain(models.Model):
    user = models.ForeignKey(Client, on_delete=models.PROTECT)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    index = models.IntegerField(null=True,blank=True) # this should default to 1
    started = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

######### Score 
class Score(models.Model):
    user = models.ForeignKey(Client,on_delete=models.PROTECT)
    total_cli = ArrayField(
                        models.IntegerField(null=True,blank=True), 
                        default=[0,0,0,0,0,0,0,0,0,0],
                        size=10,
                    )
    time_t = ArrayField(
                        models.DecimalField(max_digits=12,decimal_places=6,blank=True,null=True), 
                        default=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                        size=10, # binary correct or incorrect
                    )
    incor_cli = ArrayField(
                        models.IntegerField(null=True,blank=True), 
                        default=[0,0,0,0,0,0,0,0,0,0],
                        size=10,
                    )
    cor_cli = ArrayField(
                        models.IntegerField(null=True,blank=True), 
                        default=[0,0,0,0,0,0,0,0,0,0],
                        size=10,
                    )
    cor = ArrayField(
                        models.IntegerField(null=True,blank=True),
                        default=[0,0,0,0,0,0,0,0,0,0],
                        size=10,
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
                        models.PositiveSmallIntegerField(null=True,blank=True),         # x1,y1,x2,y2
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

class Spinner(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image1 = models.ImageField(default = 'pikachu.jpg', upload_to = 'media/main_nav/spinner_pics')
    image2 = models.ImageField(default = 'pikachu.jpg', upload_to = 'spinner_pics')
    image3 = models.ImageField(default = 'pikachu.jpg', upload_to = 'spinner_pics')
    image4 = models.ImageField(default = 'pikachu.jpg', upload_to = 'spinner_pics')
    image5 = models.ImageField(default = 'pikachu.jpg', upload_to = 'spinner_pics')
    image6 = models.ImageField(default = 'pikachu.jpg', upload_to = 'spinner_pics')
    image7 = models.ImageField(default = 'pikachu.jpg', upload_to = 'spinner_pics')
    image8 = models.ImageField(default = 'pikachu.jpg', upload_to = 'spinner_pics')
    img_list = [image1, image2, image3, image4, image5, image6, image7, image8]

        # tried using parallel iteration with zip, but apparently image field does not have attribute path now cause an error
        # but it does not seem to causing error outside of iteration.
    def save(self):
        super().save()

        img1 = Img.open(self.image1.path)
        img2 = Img.open(self.image2.path)
        img3 = Img.open(self.image3.path)
        img4 = Img.open(self.image4.path)
        img5 = Img.open(self.image5.path)
        img6 = Img.open(self.image6.path)
        img7 = Img.open(self.image7.path)
        img8 = Img.open(self.image8.path)

        img_list = [img1, img2, img3, img4, img5, img6, img7, img8]

<<<<<<< HEAD
=======
        # tried using parallel iteration with zip, but apparently image field does not have attribute path now cause an error
        # but it does not seem to causing error outside of iteration.

>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15

        for i in img_list:
            if i.height > 200 or i.width > 200 or i.height < 200 or i.width < 200:
                output_size = (200, 200)
                i.thumbnail(output_size)
                if i == img1:
                    i.save(self.image1.path)
                elif i == img2:
                    i.save(self.image2.path)
                elif i == img3:
                    i.save(self.image3.path)
                elif i == img4:
                    i.save(self.image4.path)
                elif i == img5:
                    i.save(self.image5.path)
                elif i == img6:
                    i.save(self.image6.path)
                elif i == img7:
                    i.save(self.image7.path)
                else:
                    i.save(self.image8.path)

class voice_game2(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pic1 = models.ImageField(default = 'pikachu.jpg', upload_to = 'media/main_nav/custom_game')
    pic2 = models.ImageField(default = 'pikachu.jpg', upload_to = 'media/main_nav/custom_game')

<<<<<<< HEAD
## not used
=======
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
class voice_game3(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pic1 = models.ImageField(default = 'pikachu.jpg', upload_to = 'media/main_nav/custom_game')
    pic2 = models.ImageField(default = 'pikachu.jpg', upload_to = 'media/main_nav/custom_game')
    pic3 = models.ImageField(default = 'pikachu.jpg', upload_to = 'media/main_nav/custom_game')

<<<<<<< HEAD
## not used
=======
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
class voice_game4(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pic1 = models.ImageField(default = 'pikachu.jpg', upload_to = 'media/main_nav/custom_game')
    pic2 = models.ImageField(default = 'pikachu.jpg', upload_to = 'media/main_nav/custom_game')
    pic3 = models.ImageField(default = 'pikachu.jpg', upload_to = 'media/main_nav/custom_game')
    pic4 = models.ImageField(default = 'pikachu.jpg', upload_to = 'media/main_nav/custom_game')

class voice_words2(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    title = models.CharField(default = 'Custom Game', max_length=30)
    word1 = models.CharField(max_length=30)
    word2 = models.CharField(max_length=30)

<<<<<<< HEAD
## not being used
class VoiceRecordPop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    correct = models.IntegerField(null=True,blank=True)
    incorrect = models.IntegerField(null=True,blank=True)
    notes = models.TextField(default = 'This is the session notes for the pop game')


## this is the only model for rcord that is in use
class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    correct = models.IntegerField(null=True,blank=True)
    incorrect = models.IntegerField(null=True,blank=True)
    notes = models.TextField(default = 'This is the session notes for the pop game')

## not being used
class voice_record_pancake(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    correct = models.IntegerField(null=True,blank=True)
    incorrect = models.IntegerField(null=True,blank=True)
    notes = models.TextField(default = 'This is the session notes for the pancake game')
## not being used
class voice_record_cookies(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    correct = models.IntegerField(null=True,blank=True)
    incorrect = models.IntegerField(null=True,blank=True)
    notes = models.TextField(default = 'This is the session notes for the cookies game')

=======
class voice_record(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    record1 = models.CharField(max_length=30)
    record2 = models.CharField(max_length=30)
    record3 = models.CharField(max_length=30)
    record4 = models.CharField(max_length=30)
    record5 = models.CharField(max_length=30)
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15

    





