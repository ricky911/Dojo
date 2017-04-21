# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Courses

def index(request):
	context = {
	'courses' : Courses.objects.all()
	}
	return render(request, 'main/index.html', context)

def add(request):
	Courses.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/')

def delete(request, id):
	Courses.objects.filter(id=id).delete()
	return redirect('/')

def confirm(request, id):
	context = {
	'course' : Courses.objects.get(id=id)
	}
	return render(request, 'main/confirm.html', context)
# Create your views here.
