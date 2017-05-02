# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class UserManager(models.Manager):
	def validateUser(self, post):
		is_valid = True
		errors = []
		if len(post.get('first_name')) < 2 or len(post.get('last_name')) < 2:
			is_valid = False
			errors.append('Name fields must be at least 2 characters long.')
		if not re.search(r'^[a-zA-Z]+$', post.get('first_name')) or not re.search(r'^[a-zA-Z]+$', post.get('last_name')):
			is_valid = False
			errors.append('Name fields may only contain letters.')
		if not re.search(r'\w+\@\w+\.\w+', post.get('email')):
			is_valid = False
			errors.append('Please enter a valid email.')
		if len(post.get('pw')) < 8:
			is_valid = False
			errors.append('Password must be at least 8 characters long.')
		if post.get('pw') != post.get('cpw'):
			is_valid = False
			errors.append('Passwords do not match.')
		# if not re.search(r'^\d+[/]\d+[/]\d+$', post.get('dob')):
		# 	is_valid = False
		# 	errors.append('Please enter a valid birth date.')
		return {'status': is_valid, 'errors': errors}

	def createUser(self, post):
		return User.objects.create(
			first_name=post.get('first_name'),
			last_name=post.get('last_name'),
			email=post.get('email'),
			password=bcrypt.hashpw(post.get('pw').encode(), bcrypt.gensalt()),
			)

	def loginUser(self,post):
		user = User.objects.filter(email=post.get('email')).first()
		if user and bcrypt.hashpw(post.get('pw').encode(), user.password.encode()) == user.password:
			return {'status': True, 'user': user}
		else:
			return{'status': False, 'messages': 'Invalid credentials'}

class QuoteManager(models.Manager):
	def validateQuote(self, post):
		is_valid = True
		errors = []
		if len(post.get('name')) < 3:
			is_valid = False
			errors.append('Author must be at least 3 characters')
		if len(post.get('quote')) < 10:
			is_valid = False
			errors.append('Quote must be at least 10 characters')
		return {'status': is_valid, 'errors': errors}

	# def createQuote(self, post):
	# 	return Quote.objects.create(
	# 		author=post.get('author'),
	# 		quote=post.get('quote'),
	# 		user=currentUser(request),
	# 		)

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	dob = models.DateField(auto_now=True)
	# favorite = models.ManyToManyField(Quote, related_name='favorites')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager() 

# class Author(models.Model):
# 	name = models.CharField(max_length=255)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

class Quote(models.Model):
	author = models.CharField(max_length=255)
	quote = models.TextField(max_length=255)
	favorite = models.ManyToManyField(User, related_name='favorites')
	user = models.ForeignKey(User, related_name="quotes")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = QuoteManager()


