from django.shortcuts import render
from .models import Bucket, Trashes
from django.views.generic.list import ListView
from django.views.generic import CreateView

def home(request):
    return render(request, 'desktop/home.html', {'title' : 'Home', 'posts' : Bucket.objects.all() })

class BucketListView(ListView):
    model = Bucket
    template_name = "desktop/home.html"

class TrashAddView(CreateView):
    model = Trashes
    template_name = "desktop/add_trash.html"
    fields = ["bucket", "description", "trash_name"]

