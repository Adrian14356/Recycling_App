from django.urls import path, include
from . import views
from .views import BucketListView, TrashAddView

urlpatterns = [
    path('', BucketListView.as_view(), name = "home"),
    path("add/", TrashAddView.as_view(), name = "add-trash"),
    #path("facts/", name = "facts")
]
