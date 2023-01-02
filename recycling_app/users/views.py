from .forms import UserRegistrationForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

class RegisterView(CreateView, SuccessMessageMixin):

    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    form_class = UserRegistrationForm
    success_message = ("You have been successful signed up!")