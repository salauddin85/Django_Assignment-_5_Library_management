

from django.contrib.auth.models import User
from django.db import models
from accounts.models import AccountModel
from book.models import BookModel

class BorrowBookModel(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    account = models.ForeignKey(AccountModel,on_delete=models.CASCADE,null=True,blank=True,related_name='account')
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE, null=True,blank=True)
   


