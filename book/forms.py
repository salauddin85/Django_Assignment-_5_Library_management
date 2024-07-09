from django import forms
from .models import BookModel
class BooksForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title','price','image','description']