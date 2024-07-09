from django.urls import path
# # from borrow_book.models import BorrowModel
from .views import Depositview

urlpatterns = [
    path('deposit/',Depositview.as_view(),name='deposit'),
]
