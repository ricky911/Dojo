# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Username(models.Model):
	name = models.CharField(max_length=16)
# Create your models here.
