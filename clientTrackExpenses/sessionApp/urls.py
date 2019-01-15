from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^signup$', views.userSignUp, name='signup'),
    url(r'^signin$', views.userLogin, name='signin'),
    url(r'^logout$', views.userLogout, name='logout'),
]