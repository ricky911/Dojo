from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.show)
]



  # Now from within your newly created apps/first_app/urls.py file...
print "I will be your future routes; HTTP requests will be captured by me."
  