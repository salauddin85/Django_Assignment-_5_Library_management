from django.shortcuts import render,HttpResponse
from django.views.generic import FormView,DetailView
from .forms import BooksForm
from django.urls import reverse_lazy
from .models import BookModel
from return_book.models import ReturnBookModel
from django.views.generic import TemplateView
from accounts.models import AccountModel
from django.views.generic import ListView

# Create your views here.
class BookForm(FormView):
    template_name = 'add_book.html'
    form_class = BooksForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form = form.save()
        return super().form_valid(form)
    
class DetailsBook(DetailView):
    model = BookModel
    pk_url_kwarg = 'id'
    template_name = 'details_book.html'
    # def get_success_url(self):
    #     return reverse_lazy('profile')


from django.views.generic import FormView
# from .forms import ProfileFormClass  # Replace with your actual form class
from django.views.generic import ListView
from .models import AccountModel
from borrow_book.models import BorrowBookModel

class ProfileView(ListView):
    model = AccountModel
    template_name = "profile.html"
    # context_object_name = 'accounts'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = AccountModel.objects.filter(user=self.request.user)
        context['books'] = BorrowBookModel.objects.filter(user=self.request.user)
        context['return_user'] = ReturnBookModel.objects.filter(user=self.request.user)
        context['return_books'] = ReturnBookModel.objects.all()
        # context['returns'] = 
        print(context['books'])
        print(context['return_books'])
        return context

    def get_success_url(self):
        return reverse_lazy('profile')  # Adjust the URL name as needed


    

    