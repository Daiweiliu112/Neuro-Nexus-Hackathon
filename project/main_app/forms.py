from django import forms
from accounts import models
from django.db import models as django_models

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class UploadImageForm(forms.ModelForm):
    
    class Meta:
        model = models.Image
        fields = ['title','image']

class SpinnerUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Spinner
        fields = ['image1', 'image2', 'image3', 'image4', 'image4', 'image5', 'image6', 'image7', 'image8']

class VoicePicForm(forms.ModelForm):
    class Meta:
        model = models.voice_game2
        fields = ['pic1','pic2']
class VoiceWordsForm(forms.ModelForm):
    class Meta:
        model = models.voice_words2
        fields = ['title','word1','word2']

class RecordForm(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model = models.VoiceRecordPop
        fields = ['date', 'correct', 'incorrect','notes']

class RecordFormLight(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = ['date','correct', 'incorrect','notes']

class RecordFormPancake(forms.ModelForm):
    class Meta:
        model = models.voice_record_pancake
        fields = ['date','correct', 'incorrect','notes']

class RecordFormCookies(forms.ModelForm):
    class Meta:
        model = models.voice_record_cookies
        fields = ['date','correct', 'incorrect','notes']
=======
        model = models.voice_record
        fields = ['record1','record2','record3','record4','record5']
        widgets = {
            'text':forms.TextInput(attrs = {
                'id':'post-text',
                'required':True,
                'placeholder':'Something...'
            }),
        }
>>>>>>> 2a904ff631a5a2a3d51ea4ffa064617fec668b15
