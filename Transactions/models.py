from django.db import models
from .constants import TRANSACTION_TYPE
# Create your models here.
# from book.models import BookModel
# from accounts.models import AccountModel
from django.contrib.auth.models import User

class TransectionModel(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='Transactions')
    # book = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(decimal_places=2,max_digits=10)
    balance = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    transaction_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    transaction_type = models.CharField(max_length=50,choices=TRANSACTION_TYPE,null=True,blank=True)
    

