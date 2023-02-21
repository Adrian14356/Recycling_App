from django.urls import path, include
from . import views
from .views import TrashSearchView

urlpatterns = [
    path("", TrashSearchView.as_view(), name="home"),

]
