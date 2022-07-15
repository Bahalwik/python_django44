from django.shortcuts import render
from .models import *


def home(request):
    products_images = ProductImg.objects.filter(is_active=True, is_main=True)
    return render(request, 'advertisements_app/home.html', locals())

