from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product_detail
# from django.middleware import csrf_exempt

# Create your views here.

def index(request):
    data = product_detail.objects.all().values()
    return render(request,'index.html',{'data':data})

def add(request):
    return render(request,'form.html')

# @csrf_exempt
def addrecord(request):
    x = request.POST["name"]
    y = request.POST["price"]
    z = request.POST["quantity"]
    a = request.POST["offer"]
    
    data = product_detail(product_name = x ,price = y ,quantity = z , offer = a)
    data.save()
    
    return redirect('index')

def details(request,id):
    data = product_detail.objects.get(id=id)
    name = data.product_name
    price = data.price
    quantity = data.quantity
    offer = data.offer
    res = {'name':name , "price":price , "quantity" : quantity , "offer":offer}
    return render(request,'details.html',{'data':res})