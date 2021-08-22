from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import  Transaction
# Create your views here.
@login_required
def transaction_list(request):
    spent = Transaction.objects.filter(transaction_type = 0)
    income=Transaction.objects.filter(transaction_type = 1)
    return render(request, 'transaction/transaction-list.html', {"spent" : spent ,
     'income' : income })