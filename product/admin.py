from transaction.models import Transaction
from django.contrib import admin
from .models import Product
from transaction.models import Transaction 
admin.site.register(Product)
admin.site.register(Transaction)
# Register your models here.
