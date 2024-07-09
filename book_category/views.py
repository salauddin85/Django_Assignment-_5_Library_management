from django.shortcuts import render
from django.views.generic import FormView
from .forms import BooksCategoryForm
from django.urls import reverse_lazy
# Create your views here.
class BookForm(FormView):
    template_name = 'add_book.html'
    form_class = BooksCategoryForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form = form.save()
        return super().form_valid(form)
    
    