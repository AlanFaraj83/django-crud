from django.shortcuts import render, redirect

from products.models import Products
from products.forms import ProductForm

def products(request):
    
    products = Products.objects.all()

    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            form = ProductForm()

    return render(request, "products.html", context={
        "products": products,
        "form": form
    })

def product_update(request, product_id):

    product = Products.objects.get(pk=product_id)

    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            form = ProductForm()

    return render(request, "product_update.html", context={
        "product": product,
        "form": form
    })

def product_delete(request, product_id): 
    product = Products.objects.get(pk=product_id)
    return render(request, "product_delete.html", context={
        "product": product
    })

def product_delete_confirm(request, product_id): 
    product = Products.objects.get(pk=product_id)
    product.delete()
    return redirect('products')

