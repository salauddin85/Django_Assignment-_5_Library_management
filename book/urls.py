from django.urls import path
from .views import BookForm,DetailsBook,ProfileView

urlpatterns = [
    path('add_book/',BookForm.as_view(),name='add_book'),
    path('details_book/<int:id>',DetailsBook.as_view(),name='details_book'),
    path('profile/',ProfileView.as_view(),name='profile'),

    
]


