from django.shortcuts import render, redirect
from .models import Bucket, Trash
from django.views.generic.list import ListView
from django.views.generic import CreateView
from .forms import TrashSearchForm

def home(request):
    return render(
        request, "core/home.html", {"title": "Home", "posts": Bucket.objects.all()}
    )

class TrashSearchView(ListView):
    model = Trash
    template_name = "core/home.html"
    context_object_name = 'trashes'
    form_class = TrashSearchForm

    def get_queryset(self):
        queryset = super(TrashSearchView, self).get_queryset()
        search_term = self.request.GET.get('search_term', '')
        if search_term:
            queryset = queryset.filter(trash_name__iexact = search_term)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trashes"] = self.object_list
        return context
