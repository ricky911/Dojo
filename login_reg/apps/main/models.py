# from __future__ import unicode_literals

from django.db import models
import re
class UserManager(models.Manager):
	def validateUser(self, post):
		is_valid = True
		errors = []
		if len(post.get('first_name')) < 2 or len(post.get('last_name')) < 2:
			is_valid = False
			errors.append('Name fields must be at least 2 characters long.')
		if not re.search(r'^[a-zA-Z]+$', post.get('first_name')) or not re.search(r'^[a-zA-Z]+$', post.get('last_name')):
			is_valid = False
			errors.append('Name fields can only dcontain letters.')
		if not re.search(r'\w+\@\w+\.\w+', post.get('email')):
			is_valid = False
			errors.append('Please enter a valid email.')
		if len(post.get('password')) < 8 or len(post.get('cpw')) < 8:
			is_valid = False
			errors.append('Password must be at least 8 characters long.')
		if post.get('password') != post.get('cpw'):
			is_valid = False
			errors.append('Passwords do not match.')
		return (is_valid, errors)

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	confirm = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
# Create your models here.
