from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^create$' , views.dashBoard , name='create'),
    url(r'^read$', views.read , name='read'),
    url(r'^view$' ,views.viewAll , name='view'),
    url(r'viewrow' , views.viewRow , name='viewrow')


]