
from django.urls import path
from accounts.views import login_page,Register_Page,Activate_email,cart,add_to_cart




urlpatterns = [
    path('login/',login_page,name="login"),
    path('register/',Register_Page,name="register"),
    path('activate/<email_token>/',Activate_email,name="Activate_email"),
    path('cart/', cart, name="cart"),
    path('add_to_cart/<uid>/',add_to_cart,name="add_to_cart")

]