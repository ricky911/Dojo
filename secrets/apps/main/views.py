# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
from datetime import datetime 
from django.db.models import Count
import pytz
utc = pytz.utc

def index(request):
	return render(request, 'main/index.html')

def currentUser(request):
	if 'user_id' in request.session:
		return User.objects.get(id=request.session['user_id'])

def register(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		check = User.objects.validateUser(request.POST)
		if check['status'] == True:
			user = User.objects.registerUser(request.POST)
			request.session['user_id'] = user.id
			return redirect('/secrets')
		else:
			for error in check['errors']:
				messages.add_message(request, messages.ERROR, error, extra_tags='register')
				return redirect ('/')

def login(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		check = User.objects.loginUser(request.POST)
		if check['status'] == True:
			request.session['user_id'] = check['user'].id #when logging in, use dictionary passed here
			return redirect('/secrets')
		else:
			messages.add_message(request, messages.ERROR, 'Invalid credentials', extra_tags='login')
			return redirect('/')

def indexSecret(request):
	user = currentUser(request)
	context = {
	'user': user,
	'secrets': Secret.objects.order_by('-created_at').all()[:5],
	'current_datetime': datetime.now(tz=utc),
	}
	return render(request, 'main/secrets.html', context)

def addSecret(request):
	if request.method != 'POST':
		return redirect('/secrets')
	else:
		Secret.objects.create(
			message = request.POST['message'],
			user = currentUser(request),
			)
		return redirect('/secrets')

def likeSecret(request, id):
	user = currentUser(request)
	secret = Secret.objects.get(id=id)
	secret.likes.add(user)
	return redirect('/secrets')

def delSecret(request, id):
	secret = Secret.objects.get(id=id)
	secret.delete()
	return redirect('/secrets')

def popular(request):
	user = currentUser(request)
	context = {
	'current_datetime': datetime.now(tz=utc),
	'user': user,
	'secrets': Secret.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')
	}
	return render(request, 'main/popular.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')