from django.urls import path
from .views import transaction_list

urlpatterns = [
    path("transaction", transaction_list, name="transaction_list"),

]