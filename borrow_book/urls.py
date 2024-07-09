from django.urls import path
# from .models import BorrowModel
from .views import BorrowBook

urlpatterns = [
    # path('bought_book/<int:id>',BorrowBook.as_view(),name='borrow_book'),
    path('bought_book/<int:id>',BorrowBook.as_view(),name='borrow_book'),
   
]
