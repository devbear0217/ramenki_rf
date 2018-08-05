from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^About/$', views.about, name='about'),
    url(r'^Tableware/$', views.tableware, name='tableware'),
    url(r'^Shoes/$', views.shoes, name='shoes'),
    url(r'^Pictures/$', views.pictures, name='pictures'),
    url(r'^Metals/$', views.metal, name='metal'),
    url(r'^Crystal/$', views.crystal, name='crystal'),
    url(r'^Porcelain/$', views.porcelain, name='porcelain'),
    url(r'^Other/$', views.other_products, name='other'),
    url(r'^Wear/$', views.wear, name='wear'),
    url(r'^Bags/$', views.bags, name='bags'),
]
