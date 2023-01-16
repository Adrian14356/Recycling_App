from django.urls import path
from .views import GetAllTrashes, GetTrash

urlpatterns = [
    path("trashes/", GetAllTrashes.as_view(), name = "get_trashes"),
    path("/trash?trash_name=?", GetTrash.as_view(), name = "get_trash")
]