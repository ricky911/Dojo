from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^secrets$', views.indexSecret),
	url(r'^addSecret$', views.addSecret),
	url(r'^likeSecret/(?P<id>\d+)$', views.likeSecret),
	url(r'^delSecret/(?P<id>\d+)$', views.delSecret),
	url(r'^popular$', views.popular),
]