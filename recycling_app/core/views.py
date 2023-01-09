from django.shortcuts import render
from .models import Bucket, Trash
from django.views.generic.list import ListView
from django.views.generic import CreateView


def home(request):
    return render(
        request, "core/home.html", {"title": "Home", "posts": Bucket.objects.all()}
    )


class BucketListView(ListView):
    model = Bucket
    template_name = "core/home.html"


class TrashAddView(CreateView):
    model = Trash
    template_name = "core/add_trash.html"
    fields = ["bucket", "description", "trash_name"]

    def post(self, request, *args, **kwargs):
        pass


class TrashSearchView(ListView):
    model = Trash
    template_name = "core/home.html"
