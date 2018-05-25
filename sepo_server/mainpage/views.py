# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils import timezone
#fro ranking.models import Score

# Create your views here.

def mainpage(req):
    template = get_template('MainPage.html')
    context = {}
    # context = {'rankdata' : Score.objects.order_by('rank')[:10] }

    return HttpResponse(template.render(context))

