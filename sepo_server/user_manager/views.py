# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def login(req):
	template = get_template('LoginPage.html')

	context = {}
	#context = {'login_form' : LoginForm()}
	#context.update(csrf(req))

	return HttpResponse(template.render(context))	
