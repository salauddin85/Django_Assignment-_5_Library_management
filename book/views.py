from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponse
from django.views.generic import FormView,DetailView
from .forms import BooksForm,ReviewForm
from django.urls import reverse_lazy
from .models import BookModel,ReviewModel
# from .models import ReviewModel
from return_book.models import ReturnBookModel
from django.views.generic import TemplateView
from accounts.models import AccountModel
from django.views.generic import ListView



from django.views.generic import FormView
# from .forms import ProfileFormClass  # Replace with your actual form class
from django.views.generic import ListView
# from .models import AccountModel
from borrow_book.models import BorrowBookModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
# from book.forms import ReviewForm

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
    
       
    def post(self,request,*args,**kwargs):
        review_form = ReviewForm(data = self.request.POST)
        book = self.get_object()
        if review_form.is_valid():
            review_form  = review_form.save(commit=False)
            review_form.book = book
            review_form.save()
        return self.get(request,*args,**kwargs)
    def get_context_data(self, **kwargs) :
            
            context = super().get_context_data(**kwargs)
            book = self.get_object()
            review_form = ReviewForm()
            try:
                reviews = ReviewModel.objects.filter(book = book)
            except ReviewModel.DoesNotExist:
                reviews=None
            print('review',reviews)
            
            bought_user = BorrowBookModel.objects.filter(book = book ,user = self.request.user)
            # print(bought_user)
            if bought_user.exists():

                context["review_form"] =  review_form
                context["reviews"] = reviews 
                # print(context['reviews '])
                context['bought_user'] = bought_user
            else:
                context['bought_user'] = None
            return context
        



@method_decorator(login_required,name='dispatch')
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


    

    