from django.contrib import admin
from .models import BookCategoryModel
# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ['category_name','slug']
admin.site.register(BookCategoryModel,BrandAdmin)