# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post_Community
from django.utils import timezone

# Create your views here.

def post_community(req):
    template = get_template('post_community.html')
    post_community = Post_Community.objects.filter(regdate__lte=timezone.now()).order_by('regdate')
    context = { 'Post_Community' : post_community }


    return HttpResponse(template.render(context))

