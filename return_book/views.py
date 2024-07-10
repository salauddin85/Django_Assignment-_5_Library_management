from django.shortcuts import redirect
from django.views.generic import ListView
from .models import ReturnBookModel
from accounts.models import AccountModel
# from book.models import BookModel
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from book.models import BookModel
from borrow_book.models import BorrowBookModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required,name='dispatch')
class ReturnBook(ListView):
    model = ReturnBookModel
    pk_url_kwarg = 'id'
    template_name = 'profile.html'
    

    def get_queryset(self) :
       
        id = self.kwargs.get(self.pk_url_kwarg)
        print(id)
        book = get_object_or_404(BookModel,id = id)
        
        requested_user = AccountModel.objects.get(user=self.request.user)
        
        requested_user.balance+= book.price
        book.quantity+=1
        requested_user.save()
        book.save()
        messages.success(self.request,'Succssfully Returned')
  
        ReturnBookModel.objects.create(
            user = self.request.user,
            account = requested_user,
            book = book
        )
        
        
        
        return super().get_queryset()


