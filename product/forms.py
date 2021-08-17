from django.forms import fields
from product.models import Product
from django import forms

class ProductForm(forms.ModelForm):
    name=forms.CharField(label="nom du produit", widget=forms.TextInput({ "class": "form-control"}) )
    quantity=forms.IntegerField (label="Quantité en stock", widget=forms.NumberInput({ "class": "form-control"}) )
    price=forms.IntegerField (label="Prix", widget=forms.NumberInput({ "class": "form-control"}) )
    image=forms.ImageField(label='image du produit', widget=forms.FileInput({ "class": "form-control"}))

    class Meta:
        model = Product
        fields= ('name', 'quantity', 'price', 'image')


    