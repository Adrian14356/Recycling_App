from django.urls import path
from .views import GetAllTrashes, GetTrash, AddTrash

urlpatterns = [
    path("trashes/", GetAllTrashes.as_view(), name = "get_trashes"),
    path("trash/<int:pk>/", GetTrash.as_view(), name = "get_trash"),
    path("trash/add/", AddTrash.as_view(), name = "add_trash"),
]