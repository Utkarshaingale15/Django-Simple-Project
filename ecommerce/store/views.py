from django.shortcuts import render

# Create your views here.

def store(request):
    context={}
    return render(request,'store/store.html',context)

def cart(request):
    context={}
    return render(request,'store/cart.html',context)

def checkout(request):
    context={}
    return render(request,'store/checkout.html',context)

def info(request):
    context={}
    return render(request,'store/info.html',context)

def user(request):
    context={}
    return render(request,'store/user.html',context)

