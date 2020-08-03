from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

# def product_create_view(request):
#     form = RawProductForm()
#     if (request.method == "POST"):
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             Product.objects.create(**form.cleaned_data)
#             print(form.cleaned_data)
#             form = RawProductForm()

#     context = {
#         "form": form
#     }
#     return render(request, "product/product_create.html", context)




#Create your views here. 
#Not cleanng data
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form": form,
    }
    return render(request, "product/product_create.html", context)


def product_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj,
    }
    return render(request, "product/detail.html", context)

