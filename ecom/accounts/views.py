

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib.auth import login,logout,authenticate
from accounts.models import *
from django.http import HttpResponseRedirect

# Create your views here.


def login_page(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request,'Account Not Found')
            return HttpResponseRedirect(request.path_info)
# Email verifying for profile

        if not user_obj[0].profile.is_email_verified:
            messages.warning(request,'Please Verify Your Account')
            return HttpResponseRedirect(request.path_info)    

        user_obj=authenticate(username=email,password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('/')
        messages.warning(request,'Invalid Credential')
        
    return render(request,'accounts/login.html')

def Register_Page(request):
    if request.method=="POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
# For user id is already exists
    
        user_obj = User.objects.filter(username = email)
        if user_obj.exists():
            messages.warning(request, 'Email ID Already Exists ')
# Automatically Redirect the previous page

            return HttpResponseRedirect(request.path_info)

# To create an User ID 
 
        user_obj=User.objects.create(first_name=first_name,last_name=last_name,email=email,username=email)
# To set user password
 
        user_obj.set_password(password)
        user_obj.save()
        print(user_obj)
        messages.success(request,"An email has been sent to your mail ")
        return HttpResponseRedirect(request.path_info)
    return render(request,'accounts/register.html')

# for activating account after send the verification link

def Activate_email(request,email_token):
    try:
        user=Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        return redirect("/")
    except Exception as e:
        return HttpResponse("Invalid Link")

#  ==========================>>>>>>>>>     Add to Cart Functionality     <<<<<<<<<<<======================


def add_to_cart(request,uid):

    product=Product.objects.get(uid=uid)
    user=request.user                                                         
    cart, _=Cart.objects.get_or_create(user=user,is_paid=False)
    cart_items=CartItems.objects.create(cart=cart,product=product)
    variant=request.GET.get('variant')

    print("uid :",product)
    print("user :",user)
    print("cart, _ :",cart, _)
    print("cart_items",cart_items)
    print("variant :",variant)
    print("nsdfj==",request.user.profile.get_cart_count)

    if variant:
        variant=request.GET.get('variant')
        print(variant)
        size_variant = SizeVariant.objects.get(size_name=variant)
        cart_items.size_variant=size_variant
        cart_items.save()
        print(cart_items.save())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))         #  Redirect the same page
 #   return HttpResponseRedirect(request.path_info)



def cart(request):
    context={"cart" : Cart.objects.filter(is_paid = False , user= request.user)}
    return render(request, 'products/cart.html',context)