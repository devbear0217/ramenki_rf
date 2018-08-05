# -*- coding: utf-8 -*-

from django import forms
from .models import *


class StayTunedForm(forms.ModelForm):

    class Meta:
        model = StayTuned
        exclude = [""]


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        exclude = [""]