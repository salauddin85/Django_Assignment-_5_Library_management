from django import forms
from .models import BookModel,ReviewModel
class BooksForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title','price','image','description']

    

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['name', 'Review']

