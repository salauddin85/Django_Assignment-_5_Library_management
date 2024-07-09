from django.urls import path
# from .models import BorrowModel
from .views import ReturnBook

urlpatterns = [
    # path('bought_book/<int:id>',BorrowBook.as_view(),name='borrow_book'),
    path('returnbook/<int:id>',ReturnBook.as_view(),name='return_book'),
   
]
