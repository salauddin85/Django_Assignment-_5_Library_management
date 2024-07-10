from django.contrib import admin

# Register your models here.
from .models import BookModel,ReviewModel
admin.site.register(BookModel)
admin.site.register(ReviewModel)