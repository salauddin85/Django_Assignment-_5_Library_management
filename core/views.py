from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from book.models import BookModel
from book_category.models import BookCategoryModel
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

class ShowsALLBook(ListView):
    model = BookModel
    template_name = 'home.html'
    context_object_name = 'all_books'
    
    
    
    def get_queryset(self):
       
        user_slug = self.kwargs.get('category_slug')
        # data = BookModel.objects.all()
        if user_slug :
            category = BookCategoryModel.objects.get(slug = user_slug)
            return BookModel.objects.filter(book_category= category)
        return BookModel.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categories'] = BookCategoryModel.objects.all()
        return context

