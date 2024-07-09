from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import BorrowBookModel
from accounts.models import AccountModel
from book.models import BookModel
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages

# from book.models import BookModel
class BorrowBook(ListView):
    model = BorrowBookModel
    pk_url_kwarg = 'id'
    template_name = 'profile.html'
    # success_url = reverse_lazy('profile')
    
    
    def get_queryset(self) :
       
        id = self.kwargs.get(self.pk_url_kwarg)
        print(id)
        book = get_object_or_404(BookModel,id = id)
        print('hello',book)
        # user_book = BookModel.objects.filter(user = self.request.user,id = id)
        requested_user = AccountModel.objects.get(user=self.request.user)
        
       

        if book.price< requested_user.balance and book.quantity>0:
            requested_user.balance-= book.price
            book.quantity-=1
            
            requested_user.save()
            book.save()
            messages.success(self.request,'Succssfully Borrowed')

        else:
            messages.warning('You Cannot borrow a book without book price more than account balance ')
            return redirect('home')
        
        BorrowBookModel.objects.create(
            user = self.request.user,
            account = requested_user,
            book = book,
        )
        

        
        
        return super().get_queryset()


