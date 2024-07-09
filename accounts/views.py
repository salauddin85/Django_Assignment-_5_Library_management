from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from accounts.forms import RegisterForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.contrib.auth.views import LogoutView,LoginView
class UserFormView(FormView):
    template_name = 'accounts/register.html'
    # success_url = reverse_lazy('home')
    form_class = RegisterForm

    
    def form_valid(self, form):
        user = form.save()
        print(form.cleaned_data)
        login(self.request,user)
        
        return super().form_valid(form)
    
    def get_success_url(self) :
        return reverse_lazy('home')
    

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('login')

class UserLogin(LoginView):
    template_name = 'accounts/login.html'
    # 
    def get_success_url(self):
        return reverse_lazy('home')
