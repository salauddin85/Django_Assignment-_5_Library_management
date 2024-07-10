from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from book_category.models import BookCategoryModel
from accounts.models import AccountModel
class BookModel (models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='book')
    title = models.CharField(max_length=50,unique=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    image = models.ImageField(upload_to='book/media/uploads/')
    borrow_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200)
    book_category = models.ManyToManyField(BookCategoryModel)
    quantity = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return f'Title:{self.title} '
    


class ReviewModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=30)
    Review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self) -> str:
        return  f'Reviews by {self.name}'
    