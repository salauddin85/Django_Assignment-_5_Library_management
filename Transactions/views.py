from django.shortcuts import render
# # from .forms import DepositForm
from django.contrib import messages
from .constants import DEPOSIT
# from .models import TransectionModel
from accounts.models import AccountModel
from django.views.generic.edit import FormView
from .forms import DepositForm
from .models import TransectionModel
from django.urls import reverse_lazy
from.constants import TRANSACTION_TYPE
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string



# Create your views here.
@method_decorator(login_required,name='dispatch')
class Depositview(FormView):
    form_class = DepositForm
    # title = 'DepositForm' 
    template_name = 'deposit.html'
    success_url = reverse_lazy('home')


        
    def send_transaction_email(self,user, amount,  template):
            subject = 'Deposit Confirmations'
            message = render_to_string(template, {
                'user' : user,
                'amount' : amount,
            })
            send_email = EmailMultiAlternatives(subject, '', to=[user.email])
            send_email.attach_alternative(message, "text/html")
            send_email.send()

   
    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial
        # return super().get_initial()
    def form_valid(self, form):
        amount = form.cleaned_data["transaction_amount"]
        print(amount)
        # requested_user = TransectionModel.objects.get(user=self.request.user)
        requested_user = AccountModel.objects.get(user=self.request.user)
       
        requested_user.balance+= amount
        print(requested_user.balance)
        # transaction_email(self.request.user,amount,DEPOSITE)
        messages.success(self.request,'Succssfully deposited')
        requested_user.save()
           
       
        TransectionModel.objects.create(
            user=self.request.user,
            transaction_amount=amount,
            transaction_type=TRANSACTION_TYPE,
            balance=requested_user.balance,
        )
        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        self.send_transaction_email(self.request.user, amount, "deposite_email.html")

        return super().form_valid(form)
