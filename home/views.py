# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *
from merchandise.models import *

# Create your views here.


def question(request):
    name = "Kalutsky"
    form = QuestionForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data

        new_form = form.save()

    return render(request,
                  'home/about.html',
                  locals())


def staytuned(request):
    name = "Kalutsky"
    form = StayTunedForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()

    return render(request,
                  'home/home.html',
                  locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True,
                                                  is_main=True,
                                                  product__is_active=True)
    products_images_slide = ProductImage.objects.filter(is_active=True,
                                                        is_main=True,
                                                        is_feature=True,
                                                        product__is_active=True)
    return render(request, 'home/home.html', locals())


def about(request):
    return render(request, 'home/about.html', locals())


def tableware(request):
    products_images = ProductImage.objects.filter(is_active=True,
                                                  is_main=True,
                                                  product__is_active=True)
    products_images_dishes = products_images.filter(product__category__id=1)
    return render(request, 'merchandise/tableware.html', locals())


def shoes(request):
    products_images = ProductImage.objects.filter(is_active=True,
                                                  is_main=True,
                                                  product__is_active=True)
    products_images_shoes = products_images.filter(product__category__id=2)
    return render(request, 'merchandise/shoes.html', locals())


def pictures(request):
    products_images = ProductImage.objects.filter(is_active=True,
                                                  is_main=True,
                                                  product__is_active=True)
    products_images_pictures = products_images.filter(product__category__id=3)
    return render(request, 'merchandise/pictures.html', locals())


def metal(request):
    products_images = ProductImage.objects.filter(is_active=True,
                                                  is_main=True,
                                                  product__is_active=True)
    products_images_metal = products_images.filter(product__category__id=4)
    return render(request, 'merchandise/metal.html', locals())


def crystal(request):
    products_images = ProductImage.objects.filter(is_active=True,
                                                  is_main=True,
                                                  product__is_active=True)
    products_images_shoes = products_images.filter(product__category__id=5)
    return render(request, 'merchandise/crystal.html', locals())


def porcelain(request):
    products_images = ProductImage.objects.filter(is_active=True,
                                                  is_main=True,
                                                  product__is_active=True)
    products_images_porcelain = products_images.filter(product__category__id=6)
    return render(request, 'merchandise/porcelain.html', locals())


def other_products(request):
    products_images = ProductImage.objects.filter(is_active=True,
                                                  is_main=True,
                                                  product__is_active=True)
    products_images_other_products = products_images.filter(product__category__id=7)
    return render(request, 'merchandise/shoes.html', locals())


def wear(request):
    products_images = ProductImage.objects.filter(is_active=True,
                                                  is_main=True,
                                                  product__is_active=True)
    products_images_wear = products_images.filter(product__category__id=8)
    return render(request, 'merchandise/wear.html', locals())


def bags(request):
    products_images = ProductImage.objects.filter(is_active=True,
                                                  is_main=True,
                                                  product__is_active=True)
    products_images_bags = products_images.filter(product__category__id=9)
    return render(request, 'merchandise/bags_belts.html', locals())
