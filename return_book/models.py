from django.db import models

# Create your models here.
from book.models import BookModel
from accounts.models import AccountModel
from django.contrib.auth.models import User

class ReturnBookModel(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    account = models.ForeignKey(AccountModel,on_delete=models.CASCADE)
    return_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return f'{self.user.username} {self.book.title} {self.account.account_no}'