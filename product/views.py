from product.forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from .forms import ProductForm

@login_required
def index(request):
    return render(request, "index.html")


@login_required
def product_list(request):
    user = request.user
    products = Product.objects.filter(owner=user)
    return render(request, "product/product-list.html", {"products": products})

@login_required
def detail_product(request , product_id):
    product= get_object_or_404(Product, pk=product_id)
    return render(request, "product/detail-product.html", {"product":product})
@login_required
def add_product(request):
    user=request.user
    if request.method == "POST":
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
           product= form.save(commit=False)
           product.owner=user
           product.save()
           return redirect("product_list")
    else :
        form=ProductForm()
    return render(request, "product/add-product.html", {'form': form} )
@login_required
def edit_product(request, product_id):
    product= get_object_or_404(Product, pk=product_id)
    user=request.user
    if request.method == "POST" :
        form=ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
           product= form.save(commit=False)
           product.save()
           return redirect("product_list")
    else:
        form=ProductForm(instance=product)
    return render(request, "product/edit-product.html", {'form': form})

@login_required
def remove_product(request , product_id):
    product= get_object_or_404(Product, pk=product_id)
    if request.method == "POST" :
        product.delete()
        return redirect("product_list")
    return render(request, "product/remove-product.html", {'product': product})
        

