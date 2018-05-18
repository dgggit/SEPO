# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render
from django.http.response import HttpResponse
from writer.forms import MyCustomForm

# Create your views here.

def test_writer(req):
	template = get_template('tester.html')
	context = {}

	return HttpResponse(template.render(context))

