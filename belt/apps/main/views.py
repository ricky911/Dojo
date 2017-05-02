# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def currentUser(request):
	if 'user_id' in request.session:
		return User.objects.get(id=request.session['user_id'])

def index(request):
	return render(request, 'main/index.html')

def createUser(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		check = User.objects.validateUser(request.POST)
		if check['status'] == True:
			user = User.objects.createUser(request.POST)
			request.session['user_id'] = user.id
			# messages.success(request, 'Welcome, ' + request.POST.get('first_name') + '!')
			return redirect('/quotes')
		else:
			for error in check['errors']:
				messages.add_message(request, messages.ERROR, error, extra_tags='registration')
				return redirect('/')

def loginUser(request):
	if request.method != 'POST':
		return redirect('/')
	check = User.objects.loginUser(request.POST)
	if check['status'] == True:
		request.session['user_id'] = check['user'].id
		messages.success(request, 'Welcome, ' + check['user'].first_name + '!')
		return redirect('/quotes')
	else:
		messages.add_message(request, messages.ERROR, check['messages'], extra_tags='login')
		return redirect('/')

def indexQuote(request):
	user = currentUser(request)
	# print user.quotes.all().count()
	context = {
		'current_user': user,
		'quotable_quotes': Quote.objects.order_by('-created_at').exclude(favorite=user),
		'favorites': Quote.objects.order_by('-created_at').all(),
	}

	# print context['current_user'].favorites.all()
	return render(request, 'main/welcome.html', context)

def addQuotes(request):
	if request.method != 'POST':
		return redirect('/quotes')
	else:
		check = Quote.objects.validateQuote(request.POST)
		if check['status'] == True:
			quote = Quote.objects.create(
				author=request.POST.get('name'),
				quote=request.POST.get('quote'),
				user=currentUser(request)
			)
			return redirect('/quotes')
		else:
			for error in check['errors']:
				messages.add_message(request, messages.ERROR, error, extra_tags='new_quote')
				return redirect('/quotes')

def addFav(request, id):
	user = currentUser(request)
	quote = Quote.objects.get(id=id)

	user.favorites.add(quote)

	return redirect('/quotes')

def delFav(request, id):
	user = currentUser(request)
	quote = Quote.objects.get(id=id)
	user.favorites.remove(quote)
	return redirect('/quotes')

def user(request, id):
	if 'user_id' not in request.session:
		redirect('/')
	else:
		this_user = User.objects.get(id = id)
		count = len(this_user.quotes.all())


		context = {
		'user': this_user,
		'current_user': currentUser(request),
		'quotes': Quote.objects.order_by('-created_at').all(),
		'count': count
		}
	return render(request, 'main/user.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')