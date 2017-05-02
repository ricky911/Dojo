from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.createUser),
    url(r'^login$', views.loginUser),
    url(r'^quotes$', views.indexQuote),
    url(r'^logout$', views.logout),
    url(r'^addQuotes$', views.addQuotes),
    url(r'^addFav/(?P<id>\d+)$', views.addFav),
    url(r'^delFav/(?P<id>\d+)$', views.delFav),
    url(r'^user/(?P<id>\d+)$', views.user),
]
