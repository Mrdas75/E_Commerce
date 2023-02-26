from django.shortcuts import render
from products.models import *
# Create your views here.



def index(request):
    context = {'product':Product.objects.all()}
    return render(request,"home/index.html",context)

