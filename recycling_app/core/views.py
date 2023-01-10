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


class TrashSearchView(ListView):
    model = Trash
    template_name = "core/home.html"

    def post(self, request, *args, **kwargs):
        searched = request.POST["trash_name"]
        all_trashes = Trash.objects.filter(trash_name = searched)
        return render(request, "core/home.html",{"searched" : searched, "all_trashes" : all_trashes })

