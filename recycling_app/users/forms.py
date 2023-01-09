from django.contrib.auth.forms import UserCreationForm, User
from django import forms


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password"]

class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "password"]
