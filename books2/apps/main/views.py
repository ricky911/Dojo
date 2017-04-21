# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Books

def index(request):
	context = {
	"books" : Books.objects.all()
	}
	return render(request, 'main/index.html', context)

def new(request):
	Books.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
	return redirect('/')

# Create your views here.
