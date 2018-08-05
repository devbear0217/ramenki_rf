# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    question = models.CharField(max_length=256)

    def __str__(self):
        return "Пользователь %s %s %s" % (self.name,
                                          self.email,
                                          self.question)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class StayTuned(models.Model):
    email = models.EmailField()

    def __str__(self):
        return "Пользователь %s" % self.email

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'