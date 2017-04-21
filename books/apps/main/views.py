# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Books

def index(request):
	book1 = Books.objects.create(title='Harry Potter 1', author='JK Rowling', publish_date='1997', category='Fantasy')
	book2 = Books.objects.create(title='Harry Potter 2', author='JK Rowling', publish_date='1998', category='Fantasy')
	book3 = Books.objects.create(title='Harry Potter 3', author='JK Rowling', publish_date='1999', category='Fantasy')
	book4 = Books.objects.create(title='Harry Potter 4', author='JK Rowling', publish_date='2000', category='Fantasy')
	book5 = Books.objects.create(title='Harry Potter 5', author='JK Rowling', publish_date='2003', category='Fantasy')
	
	print 'Title: {} Author: {}, Publish Date: {}, Category: {}'.format(book1.title, book1.author, book1.publish_date, book1.category)
	print 'Title: {} Author: {}, Publish Date: {}, Category: {}'.format(book2.title, book2.author, book2.publish_date, book2.category)
	print 'Title: {} Author: {}, Publish Date: {}, Category: {}'.format(book3.title, book3.author, book3.publish_date, book3.category)
	print 'Title: {} Author: {}, Publish Date: {}, Category: {}'.format(book4.title, book4.author, book4.publish_date, book4.category)
	print 'Title: {} Author: {}, Publish Date: {}, Category: {}'.format(book5.title, book5.author, book5.publish_date, book5.category)
	return render(request, 'main/index.html')


# Create your views here.
