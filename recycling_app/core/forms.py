from django import forms
from .models import Trash

class TrashSearchForm(forms.Form):
    class Meta:
        model = Trash
        fields = ["trash_name", "description"]