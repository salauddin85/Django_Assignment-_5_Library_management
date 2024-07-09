from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BookCategoryModel (models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField()
    
   
    def __str__(self) :
        return f'{self.category_name}'