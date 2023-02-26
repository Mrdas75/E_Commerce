#from django.contrib.auth.models import User

from django.shortcuts import redirect, render
from products.models import SizeVariant,Product
from accounts.models import Cart,CartItems

# Create your views here.

def get_product(request,slug):
    
    try:
        product=Product.objects.get(slug=slug)
        context={'product':product}
        a=product.size_variant
        print(a)
      
        if request.GET.get('size'):
            size = request.GET.get('size')
            print(size) 
            price = product.get_updated_price(size)
            context['selected_size'] = size
            context['updated_price'] = price
            print(price)

        return render(request,"products/products.html", context=context)
    except Exception as e:
        print(e)



