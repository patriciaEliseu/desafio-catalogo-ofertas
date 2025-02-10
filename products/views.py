from django.shortcuts import render
from .models import Products

def list_products(request):
    produtos = Products.objects.all()

    if request.GET.get('frete_gratis'):
        produtos = produtos.filter(frete_gratis=True)
    if request.GET.get('full'):
        produtos = produtos.filter(entrega='Full')
    return render (request, 'list_products.html', {'produtos': produtos})




