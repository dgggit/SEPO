# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def post_community(req):
	template = get_template('post_community.html')
	context = {'python_word' : 'Python'}

	return HttpResponse(template.render(context))
