from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AccountModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='account')
    account_no = models.IntegerField(unique=True,null=True,blank=True)
    balance = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    after_balance = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    
    def __str__(self) :
        return f'{self.user} {self.account_no}'