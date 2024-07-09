from django import forms
from .models import BookCategoryModel
class BooksCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategoryModel
        fields = '__all__'