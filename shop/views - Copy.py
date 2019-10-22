from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
def index(request):
	product=Product.objects.all()
	print(product)


	params={'product':product}
	return render(request,'shop/index.html',params)

def about(request):
	return render(request,'shop/about.html')

def contact(request):
	return HttpResponse("at contact")

def tracker(request):
	return HttpResponse("at tracker")

def search(request):
	return HttpResponse("at about")

def prodView(request):
	return HttpResponse("at prodView")

def checkout(request):
	return HttpResponse("at checkout")
