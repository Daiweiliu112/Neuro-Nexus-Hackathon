from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# This form is for the initial registeration of the user
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # It uses email as username for registering the user
    class Meta:
        model = User
        fields = ["first_name","last_name","email","password1","password2"]

# This form is for loggin in the user. It takes email as the username to authenticating
class UserAuthForm(AuthenticationForm):
    username = forms.EmailField(label="Email")