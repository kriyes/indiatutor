from django.shortcuts import render
from django.http import HttpResponse  # new
from .models import *

# Create your views here.
def home(request):

    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customer = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status="Deliverd").count
    pending = orders.filter(status="Pending").count

    context = {'orders':orders,'customers':customers,'delivered':delivered,'pending':pending}

    return render(request,'crm/crm.html',context)

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    context ={'customer': customer , 'orders':orders}

    return render(request,'crm/customer.html',context)

def products(request):
    products = Product.objects.all()
    return render(request,'crm/products.html',{'products':products})
