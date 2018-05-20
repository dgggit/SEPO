# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class MyModel(models.Model):
	title = models.CharField(max_length = 200)
	content = RichTextField(config_name = 'default'	)
