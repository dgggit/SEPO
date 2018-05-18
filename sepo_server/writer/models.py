# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_markdown.models import MarkdownField


# Create your models here.

class MyModel(models.Model):
	content = MarkdownField()
