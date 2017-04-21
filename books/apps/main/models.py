# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
	title = models.CharField(max_length=40)
	author = models.CharField(max_length=40)
	publish_date = models.IntegerField()
	category = models.CharField(max_length = 40)
	in_print = models.BooleanField()

# Create your models here.
