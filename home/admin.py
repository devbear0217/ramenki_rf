# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.


class QuestionAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]
    list_filter = ['name', ]
    search_fields = ['name',
                     'email',
                     'question']

    fields = ["email"]

    class Meta:
        model = Question


class StayTunedAdmin (admin.ModelAdmin):
    list_display = [field.name for field in StayTuned._meta.fields]
    list_filter = ['email']
    search_fields = ['email']

    fields = ["email"]

    class Meta:
        model = Question


admin.site.register(StayTuned,
                    StayTunedAdmin)
admin.site.register(Question,
                    QuestionAdmin)
