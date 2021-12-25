from django.urls import path

from .import views

urlpatterns=[

    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('info/',views.info,name="info"),
    path('user/',views.user,name="user"),

]