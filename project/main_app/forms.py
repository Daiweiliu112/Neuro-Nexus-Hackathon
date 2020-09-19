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