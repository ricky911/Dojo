from django.shortcuts import render, redirect
from .models import Products

def index(request):
	product1 = Products.objects.create(name="banana", description="banana like", weight="1", price="2", cost="3", category="fruit")
	products = Products.objects.all()
	print product1.name
	return render(request, 'main/index.html')
# Create your views here.
