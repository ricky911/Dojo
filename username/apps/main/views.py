# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
	return render(request, 'main/index.html')

def createUser(request):
	if request.method != 'POST':
		redirect('/')
	else:
		check = User.objects.validateUser(request.POST)
		if check[0] == False:
			for error in check[1]:
				messages.error(request, error)
			return redirect('/')
		else:
			user = User.objects.create(
				name = request.POST.get('name')
			)
			messages.success(request, 'The username you entered ' + request.POST.get('name') + ' is valid. Thanks!')
			return redirect('/success')

def success(request):
	context = {
	'users' : User.objects.all()
	}
	print context
	return render(request, 'main/success.html', context)

def delete(request, id):
	User.objects.filter(id=id).delete()
	return redirect('/success')

# Create your views here.
