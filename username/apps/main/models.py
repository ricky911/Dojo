# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
import re

class UserManager(models.Manager):
	def validateUser(self, post):
		is_valid = True
		errors = []
		if len(post.get('name')) == 0:
			is_valid = False
			errors.append('Name field cannot be blank')
		if len(post.get('name')) < 8 or len(post.get('name')) > 16:
			is_valid = False
			errors.append('Name field must be between 8 and 16 characters')
		return (is_valid, errors)


class User(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

# Create your models here.
