# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from classes.models import Training_site, Class_type, Course, Student #what is project name?

class Purchaser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=300)
    






# Create your models here.
