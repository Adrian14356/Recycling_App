from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Dear {username} you have ben successful signed up!")
            return redirect("home")

    else:
        form = UserRegistrationForm()

    return render(request, "users/register.html", {"form" : form})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request,  'You have been logged in')
                return redirect('home')

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="users/login.html",
        context={'form': form}
    )
