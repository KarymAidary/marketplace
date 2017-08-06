from django.shortcuts import render
from .forms import SubscribersForm
from products.models import *
# Create your views here.
def landing(request):
    form = SubscribersForm(request.POST or None)


    if request.method == 'POST' and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data = form.changed_data
        print (data["name"])

        new_form = form.save()
    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main = True, product__is_active = True)
    products_images_combs = products_images.filter(product__category__id=6)
    products_images_mirrors = products_images.filter(product__category__id=2)
    products_images_mapas = products_images.filter(product__category__id=4)
    products_images_haircurlers = products_images.filter(product__category__id=1)
    products_images_bathaccessories = products_images.filter(product__category__id=3)
    products_images_washcloths = products_images.filter(product__category__id=5)
    return render(request, 'landing/home.html', locals())