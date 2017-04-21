# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
	name = models.CharField(max_length=35)
	description = models.TextField(max_length=1000)
	weight = models.IntegerField()
	price = models.IntegerField()
	cost = models.IntegerField()
	category = models.CharField(max_length=15)