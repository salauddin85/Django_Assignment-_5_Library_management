from django.urls import path
from .views import UserFormView,UserLogoutView,UserLogin

urlpatterns = [
    path('register/',UserFormView.as_view(),name='register'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('login/',UserLogin.as_view(),name='login'),
]


