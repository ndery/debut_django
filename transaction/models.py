from django.db import models
from product.models import Product
class Transaction(models.Model):

    SPENT= 0
    INCOME=1
    TRANSACTION_TYPE = [(SPENT ,"Dépense"),(INCOME, "Revenu")]
    transaction_type=models.CharField(max_length=1, choices=TRANSACTION_TYPE, default=SPENT)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null= True)
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(default=0, max_digits=13, decimal_places=2)

    def __str__(self) :
        return f"Product: {self.product} {self.price}"
# Create your models here.
