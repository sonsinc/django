from django.shortcuts import render
from app_gen.models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products = Product.objects.filter(trending=True)
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def productDetail(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'detail.html', {'product': product})

def products(request):
    all_products = Product.objects.all().order_by('name')
    page = request.GET.get('page')
    paginator = Paginator(all_products,9) # number of products
    all_products = paginator.get_page(page)
    return render(request, 'products.html', {'all_products': all_products})