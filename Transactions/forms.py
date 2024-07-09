
from django import forms
# from .models import BorrowModel
from django import forms
from .models import TransectionModel

class DepositForm(forms.ModelForm):
    class Meta:
        model = TransectionModel
        fields = ['transaction_amount']
        labels = {
            'transaction_amount': 'Amount',
        }
    
    def clean_transaction_amount(self):
        amount=self.cleaned_data.get('transaction_amount')
        return amount
