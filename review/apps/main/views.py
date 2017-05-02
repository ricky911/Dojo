# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import datetime
import random
import string

def index(request):
	return render(request, 'main/index.html')

def generate(request):
	


# Create your views here.
